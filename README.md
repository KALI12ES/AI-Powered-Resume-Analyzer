# 🧠 AI-Powered Resume Analyzer

An intelligent resume analysis web app built using **FastAPI**, **Python**, and **OpenAI/Gemini APIs**, which evaluates a candidate's resume against a given job description and provides an AI-generated match score with feedback.

## 🚀 Features

- 📤 Upload a PDF Resume
- 📝 Paste a Job Description
- 🤖 Get a Match Score (out of 100) using GPT or Gemini
- 💬 Receive AI-generated feedback to improve your resume
- 🧪 Test via interactive Swagger UI (`/docs`)

---

## 🛠️ Tech Stack

| Layer      | Tech                          |
|------------|-------------------------------|
| Backend    | Python, FastAPI               |
| AI Model   | OpenAI (GPT-3.5/GPT-4) or Google Gemini (Text-Bison) |
| PDF Parser | PyMuPDF                       |
| Hosting    | Render / GCP / AWS (optional) |

---

## 📦 How to Run Locally

### 1. Clone the Repository

bash
git clone https://github.com/KALI12ES/AI-Powered-Resume-Analyzer.git
cd AI-Powered-Resume-Analyzer 

2. Set Up Environment

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

3. Add Your API Key
   
👉 Option A: OpenAI
export OPENAI_API_KEY=sk-xxxxxxxxx   # For Linux/macOS
$env:OPENAI_API_KEY="sk-xxxxxxxxx"   # For Windows PowerShell

👉 Option B: Google Vertex AI (Gemini)
Set credentials and project info in jd_matcher.py.

5. Run the Server

uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs to test the API.

🧠 Example Response

Edit
{
  "match_score": 84,
  "feedback": "The resume aligns well with the job description. You have experience with backend systems and relevant cloud platforms, which matches the requirements. Consider adding more measurable achievements."
}


✅ Repo Structure

resume-analyzer/
├── main.py
├── resume_parser.py
├── jd_matcher.py
├── requirements.txt
├── README.md
└── templates/ (optional HTML UI)


🧑‍💻 Author
Yaswanth Reddy
📍 Bengaluru, India
📧 yaswanthreddy8776@gmail.com
🔗 https://www.linkedin.com/in/yaswanth-reddy-2b1328215/
