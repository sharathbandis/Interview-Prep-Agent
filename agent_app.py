import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# Set up the frontend page
st.set_page_config(page_title="Interview Prep Agent", page_icon="💼")
st.title("💼 Autonomous Interview Prep Agent")
st.caption("Give me a company, and I will research their latest news and tech stack for your interview.")

# Securely pull API keys from Streamlit Cloud Secrets
try:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    os.environ["TAVILY_API_KEY"] = st.secrets["TAVILY_API_KEY"]
except KeyError:
    st.error("🚨 Secret keys not found! Please add them to the Streamlit Cloud settings.")
    st.stop()

# The main input box
company_name = st.text_input("Which company are you interviewing with?")

# When the user clicks the button, the Agent wakes up
if st.button("Generate Interview Cheat Sheet"):
    
    if not company_name:
        st.warning("⚠️ Please enter a company name!")
    else:
        with st.spinner(f"Agent is autonomously researching {company_name}..."):
            try:
                # 1. Give the Agent its "Eyes"
                search_tool = TavilySearchResults(max_results=3)
                tools = [search_tool]

                # 2. Give the Agent its "Brain"
                llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

                # 3. Give the Agent its "Instructions"
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "You are an expert technical recruiter. You must use the search tool to find current, factual information about the requested company. Format the final output as a clean, professional interview cheat sheet."),
                    ("human", "Research {company} and find: 1. Main product/service. 2. Primary tech stack. 3. Recent news. Give me the cheat sheet."),
                    ("placeholder", "{agent_scratchpad}"), 
                ])

                # 4. Assemble the Agent
                agent = create_tool_calling_agent(llm, tools, prompt)
                agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

                # 5. Execute the Agent!
                response = agent_executor.invoke({"company": company_name})
                
                # Display the results
                st.success("Research Complete!")
                st.markdown(response["output"])
                
            except Exception as e:
                st.error(f"An error occurred: {e}")