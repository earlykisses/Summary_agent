import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAQwCIHD62GwMdh9BfA1S5PZPTBJ_ptA4I")

def summarize_and_quiz_gemini(text):
    prompt = f"""
    I have the following study notes:

    {text}

    Please do two things:
    1. Give me a clear, concise summary (5–6 sentences).
    2. Create 5 quiz questions based on the notes.
    """

    model = genai.GenerativeModel("gemini-2.0-flash-001")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    with open("notes.txt", "r", encoding="utf-8") as f:
        note_text = f.read()

    result = summarize_and_quiz_gemini(note_text)
    print(result)
