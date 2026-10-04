def get_response(user_input):
    """
    Process user input and return an appropriate response.
    Uses if-elif statements to match predefined patterns.
    """
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you doing", "how's it going"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "see you", "farewell"]:
        return "Goodbye!"
    elif user_input in ["what's your name", "who are you"]:
        return "I'm a simple rule-based chatbot."
    elif user_input in ["help"]:
        return "Try saying: hello, how are you, bye, what's your name, or help"
    else:
        return "I don't understand that. Try saying 'help' for options."


def main():
    """
    Main chatbot loop that continuously interacts with the user.
    """
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    print("Chatbot: Type 'help' to see what I can do.")
    print("-" * 50)
    
    while True:
        # Get input from user
        user_input = input("You: ")
        
        # Check for empty input
        if not user_input.strip():
            print("Chatbot: Please say something!")
            continue
        
        # Get response
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        
        # Exit if user says goodbye
        if user_input.lower().strip() in ["bye", "goodbye", "see you", "farewell"]:
            break


if __name__ == "__main__":
    main()
