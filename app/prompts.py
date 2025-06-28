def build_gpt_prompt(user_input):
    return f"""
You are a regex generator.

Given the following user instruction, generate a valid regular expression (regex) without any explanation or extra text. Only output the pure regex pattern without backticks or code blocks.

User Instruction: {user_input}
"""
