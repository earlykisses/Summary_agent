import google.generativeai as genai
from PyPDF2 import PdfReader

# =====================
# Configure Gemini API
# =====================
genai.configure(api_key="AIzaSyAQwCIHD62GwMdh9BfA1S5PZPTBJ_ptA4I")  # replace with your key

# ---------------------
# File Readers
# ---------------------
def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

# ---------------------
# Gemini Function
# ---------------------
def summarize_and_quiz_gemini(text):
    prompt = f"""
    I have the following study notes:

    {text}

    Please do two things:
    1. Give me a clear, concise summary (complete).
    2. Create 10 quiz questions based on the notes.
    """

    model = genai.GenerativeModel("gemini-2.0-flash-001")
    response = model.generate_content(prompt)
    return response.text

# ---------------------
# Main
# ---------------------
if __name__ == "__main__":
    file_path = input("Enter your notes file (.txt or .pdf): ").strip()

    if file_path.endswith(".txt"):
        note_text = read_txt(file_path)
    elif file_path.endswith(".pdf"):
        note_text = read_pdf(file_path)
    else:
        print("❌ Unsupported file type. Use .txt or .pdf")
        exit()

    result = summarize_and_quiz_gemini(note_text)
    print("\n=== Gemini Output ===\n")
    print(result)
