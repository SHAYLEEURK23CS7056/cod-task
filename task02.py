import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I am doing well, thank you!", "I'm good, thanks for asking. How about you?"],
    "good": ["That's great to hear!", "Awesome!", "Good to know."],
    "not good": ["I'm sorry to hear that. How can I help you?", "Is there anything I can do to make you feel better?"],
    "thank you": ["You're welcome!", "No problem.", "Anytime!"],
    "bye": ["Goodbye!", "Take care!", "See you later!"],
    "default": ["I'm not sure I understand. Could you please rephrase that?"]
}

def get_response(user_input):
    """Get response based on user input"""
    for pattern, responses_list in responses.items():
        if pattern in user_input.lower():
            return random.choice(responses_list)
    return random.choice(responses["default"])

def chat():
    """Start the conversation with the chatbot"""
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            response = get_response(user_input)
            print(response)

if __name__ == "__main__":
    chat()
