# LinkedIn Post Generator 🚀  

**Streamlit App**: [LinkedIn Post Generator](https://huggingface.co/spaces/DrishtiSharma/linkedin-post-generator)  

---

## Overview  

The **LinkedIn Post Generator** is a Streamlit-based application designed to help users create engaging, impactful, and professional LinkedIn posts. It utilizes Large Language Models (LLMs) with few-shot learning to generate customized posts based on user preferences like topic, tone, language, and length.  

The app offers an intuitive interface, post analysis, and history management, making it a perfect tool for professionals aiming to streamline their LinkedIn content creation process.  

---

## Table of Contents  

1. [Features](#features)  
2. [Streamlit App](#streamlit-app)  
3. [Tools and Libraries Used](#tools-and-libraries-used)  
4. [Workflow Diagram](#workflow-diagram)  
5. [Project Structure](#project-structure)  
6. [Setup Instructions](#setup-instructions)  
7. [Usage](#usage)  
    - [Running the Streamlit Web App](#running-the-streamlit-web-app)  
8. [Future Enhancements](#future-enhancements)  

---

## Features  

- **Customizable Post Generation**:  
  - Select a topic (tag) and customize the post's length, tone, and language.  
  - Add additional context to refine the generated post further.  

- **Post Analysis**:  
  - Analyze generated posts for word count, character count, and tone detection.  

- **Post Management**:  
  - Maintain a session history of generated posts.  
  - Download posts as a JSON file or clear the history.  

- **Few-Shot Learning**:  
  - Generate posts based on examples extracted from preprocessed datasets for better relevance.  

---

## Streamlit App  

Access the live application here:  
[**LinkedIn Post Generator**](https://huggingface.co/spaces/DrishtiSharma/linkedin-post-generator)  

Use the intuitive interface to effortlessly generate and customize LinkedIn posts tailored to your needs.  

---

## Tools and Libraries Used  

- **Programming Language**: Python  
- **Libraries**:  
  - [Streamlit](https://streamlit.io): For building the web interface.  
  - [LangChain](https://langchain.com): To manage and streamline LLM prompts.  
  - [ChatGroq](https://chatgroq.com): For generating posts with state-of-the-art LLMs.  
  - [Pandas](https://pandas.pydata.org): For processing and filtering post data.  

- **Language Models**:  
  - Llama-based models for generating text dynamically.  

---

## Workflow Diagram  

<img width="549" alt="image" src="https://github.com/user-attachments/assets/9f33e882-0fa3-4d0d-96fc-47e54a23bdf2">

1. User provides input through the sidebar.  
2. Preferences are used to generate a custom LinkedIn post.  
3. Generated posts are analyzed and stored in session history.  
4. Users can download posts or clear history.  

Refer to [workflow.md](workflow.md) for a detailed step-by-step process.  

---

## Project Structure  

```plaintext  
📦 LinkedIn Post Generator  
├── 📂 data  
│   ├── raw_posts.json           # Raw LinkedIn post data  
│   ├── processed_posts.json     # Processed data with metadata  
├── README.md                    # Project documentation  
├── app.py                       # Streamlit application code  
├── few_shot.py                  # Few-shot learning helper for example-based post generation  
├── llm_helper.py                # Integration with ChatGroq for LLM interaction  
├── post_generator.py            # Core logic for generating LinkedIn posts  
├── preprocess.py                # Data preprocessing and tag unification logic  
├── requirements.txt             # Python dependencies  
└── workflow.md                  # Workflow documentation  
```  

---

## Setup Instructions  

### Step 1: Clone the Repository  

```bash  
git clone https://github.com/DrishtiShrrrma/linkedin-post-generator.git  
cd linkedin-post-generator  
```  

### Step 2: Install Dependencies  

```bash  
pip install -r requirements.txt  
```  

### Step 3: Set Up Environment Variables  

- Create a `.env` file in the project root.  
- Add your ChatGroq API key:  
  ```plaintext  
  GROQ_API_KEY=your_api_key  
  ```  

---

## Usage  

### Running the Streamlit Web App  

To run the app locally:  

```bash  
streamlit run app.py  
```  

- Open the URL displayed in your terminal (default: `http://localhost:8501`).  
- Use the sidebar to customize your post preferences:
  - Select topic (tag), tone, length, and language.  
  - Add additional context if desired.  
- Click **Generate Post** to create your LinkedIn post.  
- Analyze the generated post and manage your session history.  

---

## Future Enhancements  

- **Multilingual Support**: Expand language options for global users.  
- **Sentiment Analysis**: Tailor responses based on user sentiment for more empathetic posts.  
- **Voice Input**: Integrate speech-to-text for accessibility.  
- **Enhanced Tag Management**: Improve tag extraction and unification with advanced NLP.  
- **Post Scheduling**: Add integration with LinkedIn API to schedule posts directly.  

---

## Reference

https://www.youtube.com/watch?v=qZ_J-Xg0QM4 
