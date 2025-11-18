"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Write code to integrate a multilingual FAQ section into an investment education website, inspired by Immediate Migna's accessible and inclusive design.
Generated: DETERMINISTIC_1864954cb24224cc
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import json

# Initialize the Flask application
app = Flask(__name__)

# Load FAQ data from JSON file
def load_faqs():
    try:
        with open('faqs.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "FAQ data file not found"}
    except json.JSONDecodeError:
        return {"error": "FAQ data file is invalid"}

# Load FAQs
faqs = load_faqs()

# Route to fetch FAQs based on language preference
@app.route('/faqs/<language>', methods=['GET'])
def get_faqs(language):
    """
    Route to fetch FAQs in the requested language.
    :param language: Language code (e.g., 'en', 'es', 'fr').
    :return: JSON response containing FAQs in the requested language.
    """
    if faqs.get("error"):
        return jsonify(faqs), 500  # Return error if FAQ data could not be loaded

    if language in faqs:
        return jsonify(faqs[language])  # Return FAQs in the requested language
    else:
        # Handle case where the requested language is not available
        return jsonify({"error": f"Language '{language}' not supported"}), 404

# Default route to render FAQ page
@app.route('/faq', methods=['GET'])
def faq_page():
    """
    Default route to render FAQ page with language selection.
    """
    return render_template('faq.html')  # Render a template for FAQs

# Run the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

```json
// Example faqs.json file content
{
    "en": [
        {
            "question": "What is investment?",
            "answer": "Investment is the act of allocating resources, usually money, with the expectation of generating an income or profit."
        },
        {
            "question": "How do I start investing?",
            "answer": "You can start by learning basic investment principles, setting financial goals, and consulting a financial advisor."
        }
    ],
    "es": [
        {
            "question": "¿Qué es la inversión?",
            "answer": "La inversión es el acto de asignar recursos, generalmente dinero, con la expectativa de generar ingresos o beneficios."
        },
        {
            "question": "¿Cómo empiezo a invertir?",
            "answer": "Puedes comenzar aprendiendo principios básicos de inversión, estableciendo metas financieras y consultando a un asesor financiero."
        }
    ],
    "fr": [
        {
            "question": "Qu'est-ce que l'investissement?",
            "answer": "L'investissement consiste à allouer des ressources, généralement de l'argent, dans l'attente de générer un revenu ou un profit."
        },
        {
            "question": "Comment commencer à investir?",
            "answer": "Vous pouvez commencer par apprendre les principes fondamentaux de l'investissement, fixer des objectifs financiers et consulter un conseiller financier."
        }
    ]
}
```

```html
<!-- Example faq.html template -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQs - Investment Education</title>
</head>
<body>
    <h1>Frequently Asked Questions</h1>
    <p>Select your preferred language:</p>
    <ul>
        <li><a href="/faqs/en">English</a></li>
        <li><a href="/faqs/es">Español</a></li>
        <li><a href="/faqs/fr">Français</a></li>
    </ul>
</body>
</html>
```
