import google.generativeai as genai
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import random
import os

# =============================
# Gemini Setup
# =============================
# GEMINI_API_KEY ="AIzaSyAQwCIHD62GwMdh9BfA1S5PZPTBJ_ptA4I"  # keep in .env OR paste directly (not safe)
genai.configure(api_key="AIzaSyAQwCIHD62GwMdh9BfA1S5PZPTBJ_ptA4I")

# -----------------------------
# File Readers
# -----------------------------
def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def read_image(file_path):
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img)
    return text

# -----------------------------
# Offline Summarizer + Quiz
# -----------------------------
def summarize_text(text, sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join(str(sentence) for sentence in summary)

def generate_quiz(text, num_questions=5):
    words = list(set([w for w in text.split() if len(w) > 6]))
    random.shuffle(words)
    questions = []
    for word in words[:num_questions]:
        questions.append(f"What does the term '{word}' mean in the context of your notes?")
    return questions

# -----------------------------
# Gemini Summarizer + Quiz
# -----------------------------
def summarize_and_quiz_gemini(text):
    prompt = f"""
    I have the following study notes:

    {text}

    Please do two things:
    1. Give me a clear, concise summary (5–6 sentences).
    2. Create 5 quiz questions based on the notes.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    file_path = input("Enter your notes file (txt/pdf/jpg/png): ").strip()

    if file_path.endswith(".txt"):
        note_text = read_txt(file_path)
    elif file_path.endswith(".pdf"):
        note_text = read_pdf(file_path)
    elif file_path.lower().endswith((".jpg", ".jpeg", ".png")):
        note_text = read_image(file_path)
    else:
        print("Unsupported file type.")
        exit()

    print("\n=== Gemini Output ===\n")
    print(summarize_and_quiz_gemini(note_text))

    print("\n=== Offline Output ===\n")
    print("Summary:", summarize_text(note_text))
    print("Quiz:")
    for q in generate_quiz(note_text, 5):
        print("-", q)
