from ollama import Client

client = Client()

def ask_model(prompt):
    response = client.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": "Answer only one number between 0 and 180."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']
