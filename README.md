# Courses QA RAG System

## Overview

Courses QA RAG System is a Retrieval-Augmented Generation (RAG) application that answers user questions about courses, pricing, duration, prerequisites, certificates, and learning paths.

The system uses a custom CSV dataset containing course-related questions and answers, converts the data into vector embeddings using Hugging Face Instructor Embeddings, stores them in a FAISS vector database, and retrieves the most relevant information to generate accurate responses.

---

## Features

* Question Answering over course information
* Vector Search using FAISS
* Retrieval-Augmented Generation (RAG)
* Hugging Face Instructor Embeddings
* Google PaLM Integration
* Custom Prompt Engineering
* CSV-Based Knowledge Base

---

## Tech Stack

* Python
* LangChain
* Google PaLM
* FAISS
* Hugging Face Instructor Embeddings
* CSVLoader
* Python Dotenv

---

## Project Structure

```text
courses-rag/
│
├── main.py
├── coursesqa.csv
├── .env
├── faiss_index/
├── requirements.txt
└── README.md
```

---

## Dataset Format

The application uses a CSV file containing questions and answers.

Example:

| prompt                                  | response                     |
| --------------------------------------- | ---------------------------- |
| What is the price of the Python course? | The Python course costs $99. |
| How long is the Data Science course?    | The duration is 12 weeks.    |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MohamedNaeem12/courses-rag.git
cd courses-rag
```

Create a virtual environment:

```bash
conda create -n courses-rag python=3.11
conda activate courses-rag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Create Vector Database

Generate embeddings and build the FAISS index:

```bash
python main.py
```

This will:

1. Load the CSV dataset.
2. Create embeddings.
3. Store vectors inside the FAISS index.

---

## Retrieval Pipeline

```text
User Question
      ↓
Retriever
      ↓
FAISS Vector Database
      ↓
Relevant Documents
      ↓
Google PaLM
      ↓
Final Answer
```

---

## Example Questions

* What is the price of the Python course?
* How long is the Data Science course?
* Does the AI course provide a certificate?
* What are the prerequisites for Machine Learning?
* Which course should I take to become an AI Engineer?

---

## Future Improvements

* Hybrid Search (BM25 + Vector Search)
* Reranking
* Metadata Filtering
* Multi-Query Retrieval
* Streamlit User Interface
* Course Recommendation Engine
* Migration to Gemini or Open-Source LLMs

---

## Author

Mohamed Naeem

AI & Data Analysis Enthusiast
