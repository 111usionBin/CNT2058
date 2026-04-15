import os

from dotenv import load_dotenv
from google import genai

# Load variables from .env into environment.
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="안녕"
)
print(response.text)