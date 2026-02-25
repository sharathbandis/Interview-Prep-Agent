
# 💼 Autonomous AI Interview Prep Agent

![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)https://interview-prep-agent.streamlit.app/

## 📌 Overview
An intelligent, cloud-deployed AI agent that autonomously researches companies in real-time to generate comprehensive technical interview cheat sheets. 

Unlike traditional LLMs that rely on static, outdated training data, this Agent utilizes **Tool Calling** to browse the live internet, read recent corporate news, and analyze the target company's current technology stack.

## 🏗️ System Architecture
1. **User Interface:** Built with **Streamlit** for a lightweight, responsive web experience.
2. **Orchestration:** Powered by **LangChain** to manage the ReAct (Reasoning and Acting) loop.
3. **The "Brain" (LLM):** Utilizes Meta's **Llama-3.3-70b-versatile** via the **Groq API** for ultra-fast, high-reasoning inference.
4. **The "Eyes" (Tools):** Integrates the **Tavily Search API**, allowing the agent to autonomously query the web, scrape results, and synthesize real-time data.

## ⚙️ Tech Stack
* **Language:** Python
* **Framework:** LangChain (create_tool_calling_agent, AgentExecutor)
* **LLM Provider:** Groq
* **Web Search:** Tavily API
* **Frontend & Hosting:** Streamlit Community Cloud

## 🚀 Live Demo
You can test the live application here: https://interview-prep-agent.streamlit.app/

## 💻 Local Installation

If you want to run this agent locally on your own machine:

1. **Clone the repository:**

   git clone https://github.com/sharathbandis/Interview-Prep-Agent.git

   cd Interview-Prep-Agent



3. **Install the dependencies:**

   pip install -r requirements.txt




4. **Set up your API Keys securely:**
Create a folder named `.streamlit` and a file inside it called `secrets.toml`.

   mkdir .streamlit
   touch .streamlit/secrets.toml




Add your keys to `secrets.toml`:

   GROQ_API_KEY = "your_groq_key_here"
   
   TAVILY_API_KEY = "your_tavily_key_here"




4. **Run the application:**

python -m streamlit run agent_app.py





## 🧠 How it Works (The Agentic Loop)

When a user inputs a company name, the LangChain Agent takes control. Instead of guessing, it formulates a search query, uses the Tavily tool to fetch live search engine results, reads the context, and only then generates the final formatted response.
