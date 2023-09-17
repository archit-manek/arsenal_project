import requests
from settings import properties
from settings import endpoints

def get_goals_scored():
    response = requests.get(f'{endpoints.BASE_URL}/team?key={properties.API_KEY}')
    if response.status_code == 200:
        return response.json()
    return None

print(get_goals_scored())