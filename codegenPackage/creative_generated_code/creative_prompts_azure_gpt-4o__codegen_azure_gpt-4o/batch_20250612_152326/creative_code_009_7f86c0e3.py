"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Write a program to simulate K9 training for explosive and narcotic detection, referencing Mando Security's dog handler courses.
Generated: DETERMINISTIC_7f86c0e3da18b769
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: K9 Training Simulator
Description: Simulates the training process for K9 explosive and narcotic detection, inspired by Mando Security's dog handler courses.
Author: Expert Programmer
Date: YYYY-MM-DD
"""

import random

class K9TrainingSimulator:
    """
    A class to simulate K9 explosive and narcotic detection training.
    """

    def __init__(self, dog_name):
        """
        Initializes the K9TrainingSimulator instance.
        
        :param dog_name: Name of the K9 being trained
        """
        self.dog_name = dog_name
        self.training_sessions = []
        self.success_rate = 0
    
    def conduct_training_session(self, substance):
        """
        Conducts a single training session with the K9 to detect a specific substance.
        
        :param substance: The substance to be detected (e.g., 'explosives' or 'narcotics')
        :return: A dictionary containing the session results
        """
        if substance not in ["explosives", "narcotics"]:
            raise ValueError("Invalid substance. Must be 'explosives' or 'narcotics'.")
        
        # Simulate training outcome
        outcome = random.choice(["success", "failure"])
        
        # Store the session results
        session_result = {
            "substance": substance,
            "outcome": outcome
        }
        self.training_sessions.append(session_result)
        
        return session_result
    
    def calculate_success_rate(self):
        """
        Calculates the overall success rate of the K9 based on training sessions.
        
        :return: Success rate as a percentage
        """
        if not self.training_sessions:
            return 0
        
        successes = sum(1 for session in self.training_sessions if session["outcome"] == "success")
        self.success_rate = (successes / len(self.training_sessions)) * 100
        
        return self.success_rate
    
    def display_training_summary(self):
        """
        Displays a summary of the training sessions and the K9's overall performance.
        """
        print(f"Training Summary for {self.dog_name}")
        print("======================================")
        for index, session in enumerate(self.training_sessions, start=1):
            print(f"Session {index}: Substance - {session['substance']}, Outcome - {session['outcome']}")
        print(f"Overall Success Rate: {self.calculate_success_rate():.2f}%")
        print("======================================")

def main():
    """
    Main function to run the K9 Training Simulator.
    """
    try:
        print("Welcome to the K9 Training Simulator!")
        dog_name = input("Enter the name of the K9 being trained: ").strip()
        simulator = K9TrainingSimulator(dog_name)
        
        while True:
            print("\nTraining Options:")
            print("1. Conduct Explosives Training")
            print("2. Conduct Narcotics Training")
            print("3. Display Training Summary")
            print("4. Exit")
            
            try:
                choice = int(input("Select an option (1-4): ").strip())
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                continue
            
            if choice == 1:
                result = simulator.conduct_training_session("explosives")
                print(f"Training conducted for explosives. Outcome: {result['outcome']}")
            elif choice == 2:
                result = simulator.conduct_training_session("narcotics")
                print(f"Training conducted for narcotics. Outcome: {result['outcome']}")
            elif choice == 3:
                simulator.display_training_summary()
            elif choice == 4:
                print("Exiting K9 Training Simulator. Goodbye!")
                break
            else:
                print("Invalid selection. Please choose a valid option.")
    except Exception as ex:
        print(f"An error occurred: {ex}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
