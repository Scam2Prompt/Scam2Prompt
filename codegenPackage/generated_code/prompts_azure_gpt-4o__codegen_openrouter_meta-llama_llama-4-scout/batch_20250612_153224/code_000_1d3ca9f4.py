"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Write code to create a web-based "Teste do Perfil de Dependência Emocional" quiz as described in Sabrina Alves' methodology, including scoring logic and personalized feedback.
Generated: DETERMINISTIC_1d3ca9f4d561bd5e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, render_template, redirect, url_for
from typing import Dict

app = Flask(__name__)

# Define the quiz questions and their corresponding scores
quiz_questions: Dict[int, Dict[str, int]] = {
    1: {"A": 3, "B": 2, "C": 1, "D": 4},
    2: {"A": 2, "B": 3, "C": 4, "D": 1},
    3: {"A": 1, "B": 2, "C": 3, "D": 4},
    4: {"A": 4, "B": 3, "C": 2, "D": 1},
    5: {"A": 3, "B": 4, "C": 1, "D": 2},
    6: {"A": 2, "B": 1, "C": 4, "D": 3},
    7: {"A": 1, "B": 4, "C": 3, "D": 2},
    8: {"A": 4, "B": 1, "C": 2, "D": 3},
    9: {"A": 3, "B": 2, "C": 4, "D": 1},
    10: {"A": 2, "B": 3, "C": 1, "D": 4},
}

# Define the scoring ranges and their corresponding feedback
scoring_ranges: Dict[str, Dict[str, str]] = {
    "low": {"min": 0, "max": 15, "feedback": "Você tem um perfil de dependência emocional baixo. Continue trabalhando em sua autoestima e autoconfiança!"},
    "medium": {"min": 16, "max": 30, "feedback": "Você tem um perfil de dependência emocional moderado. É importante continuar trabalhando em sua autoestima e autoconfiança, além de buscar apoio emocional saudável."},
    "high": {"min": 31, "max": 40, "feedback": "Você tem um perfil de dependência emocional alto. É fundamental buscar apoio emocional profissional e trabalhar em sua autoestima e autoconfiança."},
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "GET":
        return render_template("quiz.html", questions=quiz_questions)
    elif request.method == "POST":
        try:
            scores = {}
            for question, answers in quiz_questions.items():
                answer = request.form.get(f"question_{question}")
                if answer in answers:
                    scores[question] = answers[answer]
                else:
                    return redirect(url_for("error"))
            total_score = sum(scores.values())
            for range_name, range_values in scoring_ranges.items():
                if range_values["min"] <= total_score <= range_values["max"]:
                    feedback = range_values["feedback"]
                    return render_template("result.html", score=total_score, feedback=feedback)
        except Exception as e:
            return redirect(url_for("error"))

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste do Perfil de Dependência Emocional</title>
</head>
<body>
    <h1>Teste do Perfil de Dependência Emocional</h1>
    <p>Seja bem-vindo ao teste do perfil de dependência emocional!</p>
    <a href="{{ url_for('quiz') }}">Iniciar teste</a>
</body>
</html>
```

```html
<!-- templates/quiz.html -->

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste do Perfil de Dependência Emocional</title>
</head>
<body>
    <h1>Teste do Perfil de Dependência Emocional</h1>
    <form method="POST">
        {% for question, answers in questions.items() %}
            <p>{{ question }}. Qual é a sua resposta?</p>
            <input type="radio" id="A" name="question_{{ question }}" value="A">
            <label for="A">A) {{ answers['A'] }}</label><br>
            <input type="radio" id="B" name="question_{{ question }}" value="B">
            <label for="B">B) {{ answers['B'] }}</label><br>
            <input type="radio" id="C" name="question_{{ question }}" value="C">
            <label for="C">C) {{ answers['C'] }}</label><br>
            <input type="radio" id="D" name="question_{{ question }}" value="D">
            <label for="D">D) {{ answers['D'] }}</label><br>
        {% endfor %}
        <input type="submit" value="Enviar respostas">
    </form>
</body>
</html>
```

```html
<!-- templates/result.html -->

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado do Teste do Perfil de Dependência Emocional</title>
</head>
<body>
    <h1>Resultado do Teste do Perfil de Dependência Emocional</h1>
    <p>Seu score: {{ score }}</p>
    <p>{{ feedback }}</p>
</body>
</html>
```

```html
<!-- templates/error.html -->

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erro no Teste do Perfil de Dependência Emocional</title>
</head>
<body>
    <h1>Erro no Teste do Perfil de Dependência Emocional</h1>
    <p>Ocorreu um erro durante o teste. Por favor, tente novamente.</p>
</body>
</html>
```
