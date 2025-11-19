"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: Write a code for a simple screening tool that could be used to identify children with Autism Spectrum Disorders, inspired by Jewel Child Development Screening Tool.
Generated: DETERMINISTIC_4e0b38b4201d59b1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox

class AutismScreeningTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Autism Spectrum Disorder Screening Tool")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        self.questions = [
            "Does your child respond to their name when called?",
            "Does your child make eye contact when interacting?",
            "Does your child engage in pretend or imaginative play?",
            "Does your child point to show interest in something?",
            "Does your child show interest in other children?",
            "Does your child have unusual or repetitive movements?",
            "Does your child have intense interests in specific topics?",
            "Does your child have difficulty with changes in routine?",
            "Does your child respond to others' emotions appropriately?",
            "Does your child have delayed speech or language skills?"
        ]
        
        self.responses = []
        self.current_question = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header = tk.Label(
            self.root,
            text="Autism Spectrum Disorder Screening Tool",
            font=("Arial", 16, "bold"),
            pady=10
        )
        header.pack()
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Please answer the following questions about your child's behavior:",
            font=("Arial", 10),
            pady=5
        )
        instructions.pack()
        
        # Question display
        self.question_label = tk.Label(
            self.root,
            text=self.questions[self.current_question],
            font=("Arial", 12),
            wraplength=500,
            pady=20
        )
        self.question_label.pack()
        
        # Response buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.yes_button = tk.Button(
            button_frame,
            text="Yes",
            command=lambda: self.record_response(True),
            width=10
        )
        self.yes_button.pack(side=tk.LEFT, padx=10)
        
        self.no_button = tk.Button(
            button_frame,
            text="No",
            command=lambda: self.record_response(False),
            width=10
        )
        self.no_button.pack(side=tk.LEFT, padx=10)
        
        # Progress indicator
        self.progress_label = tk.Label(
            self.root,
            text=f"Question {self.current_question + 1} of {len(self.questions)}",
            font=("Arial", 10),
            pady=10
        )
        self.progress_label.pack()
        
        # Navigation buttons
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=20)
        
        self.prev_button = tk.Button(
            nav_frame,
            text="Previous",
            command=self.prev_question,
            state=tk.DISABLED,
            width=10
        )
        self.prev_button.pack(side=tk.LEFT, padx=10)
        
        self.next_button = tk.Button(
            nav_frame,
            text="Next",
            command=self.next_question,
            width=10
        )
        self.next_button.pack(side=tk.LEFT, padx=10)
        
        # Exit button
        exit_button = tk.Button(
            self.root,
            text="Exit",
            command=self.root.quit,
            width=10
        )
        exit_button.pack(side=tk.BOTTOM, pady=20)
    
    def record_response(self, response):
        if len(self.responses) <= self.current_question:
            self.responses.append(response)
        else:
            self.responses[self.current_question] = response
    
    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.update_ui()
        else:
            self.show_results()
    
    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.update_ui()
    
    def update_ui(self):
        self.question_label.config(text=self.questions[self.current_question])
        self.progress_label.config(text=f"Question {self.current_question + 1} of {len(self.questions)}")
        
        # Update button states
        self.prev_button.config(state=tk.NORMAL if self.current_question > 0 else tk.DISABLED)
        self.next_button.config(text="Next" if self.current_question < len(self.questions) - 1 else "Finish")
    
    def show_results(self):
        # Scoring: Higher scores indicate more ASD-related behaviors
        score = sum(1 for response in self.responses if not response)
        
        result_message = f"Screening completed. Score: {score}/{len(self.questions)}\n\n"
        
        if score >= 6:
            result_message += "The screening suggests a higher likelihood of Autism Spectrum Disorder. " \
                             "Please consult with a healthcare professional for further evaluation."
        elif score >= 3:
            result_message += "The screening suggests some behaviors associated with Autism Spectrum Disorder. " \
                             "Consider discussing these results with a healthcare professional."
        else:
            result_message += "The screening does not suggest significant signs of Autism Spectrum Disorder. " \
                             "However, if you have concerns, please consult with a healthcare professional."
        
        messagebox.showinfo("Screening Results", result_message)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutismScreeningTool(root)
    root.mainloop()
```
