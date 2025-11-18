"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Write code to create a web-based "Teste do Perfil de Dependência Emocional" quiz as described in Sabrina Alves' methodology, including scoring logic and personalized feedback.
Generated: DETERMINISTIC_1d3ca9f4d561bd5e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Question data for the Emotional Dependency Profile Quiz
quiz_questions = [
    {"question": "Você sente necessidade de aprovação constante dos outros?", "options": ["Sim", "Não"]},
    {"question": "Você acha difícil tomar decisões sozinho(a)?", "options": ["Sim", "Não"]},
    {"question": "Você sente medo de ser abandonado(a)?", "options": ["Sim", "Não"]},
    {"question": "Você frequentemente coloca as necessidades dos outros acima das suas?", "options": ["Sim", "Não"]},
    {"question": "Você sente dificuldade em dizer 'não'?", "options": ["Sim", "Não"]},
]

# Scoring logic: Each "Sim" answer adds 1 point
def calculate_score(answers):
    score = sum(1 for answer in answers if answer == "Sim")
    return score

# Feedback based on the score
def generate_feedback(score):
    if score <= 1:
        return "Você tem um perfil de dependência emocional muito baixo. Parabéns pela sua independência emocional!"
    elif score <= 3:
        return "Você apresenta sinais moderados de dependência emocional. Considere refletir sobre situações em que pode reforçar sua autonomia."
    else:
        return "Você possui um perfil de dependência emocional elevado. Pode ser útil buscar apoio para trabalhar sua autoconfiança e independência."

@app.route('/')
def home():
    # Render the home page with the quiz introduction
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Retrieve answers and process the final result
        answers = [request.form.get(f"q{i}") for i in range(len(quiz_questions))]
        if None in answers:
            return render_template('quiz.html', questions=quiz_questions, error="Por favor, responda todas as perguntas.")
        # Calculate score and generate feedback
        score = calculate_score(answers)
        feedback = generate_feedback(score)
        return render_template('results.html', score=score, feedback=feedback)
    return render_template('quiz.html', questions=quiz_questions)

@app.route('/reset')
def reset():
    # Reset the quiz and redirect to the home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Accompanying HTML Files:

**1. `templates/index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste do Perfil de Dependência Emocional</title>
</head>
<body>
    <h1>Bem-vindo ao Teste do Perfil de Dependência Emocional!</h1>
    <p>Responda às perguntas para descobrir mais sobre sua dependência emocional.</p>
    <a href="/quiz">Iniciar Quiz</a>
</body>
</html>
```

**2. `templates/quiz.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz</title>
</head>
<body>
    <h1>Teste do Perfil de Dependência Emocional</h1>
    <form method="POST" action="/quiz">
        {% for index, question in enumerate(questions) %}
            <div>
                <p>{{ question.question }}</p>
                {% for option in question.options %}
                    <label>
                        <input type="radio" name="q{{ index }}" value="{{ option }}">
                        {{ option }}
                    </label>
                {% endfor %}
            </div>
        {% endfor %}
        {% if error %}
            <p style="color:red;">{{ error }}</p>
        {% endif %}
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

**3. `templates/results.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultados</title>
</head>
<body>
    <h1>Resultados do Teste</h1>
    <p>Sua pontuação: {{ score }}</p>
    <p>Feedback: {{ feedback }}</p>
    <a href="/reset">Refazer o teste</a>
</body>
</html>
```
