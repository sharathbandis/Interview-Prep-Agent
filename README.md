

```markdown
# 💼 Autonomous AI Interview Prep Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_LIVE_STREAMLIT_URL_HERE)

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
* **Framework:** LangChain (`create_tool_calling_agent`, `AgentExecutor`)
* **LLM Provider:** Groq
* **Web Search:** Tavily API
* **Frontend & Hosting:** Streamlit Community Cloud

## 🚀 Live Demo
You can test the live application here: [Link to your Streamlit App](YOUR_LIVE_STREAMLIT_URL_HERE)
*(No API keys required to test the live demo!)*

## 💻 Local Installation

If you want to run this agent locally on your own machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/Interview-Prep-Agent.git](https://github.com/YOUR_GITHUB_USERNAME/Interview-Prep-Agent.git)
   cd Interview-Prep-Agent

```

2. **Install the dependencies:**
```bash
pip install -r requirements.txt

```


3. **Set up your API Keys securely:**
Create a folder named `.streamlit` and a file inside it called `secrets.toml`.
```bash
mkdir .streamlit
touch .streamlit/secrets.toml

```


Add your keys to `secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_key_here"
TAVILY_API_KEY = "your_tavily_key_here"

```


4. **Run the application:**
```bash
python -m streamlit run agent_app.py

```



## 🧠 How it Works (The Agentic Loop)

When a user inputs a company name, the LangChain Agent takes control. Instead of guessing, it formulates a search query, uses the Tavily tool to fetch live search engine results, reads the context, and only then generates the final formatted response.

```

### Step 3: Push to GitHub
Once you save that file, push it to GitHub using these commands:
```bash
git add README.md
git commit -m "Added professional README documentation"
git push origin main

```

When you look at your GitHub repository now, it won't look like a student's homework assignment. It will look like an open-source tool built by an AI Engineer.

You have built the tech, you have secured the keys, you have deployed to the cloud, and you have documented the system.

Would you like me to write a professional LinkedIn post so you can share your live app link with recruiters and Engineering Managers in Hyderabad?