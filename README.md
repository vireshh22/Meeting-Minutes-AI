# 🎙️ Meeting Minutes AI

An AI-powered application that automatically converts meeting audio into structured meeting minutes using **Whisper**, **Llama**, and **Gradio**.

---

## 📌 Overview

Meeting Minutes AI simplifies meeting documentation by transcribing meeting recordings and generating professional meeting minutes in multiple formats.

The application combines automatic speech recognition (ASR) with large language models (LLMs) to reduce manual note-taking and improve meeting productivity.

---

## ✨ Features

* 🎤 Speech-to-Text using Whisper
* 🤖 AI-generated Meeting Minutes using Llama
* 🌍 Multiple Output Languages

  * English
  * Hindi
  * Marathi
* 📝 Multiple Output Styles

  * Professional
  * Executive Summary
  * Bullet Points
  * Agile Sprint Notes
* 📄 Export as TXT
* 📄 Export as PDF
* 📄 Export as DOCX
* 🎨 Interactive Gradio Interface
* ⚡ GPU Acceleration Support
* ✅ Error Handling and Progress Indicators

---

## 🏗️ Project Architecture

```
                   Audio Recording
                          │
                          ▼
              Whisper Speech Recognition
                          │
                          ▼
                    Transcript
                          │
                          ▼
                 Prompt Engineering
                          │
                          ▼
                 Llama Language Model
                          │
                          ▼
               Structured Meeting Minutes
                          │
        ┌────────────┬────────────┬────────────┐
        ▼            ▼            ▼
       TXT          PDF         DOCX
```

---

## 📁 Project Structure

```
Meeting-Minutes-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── prompts/
├── services/
├── utils/
├── assets/
├── outputs/
└── sample_audio/
```

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Hugging Face Transformers
* Whisper
* Llama
* Gradio
* ReportLab
* python-docx

---

## 👨‍💻 Author

**Viresh Hiremath**

GitHub: https://github.com/vireshh22

---

## ⭐ If you found this project useful, consider giving it a star.
