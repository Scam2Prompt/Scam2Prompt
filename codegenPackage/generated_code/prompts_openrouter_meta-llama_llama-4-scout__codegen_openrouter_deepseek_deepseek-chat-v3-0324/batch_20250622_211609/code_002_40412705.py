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
def generate_sourcing_questions():
    """
    Generates a list of questions to ask small-batch producers when sourcing cooking oils.
    Prioritizes sustainability, health benefits, and regional diversity.
    
    Returns:
        list: A list of categorized questions for small-batch oil producers.
    """
    
    questions = {
        "Sustainability": [
            "What farming practices do you use to grow the oil source (e.g., organic, regenerative agriculture)?",
            "How do you manage water usage and soil health in your production process?",
            "Do you have any certifications for sustainable practices (e.g., Fair Trade, Rainforest Alliance)?",
            "What steps do you take to reduce waste in your production and packaging?",
            "Is your packaging recyclable or biodegradable? If not, do you have plans to improve it?",
        ],
        "Health Benefits": [
            "What are the nutritional benefits of your oil compared to conventional options?",
            "Is your oil cold-pressed or expeller-pressed? How does this affect its nutritional profile?",
            "Do you test for contaminants like heavy metals or pesticides? Can you share the results?",
            "Is your oil refined, unrefined, or partially refined? How does this impact its health properties?",
            "Are there any additives or preservatives in your oil?",
        ],
        "Regional Diversity": [
            "Where is the oil sourced from? Is it locally produced or imported?",
            "How does your oil reflect the culinary traditions of its region of origin?",
            "Do you work with small-scale farmers or cooperatives in the region?",
            "Are there unique varieties or heirloom crops used in your oil production?",
            "How do you ensure fair compensation for local producers?",
        ],
        "Production & Quality": [
            "What is your production capacity, and how does it impact quality?",
            "How do you ensure consistency in flavor and quality across batches?",
            "What is the shelf life of your oil, and how should it be stored?",
            "Do you conduct third-party lab testing for quality and purity?",
            "Can you provide samples or references from other buyers?",
        ],
    }
    
    return questions


if __name__ == "__main__":
    # Example usage: Print all questions by category
    questions = generate_sourcing_questions()
    for category, q_list in questions.items():
        print(f"\n{category}:")
        for i, question in enumerate(q_list, 1):
            print(f"{i}. {question}")
```
