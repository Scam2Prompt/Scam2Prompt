"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Generate a list of questions to ask small-batch producers when sourcing cooking oils, prioritizing factors like sustainability, health benefits, and regional diversity.
Generated: DETERMINISTIC_40412705fc807682
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Module to generate a list of questions for small-batch producers when sourcing cooking oils.
The questions prioritize factors like sustainability, health benefits, and regional diversity.
"""

class CookingOilProducerQuestionnaire:
    def __init__(self):
        self.questions = []

    def add_question(self, category, question, description=""):
        """
        Add a question to the questionnaire.

        Args:
            category (str): Category of the question (e.g., sustainability, health benefits).
            question (str): The question to ask.
            description (str, optional): A brief description of the question. Defaults to "".
        """
        self.questions.append({"category": category, "question": question, "description": description})

    def get_questions(self):
        """
        Get the list of questions.

        Returns:
            list: A list of dictionaries containing the questions and their categories.
        """
        return self.questions


def main():
    try:
        questionnaire = CookingOilProducerQuestionnaire()

        # Sustainability questions
        questionnaire.add_question(
            "Sustainability",
            "What practices do you use to ensure sustainable oil production (e.g., crop rotation, organic farming)?",
        )
        questionnaire.add_question(
            "Sustainability",
            "How do you minimize waste and reduce environmental impact in your production process?",
        )
        questionnaire.add_question(
            "Sustainability",
            "Are you certified by any third-party organizations (e.g., USDA Organic, Fair Trade)?",
        )

        # Health benefits questions
        questionnaire.add_question(
            "Health Benefits",
            "What types of oil do you produce, and what are their nutritional benefits?",
        )
        questionnaire.add_question(
            "Health Benefits",
            "How do you ensure the quality and purity of your oils?",
        )
        questionnaire.add_question(
            "Health Benefits",
            "Do you use any additives or preservatives in your oils?",
        )

        # Regional diversity questions
        questionnaire.add_question(
            "Regional Diversity",
            "What region or country do you source your raw materials from?",
        )
        questionnaire.add_question(
            "Regional Diversity",
            "How do you support local farmers and communities in your supply chain?",
        )
        questionnaire.add_question(
            "Regional Diversity",
            "Do you offer any unique or heirloom varieties of oils?",
        )

        # General questions
        questionnaire.add_question(
            "General",
            "What is your production process, and how do you ensure consistency in quality?",
        )
        questionnaire.add_question(
            "General",
            "What is your pricing structure, and are there any discounts for bulk orders?",
        )

        questions = questionnaire.get_questions()

        # Print the questions
        for i, q in enumerate(questions, start=1):
            print(f"{i}. **{q['category']}:** {q['question']}")
            if q["description"]:
                print(f"   - {q['description']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
