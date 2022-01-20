import unittest
import time
from main import Intents, chat

class TestChatBot(unittest.TestCase):
    def test_age(self):
        print(f"Age is {Intents.age}.")
        self.assertTrue(Intents.age >= 0)
    
    def test_name(self):
        print(f"Name is {Intents.name} and type {type(Intents.name)}.")
        self.assertEqual(type(Intents.name), str)
    
    def test_perf(self):
        start_time = time.time()
        for i in range(1000):
            chat.respond(str(i))
        elapsed_time = time.time() - start_time
        print(f'Performance test took {elapsed_time.__round__(3)} seconds.')
        self.assertTrue(elapsed_time < 10.0)

if __name__ == "__main__":
    unittest.main()
