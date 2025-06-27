import requests

url = "https://tailortalk-backend-1.onrender.com/book"

data = {
    "message": "I want to book on 2025-06-27 at 10:00"
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:")
print(response.json())

