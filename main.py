import os
import subprocess

import httpx
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from task_performer import task_manager_AI

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


load_dotenv()


openai_api_key = os.getenv("AIPROXY_TOKEN")
openai_api_chat = (
    "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"  # Test URL
)

headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json",
}


def get_completions(prompt: str):
    """
    Sends the task prompt to the API and retrieves the completion.
    """
    try:

        data = {
            "model": "gpt-4o-mini",  # Choose your preferred model here
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 150,
        }

        response = requests.post(openai_api_chat, headers=headers, json=data)

        if response.status_code == 200:
            response_data = response.json()
            completion = response_data["choices"][0]["message"]["content"]
            return {"response": completion}
        else:
            return {
                "error": f"API call failed with status code {response.status_code}",
                "details": response.text,
            }

    except Exception as e:
        return {"error": str(e)}


app = FastAPI()


@app.post("/run")
async def run_task(task_description: str):
    """
    This endpoint simulates running a task based on the task description.
    It will handle different tasks like installing packages and executing scripts.
    """
    task = get_completions(task_description)
    task_manager_AI(task)


@app.get("/ask")
def ask(prompt: str):
    """
    Receives a prompt and calls the get_completions function to process it.
    The model's response is returned.
    """
    result = get_completions(prompt)
    return result
