import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
#MODEL_NAME = "llama-3.1-8b-instant"
MODEL_NAME = "qwen/qwen3.8-27b"