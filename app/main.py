from fastapi import FastAPI, HTTPException
from app.regex_generator import generate_regex
from app.test_regex import test_regex
from fastapi.responses import JSONResponse

app = FastAPI(title="Intelligent Regex Generator")

@app.post("/generate")
def generate(prompt: str):
    regex = generate_regex(prompt)
    if regex and not regex.startswith("OpenAI Error:"):
        return {"regex": regex}
    else:
        return JSONResponse(status_code=500, content={"error": regex or "Failed to generate regex from OpenAI API."})
