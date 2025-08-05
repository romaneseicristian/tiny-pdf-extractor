from flask import Flask, request, render_template, jsonify
import sys
import os

sys.path.append("PDF-Extract-Kit")
from pdf_extract_kit import extract_text_from_pdf

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    file = request.files.get("pdf")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    file_path = os.path.join("uploaded.pdf")
    file.save(file_path)

    extracted_text = extract_text_from_pdf(file_path)

    # For now, just return the raw text (you can add summarization later)
    return jsonify({"summary": extracted_text})

if __name__ == "__main__":
    app.run(debug=True)