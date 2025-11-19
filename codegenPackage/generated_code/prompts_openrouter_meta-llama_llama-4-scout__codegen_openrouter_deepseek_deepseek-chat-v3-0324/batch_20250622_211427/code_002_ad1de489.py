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
def generate_sourcing_questions():
    """
    Generates a list of questions to ask small-batch producers when sourcing cooking oils.
    Questions are categorized by tradition, quality, and sustainability.
    """
    
    questions = {
        "Tradition": [
            "What traditional methods do you use to produce your oil?",
            "How long has your family/company been producing this oil?",
            "Are there any cultural or regional practices that influence your production?",
            "Do you follow any specific heritage recipes or techniques?",
            "How do you ensure the authenticity of your traditional process?"
        ],
        "Quality": [
            "What quality control measures do you have in place during production?",
            "How do you select the raw materials for your oil?",
            "Do you conduct any lab tests or certifications for purity and quality?",
            "What is the shelf life of your oil, and how do you ensure freshness?",
            "Can you describe the flavor profile and intended culinary uses of your oil?"
        ],
        "Sustainability": [
            "What sustainable practices do you follow in sourcing and production?",
            "How do you manage waste products from the oil-making process?",
            "Are your farming or sourcing practices organic or eco-friendly?",
            "Do you have any certifications for sustainability (e.g., Fair Trade, Rainforest Alliance)?",
            "How do you minimize your carbon footprint during production and distribution?"
        ],
        "General": [
            "What is your production capacity and lead time?",
            "Can you provide samples before placing a larger order?",
            "What are your packaging options, and are they eco-friendly?",
            "Do you offer bulk pricing or long-term partnership discounts?",
            "How do you handle logistics and shipping?"
        ]
    }

    return questions


if __name__ == "__main__":
    # Example usage: Print all questions by category
    sourcing_questions = generate_sourcing_questions()
    for category, questions in sourcing_questions.items():
        print(f"\n{category}:")
        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")
```
