# Interactive PDF Summarization & Q&A with AWS Bedrock (RAG with FAISS + LangChain)

## 📖 Overview
This app lets you **chat with your PDFs** and get detailed summaries/answers using
foundation models on **Amazon Bedrock**. It builds a Retrieval-Augmented Generation (RAG)
pipeline with **Titan Embeddings** for vectorization, **FAISS** for similarity search,
and **Llama 3 / Claude 3** (via Bedrock) for generation. A **Streamlit** UI ties it
all together.

There are two variants provided (you can keep one or both):
1. Chat with Screenplays (folder: `screenplays`, FAISS index: `faiss_index_screenplays`)
2. Chat with PDFs (folder: `data`, FAISS index: `faiss_index`)

---

## ✅ Prerequisites
- Python 3.10+ recommended  
- An AWS account with access to **Amazon Bedrock** in a supported region  
- AWS CLI installed (`aws --version` to verify)  
- The following Bedrock models access requested:  
  - Embeddings: `amazon.titan-embed-text-v2:0`  
  - LLM (primary): `meta.llama3-70b-instruct-v1:0`  
  - LLM (optional/fast): `anthropic.claude-3-haiku-20240307-v1:0`  

> ⚠️ **Note:** Amazon Bedrock is region-specific. Ensure your AWS region supports both Titan Embeddings and your chosen LLMs.

---

## 🔑 Step 1 — Create an IAM user with programmatic access
1. Go to **AWS Console → IAM → Users → “Create user”**  
2. Name: `bedrock-rag-user` (or any name)  
3. Access type: **Programmatic access**  
4. Attach a custom inline policy like:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels"
      ],
      "Resource": "*"
    }
  ]
}
```

5. Save the **Access Key ID** and **Secret Access Key**.

---

## ⚙️ Step 2 — Configure AWS CLI
Run:
```bash
aws configure
```
Provide:  
- AWS Access Key ID  
- AWS Secret Access Key  
- Default region (e.g., `us-east-1`)  
- Output format: `json`  

---

## 📥 Step 3 — Request Model Access in Bedrock
1. Go to **AWS Console → Amazon Bedrock → Model access**  
2. Request access for:  
   - `amazon.titan-embed-text-v2:0`  
   - `meta.llama3-70b-instruct-v1:0`  
   - `anthropic.claude-3-haiku-20240307-v1:0` (optional)  
3. Wait until status = **Access granted**.  

---

## 📂 Step 4 — Project Structure
```
.
├── screenplay_rag.py      # App for screenplays (uses ./screenplays)
├── app.py              # App for general PDFs (uses ./data)
├── screenplays/             # Put screenplay PDFs here
├── data/                    # Put other PDFs here
└── README.txt               # This file
```

---

## 🐍 Step 5 — Setup Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# OR
.venv\Scripts\activate    # Windows
```

---

## 📦 Step 6 — Install Dependencies
```bash
pip install --upgrade pip
pip install boto3 streamlit langchain langchain-community faiss-cpu pypdf numpy
```

---

## 📑 Step 7 — Place Your PDFs
- For **screenplay app** → place files in `./screenplays`  
- For **generic PDF app** → place files in `./data`  

The app will build a FAISS index after clicking **Vectors Update** in the sidebar.

---

## ▶️ Step 8 — Run the Apps
```bash
# Screenplays Q&A app
streamlit run screenplay_rag.py

# General PDF Q&A app
streamlit run app.py
```

In the Streamlit UI:
- Enter your question in the text box  
- Click **Vectors Update** once to build FAISS index  
- Click **Llama2 Output** (Llama 3 in code) to generate answers  

---

## 🛠️ Troubleshooting
- **AccessDeniedException** → Ensure model access is granted in the same region as `aws configure`.  
- **FAISS warnings** → Keep `allow_dangerous_deserialization=True` when loading indexes.  
- **Apple Silicon issues** → Pin FAISS version (`pip install faiss-cpu==1.8.0`).  

---

## 📌 Tech Stack
- **AWS Bedrock** (Titan Embeddings, Llama 3, Claude 3)  
- **LangChain** (RetrievalQA, loaders, embeddings)  
- **FAISS** (vector database)  
- **Streamlit** (UI frontend)  

---

## 📜 License
MIT (or your preferred license)
