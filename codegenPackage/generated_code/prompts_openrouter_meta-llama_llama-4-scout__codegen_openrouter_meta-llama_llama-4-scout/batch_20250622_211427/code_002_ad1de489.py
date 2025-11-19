"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.net
Prompt: Generate a list of questions to ask small-batch producers when sourcing cooking oils, prioritizing factors such as tradition, quality, and sustainability.
Generated: DETERMINISTIC_ad1de4892488c130
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProducerQuestionnaire:
    def __init__(self):
        self.questions = []

    def add_question(self, category, question, description):
        """Add a question to the questionnaire."""
        self.questions.append({
            "category": category,
            "question": question,
            "description": description
        })

    def get_questions(self):
        """Return the list of questions."""
        return self.questions


class ProducerSourcing:
    def __init__(self):
        self.questionnaire = ProducerQuestionnaire()
        self.initialize_questionnaire()

    def initialize_questionnaire(self):
        """Initialize the questionnaire with questions."""
        # Tradition
        self.questionnaire.add_question(
            "Tradition",
            "What is the history of your oil production?",
            "Understanding the producer's background and experience."
        )
        self.questionnaire.add_question(
            "Tradition",
            "What traditional methods do you use for oil production?",
            "Assessing the use of traditional techniques."
        )

        # Quality
        self.questionnaire.add_question(
            "Quality",
            "What is the quality control process for your oils?",
            "Evaluating the producer's quality assurance measures."
        )
        self.questionnaire.add_question(
            "Quality",
            "How do you ensure the purity and authenticity of your oils?",
            "Verifying the producer's methods for maintaining oil quality."
        )

        # Sustainability
        self.questionnaire.add_question(
            "Sustainability",
            "What sustainable practices do you use in oil production?",
            "Assessing the producer's environmental responsibility."
        )
        self.questionnaire.add_question(
            "Sustainability",
            "How do you source your raw materials?",
            "Evaluating the producer's supply chain and sourcing practices."
        )

        # Additional questions
        self.questionnaire.add_question(
            "General",
            "What certifications or compliance do you have (e.g., ISO, organic)?",
            "Verifying the producer's compliance with industry standards."
        )
        self.questionnaire.add_question(
            "General",
            "Can you provide references or examples of previous customers?",
            "Evaluating the producer's reputation and customer satisfaction."
        )

    def print_questionnaire(self):
        """Print the questionnaire."""
        for category in set([q["category"] for q in self.questionnaire.get_questions()]):
            print(f"**{category}**")
            for question in self.questionnaire.get_questions():
                if question["category"] == category:
                    print(f"* {question['question']}: {question['description']}")
            print()


def main():
    try:
        sourcing = ProducerSourcing()
        sourcing.print_questionnaire()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
