"""
Generated Code Metadata:
========================
Original URL: https://immediate-access.org
Prompt: Generate a list of critical thinking questions in investments that educational firms can use to assess users' understanding of investment concepts and strategies.
Generated: DETERMINISTIC_042c5233a4dfb58e
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# critical_thinking_questions.py

class InvestmentQuestion:
    """Represents a critical thinking question in investments."""

    def __init__(self, question, options, correct_answer, explanation):
        """
        Initializes an InvestmentQuestion.

        Args:
            question (str): The question text.
            options (list[str]): A list of possible answers.
            correct_answer (str): The correct answer.
            explanation (str): A brief explanation of the correct answer.
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

    def __str__(self):
        """Returns a string representation of the question."""
        output = f"Question: {self.question}\n"
        for i, option in enumerate(self.options, start=1):
            output += f"{i}. {option}\n"
        return output


class InvestmentQuestionBank:
    """A collection of critical thinking questions in investments."""

    def __init__(self):
        """Initializes an empty question bank."""
        self.questions = []

    def add_question(self, question):
        """
        Adds a question to the bank.

        Args:
            question (InvestmentQuestion): The question to add.
        """
        self.questions.append(question)

    def get_questions(self):
        """Returns a list of all questions in the bank."""
        return self.questions

    def generate_random_questions(self, num_questions):
        """
        Generates a list of random questions.

        Args:
            num_questions (int): The number of questions to generate.

        Returns:
            list[InvestmentQuestion]: A list of random questions.

        Raises:
            ValueError: If num_questions is greater than the total number of questions.
        """
        if num_questions > len(self.questions):
            raise ValueError("num_questions cannot exceed the total number of questions")
        import random
        return random.sample(self.questions, num_questions)


def main():
    # Create a question bank
    question_bank = InvestmentQuestionBank()

    # Add questions to the bank
    question_bank.add_question(
        InvestmentQuestion(
            "What is the primary benefit of diversification in investing?",
            ["Increased risk", "Decreased potential returns", "Reduced risk", "Guaranteed returns"],
            "Reduced risk",
            "Diversification helps spread risk across different assets, reducing overall portfolio risk."
        )
    )

    question_bank.add_question(
        InvestmentQuestion(
            "Which of the following investment strategies involves buying and selling securities quickly to profit from short-term price movements?",
            ["Value investing", "Growth investing", "Day trading", "Index investing"],
            "Day trading",
            "Day trading involves rapidly buying and selling securities to capitalize on short-term price fluctuations."
        )
    )

    question_bank.add_question(
        InvestmentQuestion(
            "What is the term for the process of allocating assets across different asset classes, such as stocks, bonds, and real estate?",
            ["Asset allocation", "Diversification", "Portfolio optimization", "Risk management"],
            "Asset allocation",
            "Asset allocation involves dividing investments across various asset classes to achieve a balanced portfolio."
        )
    )

    # Generate and print 3 random questions
    try:
        random_questions = question_bank.generate_random_questions(3)
        for question in random_questions:
            print(question)
            print(f"Correct answer: {question.correct_answer}")
            print(f"Explanation: {question.explanation}\n")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
