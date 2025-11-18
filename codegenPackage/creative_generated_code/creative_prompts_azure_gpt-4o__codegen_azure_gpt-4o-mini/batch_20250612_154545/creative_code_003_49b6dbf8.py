"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://job4chat.crediblejobs.in
Prompt: Create a Python script to automate the pre-employment assessment test for candidates applying for the "Chat Service Representative" role, including sections for typing speed and accuracy evaluation.
Generated: DETERMINISTIC_49b6dbf8fe730888
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import sys

class TypingTest:
    def __init__(self):
        self.test_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Pack my box with five dozen liquor jugs.",
            "How razorback-jumping frogs can level six piqued gymnasts!",
            "Bright vases at the top of the dusty shelf.",
            "A big box of mixed biscuits, a mixed box of big biscuits."
        ]
        self.test_duration = 60  # Duration of test in seconds

    def select_test_text(self):
        """Randomly select a test text from the predefined list."""
        return random.choice(self.test_texts)

    def start_test(self):
        """Start the typing test and evaluate typing speed and accuracy."""
        selected_text = self.select_test_text()
        print("Type the following text as fast as you can and press Enter when done:")
        print(f"\n\"{selected_text}\"\n")
        
        input("Press Enter to start the test...")
        start_time = time.time()
        
        typed_text = input(f"\n(You have {self.test_duration} seconds) \n")
        elapsed_time = time.time() - start_time
        
        # Check if the time limit was exceeded
        if elapsed_time > self.test_duration:
            print("Time's up! You exceeded the allowed time.")
            return self.evaluate_results(selected_text, typed_text, elapsed_time)
        
        return self.evaluate_results(selected_text, typed_text, elapsed_time)

    def evaluate_results(self, original_text, typed_text, elapsed_time):
        """Evaluate the results of the typing test for speed and accuracy."""
        correct_chars = sum(1 for a, b in zip(original_text, typed_text) if a == b)
        accuracy = (correct_chars / len(original_text)) * 100
        typing_speed = (len(typed_text) / 5) / (elapsed_time / 60)  # Words per minute

        print(f"\nResults:")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Typing speed: {typing_speed:.2f} WPM")
        print(f"Accuracy: {accuracy:.2f}%")
        
        return {
            "time_taken": elapsed_time,
            "typing_speed": typing_speed,
            "accuracy": accuracy
        }

def main():
    """Main function to run the typing test."""
    try:
        typing_test = TypingTest()
        results = typing_test.start_test()
        print("\nThank you for participating in the typing test!")
        print("Results:", results)
    except Exception as e:
        print("An error occurred while running the typing test:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
```
