# 🔬 ResearchMind: Autonomous Multi-Agent Research Engine
ResearchMind is an advanced AI-driven research pipeline that utilizes a multi-agent architecture to perform deep-web investigation, objective content synthesis, and critical fact-checking. By leveraging LangChain and Qwen-Coder-3, the system automates the transition from a simple query to a verified, professional research report.

**Live App Demo** - https://multi-agentic-research-system.streamlit.app/

# 🚀 Key Features
* Autonomous Multi-Agent Workflow: Orchestrates four distinct AI entities (Searcher, Reader, Writer, and Critic) to simulate a professional research department.
* Deep-Web Scraping & Cleaning: Uses Tavily API for broad discovery and BeautifulSoup4 for targeted content extraction, stripping away HTML noise (scripts, styles, nav) for high-signal LLM input.
* Self-Correction & Peer Review: Features a Critic Agent that evaluates the generated report for clarity, technical depth, and factual consistency, providing a feedback loop for quality assurance.
* Production-Ready Deployment: Fully containerized using Docker for consistent environment replication across development and production stages.
* Modular Pipeline Design: Built with a state-managed pipeline (pipeline.py) that separates business logic from the UI layer, allowing for easy integration into other APIs or services.

# 🏗️ Technical Architecture
The system operates through a sequential and evaluative state-flow:

* Discovery Phase (Search Agent): Identifies the 5 most relevant and recent URLs using professional search tools.
* Analysis Phase (Reader Agent): Intelligently selects the highest-authority source and performs deep-content scraping.
* Synthesis Phase (Writer Chain): Merges discovery and analysis data into a structured Markdown report featuring an Introduction, Key Findings, and Bibliography.
* Audit Phase (Critic Agent): Conducts a final review of the output, highlighting strengths and identifying areas for improvement.

# 🛠️ Tech Stack

* LLM Orchestration: LangChain, ChatHuggingFace
* Inference Engine: Qwen/Qwen3-Coder-Next (via Hugging Face Endpoint)
* Web Intel: Tavily AI, BeautifulSoup4, Requests
* Frontend: Streamlit (Custom CSS-themed UI)
* Infrastructure: Docker, Python-dotenv

# 📦 Installation & Setup
Prerequisites

* Python 3.10+
* Hugging Face API Token
* Tavily API Key

Local Setup

1. Clone the Repo:
```
git clone https://github.com/Anvesh-Vishwakarma/Multi-Agentic-Research-System-.git
```

2. Environment Configuration:
Create a .env file in the root directory:
```
HUGGINGFACE_API_KEY=your_hf_token
TAVILY_API_KEY=your_tavily_key
```

3. Install Dependencies:
```
pip install -r requirement.txt
```

4. Launch Application:
```
streamlit run app.py
```














