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

# Build a secure sidebar for API Keys
with st.sidebar:
    st.header("🔑 API Keys")
    groq_api_key = st.text_input("Groq API Key", type="password")
    tavily_api_key = st.text_input("Tavily Search API Key", type="password")
    st.markdown("*(These keys are not saved anywhere. They only exist while this tab is open).*")

# The main input box
company_name = st.text_input("Which company are you interviewing with?")

# When the user clicks the button, the Agent wakes up
if st.button("Generate Interview Cheat Sheet"):
    
    # Safety checks
    if not groq_api_key or not tavily_api_key:
        st.warning("⚠️ Please enter both API keys in the sidebar first!")
    elif not company_name:
        st.warning("⚠️ Please enter a company name!")
    else:
        # Load the keys into the environment
        os.environ["GROQ_API_KEY"] = groq_api_key
        os.environ["TAVILY_API_KEY"] = tavily_api_key

        with st.spinner(f"Agent is searching the live internet for {company_name}..."):
            try:
                # 1. Give the Agent its "Eyes" (Tavily Search Tool)
                search_tool = TavilySearchResults(max_results=3)
                tools = [search_tool]

                # 2. Give the Agent its new "Brain" (Groq running Meta's Llama 3)
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
                
                # Display the results on the web page
                st.success("Research Complete!")
                st.markdown(response["output"])
                
            except Exception as e:
                st.error(f"An error occurred: {e}")