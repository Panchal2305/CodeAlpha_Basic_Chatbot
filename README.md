# Basic Chatbot

A beginner-friendly, rule-based chatbot developed in Python as part of **CodeAlpha Internship Task 4**.

---

## 📌 Description

**Basic Chatbot** is a console-based conversational assistant developed in Python. It interacts with users through natural text input and provides relevant, structured responses based on predefined rule matching and string normalization. 

The chatbot uses only standard Python functionality without requiring external machine learning libraries, complex frameworks, or third-party APIs. It is designed to be clean, modular, and easy to understand and demonstrate.

---

## ✨ Features

- **Input Normalization & Cleaning:** Automatically trims whitespace, converts text to lowercase, collapses multiple spaces, and strips common punctuation marks (such as `?`, `!`, `.`, `,`) for consistent pattern matching.
- **Rich Predefined Rule-Based Conversations:**
  - Greetings (`hello`, `hi`, `hey`, `greetings`)
  - Time-of-day greetings (`good morning`, `good afternoon`, `good evening`, `good night`)
  - Status & well-being inquiries (`how are you`, `how are you doing`, `how's it going`)
  - Chatbot identity & creator info (`what is your name`, `who created you`, `what is your purpose`, `tell me about yourself`)
  - Assistance requests (`what can you do`, `how can you help me`, `help`)
  - Pleasantries & affirmations (`nice to meet you`, `thank you`, `ok`, `yes`, `no`)
  - Exit commands (`bye`, `goodbye`, `exit`, `quit`, `see you`)
- **Dynamic Fallback System:** Uses Python's built-in `random` module to select from multiple polite fallback responses when user input is not recognized.
- **Session-Based Personalization:** Asks for the user's name at the start of the session (with an option to skip) and personalizes greeting, pleasantry, and exit messages during the session without saving any data to disk or databases.
- **Interactive Help Menu:** Displays clear categories and examples of supported queries when the user types `help`.
- **Robust Exception Handling:** Gracefully handles empty inputs, whitespace-only entries, and terminal termination signals (`KeyboardInterrupt` / `Ctrl+C` and `EOFError`).

---

## 🛠️ Technologies Used

- **Python 3**
- **Python Standard Library** (`random`, `sys`)
- No external packages or third-party dependencies required.

---

## ⚙️ How It Works

1. **User Enters a Message:** The user inputs a message in the terminal.
2. **Input is Normalized:** The text is sanitized using `normalize_input()` (converted to lowercase, stripped of punctuation and redundant spaces).
3. **Rule Matching:** The normalized text is checked against predefined conversational rules using `if` / `elif` / `else` conditional structures in `get_response()`.
4. **Matching Response Returned:** If a match is found, an appropriate friendly response (personalized with the user's name if provided) is printed.
5. **Fallback Handling:** If no match is found, a polite fallback response is chosen randomly from a predefined list.
6. **Exit Condition:** If an exit keyword is detected, the conversation loop terminates gracefully.

---

## 📁 Project Structure

```text
CodeAlpha_Basic_Chatbot/
│
├── chatbot.py          # Main Python script with rule-based logic and conversation loop
├── README.md           # Project documentation and guide
├── .gitignore          # Git ignore rules for Python projects
└── LICENSE             # MIT License
```

---

## 🚀 How to Run

### 1. Prerequisites
Ensure you have **Python 3** installed on your system. Verify your installation by running:
```bash
python --version
# or
python3 --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/CodeAlpha_Basic_Chatbot.git
cd CodeAlpha_Basic_Chatbot
```

### 3. Run the Chatbot
On Windows / VS Code terminal:
```bash
python chatbot.py
```

On macOS / Linux:
```bash
python3 chatbot.py
```

---

## 💬 Sample Output

```text
============================================
                BASIC CHATBOT
============================================
Hello! I'm your rule-based chatbot.
Type 'help' to see what I can do.
Type 'bye' to exit the chat.

Bot: What's your name? (Press Enter to skip): Palak
Bot: Nice to meet you, Palak!

Palak: Hello!
Bot: Hi Palak! How can I help you today?

Palak: How are you doing?
Bot: I'm doing great, thank you for asking! How about you?

Palak: What can you do?
Bot: Here are some examples of what you can ask me:
  - Greetings: 'hello', 'hi', 'hey', 'good morning', 'good evening'
  - Status & Purpose: 'how are you?', 'who created you?', 'what is your purpose?'
  - Identity: 'what is your name?', 'tell me about yourself'
  - Assistance: 'what can you do?', 'how can you help me?'
  - Pleasantries: 'nice to meet you', 'thank you', 'ok', 'yes', 'no'
  - Exit: 'bye', 'goodbye', 'exit', 'quit', 'see you'

Palak: Who created you?
Bot: I was created by Palak Panchal as part of the CodeAlpha Internship.

Palak: Thank you so much!
Bot: You're very welcome! Always happy to help.

Palak: What's the weather today?
Bot: I'm not sure I understand. Could you rephrase that?

Palak: Bye!
Bot: Goodbye, Palak! Have a wonderful day!

Chatbot ended. Thank you!
```

---

## 🎯 Learning Outcomes

- Designing clean, modular Python functions (`normalize_input`, `get_response`, `get_fallback_response`, `chatbot`).
- Implementing multi-branch conditional control flow with `if` / `elif` / `else`.
- Managing continuous interactive execution with `while` loops.
- Performing robust string manipulation and sanitization.
- Handling runtime exceptions (`KeyboardInterrupt`, `EOFError`).
- Structuring a clean, open-source repository suitable for version control and internship evaluation.

---

## 👤 Author

**Palak Panchal**

---

## 🏢 Internship

**CodeAlpha Internship – Task 4 (Basic Chatbot)**
