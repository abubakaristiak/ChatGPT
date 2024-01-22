import openai
openai.api_key = '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'   # this is my turbo-3.5 api security key


messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
while True:
    message = input("User (Type what you want!): ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
