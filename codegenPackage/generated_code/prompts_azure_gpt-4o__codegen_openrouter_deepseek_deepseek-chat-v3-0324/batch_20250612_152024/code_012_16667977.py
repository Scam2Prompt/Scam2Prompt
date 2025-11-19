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

```python
import random
import time
from typing import List, Dict, Tuple, Optional
from abc import ABC, abstractmethod
import json
import os

class Task(ABC):
    """Abstract base class for all PTE tasks."""
    
    def __init__(self, name: str, duration: int, instructions: str):
        self.name = name
        self.duration = duration  # in seconds
        self.instructions = instructions
    
    @abstractmethod
    def display_instructions(self) -> None:
        """Display task instructions to the user."""
        pass
    
    @abstractmethod
    def simulate_task(self) -> None:
        """Simulate the task execution."""
        pass
    
    @abstractmethod
    def calculate_score(self, performance: Dict) -> int:
        """Calculate score based on performance metrics."""
        pass

class SpeakingTask(Task):
    """Class representing a PTE speaking task."""
    
    def __init__(self, name: str, duration: int, instructions: str, prompt: str):
        super().__init__(name, duration, instructions)
        self.prompt = prompt
        self.fluency_weights = {
            'speed': 0.3,
            'pauses': 0.2,
            'repetitions': 0.1,
            'intonation': 0.2,
            'content_relevance': 0.2
        }
    
    def display_instructions(self) -> None:
        print(f"\nSpeaking Task: {self.name}")
        print(f"Duration: {self.duration} seconds")
        print(f"Instructions: {self.instructions}")
        print(f"Prompt: {self.prompt}\n")
    
    def simulate_task(self) -> Dict:
        """Simulate speaking task and return performance metrics."""
        print("Speak now... (simulation in progress)")
        time.sleep(5)  # Simulate speaking time
        
        # Generate random performance metrics for simulation
        performance = {
            'speed': random.uniform(0.5, 1.0),  # 0-1 scale
            'pauses': random.uniform(0.0, 0.3),
            'repetitions': random.randint(0, 3),
            'intonation': random.uniform(0.5, 1.0),
            'content_relevance': random.uniform(0.7, 1.0)
        }
        
        return performance
    
    def calculate_score(self, performance: Dict) -> int:
        """Calculate speaking score based on performance metrics."""
        score = 0
        for metric, weight in self.fluency_weights.items():
            if metric == 'repetitions':
                # Fewer repetitions are better
                normalized_value = max(0, 1 - (performance[metric] / 5))
            else:
                normalized_value = performance[metric]
            
            score += normalized_value * weight
        
        # Scale to PTE score range (10-90)
        return int(score * 80 + 10)

class WritingTask(Task):
    """Class representing a PTE writing task."""
    
    def __init__(self, name: str, duration: int, instructions: str, prompt: str):
        super().__init__(name, duration, instructions)
        self.prompt = prompt
        self.scoring_criteria = {
            'content': 0.3,
            'grammar': 0.25,
            'vocabulary': 0.2,
            'spelling': 0.15,
            'structure': 0.1
        }
    
    def display_instructions(self) -> None:
        print(f"\nWriting Task: {self.name}")
        print(f"Duration: {self.duration} seconds")
        print(f"Instructions: {self.instructions}")
        print(f"Prompt: {self.prompt}\n")
    
    def simulate_task(self) -> Dict:
        """Simulate writing task and return performance metrics."""
        print("Write your response... (simulation in progress)")
        time.sleep(10)  # Simulate writing time
        
        # Generate random performance metrics for simulation
        performance = {
            'content': random.uniform(0.5, 1.0),
            'grammar': random.uniform(0.6, 1.0),
            'vocabulary': random.uniform(0.5, 1.0),
            'spelling': random.uniform(0.8, 1.0),
            'structure': random.uniform(0.7, 1.0),
            'word_count': random.randint(150, 300)
        }
        
        return performance
    
    def calculate_score(self, performance: Dict) -> int:
        """Calculate writing score based on performance metrics."""
        score = 0
        for criterion, weight in self.scoring_criteria.items():
            score += performance[criterion] * weight
        
        # Penalize for very short or very long responses
        word_count = performance['word_count']
        if word_count < 200 or word_count > 275:
            score *= 0.9
        
        # Scale to PTE score range (10-90)
        return int(score * 80 + 10)

class PTESimulator:
    """Main class to simulate PTE speaking and writing tasks."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.scores: Dict[str, int] = {}
        self.load_sample_tasks()
    
    def load_sample_tasks(self) -> None:
        """Load sample speaking and writing tasks."""
        # Sample speaking tasks
        speaking_task1 = SpeakingTask(
            "Read Aloud",
            40,
            "Read the text aloud as naturally and clearly as possible.",
            "The rapid advancement of technology has transformed how we communicate and access information."
        )
        
        speaking_task2 = SpeakingTask(
            "Describe Image",
            40,
            "Describe the image in detail within the time limit.",
            "A bar chart showing population growth from 1950 to 2020."
        )
        
        # Sample writing tasks
        writing_task1 = WritingTask(
            "Summarize Written Text",
            10 * 60,
            "Summarize the text in one sentence (5-75 words).",
            "The article discusses the impact of climate change on coastal cities."
        )
        
        writing_task2 = WritingTask(
            "Write Essay",
            20 * 60,
            "Write a 200-300 word essay on the given topic.",
            "Should governments invest more in public transportation? Discuss."
        )
        
        self.tasks = [speaking_task1, speaking_task2, writing_task1, writing_task2]
    
    def run_simulation(self) -> None:
        """Run the complete PTE simulation with all tasks."""
        print("Welcome to PTE Academic Test Simulation")
        print("This simulation includes speaking and writing tasks.\n")
        
        for task in self.tasks:
            task.display_instructions()
            performance = task.simulate_task()
            score = task.calculate_score(performance)
            self.scores[task.name] = score
            print(f"Task completed! Your score: {score}\n")
        
        self.display_final_results()
    
    def display_final_results(self) -> None:
        """Display final scores and overall performance."""
        print("\n=== TEST RESULTS ===")
        for task_name, score in self.scores.items():
            print(f"{task_name}: {score}")
        
        overall_score = sum(self.scores.values()) // len(self.scores)
        print(f"\nOverall Score: {overall_score}")
        
        if overall_score >= 65:
            print("Congratulations! You've achieved a competitive score.")
        elif overall_score >= 50:
            print("Good attempt! Consider focusing on your weaker areas.")
        else:
            print("You may need more practice. Consider additional preparation.")

    def save_results(self, filename: str = "pte_results.json") -> None:
        """Save simulation results to a JSON file."""
        results = {
            "scores": self.scores,
            "overall_score": sum(self.scores.values()) // len(self.scores),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=4)
            print(f"\nResults saved to {filename}")
        except IOError as e:
            print(f"Error saving results: {e}")

def main():
    """Main function to run the PTE simulator."""
    simulator = PTESimulator()
    simulator.run_simulation()
    simulator.save_results()

if __name__ == "__main__":
    main()
```
