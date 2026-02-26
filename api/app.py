from fastapi import FastAPI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

# os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LangServe API",
    version="1.0",
    description="A simple API to demonstrate LangServe with OllamaLLM and OpenAI"
)

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai",
# )


ollama_model = OllamaLLM(model="llama3.2")

# prompt1 = PromptTemplate.from_template("Write me an essay {topic} in 100 words.")
prompt2 = PromptTemplate.from_template("Write me an essay {topic} in 100 words.")

# add_routes(
#     app,
#     prompt1|model,
#     path="/essay",
# )

add_routes(
    app,
    prompt2|ollama_model,
    path="/essay",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)