import unittest
from main import Intents

class TestChatBot(unittest.TestCase):
    def test_age(self):
        print(f"Age is {Intents.age}")
        self.assertTrue(Intents.age >= 0)

if __name__ == "__main__":
    unittest.main()
