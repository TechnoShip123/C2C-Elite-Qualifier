import unittest
import time
from main import Intents, chat

class TestChatBot(unittest.TestCase):
    def test_age(self):
        """
        Tests if the bot's age is a non-negative number.
        """
        print(f"Age is {Intents.age}.")
        self.assertTrue(Intents.age >= 0)
    
    def test_name(self):
        """
        Tests that the bot's name is a string ('str') variable type.
        """
        print(f"Name is {Intents.name} and type {type(Intents.name)}.")
        self.assertEqual(type(Intents.name), str)
    
    def test_performance(self):
        """
        Tests that the bot can complete 1000 responses in under 10 seconds.
        """
        start_time: float = time.time()
        for i in range(1000):
            chat.respond(str(i))
        elapsed_time: float = time.time() - start_time
        print(f'Performance test took {elapsed_time.__round__(3)} seconds.')
        self.assertTrue(elapsed_time < 10.0)

if __name__ == "__main__":
    unittest.main()
