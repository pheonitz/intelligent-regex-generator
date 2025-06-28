🚀 Intelligent Regex Generator (Gemini API Powered)
A FastAPI-based backend service that takes a user prompt (like "Generate regex for email validation") and returns a valid Regular Expression (Regex).
This project uses Google Gemini API (via Gemini Python SDK) for AI-powered regex generation.

✅ Features
AI-generated Regex patterns based on natural language prompts

Supports predefined patterns for common types (email, phone, URL, etc.)

Built with FastAPI

Gemini API integrated (via google-generativeai Python SDK)

Swagger UI for easy testing

✅ Tech Stack
Python

FastAPI

Gemini API (Gemini-Pro model)

Uvicorn (FastAPI server)

Dotenv (for API key management)

✅ Project Structure
graphql
Copy
Edit
intelligent-regex-generator/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entrypoint
│   ├── regex_generator.py   # Main regex generation logic
│   ├── gemini_client.py     # Gemini API call handling
│   └── prompts.py           # Builds AI prompt text
├── .gitignore
├── .env                    # (Contains your Gemini API key, ignored by Git)
├── requirements.txt
└── README.md
✅ Setup Instructions
1. Clone this repository:
bash
Copy
Edit
git clone https://github.com/yourusername/intelligent-regex-generator.git
cd intelligent-regex-generator
2. Create Python Virtual Environment:
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate # On Linux/Mac
3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
4. Setup Gemini API Key:
Get your Gemini API Key from Google AI Studio:
👉 https://aistudio.google.com/app/apikey

Create a .env file in project root and add:

ini
Copy
Edit
GEMINI_API_KEY=AIzaXXXXXXXXXXXXXXXXXXXXXXXX
✅ (Never push this file to GitHub)

5. Run FastAPI server:
bash
Copy
Edit
uvicorn app.main:app --reload
