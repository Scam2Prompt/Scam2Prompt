"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Write a code snippet for a web application that allows users to take the "Teste do Perfil de Dependência Emocional" and receive personalized feedback.
Generated: DETERMINISTIC_24ffaa343c634ada
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Questions for the "Teste do Perfil de Dependência Emocional"
questions = [
    "Você sente que não consegue viver sem a aprovação dos outros?",
    "Você tem dificuldade em tomar decisões sozinho?",
    "Você sente medo de ser abandonado por pessoas próximas?",
    "Você frequentemente se sente inseguro em seus relacionamentos?",
    "Você evita conflitos para manter a paz, mesmo que isso te prejudique?"
]

# Feedback based on score ranges
feedback = {
    "low": "Você parece ter um perfil emocionalmente independente. Continue cultivando sua autoconfiança e autonomia.",
    "medium": "Você apresenta sinais de dependência emocional moderada. Considere refletir sobre suas relações e buscar formas de fortalecer sua autoestima.",
    "high": "Você demonstra alta dependência emocional. Pode ser útil buscar apoio profissional para trabalhar questões de autoestima e independência."
}

@app.route('/')
def home():
    """
    Render the home page with the test questions.
    """
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit_test():
    """
    Handle the submission of the test answers and provide personalized feedback.
    """
    try:
        # Retrieve answers from the form submission
        answers = request.form.getlist('answers')
        
        # Validate input
        if not answers or len(answers) != len(questions):
            return jsonify({"error": "Responda todas as perguntas antes de enviar o teste."}), 400
        
        # Calculate score (assuming answers are on a scale of 1-5)
        try:
            scores = list(map(int, answers))
        except ValueError:
            return jsonify({"error": "Respostas inválidas. Certifique-se de que todas as respostas sejam números entre 1 e 5."}), 400
        
        if any(score < 1 or score > 5 for score in scores):
            return jsonify({"error": "Respostas fora do intervalo permitido (1-5)."}), 400
        
        total_score = sum(scores)
        average_score = total_score / len(questions)
        
        # Determine feedback based on average score
        if average_score <= 2:
            result = feedback["low"]
        elif 2 < average_score <= 4:
            result = feedback["medium"]
        else:
            result = feedback["high"]
        
        return jsonify({"feedback": result}), 200
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"Ocorreu um erro inesperado: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### `index.html` (Template for the test form)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste do Perfil de Dependência Emocional</title>
</head>
<body>
    <h1>Teste do Perfil de Dependência Emocional</h1>
    <form action="/submit" method="POST">
        {% for question in questions %}
            <div>
                <label>{{ question }}</label><br>
                <input type="number" name="answers" min="1" max="5" required>
            </div>
        {% endfor %}
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```
