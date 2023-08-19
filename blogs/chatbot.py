import openai

# Replace 'your-api-key' with your actual API key
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key


# Define a function to interact with the chatbot
def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,  # Adjust the response length as needed
    )
    return response.choices[0].text.strip()


# Main loop to chat with the bot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    bot_response = chat_with_bot(user_input)
    print(f"Bot: {bot_response}")

print("Goodbye!")
