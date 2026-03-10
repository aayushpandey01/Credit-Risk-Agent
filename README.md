# Credit-Risk-Agent
An autonomous AI powered Credit Risk Monitoring system that combines traditional machine learning with modern LLM based reasoning to simulate real world banking risk analysis.

This project integrates a Probability of Default (PD) model, Early Warning Signals (EWS), portfolio drift monitoring (PSI), and an LLM agent (Groq via LangChain 1.x) to generate structured, explainable, and actionable credit risk insights.

Banks continuously monitor borrower risk to prevent defaults and manage portfolio exposure.

This system replicates a real credit risk monitoring workflow by:

Predicting Probability of Default (PD)

Detecting early warning risk triggers

Monitoring portfolio stability using PSI

Providing structured risk explanations

Suggesting mitigation strategies

Enabling natural language risk queries via LLM agent

Unlike a static dashboard, this is a tool calling autonomous AI agent capable of reasoning and decision support.


- System Architecture:-

User Query
↓
LLM Agent (Groq Llama 3 / Gemini)
↓
Tool Calling Layer
↓

PD Prediction Tool

Early Warning Tool

Drift Detection Tool (PSI)
↓
Structured Risk Analysis + Action Recommendations


📊 Core Components
1️⃣ Probability of Default (PD) Model

Logistic Regression with scaling pipeline

Trained on synthetic credit dataset

Model saved using Pickle

Customer-level risk scoring

2️⃣ Early Warning System (EWS)

Detects critical risk indicators such as:-

High credit utilization

Multiple missed payments

High Days Past Due (DPD)

3️⃣ Portfolio Drift Monitoring

Implements:-

Population Stability Index (PSI)

Drift detection for model monitoring

Portfolio health analysis

4️⃣ Autonomous LLM Agent

Built using LangChain

Tool calling architecture

Structured professional responses

Financial risk reasoning

Actionable mitigation suggestions

Supports:-

Groq

5️⃣ Streamlit Interface

Interactive UI

Natural language queries

Real time AI reasoning

Customer level analysis

🛠 Tech Stack

Python

Scikit-learn

Logistic Regression

Streamlit

LangChain

Groq 

Population Stability Index (PSI)

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-url>
cd credit_risk_agent
2️⃣ Create Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set API Key

For Groq:-

setx GROQ_API_KEY "your_api_key"

Restart terminal after setting the key.

5️⃣ Train Model
python model/train_model.py
6️⃣ Run Application
streamlit run app_agent.py
