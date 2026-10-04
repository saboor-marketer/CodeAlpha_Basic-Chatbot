# Basic Chatbot

A simple rule-based chatbot built with Python that responds to predefined user inputs.

## Description

This chatbot demonstrates fundamental programming concepts including:
- **Functions**: Modular code organization with `get_response()` and `main()`
- **If-elif statements**: Pattern matching for user inputs
- **Loops**: Continuous interaction using a `while` loop
- **Input/Output**: User interaction via `input()` and `print()`

## Features

- Greeting responses (hello, hi, hey, greetings)
- Status check responses (how are you, how are you doing, how's it going)
- Farewell responses (bye, goodbye, see you, farewell)
- Identity responses (what's your name, who are you)
- Help command to show available options
- Handles empty input gracefully

## Requirements

- Python 3.x

## Installation

No additional packages required. This uses only Python standard library.

## Usage

1. Navigate to the project directory:
```bash
cd "C:\Users\Dell\Desktop\Basic Chatbot"
```

2. Run the chatbot:
```bash
python chatbot.py
```

3. Interact with the chatbot by typing messages and pressing Enter

4. Type `bye` to exit the program

## Example Conversation

```
Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.
Chatbot: Type 'help' to see what I can do.
--------------------------------------------------
You: hello
Chatbot: Hi!
You: how are you
Chatbot: I'm fine, thanks!
You: what's your name
Chatbot: I'm a simple rule-based chatbot.
You: bye
Chatbot: Goodbye!
```

## Supported Commands

| Command | Response |
|---------|----------|
| hello, hi, hey, greetings | Hi! |
| how are you, how are you doing, how's it going | I'm fine, thanks! |
| bye, goodbye, see you, farewell | Goodbye! |
| what's your name, who are you | I'm a simple rule-based chatbot. |
| help | Shows available commands |

## Code Structure

- `get_response(user_input)`: Processes user input and returns appropriate response using if-elif statements
- `main()`: Main program loop that handles continuous user interaction
- `if __name__ == "__main__":`: Entry point for the program

## Future Enhancements

- Add more response patterns
- Implement case-insensitive matching (already implemented)
- Add random responses for variety
- Implement conversation context/memory
- Add more sophisticated pattern matching
