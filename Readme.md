# 🧠 MCQ Generator using LangChain, OpenAI & Streamlit

---

## 📌 Overview

This project is a **web-based application** that allows users to upload textual content (PDF or TXT), and automatically generates **Multiple-Choice Questions (MCQs)** based on the uploaded content. It uses **OpenAI’s GPT-3.5** language model orchestrated via **LangChain**, and presents results in a **Streamlit** interface. The app also includes a **review step** where the generated questions are evaluated for tone and complexity.

The goal is to assist educators, trainers, and students in **rapidly creating assessments** that are contextual, accurate, and tailored to specific topics and difficulty levels.

---

## 🎯 Key Concepts Used

### 1. Natural Language Processing (NLP)
- Leveraging LLMs to understand context and generate relevant questions.
- Formatting and structuring output using prompt engineering.

### 2. Prompt Engineering
- Designing structured prompts for GPT-3.5 to follow a specific response format (`response.json`).
- Two-stage prompting: one for generation, one for evaluation.

### 3. LangChain Framework
- Used to chain multiple LLM steps together:
  - **LLMChain 1**: Generates MCQs.
  - **LLMChain 2**: Reviews and refines the MCQs.
  - Combined using `SequentialChain`.

### 4. File Parsing
- Reading text content from `.pdf` files using `PyPDF2`.
- Supporting plain `.txt` files for simplicity.

### 5. Streamlit UI
- Interactive frontend with file uploader and form fields.
- Displays formatted MCQs in a table and evaluation feedback in text.

### 6. Logging and Debugging
- Custom `logger.py` to create logs with timestamps for debugging.
- Exception handling to avoid UI crashes and provide feedback.

---

## 🛠️ Tools & Technologies

| Tool/Library     | Purpose                                  |
|------------------|------------------------------------------|
| **Python**       | Main programming language                |
| **Streamlit**    | UI development and real-time interaction |
| **OpenAI GPT-3.5** | LLM for text generation and evaluation |
| **LangChain**    | To chain and manage LLM tasks            |
| **PyPDF2**       | To extract text from PDF files           |
| **dotenv**       | To securely store API keys               |
| **pandas**       | To create and display quiz tables        |

---

## 🧱 Implementation Steps

### Step 1: Project Initialization
- Created a Python environment and initialized project structure.
- Added `.gitignore` to avoid committing sensitive files like `.env`.

### Step 2: File Handling Utilities
- Implemented `read_file()` in `utils.py`:
  - Detects file type (`.pdf` or `.txt`).
  - Uses `PyPDF2` to extract text from PDF pages.
- Implemented `get_table_data()` to parse the model's JSON output into a table-friendly format.

### Step 3: LangChain Chains (MCQ.py)
- Defined `PromptTemplate` for **MCQ generation**:
  - Prompt includes subject, tone, number of questions, and a guide format (`response.json`).
- Defined `PromptTemplate` for **reviewing** the MCQs.
- Combined both chains using `SequentialChain` as `generate_evaluate_chain`.

### Step 4: Streamlit App Interface (app.py)
- Created a form for user inputs:
  - File uploader
  - Number of questions
  - Subject
  - Difficulty tone
- Triggered backend processing on button click.
- Displayed results using:
  - `st.table()` for questions
  - `st.text_area()` for review summary

### Step 5: Logging Setup
- Used `logging` module to create timestamped log files inside a `logs/` directory.
- Captured exceptions and traced errors in both backend and UI.

---

## 📈 Example Workflow

1. User uploads a file (e.g., *biology_notes.pdf*).
2. Enters:
   - Number of MCQs: `5`
   - Subject: `Biology`
   - Tone: `Easy`
3. Application extracts text.
4. `LangChain` passes the prompt to OpenAI GPT-3.5.
5. Model generates 5 biology MCQs in the defined JSON format.
6. Second model evaluates question complexity.
7. MCQs and review summary are displayed in the frontend.
8. User downloads the csv file

---

## ✅ Output Format

Each question includes:
- Question text
- 4 answer options (a–d)
- Correct answer label

Displayed as a table in Streamlit with an accompanying review paragraph.
Also provided an option to download as a csv file.

---

## 📚 Learning Outcomes

- Building LangChain chains and customizing prompt workflows.
- Working with LLMs to generate structured output (JSON).
- Handling different file formats in Python.
- Deploying simple AI apps using Streamlit.
- Logging, debugging, and maintaining modular code.

