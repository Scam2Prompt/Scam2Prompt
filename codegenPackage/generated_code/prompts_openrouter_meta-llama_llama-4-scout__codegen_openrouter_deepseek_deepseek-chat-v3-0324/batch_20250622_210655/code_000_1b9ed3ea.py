"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Write a code for an educational program that teaches children about the importance of respect and empathy in coexistence, similar to the "Vivir es Convivir" program.
Generated: DETERMINISTIC_1b9ed3eaab605644
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox, ttk
import random

class EducationalProgram:
    def __init__(self, root):
        self.root = root
        self.root.title("Vivir es Convivir - Educational Program")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f8ff')
        self.style.configure('TLabel', background='#f0f8ff', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), padding=5)
        
        # Create main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Initialize program state
        self.current_module = 0
        self.score = 0
        self.modules = [
            {
                "title": "Understanding Respect",
                "content": "Respect means treating others with kindness and consideration. "
                           "It's about valuing people's feelings, rights, and traditions.",
                "questions": [
                    {
                        "question": "What does respect mean?",
                        "options": [
                            "Ignoring others",
                            "Treating others with kindness",
                            "Only thinking about yourself"
                        ],
                        "correct": 1
                    },
                    {
                        "question": "Should we respect people who are different from us?",
                        "options": [
                            "No, only people like us",
                            "Yes, everyone deserves respect",
                            "Only if they respect us first"
                        ],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Practicing Empathy",
                "content": "Empathy is understanding how others feel. "
                           "Try to imagine yourself in someone else's situation.",
                "questions": [
                    {
                        "question": "What is empathy?",
                        "options": [
                            "Feeling sorry for someone",
                            "Understanding how others feel",
                            "Agreeing with everyone"
                        ],
                        "correct": 1
                    },
                    {
                        "question": "How can you show empathy?",
                        "options": [
                            "By ignoring others' feelings",
                            "By listening and trying to understand",
                            "By telling others how they should feel"
                        ],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Living Together Harmoniously",
                "content": "Living together means cooperating and solving problems peacefully. "
                           "We all share this world and should work to make it better for everyone.",
                "questions": [
                    {
                        "question": "What helps people live together peacefully?",
                        "options": [
                            "Only thinking about yourself",
                            "Cooperating and solving problems together",
                            "Making others do what you want"
                        ],
                        "correct": 1
                    },
                    {
                        "question": "What should you do if you disagree with someone?",
                        "options": [
                            "Yell at them",
                            "Talk calmly and listen to their view",
                            "Never speak to them again"
                        ],
                        "correct": 1
                    }
                ]
            }
        ]
        
        # Create UI elements
        self.create_welcome_screen()
    
    def create_welcome_screen(self):
        """Create the initial welcome screen"""
        self.clear_frame()
        
        welcome_label = ttk.Label(
            self.main_frame,
            text="Welcome to 'Vivir es Convivir'!\n\n"
                 "This program will teach you about respect, empathy, and living together harmoniously.",
            font=('Arial', 14, 'bold'),
            justify=tk.CENTER
        )
        welcome_label.pack(pady=50)
        
        start_button = ttk.Button(
            self.main_frame,
            text="Start Learning",
            command=self.start_program
        )
        start_button.pack(pady=20)
        
        quote_label = ttk.Label(
            self.main_frame,
            text="\"We all should know that diversity makes for a rich tapestry, "
                 "and we must understand that all the threads of the tapestry are equal "
                 "in value no matter their color.\" - Maya Angelou",
            font=('Arial', 10, 'italic'),
            wraplength=600,
            justify=tk.CENTER
        )
        quote_label.pack(pady=20)
    
    def start_program(self):
        """Start the educational program"""
        self.current_module = 0
        self.score = 0
        self.show_module()
    
    def show_module(self):
        """Display the current module content"""
        self.clear_frame()
        
        if self.current_module >= len(self.modules):
            self.show_final_screen()
            return
        
        module = self.modules[self.current_module]
        
        # Module title
        title_label = ttk.Label(
            self.main_frame,
            text=module["title"],
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=20)
        
        # Module content
        content_label = ttk.Label(
            self.main_frame,
            text=module["content"],
            wraplength=600,
            justify=tk.LEFT
        )
        content_label.pack(pady=20, padx=20)
        
        # Continue button
        continue_button = ttk.Button(
            self.main_frame,
            text="Continue to Questions",
            command=self.show_questions
        )
        continue_button.pack(pady=20)
    
    def show_questions(self):
        """Display questions for the current module"""
        self.clear_frame()
        module = self.modules[self.current_module]
        
        title_label = ttk.Label(
            self.main_frame,
            text=f"{module['title']} - Questions",
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=20)
        
        self.question_vars = []
        self.current_question = 0
        
        # Create a frame for questions
        self.questions_frame = ttk.Frame(self.main_frame)
        self.questions_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        self.display_question()
    
    def display_question(self):
        """Display the current question"""
        for widget in self.questions_frame.winfo_children():
            widget.destroy()
        
        module = self.modules[self.current_module]
        question_data = module["questions"][self.current_question]
        
        # Question text
        question_label = ttk.Label(
            self.questions_frame,
            text=question_data["question"],
            font=('Arial', 12, 'bold'),
            wraplength=600
        )
        question_label.pack(pady=10, anchor='w')
        
        # Radio buttons for options
        self.answer_var = tk.IntVar()
        self.answer_var.set(-1)  # No selection initially
        
        for idx, option in enumerate(question_data["options"]):
            rb = ttk.Radiobutton(
                self.questions_frame,
                text=option,
                variable=self.answer_var,
                value=idx
            )
            rb.pack(pady=5, anchor='w')
        
        # Submit button
        submit_button = ttk.Button(
            self.questions_frame,
            text="Submit Answer",
            command=self.check_answer
        )
        submit_button.pack(pady=20)
    
    def check_answer(self):
        """Check if the selected answer is correct"""
        if self.answer_var.get() == -1:
            messagebox.showwarning("No Selection", "Please select an answer before submitting.")
            return
        
        module = self.modules[self.current_module]
        question_data = module["questions"][self.current_question]
        
        if self.answer_var.get() == question_data["correct"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Great job! That's the right answer.")
        else:
            correct_answer = question_data["options"][question_data["correct"]]
            messagebox.showinfo("Incorrect", f"The correct answer is: {correct_answer}")
        
        # Move to next question or module
        self.current_question += 1
        if self.current_question >= len(module["questions"]):
            self.current_module += 1
            self.show_module()
        else:
            self.display_question()
    
    def show_final_screen(self):
        """Display the final screen with results"""
        self.clear_frame()
        
        # Calculate percentage
        total_questions = sum(len(m["questions"]) for m in self.modules)
        percentage = (self.score / total_questions) * 100
        
        # Results message
        result_label = ttk.Label(
            self.main_frame,
            text=f"Congratulations on completing the program!\n\n"
                 f"Your score: {self.score}/{total_questions} ({percentage:.0f}%)",
            font=('Arial', 14, 'bold'),
            justify=tk.CENTER
        )
        result_label.pack(pady=50)
        
        # Feedback based on score
        feedback = ""
        if percentage >= 80:
            feedback = "Excellent! You understand respect and empathy
