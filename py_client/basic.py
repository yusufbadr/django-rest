import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Abc123", "content":"Hello World", "price": "134"})





print(get_response.json())