import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract

genai.configure(api_key="AIzaSyAQwCIHD62GwMdh9BfA1S5PZPTBJ_ptA4I") 
def read_txt(file):
    return file.read().decode("utf-8")

def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

def read_image(file):
    img = Image.open(file)
    text = pytesseract.image_to_string(img)
    return text

def summarize_and_quiz_gemini(text):
    prompt = f"""
    I have the following study notes:

    {text}

    Please do these things:
    1. Give me a clear, concise summary in bullentin point in good layout.
    2. Create 10 quiz questions based on the notes.
    3. Provide answers to the quiz questions.
    4. Format the output neatly.
    5. Make the quiz more interactive and engaging.
    """
    model = genai.GenerativeModel("gemini-2.0-flash-001")
    response = model.generate_content(prompt)
    return response.text
def main():
    st.title("📚 AI Study Agent")
    st.write("Upload your notes (TXT, PDF, or Image) and get a summary + quiz!")

    uploaded_file = st.file_uploader("Choose a file", type=["txt","pdf","jpg","jpeg","png"])

    if uploaded_file:
        if uploaded_file.name.endswith(".txt"):
            note_text = read_txt(uploaded_file)
        elif uploaded_file.name.endswith(".pdf"):
            note_text = read_pdf(uploaded_file)
        elif uploaded_file.name.lower().endswith((".jpg","jpeg","png")):
            note_text = read_image(uploaded_file)
        else:
            st.error("Unsupported file type")
            st.stop()

        with st.spinner("Generating summary and quiz..."):
            result = summarize_and_quiz_gemini(note_text)

        st.subheader("📄 Summary + Quiz")
        st.text(result)

if __name__ == "__main__":
    main()
