# tiny-pdf-extractor
This is a personal project I started to build a simple PDF summarizer using Python. The idea is to let users upload a PDF and get a quick summary of its contents. Eventually, I want to make it available online through GitHub Pages, so anyone can use it without installing anything.
I’m still learning Python, so some parts of this have been a bit tricky—but I’m figuring things out step by step.

What’s Working
- I’ve set up a Python environment (3.12.1) and installed the PyPDF2 library, which lets me extract text from PDF files.
- The basic summarizer script works when run in the correct environment—it can read a PDF and generate a summary.
- I’ve written documentation and started organizing the project so it’s easier to follow.

What’s Not Working (Yet)
- Python version conflict: I accidentally ran the script using Python 3.13.5, but PyPDF2 was installed in 3.12.1. This caused a ModuleNotFoundError. I haven’t resolved this yet, but I plan to either install the library in 3.13.5 or switch the interpreter.
- Submodule issues: The summarizer depends on a submodule called PDF-Extract-Kit. I originally pointed it to a repo under my own username, which doesn’t exist. That caused GitHub Actions to fail during builds. I’ve now fixed the reference to point to the correct repo: opendatalab/PDF-Extract-Kit.
- Text formatting: Some PDFs mash lines together when extracted, which makes the summaries messy. I’ll need to add some logic to clean up the text before summarizing. But this is veeeeeery tricky for me, I could use copilot but it ruins the purpose, so I will try to figure it out on my own using various forums or overflow.

Hosting Plans
Since GitHub Pages only supports static content, I’ll need to host the Python backend somewhere else—like Replit, Render, or Hugging Face Spaces. The plan is:
- Host the frontend (HTML/JS) on GitHub Pages.
- Host the backend (Python summarizer) on a platform that supports Python.
- Connect the two via API calls so users can upload PDFs and get summaries directly from the browser.

Why This Project Matters to Me
I’m doing this mostly to learn—Python, Git, GitHub Actions, and how to build something that actually works online. I’ve hit a few bumps, but each one’s been a chance to understand things better. This project is still in progress, and I’ll keep updating it as I go.(hopefully)
