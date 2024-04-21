import requests

def ask(question):
    prompt = {
        "modelUri": "gpt://b1go49j0b7vtucfjk8dm/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "100"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты персональный помощник по имени Ева. Отвечай кратко"
            },
            {
                "role": "user",
                "text": question
            }
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNw3ylZdvbaDGdt2fsfqoQDJtTFHlBFcA75AM9"
    }

    response = requests.post(url, headers=headers, json=prompt)
    res = response.text.split('"')[13]
    table = str.maketrans({'`': '', '(': '', ')': ' ', '@': 'at ', '_': ' ', '*': ''})
    return res.translate(table)


