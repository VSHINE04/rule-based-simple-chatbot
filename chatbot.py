import nltk
import re
from nltk.chat.util import Chat,reflections

pairs = [
    [r"hi|hello|hey", ["Hello! Welcome to LearnX, your personal learning assistant."]],
    [r"i want to learn python", ["Great choice! You can start with our Python Basics course. Would you like a link?"]],
    [r"what courses do you have?", ["We offer courses on Python, Web Development, Data Structures, and more!"]],
    [r"how do i login?", ["Click on the 'Login' button at the top right and enter your email and password."]],
    [r"i forgot my password", ["No worries! Click on 'Forgot Password' on the login page to reset it."]],
    [r"bye|exit", ["Goodbye! Happy learning with LearnX!"]],
    [r"(.*)", ["Sorry, I didn't get that. You can ask about courses, login, or help."]]
]
class RuleBasedChatbot:
    def __init__(self,pairs):
        self.chat = Chat(pairs,reflections)

    def respond(self,user_input):
        return self.chat.respond(user_input)

def chat_with_bot():
    print("Hello, I am your chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

chatbot = RuleBasedChatbot(pairs)
chat_with_bot()