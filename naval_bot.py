from chatterbot import ChatBot

chatbot = ChatBot("NavalBot")

from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train("chatterbot.corpus.english")

naval_responses = {
    "life_advice": "Invest in yourself. Your mind is your most valuable asset.",
    "investing": "Invest for the long term. Compounding is your best friend.",
    "startups": "Focus on solving problems that you're passionate about.",
    "personal_growth": "Learn continuously. Personal growth is a lifelong journey.",
    # Add more responses for different topics
}


def get_response(user_query):
    # Check if the user's query matches predefined topics
    for topic, response in naval_responses.items():
        if topic in user_query.lower():
            return response

    # If no predefined topic matches, let ChatterBot generate a response
    return chatbot.get_response(user_query).text


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("NavalBot: Goodbye!")
        break

    response = get_response(user_input)
    print("NavalBot:", response)
