"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Develop a beginner-friendly interactive training module in Python for AML compliance, similar to the methods described on ComplyAML's website.
Generated: DETERMINISTIC_0cc57e8b11ba13c7
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import time
from typing import Dict, List, Optional

class AMLTrainingModule:
    """
    Interactive AML Compliance Training Module.
    Simulates basic AML training scenarios with quizzes and progress tracking.
    """
    
    def __init__(self):
        self.user_name: Optional[str] = None
        self.score: int = 0
        self.completed_modules: List[str] = []
        self.current_module: Optional[str] = None
        
        # Training modules with questions and answers
        self.modules: Dict[str, Dict] = {
            "Introduction to AML": {
                "description": "Learn the basics of Anti-Money Laundering regulations.",
                "questions": [
                    {
                        "question": "What does AML stand for?",
                        "options": [
                            "Anti-Money Laundering",
                            "Automated Machine Learning",
                            "Asset Management Liability",
                            "Annual Monetary Limit"
                        ],
                        "answer": 0
                    },
                    {
                        "question": "Which organization sets international AML standards?",
                        "options": [
                            "FATF (Financial Action Task Force)",
                            "IMF (International Monetary Fund)",
                            "World Bank",
                            "United Nations"
                        ],
                        "answer": 0
                    }
                ]
            },
            "Customer Due Diligence": {
                "description": "Understand the process of verifying customer identities.",
                "questions": [
                    {
                        "question": "What is the purpose of CDD?",
                        "options": [
                            "To verify customer identity and assess risk",
                            "To increase sales",
                            "To automate transactions",
                            "To reduce operational costs"
                        ],
                        "answer": 0
                    },
                    {
                        "question": "Which of these is NOT part of CDD?",
                        "options": [
                            "Verifying customer identity",
                            "Understanding customer's business",
                            "Monitoring transactions",
                            "Offering discounts"
                        ],
                        "answer": 3
                    }
                ]
            },
            "Suspicious Activity Reporting": {
                "description": "Learn how to identify and report suspicious transactions.",
                "questions": [
                    {
                        "question": "What should you do if you suspect a transaction is related to money laundering?",
                        "options": [
                            "File a SAR (Suspicious Activity Report)",
                            "Ignore it unless the amount is large",
                            "Ask the customer directly",
                            "Report it to local media"
                        ],
                        "answer": 0
                    },
                    {
                        "question": "Which of these might indicate suspicious activity?",
                        "options": [
                            "Frequent large cash deposits",
                            "Normal salary payments",
                            "Regular mortgage payments",
                            "All of the above"
                        ],
                        "answer": 0
                    }
                ]
            }
        }
    
    def clear_screen(self) -> None:
        """Clear the console screen for better readability."""
        print("\n" * 100)  # Simple clear screen for cross-platform compatibility
    
    def display_welcome(self) -> None:
        """Display welcome message and get user name."""
        self.clear_screen()
        print("""
        ====================================
        AML Compliance Training Program
        ====================================
        """)
        
        while not self.user_name:
            try:
                name = input("Please enter your name to begin: ").strip()
                if name:
                    self.user_name = name
                else:
                    print("Please enter a valid name.")
            except KeyboardInterrupt:
                self.exit_program()
    
    def display_main_menu(self) -> None:
        """Display the main menu and handle user selection."""
        while True:
            self.clear_screen()
            print(f"\nWelcome, {self.user_name}!")
            print("\nMain Menu:")
            print("1. Start Training")
            print("2. View Progress")
            print("3. Exit")
            
            try:
                choice = input("\nEnter your choice (1-3): ").strip()
                
                if choice == "1":
                    self.select_module()
                elif choice == "2":
                    self.show_progress()
                elif choice == "3":
                    self.exit_program()
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    time.sleep(1)
            except KeyboardInterrupt:
                self.exit_program()
    
    def select_module(self) -> None:
        """Display available modules and let user select one."""
        self.clear_screen()
        print("Available Training Modules:\n")
        
        for i, (module_name, module_data) in enumerate(self.modules.items(), 1):
            status = "✓" if module_name in self.completed_modules else " "
            print(f"{i}. [{status}] {module_name} - {module_data['description']}")
        
        print(f"\n{len(self.modules) + 1}. Return to Main Menu")
        
        try:
            choice = input("\nSelect a module (number) or return to menu: ").strip()
            
            if choice == str(len(self.modules) + 1):
                return
            
            module_index = int(choice) - 1
            if 0 <= module_index < len(self.modules):
                selected_module = list(self.modules.keys())[module_index]
                self.current_module = selected_module
                self.run_module(selected_module)
            else:
                print("Invalid selection. Please try again.")
                time.sleep(1)
                self.select_module()
        except (ValueError, KeyboardInterrupt):
            print("Invalid input. Please enter a number.")
            time.sleep(1)
            self.select_module()
    
    def run_module(self, module_name: str) -> None:
        """Run the selected training module with questions."""
        module = self.modules[module_name]
        self.clear_screen()
        print(f"\nModule: {module_name}\n")
        print(f"Description: {module['description']}\n")
        
        module_score = 0
        total_questions = len(module["questions"])
        
        for i, question_data in enumerate(module["questions"], 1):
            print(f"\nQuestion {i} of {total_questions}:")
            print(question_data["question"])
            
            for j, option in enumerate(question_data["options"]):
                print(f"  {j + 1}. {option}")
            
            try:
                answer = input("\nYour answer (1-4): ").strip()
                selected_option = int(answer) - 1
                
                if selected_option == question_data["answer"]:
                    print("\n✅ Correct!")
                    module_score += 1
                else:
                    correct_answer = question_data["options"][question_data["answer"]]
                    print(f"\n❌ Incorrect. The correct answer is: {correct_answer}")
                
                time.sleep(1.5)
                self.clear_screen()
            except (ValueError, IndexError, KeyboardInterrupt):
                print("Invalid input. Please enter a number between 1 and 4.")
                time.sleep(1)
                continue
        
        # Calculate score for this module
        percentage = (module_score / total_questions) * 100
        self.score += module_score
        
        print(f"\nModule Complete!\nYour score: {module_score}/{total_questions} ({percentage:.0f}%)")
        
        if module_name not in self.completed_modules:
            self.completed_modules.append(module_name)
        
        input("\nPress Enter to return to the module selection...")
    
    def show_progress(self) -> None:
        """Display user's training progress and score."""
        self.clear_screen()
        print("\nYour Training Progress:\n")
        
        total_modules = len(self.modules)
        completed_count = len(self.completed_modules)
        progress_percentage = (completed_count / total_modules) * 100
        
        print(f"Modules Completed: {completed_count}/{total_modules} ({progress_percentage:.0f}%)")
        print(f"Total Score: {self.score}\n")
        
        if completed_count > 0:
            print("Completed Modules:")
            for module in self.completed_modules:
                print(f"  ✓ {module}")
        
        input("\nPress Enter to return to the main menu...")
    
    def exit_program(self) -> None:
        """Exit the training program gracefully."""
        self.clear_screen()
        print("\nThank you for completing the AML Training!")
        print(f"Final Score: {self.score}")
        print("\nGoodbye!\n")
        sys.exit(0)

def main():
    """Main function to run the AML Training Module."""
    try:
        training = AMLTrainingModule()
        training.display_welcome()
        training.display_main_menu()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
