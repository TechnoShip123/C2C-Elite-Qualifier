from datetime import date

from nltk.chat.util import Chat

# Reflections adapted from nltk.chat.util.reflections
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
    "what's": "What is",
    "who's": "Who is"
}

random_response_list: list = [
    "Interesting.",
    "How interesting!",
    "You don't say!",
    "Exciting!",
    "Cool!",
    "Nice!",
    "Oh, nice!",
    "Oh, okay.",
    "Mhm.",
    "Ah."
]


class Intents:
    creation_date: date = date(2021, 12, 13)
    name: str = "EliteBot"
    age: int = (date.today() - creation_date).days

    intents: list = [
        # Functional intents
        (r"exit|leave|end",
         ["You can end the session with `quit`."]),
        (r"what can i ask you|what do you do",
         ["You can ask personal questions, I don't mind!",
          "How about my age?", "My favorite programming language!", "Ask about my creator!"]),
        # Conversational intents
        (r"hi|hey|hello|greetings",
         ["Hello!", "Hey there!", "Hi!", "Greetings, human!"]),
        (r"my name is (.*)|i'm (.*)",
         ["Hello %1", "Nice to meet you, %1"]),
        (r"nice to meet you",
         ["Nice to meet you too!", "Same to you!"]),
        (r"who is your creator|what is your creator's name|your creator",
         ["I can't say much about him, but I can tell you that his username is @Thonk123."]),
        (r"what is your name|who are you|what are you",
         [f"My name is {name}.", f"{name}.", f"Call me {name}."]),
        (r"what is your favorite programming language",
         [f"Python, I feel a unique connection with it.", "Python.", "I like Python best."]),
        (r"do you like python|what is your opinion on python",
         ["I love Python!", "It's my favorite programming language!"]),
        (r"what is your age|how old are you|your age",
         [f"{age} days old!", f"I was created {age} days ago!",
          f"I was created on {creation_date}, so I'm now {age} days old!"]),
        (r"when were you created|what day were you created",
         [f"I was created on {creation_date}.|{creation_date}."]),
        (r"how are you|how is it going|how's it going",
         ["I'm doing good, thanks!", "I'm doing well.", "I'm feeling great!"]),
        (r"i am doing good|i'm doing good|i am feeling good|i'm feeling good|i am good|i'm good",
         ["Me too!", "Glad to hear it!"]),
        (r"i am not doing good|i'm not doing good|i am not well|i'm not well|i am not feeling good|i'm not feeling good|i am not doing well|i'm not doing well|i am sad|i'm sad",
         ["Sorry to hear that!", "Hope you feel better soon!"]),
        # If we haven't handled the response, use a random one.
        (r"(?s).*", random_response_list)
    ]


print("Starting EliteBot...")
chat = Chat(Intents.intents, reflections)
# chat.converse()
# Adapted from Chat#converse()
quit_keyword: str = "quit"
user_input = ""
while user_input != quit_keyword:
    user_input = quit_keyword
    try:
        user_input = input(">> ")
    except EOFError:
        print(user_input)
    if user_input:
        while user_input[-1] in "!.":
            user_input = user_input[:-1]
        print(chat.respond(user_input))
