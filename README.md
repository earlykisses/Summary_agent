AI Study Agent 📚

AI Study Agent is a Streamlit web app that helps you turn your study notes into interactive summaries and quizzes. Simply upload your notes in TXT, PDF, or image format, and the AI generates a concise summary and a set of quiz questions with answers.

Features

✅ Upload notes in TXT, PDF, or image (JPG/PNG) formats

✅ Extracts text from files using PyPDF2 (PDF) and pytesseract (images)

✅ Generates clear bullet-point summaries

✅ Creates interactive quizzes based on your notes

✅ Uses Google Gemini 2 AI for content generation

✅ Neat and readable output

Installation

Clone the repository:

git clone https://github.com/earklykisses/Summary_agent.git
cd Summary_agent


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Install Tesseract OCR (required for image text extraction):

Windows: Download installer

Mac: brew install tesseract

Linux: sudo apt install tesseract-ocr

Usage

Run the Streamlit app:

streamlit run app.py


Open the URL in your browser (usually http://localhost:8501)

Upload a file (TXT, PDF, or image)

View the generated summary and quiz

File Handling

TXT: Reads text directly

PDF: Extracts text using PyPDF2

Images: Extracts text using pytesseract

Configuration:-

Set your Google Gemini API key in the code:-

"genai.configure(api_key="YOUR_API_KEY")"

Requirements:-
Python 3.9+
streamlit
google-generativeai
PyPDF2
Pillow
pytesseract

Create a requirements.txt with:-
streamlit
google-generativeai
PyPDF2
Pillow
pytesseract

