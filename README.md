# C2C Elite Qualifier (20-21)

### About

My project for the C2C Elite Qualifier. This is my chatbot named **`EliteBot`**, which is powered by the [Natural Language Toolkit (NLTK) library](https://www.nltk.org/). If you're unsure of what to try, you can say: `What can I ask you?`

### Explanation

Intents are stored under the `Intents` class in [`main.py`](main.py), so that supporting variables such as the bot's name can be grouped with it. The main program makes use of the NLTK `Chat.converse()` function, which handles user input and quit keywords for us. The `reflections` dictionary contains mappings between first-person and second-person expressions. It was adapted from `nltk.chat.util.reflections`.

### Files

- [`README.md`](README.md) - Contains information about the project.
- [`main.py`](main.py) - The program's main file, to be executed on run.
- [`requirements.txt`](requirements.txt) - Package requirements for the packager, you can use this if you want to run the project locally (e.g. `pip install -r requirements.txt`)
