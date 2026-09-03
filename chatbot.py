"""
CodeAlpha Internship Task 4: Basic Chatbot
Author: Palak Panchal
Description: A beginner-friendly, rule-based chatbot built using Python standard library.
"""

import random


def normalize_input(user_input: str) -> str:
    """
    Cleans and normalizes user input by:
    - Converting text to lowercase
    - Stripping leading and trailing whitespace
    - Removing common punctuation marks
    - Collapsing multiple consecutive spaces into a single space

    Parameters:
        user_input (str): The raw text entered by the user.

    Returns:
        str: Cleaned and normalized text.
    """
    cleaned = user_input.lower().strip()
    punctuation_to_remove = "?!.,:;\"'~`"
    cleaned = "".join(char for char in cleaned if char not in punctuation_to_remove)
    return " ".join(cleaned.split())


def get_fallback_response() -> str:
    """
    Returns a randomly selected polite fallback response when user input is not recognized.

    Returns:
        str: A fallback response.
    """
    fallbacks = [
        "I'm not sure I understand. Could you rephrase that?",
        "I don't have an answer for that yet. Type 'help' to see what I can answer!",
        "Sorry, I didn't catch that. Try asking something else or type 'help'.",
        "I'm still learning! Could you try asking in a different way?",
        "I didn't quite get that. Type 'help' for a list of things you can ask me.",
    ]
    return random.choice(fallbacks)


def get_help_message() -> str:
    """
    Returns a formatted help message listing supported conversation topics.

    Returns:
        str: The help message string.
    """
    return (
        "Here are some examples of what you can ask me:\n"
        "  - Greetings: 'hello', 'hi', 'hey', 'good morning', 'good evening'\n"
        "  - Status & Purpose: 'how are you?', 'who created you?', 'what is your purpose?'\n"
        "  - Identity: 'what is your name?', 'tell me about yourself'\n"
        "  - Assistance: 'what can you do?', 'how can you help me?'\n"
        "  - Pleasantries: 'nice to meet you', 'thank you', 'ok', 'yes', 'no'\n"
        "  - Exit: 'bye', 'goodbye', 'exit', 'quit', 'see you'"
    )


def get_response(user_input: str, user_name: str = "") -> str:
    """
    Processes user input and returns an appropriate rule-based response.

    Parameters:
        user_input (str): The raw text entered by the user.
        user_name (str): Optional name of the user for session personalization.

    Returns:
        str: The chatbot's response.
    """
    normalized = normalize_input(user_input)

    # 1. Greetings
    if normalized in ["hello", "hi", "hey", "greetings"]:
        if user_name:
            return f"Hi {user_name}! How can I help you today?"
        return "Hi! How can I help you today?"

    # 2. Time-of-day greetings
    elif normalized in ["good morning", "morning"]:
        greeting_suffix = f", {user_name}" if user_name else ""
        return f"Good morning{greeting_suffix}! Hope you have a wonderful day ahead!"

    elif normalized in ["good afternoon", "afternoon"]:
        greeting_suffix = f", {user_name}" if user_name else ""
        return f"Good afternoon{greeting_suffix}! How is your day going so far?"

    elif normalized in ["good evening", "evening"]:
        greeting_suffix = f", {user_name}" if user_name else ""
        return f"Good evening{greeting_suffix}! How can I assist you tonight?"

    elif normalized in ["good night", "night"]:
        greeting_suffix = f", {user_name}" if user_name else ""
        return f"Good night{greeting_suffix}! Sleep well and take care!"

    # 3. Status and well-being
    elif normalized in ["how are you", "how are you doing", "hows it going", "how is it going"]:
        return "I'm doing great, thank you for asking! How about you?"

    # 4. Chatbot name and identity
    elif normalized in ["what is your name", "who are you", "whats your name"]:
        return "I'm a simple rule-based chatbot created in Python."

    elif normalized in ["tell me something about yourself", "tell me about yourself", "about yourself"]:
        return (
            "I am a lightweight, rule-based chatbot designed to demonstrate "
            "core Python programming concepts like string normalization, "
            "conditional logic, and modular functions."
        )

    # 5. Creator, purpose, and capabilities
    elif normalized in ["who created you", "who made you", "who is your creator"]:
        return "I was created by Palak Panchal as part of the CodeAlpha Internship."

    elif normalized in ["what is your purpose", "whats your purpose", "why were you created"]:
        return "My purpose is to demonstrate a rule-based conversational assistant using clean Python standard library code."

    elif normalized in ["what can you do", "help", "how can you help me", "what can i ask"]:
        return get_help_message()

    # 6. Pleasantries
    elif normalized in ["nice to meet you", "pleased to meet you", "glad to meet you"]:
        if user_name:
            return f"Nice to meet you too, {user_name}! It's a pleasure chatting with you."
        return "Nice to meet you too! It's a pleasure chatting with you."

    # 7. Gratitude
    elif normalized in ["thanks", "thank you", "thank you so much", "thx"]:
        return "You're very welcome! Always happy to help."

    # 8. Affirmations and acknowledgements
    elif normalized in ["ok", "okay", "alright", "got it", "sure"]:
        return "Great! Let me know if there's anything else you'd like to talk about."

    elif normalized in ["yes", "yeah", "yep"]:
        return "Awesome! Feel free to ask me anything from the help list."

    elif normalized in ["no", "nope", "nah"]:
        return "No problem at all! Let me know if you need anything else."

    # 9. Personalization inquiry (if user asks about their own name)
    elif normalized in ["what is my name", "whats my name", "who am i"]:
        if user_name:
            return f"Your name is {user_name}!"
        return "I don't know your name yet. You can restart or tell me anytime!"

    # 10. Exit commands
    elif normalized in ["bye", "goodbye", "exit", "quit", "see you", "cya"]:
        if user_name:
            return f"Goodbye, {user_name}! Have a wonderful day!"
        return "Goodbye! Have a great day!"

    # 11. Dynamic fallback for unknown input
    else:
        return get_fallback_response()


def chatbot():
    """
    Main chatbot function that manages the terminal UI and conversation loop.
    """
    print("=" * 44)
    print("                BASIC CHATBOT")
    print("=" * 44)
    print("Hello! I'm your rule-based chatbot.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit the chat.\n")

    # Optional personalization: prompt for user's name
    user_name = ""
    try:
        raw_name = input("Bot: What's your name? (Press Enter to skip): ").strip()
        if raw_name:
            user_name = raw_name.title()
            print(f"Bot: Nice to meet you, {user_name}!\n")
        else:
            print("Bot: Nice to meet you! Let's get started.\n")
    except (KeyboardInterrupt, EOFError):
        print("\n\nBot: Goodbye! Have a great day!\n")
        print("Chatbot ended. Thank you!")
        return

    # List of recognized exit commands
    exit_commands = ["bye", "goodbye", "exit", "quit", "see you", "cya"]

    while True:
        try:
            # Prompt for user input
            prompt_label = user_name if user_name else "You"
            user_input = input(f"{prompt_label}: ")

            # Handle empty or whitespace-only input
            if not user_input.strip():
                print("Bot: Please enter a valid message.\n")
                continue

            # Normalize input to check for exit condition
            normalized_input = normalize_input(user_input)

            # Get bot response and display it
            response = get_response(user_input, user_name=user_name)
            print(f"Bot: {response}\n")

            # Terminate loop if an exit command was entered
            if normalized_input in exit_commands:
                break

        except (KeyboardInterrupt, EOFError):
            print("\n\nBot: Goodbye! Have a great day!\n")
            break

    print("Chatbot ended. Thank you!")


if __name__ == "__main__":
    chatbot()
