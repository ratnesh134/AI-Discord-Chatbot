import requests
from config import MANTIS_API_TOKEN, MANTIS_PROJECT_ID, MANTIS_CATEGORY, MANTIS_BASE_URL

def create_ticket(summary, description, user_email="noreply@example.com"):
    url = f"{MANTIS_BASE_URL}/api/rest/issues/"
    headers = {
        "Authorization": MANTIS_API_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "summary": summary[:100],
        "description": description,
        "project": {"id": MANTIS_PROJECT_ID},
        "reporter": {"name": user_email},
        "category": {"name": MANTIS_CATEGORY}
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        return response.json()["issue"]["id"]
    else:
        print("Error creating ticket:", response.text)
        return None
