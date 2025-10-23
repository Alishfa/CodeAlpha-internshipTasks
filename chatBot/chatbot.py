import random
from datetime import datetime
import pyjokes

def get_response(user_input):
    user_input = user_input.lower()
    if any(greet in user_input for greet in['hello','hi','hey']):
        return random.choice([ "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to meet you!"])
    elif 'time' in user_input:
        current_time=datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif 'date' in user_input:
        current_date=datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {current_date}."
    elif any(word in user_input for word in ['how are you','how is it going']):
        return random.choice(["I'm doing great! thanks for asking!",
            "I'm functioning as expected! How about you?",
            "All systems operational! What about you?"])
    elif 'joke' in user_input:
        return random.choice([pyjokes.get_joke(category='all')])
    elif any(bye in user_input for bye in ['bye','goodbye','see you']):
        return random.choice(["Goodbye! Have a great day!",
            "See you later! Take care!",
             "Bye! Looking forward to our next chat!"])
    elif 'thank you' in user_input or 'thanks' in user_input:
        return random.choice(["You're welcome!",
            "No problem! Happy to help!",
            "Anytime! Let me know if you need anything else!"])
    elif 'help' in user_input:
        return ("I can help you with:\n"
                "- Greetings (say hello!)\n"
                "- Tell you the time and date\n"
                "- Have a simple conversation\n"
                "- Just try talking to me!")
    else:
        return random.choice([
            "That's interesting! Tell me more.",
            "I'm not sure I understand. Can you rephrase that?",
            "Hmm, I'm still learning. What else would you like to talk about?",
            "Could you ask me something else? I'm still a simple bot!"
        ])
def main():
    # Print welcome message
    print("=" * 50)
    print("Welcome to PyBot - Your Simple Python Chatbot!")
    print("=" * 50)
    print("Type 'quit' or 'exit' to end the conversation.\n")
    while True:
        User_input=input("You: ")
        if not User_input.strip():
            print("PyBot: Please enter a message.")
            continue
        if User_input.lower()in['exit','quit']:
            break
        response=get_response(User_input)
        print(f"PyBot: {response}\n")
if __name__=="__main__":
    main()