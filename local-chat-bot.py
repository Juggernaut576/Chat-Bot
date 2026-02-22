from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
from dotenv import load_dotenv

# Load environment variables (for LangSmith)
load_dotenv()

# Prompt Template (use normal PromptTemplate for OllamaLLM)
prompt = PromptTemplate.from_template(
    "Answer the following question:\n\n{question}"
)

# Streamlit UI
st.title("LangChain Demo with Ollama + LangSmith")
input_text = st.text_input("Enter your question here:")

# Ollama LLM
llm = OllamaLLM(model="llama3.2")

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Run only when user enters text
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)