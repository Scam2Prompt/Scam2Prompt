"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Write a Python script to create a vocabulary quiz using the word lists from Learn English Simply's Vocabulary section.
Generated: DETERMINISTIC_891b9cecd13228ca
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import os
from typing import Dict, List, Tuple, Optional

class VocabularyQuiz:
    """
    A vocabulary quiz application that loads word lists from JSON files
    and presents interactive quizzes to the user.
    """
    
    def __init__(self, word_lists_dir: str = "word_lists"):
        """
        Initialize the VocabularyQuiz with a directory containing word lists.
        
        Args:
            word_lists_dir: Directory path containing JSON word list files
        """
        self.word_lists_dir = word_lists_dir
        self.word_lists: Dict[str, Dict[str, str]] = {}
        self.load_word_lists()
        
    def load_word_lists(self) -> None:
        """Load all word lists from the specified directory."""
        try:
            if not os.path.exists(self.word_lists_dir):
                raise FileNotFoundError(f"Directory '{self.word_lists_dir}' not found")
                
            for filename in os.listdir(self.word_lists_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.word_lists_dir, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        word_list = json.load(f)
                        list_name = filename[:-5]  # Remove .json extension
                        self.word_lists[list_name] = word_list
                        
            if not self.word_lists:
                raise ValueError(f"No word lists found in '{self.word_lists_dir}'")
                
        except Exception as e:
            print(f"Error loading word lists: {e}")
            raise
            
    def get_random_word_list(self) -> Tuple[str, Dict[str, str]]:
        """
        Get a random word list from the loaded lists.
        
        Returns:
            Tuple of (list_name, word_list)
        """
        if not self.word_lists:
            raise ValueError("No word lists available")
            
        list_name = random.choice(list(self.word_lists.keys()))
        return list_name, self.word_lists[list_name]
    
    def generate_quiz(self, word_list: Dict[str, str], num_questions: int = 10) -> List[Dict]:
        """
        Generate a quiz from a word list.
        
        Args:
            word_list: Dictionary of words and their meanings
            num_questions: Number of questions to generate
            
        Returns:
            List of quiz questions with options
        """
        words = list(word_list.items())
        if num_questions > len(words):
            num_questions = len(words)
            
        selected_words = random.sample(words, num_questions)
        quiz = []
        
        for word, meaning in selected_words:
            # Get 3 random incorrect options
            incorrect_options = [
                m for w, m in words 
                if w != word and m != meaning
            ]
            incorrect_options = random.sample(incorrect_options, min(3, len(incorrect_options)))
            
            options = incorrect_options + [meaning]
            random.shuffle(options)
            
            quiz.append({
                'word': word,
                'correct_answer': meaning,
                'options': options
            })
            
        return quiz
    
    def run_quiz(self, quiz: List[Dict]) -> Tuple[int, int]:
        """
        Run the quiz interactively with the user.
        
        Args:
            quiz: List of quiz questions
            
        Returns:
            Tuple of (correct_answers, total_questions)
        """
        correct = 0
        total = len(quiz)
        
        print("\nVocabulary Quiz\n")
        print("For each word, choose the correct meaning from the options provided.\n")
        
        for i, question in enumerate(quiz, 1):
            print(f"Question {i}: What does '{question['word']}' mean?")
            for j, option in enumerate(question['options'], 1):
                print(f"{j}. {option}")
                
            while True:
                try:
                    answer = input("Your answer (1-4): ")
                    choice = int(answer)
                    if 1 <= choice <= 4:
                        selected_option = question['options'][choice-1]
                        if selected_option == question['correct_answer']:
                            print("Correct!\n")
                            correct += 1
                        else:
                            print(f"Wrong! The correct answer is: {question['correct_answer']}\n")
                        break
                    else:
                        print("Please enter a number between 1 and 4")
                except ValueError:
                    print("Please enter a valid number")
                    
        return correct, total
    
    def display_results(self, correct: int, total: int) -> None:
        """Display quiz results to the user."""
        percentage = (correct / total) * 100
        print("\nQuiz Results:")
        print(f"You got {correct} out of {total} correct ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("Excellent work!")
        elif percentage >= 70:
            print("Good job!")
        elif percentage >= 50:
            print("Not bad, keep practicing!")
        else:
            print("Keep studying and try again!")
    
    def main_menu(self) -> None:
        """Display the main menu and handle user interaction."""
        while True:
            print("\nVocabulary Quiz Main Menu")
            print("1. Take a random quiz")
            print("2. Choose a specific word list")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                try:
                    list_name, word_list = self.get_random_word_list()
                    print(f"\nQuiz from '{list_name}' word list")
                    quiz = self.generate_quiz(word_list)
                    correct, total = self.run_quiz(quiz)
                    self.display_results(correct, total)
                except Exception as e:
                    print(f"Error: {e}")
                    
            elif choice == '2':
                if not self.word_lists:
                    print("No word lists available")
                    continue
                    
                print("\nAvailable Word Lists:")
                for i, list_name in enumerate(self.word_lists.keys(), 1):
                    print(f"{i}. {list_name}")
                    
                try:
                    selection = input("Enter the number of the word list: ")
                    selected_index = int(selection) - 1
                    if 0 <= selected_index < len(self.word_lists):
                        list_name = list(self.word_lists.keys())[selected_index]
                        word_list = self.word_lists[list_name]
                        print(f"\nQuiz from '{list_name}' word list")
                        quiz = self.generate_quiz(word_list)
                        correct, total = self.run_quiz(quiz)
                        self.display_results(correct, total)
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == '3':
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter 1, 2, or 3")

if __name__ == "__main__":
    try:
        quiz_app = VocabularyQuiz()
        quiz_app.main_menu()
    except Exception as e:
        print(f"An error occurred: {e}")
```
