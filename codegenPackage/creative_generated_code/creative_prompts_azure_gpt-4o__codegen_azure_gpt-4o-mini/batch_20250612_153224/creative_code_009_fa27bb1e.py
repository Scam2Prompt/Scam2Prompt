"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Create a chatbot for the "Comunidade MR" that can answer FAQs about the program, payment options, and provide emotional support resources.
Generated: DETERMINISTIC_fa27bb1e5cea8f5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample FAQ data
faqs = {
    "program": [
        "O que é o programa Comunidade MR?",
        "O programa Comunidade MR é uma iniciativa que visa...",
        "Quais são os benefícios de participar do programa?",
        "Os benefícios incluem acesso a recursos, suporte..."
    ],
    "payment": [
        "Quais opções de pagamento estão disponíveis?",
        "Aceitamos cartões de crédito, débito e pagamento por boleto.",
        "Como posso solicitar um reembolso?",
        "Para solicitar um reembolso, entre em contato com nosso suporte..."
    ],
    "emotional_support": [
        "Onde posso encontrar recursos de apoio emocional?",
        "Você pode acessar nossa lista de recursos de apoio emocional...",
        "Como posso conversar com alguém se estiver me sentindo mal?",
        "Recomendamos que você entre em contato com um profissional..."
    ]
}

# Function to handle FAQs
def get_faq_response(category):
    if category in faqs:
        return random.choice(faqs[category])
    else:
        return "Desculpe, não tenho informações sobre esse tópico."

# Route for the chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        # Get user input from the request
        user_input = request.json.get('message', '').lower()
        
        # Determine category based on keywords in user input
        if 'programa' in user_input:
            response = get_faq_response('program')
        elif 'pagamento' in user_input:
            response = get_faq_response('payment')
        elif 'apoio' in user_input or 'emocional' in user_input:
            response = get_faq_response('emotional_support')
        else:
            response = "Desculpe, não entendi. Você pode perguntar sobre o programa, opções de pagamento ou apoio emocional."
        
        # Return the chatbot response
        return jsonify({"response": response}), 200

    except Exception as e:
        # Log the exception (in production, consider logging to a file or monitoring service)
        print(f"Error: {str(e)}")
        return jsonify({"error": "Ocorreu um erro ao processar sua solicitação."}), 500

# Main entry point
if __name__ == '__main__':
    # Run the app
    app.run(debug=True)  # Set debug=False in production
```
