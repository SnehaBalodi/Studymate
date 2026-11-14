from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from openai import AuthenticationError, OpenAI
import uvicorn

load_dotenv()

# Explicitly fetch your Nebius key from the .env file
nebius_key = os.getenv("NEBIUS_API_KEY")

# Initialize the OpenAI client pointing to the Nebius server
client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=nebius_key
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "StudyMate AI is running!"}

@app.get("/ask")
def ask(question: str):
    try:
        response = client.chat.completions.create(
            model="nvidia/NVDA-Nemotron-Nano-9B-v2",
            messages=[
                {
                    "role": "system",
                    "content": "You are StudyMate, a helpful AI study assistant. Explain concepts clearly."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
    except AuthenticationError as error:
        raise HTTPException(
            status_code=503,
            detail="Nebius authentication failed. Set a valid NEBIUS_API_KEY in .env and restart the server."
        ) from error

    return {"response": response.choices[0].message.content}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)