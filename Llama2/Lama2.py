import requests
import json

def send_message(message, model="gpt-3.5-turbo", temperature=0.7):
    url = ""

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant. And your name is 'Llama2'."
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = send_message(user_input)
        if response:
            reply = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            print("Wat-chan:", reply)

if __name__ == "__main__":
    main()
