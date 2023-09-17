import requests
from config import properties
from config import endpoints

def get_goals_scored():
    response = requests.get(f'{BASE_URL}/team?key={API_KEY}')
    if response.status_code == 200:
        return response.json()
    return None

print(get_goals_scored())