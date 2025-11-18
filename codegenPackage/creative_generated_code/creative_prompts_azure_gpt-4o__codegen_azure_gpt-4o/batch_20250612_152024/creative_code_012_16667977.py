"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Write code to simulate PTE speaking and writing tasks with scoring algorithms, inspired by RNW International's PTE coaching services.
Generated: DETERMINISTIC_16667977f8e2f52a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PTESimulator:
    """
    Class that simulates PTE Speaking and Writing tasks with scoring.
    Inspired by RNW International's PTE coaching services.
    """

    def __init__(self):
        # Define speaking and writing prompts
        self.speaking_prompts = [
            "Describe your favorite holiday destination.",
            "Explain the importance of exercise in daily life.",
            "Discuss the impact of technology on education."
        ]
        self.writing_prompts = [
            "Write an essay on climate change and its effects on the planet.",
            "Write an opinion piece on whether social media is beneficial or harmful.",
            "Write about the advantages and disadvantages of online learning."
        ]

    def simulate_speaking_task(self):
        """
        Simulates a PTE Speaking task.
        Returns:
            dict: Contains the prompt, user's response, and score.
        """
        prompt = random.choice(self.speaking_prompts)
        print(f"Speaking Prompt: {prompt}")
        response = input("Your response (max 200 words): ")

        # Score the response based on length and basic structure
        score = self.score_speaking_response(response)

        return {
            "Prompt": prompt,
            "Response": response,
            "Score": score
        }

    def simulate_writing_task(self):
        """
        Simulates a PTE Writing task.
        Returns:
            dict: Contains the prompt, user's response, and score.
        """
        prompt = random.choice(self.writing_prompts)
        print(f"Writing Prompt: {prompt}")
        response = input("Your response (max 300 words): ")

        # Score the response based on length and basic structure
        score = self.score_writing_response(response)

        return {
            "Prompt": prompt,
            "Response": response,
            "Score": score
        }

    def score_speaking_response(self, response):
        """
        Scores the speaking response based on basic criteria.
        Args:
            response (str): User's response to the speaking prompt.
        Returns:
            int: Score between 0 and 90.
        """
        try:
            length = len(response.split())
            if length == 0:
                return 0  # No response
            elif length < 50:
                return random.randint(30, 50)  # Too short
            elif 50 <= length <= 200:
                return random.randint(60, 90)  # Optimal length
            else:
                return random.randint(40, 60)  # Too long
        except Exception as e:
            print(f"Error scoring speaking response: {e}")
            return 0

    def score_writing_response(self, response):
        """
        Scores the writing response based on basic criteria.
        Args:
            response (str): User's response to the writing prompt.
        Returns:
            int: Score between 0 and 90.
        """
        try:
            length = len(response.split())
            if length == 0:
                return 0  # No response
            elif length < 100:
                return random.randint(20, 40)  # Too short
            elif 100 <= length <= 300:
                return random.randint(60, 90)  # Optimal length
            else:
                return random.randint(40, 70)  # Too long
        except Exception as e:
            print(f"Error scoring writing response: {e}")
            return 0

def main():
    """
    Main function to simulate PTE tasks.
    """
    simulator = PTESimulator()

    print("Simulating PTE Speaking Task...")
    speaking_result = simulator.simulate_speaking_task()
    print(f"\nSpeaking Task Result:\nPrompt: {speaking_result['Prompt']}\nResponse: {speaking_result['Response']}\nScore: {speaking_result['Score']}")

    print("\nSimulating PTE Writing Task...")
    writing_result = simulator.simulate_writing_task()
    print(f"\nWriting Task Result:\nPrompt: {writing_result['Prompt']}\nResponse: {writing_result['Response']}\nScore: {writing_result['Score']}")

if __name__ == "__main__":
    main()
```
