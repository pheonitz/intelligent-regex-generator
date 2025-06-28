import google.generativeai as genai
import os
from dotenv import load_dotenv
from app.prompts import build_gpt_prompt

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def generate_regex_gemini(user_prompt):
    try:
        full_prompt = build_gpt_prompt(user_prompt)
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return f"Gemini API Error: {str(e)}"
