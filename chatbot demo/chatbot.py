import random

# Simple rule-based chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you?": ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
}

def get_bot_response(message):
    message = message.lower()
    for key in responses.keys():
        if key in message:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand that."

# Simulated chat session
def chat_with_bot(messages):
    print("Welcome to the AI Chatbot! Type 'bye' to exit.")
    for user_input in messages:
        print(f"You: {user_input}")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye!")
            break
        response = get_bot_response(user_input)
        print(f"Bot: {response}")

# Example messages to simulate the chat
example_messages = [
    "hello",
    "how are you?",
    "what is your name?",
    "bye"
]

# Start the chat
chat_with_bot(example_messages)