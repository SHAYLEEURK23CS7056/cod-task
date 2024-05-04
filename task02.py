import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking. How about you?']],
    ['(.*)(good|well|fine)', ['That\'s great to hear!', 'Awesome!', 'Good to know.']],
    ['(.*)(bad|not good)', ['I\'m sorry to hear that. How can I help you?', 'Is there anything I can do to make you feel better?']],
    ['what can you do?', ['I can provide information, answer questions, or just have a chat with you. Feel free to ask!']],
    ['(.*)(thank you|thanks)', ['You\'re welcome!', 'No problem.', 'Anytime!']],
    ['(bye|goodbye)', ['Goodbye!', 'Take care!', 'See you later!']],
    ['(.*)', ["I'm not sure I understand. Could you please rephrase that?"]]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print(response)

if __name__ == "__main__":
    chat()
