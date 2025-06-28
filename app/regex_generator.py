from app.gemini_client import generate_regex_gemini

def generate_regex(prompt):
    prompt_lower = prompt.lower()

    # Static rules for known patterns
    if "email" in prompt_lower:
        return r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    elif "phone" in prompt_lower:
        return r"[6-9]\d{9}"
    else:
        # Use Gemini API
        return generate_regex_gemini(prompt)
