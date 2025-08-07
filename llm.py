import requests
from config import GROQ_API_KEY

def ask_llm(user_query):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {"role": "system", "content": "You're a helpful assistant for washing machine problems. Try to resolve the issue. If you cannot, suggest creating a support ticket."},
        {"role": "user", "content": user_query}
    ]

    payload = {
        "model": "llama3-70b-8192",
        "messages": messages,
        "temperature": 0.5
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
