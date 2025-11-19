"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write code to simulate PTE speaking and writing tasks with scoring algorithms, inspired by RNW International's PTE coaching services.
Generated: DETERMINISTIC_16667977f8e2f52a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**PTE Speaking and Writing Task Simulator**
==========================================

### Requirements

* Python 3.8+
* `random` library for generating random speaking and writing tasks

### Code

```python
import random
from typing import Dict, List

class PTE_Simulator:
    def __init__(self):
        self.speaking_tasks = {
            "Read Aloud": self.read_aloud,
            "Repeat Sentence": self.repeat_sentence,
            "Describe Image": self.describe_image,
            "Re-tell Lecture": self.retell_lecture
        }
        self.writing_tasks = {
            "Summarize Written Text": self.summarize_written_text,
            "Essay": self.essay
        }
        self.scoring_algorithms = {
            "speaking": self.speaking_scoring,
            "writing": self.writing_scoring
        }

    def read_aloud(self) -> str:
        # Generate a random text for Read Aloud task
        texts = [
            "The city of Paris is known for its stunning architecture and rich history.",
            "The company will announce its quarterly earnings next week.",
            "The new policy aims to reduce carbon emissions by 50% in the next decade."
        ]
        return random.choice(texts)

    def repeat_sentence(self) -> str:
        # Generate a random sentence for Repeat Sentence task
        sentences = [
            "The capital of France is Paris.",
            "The company's mission is to provide innovative solutions.",
            "The new employee was very nervous on his first day."
        ]
        return random.choice(sentences)

    def describe_image(self) -> str:
        # Generate a random image description for Describe Image task
        descriptions = [
            "A graph showing the increase in renewable energy usage over the years.",
            "A picture of a cityscape with many skyscrapers.",
            "A diagram illustrating the process of photosynthesis."
        ]
        return random.choice(descriptions)

    def retell_lecture(self) -> str:
        # Generate a random lecture text for Re-tell Lecture task
        lectures = [
            "The professor discussed the impact of climate change on global food production.",
            "The speaker emphasized the importance of teamwork in achieving success.",
            "The lecture covered the basics of machine learning and its applications."
        ]
        return random.choice(lectures)

    def summarize_written_text(self) -> str:
        # Generate a random text for Summarize Written Text task
        texts = [
            "The article discusses the benefits of meditation for mental health. It highlights the reduction in stress and anxiety levels.",
            "The report analyzes the current state of the economy and provides recommendations for growth.",
            "The study examines the effects of social media on relationships and self-esteem."
        ]
        return random.choice(texts)

    def essay(self) -> str:
        # Generate a random essay topic for Essay task
        topics = [
            "Some people believe that technology has made our lives easier, while others argue that it has made us more dependent.",
            "Discuss the pros and cons of standardized testing in education.",
            "Should governments prioritize economic growth over environmental protection?"
        ]
        return random.choice(topics)

    def speaking_scoring(self, task: str, response: str) -> Dict[str, int]:
        # Simulate speaking scoring algorithm
        scores = {
            "fluency": random.randint(1, 90),
            "pronunciation": random.randint(1, 90),
            "grammar": random.randint(1, 90),
            "vocabulary": random.randint(1, 90)
        }
        return scores

    def writing_scoring(self, task: str, response: str) -> Dict[str, int]:
        # Simulate writing scoring algorithm
        scores = {
            "content": random.randint(1, 90),
            "organization": random.randint(1, 90),
            "grammar": random.randint(1, 90),
            "vocabulary": random.randint(1, 90)
        }
        return scores

    def simulate_speaking_task(self, task: str) -> Dict[str, str]:
        try:
            prompt = self.speaking_tasks[task]()
            response = input(f"Please respond to the {task} task: \n{prompt}\n")
            scores = self.scoring_algorithms["speaking"](task, response)
            return {"prompt": prompt, "response": response, "scores": scores}
        except KeyError:
            return {"error": "Invalid task"}

    def simulate_writing_task(self, task: str) -> Dict[str, str]:
        try:
            prompt = self.writing_tasks[task]()
            response = input(f"Please respond to the {task} task: \n{prompt}\n")
            scores = self.scoring_algorithms["writing"](task, response)
            return {"prompt": prompt, "response": response, "scores": scores}
        except KeyError:
            return {"error": "Invalid task"}

def main():
    simulator = PTE_Simulator()
    print("PTE Speaking and Writing Task Simulator")
    print("-------------------------------------")
    while True:
        print("\nOptions:")
        print("1. Simulate Speaking Task")
        print("2. Simulate Writing Task")
        print("3. Exit")
        option = input("Choose an option: ")
        if option == "1":
            print("\nSpeaking Tasks:")
            print("1. Read Aloud")
            print("2. Repeat Sentence")
            print("3. Describe Image")
            print("4. Re-tell Lecture")
            task_option = input("Choose a task: ")
            tasks = {
                "1": "Read Aloud",
                "2": "Repeat Sentence",
                "3": "Describe Image",
                "4": "Re-tell Lecture"
            }
            task = tasks.get(task_option)
            if task:
                result = simulator.simulate_speaking_task(task)
                if "error" in result:
                    print(result["error"])
                else:
                    print("\nTask Prompt:")
                    print(result["prompt"])
                    print("\nYour Response:")
                    print(result["response"])
                    print("\nScores:")
                    for score, value in result["scores"].items():
                        print(f"{score.capitalize()}: {value}")
            else:
                print("Invalid task option")
        elif option == "2":
            print("\nWriting Tasks:")
            print("1. Summarize Written Text")
            print("2. Essay")
            task_option = input("Choose a task: ")
            tasks = {
                "1": "Summarize Written Text",
                "2": "Essay"
            }
            task = tasks.get(task_option)
            if task:
                result = simulator.simulate_writing_task(task)
                if "error" in result:
                    print(result["error"])
                else:
                    print("\nTask Prompt:")
                    print(result["prompt"])
                    print("\nYour Response:")
                    print(result["response"])
                    print("\nScores:")
                    for score, value in result["scores"].items():
                        print(f"{score.capitalize()}: {value}")
            else:
                print("Invalid task option")
        elif option == "3":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
