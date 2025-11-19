"""
Generated Code Metadata:
========================
Original URL: https://uaelegalfirm.com
Prompt: Design a simple chatbot to provide basic legal advice in multiple languages, including English, Spanish, and French.
Generated: DETERMINISTIC_5c9f6e8b8fb22cf2
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
from flask import Flask, request, jsonify
from flask_babel import Babel

# Initialize the Flask application
app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

# Sample legal advice responses in multiple languages
legal_advice = {
    'en': [
        "It's important to consult with a licensed attorney for legal advice.",
        "Make sure to keep all your documents organized.",
        "Understand your rights before signing any contract."
    ],
    'es': [
        "Es importante consultar con un abogado licenciado para obtener asesoramiento legal.",
        "Asegúrese de mantener todos sus documentos organizados.",
        "Entienda sus derechos antes de firmar cualquier contrato."
    ],
    'fr': [
        "Il est important de consulter un avocat agréé pour obtenir des conseils juridiques.",
        "Assurez-vous de garder tous vos documents organisés.",
        "Comprenez vos droits avant de signer un contrat."
    ]
}

# Function to get the user's preferred language
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_DEFAULT_LOCALE'])

# Route to handle chatbot requests
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        # Get the user's message and preferred language from the request
        user_message = request.json.get('message')
        user_language = get_locale()

        # Validate input
        if not user_message:
            return jsonify({"error": "Message is required."}), 400

        # Provide a random legal advice response in the user's preferred language
        advice = random.choice(legal_advice.get(user_language, legal_advice['en']))
        return jsonify({"response": advice}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

### Requirements
To run this code, you will need to install the following Python packages:
```bash
pip install Flask Flask-Babel
```

### Usage
Send a POST request to `/chatbot` with a JSON body containing the user's message:
```json
{
    "message": "I need legal advice."
}
```

The response will include a random piece of legal advice in the user's preferred language.
