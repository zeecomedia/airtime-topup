import requests


from fastapi import FastAPI

app = FastAPI()


@app.post("/topup")
async def topup_airtime():
    url = "https://dancitysub.com/api/data/"
    payload = {
        "network": "MTN",
        "mobile_number": "08166XXXXXX",
        "plan": 7,
        "Ported_number": True
    }
    headers = {
        'Authorization': f'Token {AUTH}',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=payload, 
                             headers=headers)

    return response.json()







