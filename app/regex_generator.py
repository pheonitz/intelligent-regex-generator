import openai
import os
from dotenv import load_dotenv
from app.prompts import build_gpt_prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_regex(prompt):
    prompt_lower = prompt.lower()

    # Static predefined quick patterns
    if "email" in prompt_lower:
        return r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    elif "phone" in prompt_lower and "india" in prompt_lower:
        return r"[6-9]\d{9}"
    elif "url" in prompt_lower:
        return r"https?://(?:www\.)?\S+"
    else:
        try:
            gpt_prompt = build_gpt_prompt(prompt)
            response = openai.ChatCompletion.create(
                model="gpt-4o",   # or "gpt-3.5-turbo" if you want free tier
                messages=[{"role": "user", "content": gpt_prompt}],
                temperature=0
            )
            regex_result = response['choices'][0]['message']['content'].strip()
            return regex_result
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            return f"OpenAI Error: {str(e)}"
