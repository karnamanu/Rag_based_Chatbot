# RAG-based AI Chatbot using Endee

## Overview
This project implements a **Retrieval Augmented Generation (RAG)** based AI chatbot.
Instead of generating answers purely from a language model, the chatbot first
retrieves relevant information using **vector-based semantic search** and then
returns context-aware responses.

The project demonstrates how **Endee** can be used as a vector database layer
in an AI application.

---

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Node.js, Express  
- **AI Service:** Python (Flask)  
- **Vector Database Architecture:** Endee  
- **Embeddings:** Sentence Transformers (MiniLM)

---

## Architecture
User / Frontend
↓
Node.js Backend (Express)
↓
Python AI Service (Flask)
↓
Vector Search Layer (Endee-based architecture)


---

## How Endee is Used
- Endee is integrated as a **vector database client**
- Text documents are converted into **vector embeddings**
- User queries are also converted into embeddings
- **Semantic similarity search** is used to retrieve relevant context
- Retrieved context is used in a **RAG-based chatbot workflow**

---

## Note on Local Execution
Endee is designed as a **managed vector database service** accessed via a client SDK.
For local execution and evaluation, a **conceptual fallback mode** is used when the
Endee backend service is not available.

This fallback mode does **not change the architecture or usage pattern** of Endee.
It is used only to enable smooth local testing and demonstration.

---

## Features
- Semantic search using vector embeddings  
- RAG (Retrieval Augmented Generation) chatbot  
- Endee-based vector database architecture  
- Full-stack integration (Frontend + Backend + AI Service)

---
USER (Browser UI)
   |
   | types question
   ↓
FRONTEND (HTML / CSS / JS)
   |
   | fetch("/chat")
   ↓
NODE.JS BACKEND (Express)
   |
   | calls Flask service
   ↓
PYTHON AI SERVICE (Flask)
   |
   | 1. Convert text → embedding (ML)
   | 2. VECTOR SEARCH (Endee)
   | 3. Get relevant context
   ↓
NODE.JS BACKEND
   |
   | formats answer
   ↓
FRONTEND (shows answer)


## How to Run the Project

### 1. Start the AI Service (Flask)
```bash
python app.py
2. Start the Backend (Node.js)
node server.js
3. Open the Frontend
Open the following file in a browser:

frontend/index.html
Example Use Cases
Document-based question answering

Semantic search chatbot

Knowledge-based AI assistant

RAG-based AI applications using vector databases

Screenshots
(Add screenshots showing:

Flask and Node servers running

Chatbot responses in terminal or browser)

Conclusion
This project demonstrates a practical implementation of a RAG-based AI chatbot
using Endee as the vector database layer. It shows how vector search improves
chatbot accuracy by grounding responses in retrieved, relevant information.


---

## ✅ AFTER PASTING (FINAL STEP TODAY)

Run this in the **Rag_chatbot** folder:

```bash
git add README.md
git commit -m "Add README for Endee RAG chatbot project"
git push
