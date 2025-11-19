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

**Emotional Dependency Profile Test**
=====================================

**Language:** Python 3.9+
**Framework:** Flask 2.0+
**Database:** SQLite 3

**Code:**
```python
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

# Database configuration
DATABASE_NAME = "emotional_dependency_test.db"

# Create database and table if not exists
def create_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                result TEXT NOT NULL
            );
        """)
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error creating database: {e}")

create_database()

# Define test questions and answers
test_questions = [
    {"question": "Quando estou em uma relação, sinto que preciso estar sempre com a outra pessoa.", 
     "answers": ["Discordo fortemente", "Discordo", "Neutro", "Concordo", "Concordo fortemente"]},
    {"question": "Sinto que não posso tomar decisões sem a opinião da outra pessoa.", 
     "answers": ["Discordo fortemente", "Discordo", "Neutro", "Concordo", "Concordo fortemente"]},
    {"question": "Fico ansioso ou deprimido quando estou sozinho.", 
     "answers": ["Discordo fortemente", "Discordo", "Neutro", "Concordo", "Concordo fortemente"]},
    {"question": "Acredito que a outra pessoa é responsável pela minha felicidade.", 
     "answers": ["Discordo fortemente", "Discordo", "Neutro", "Concordo", "Concordo fortemente"]},
    {"question": "Sinto que preciso de ajuda para lidar com meus problemas.", 
     "answers": ["Discordo fortemente", "Discordo", "Neutro", "Concordo", "Concordo fortemente"]},
]

# Define scoring system
def calculate_score(answers):
    score = 0
    for answer in answers:
        score += int(answer)
    return score

def get_result(score):
    if score <= 10:
        return "Você tem um perfil de dependência emocional baixo."
    elif score <= 15:
        return "Você tem um perfil de dependência emocional moderado."
    else:
        return "Você tem um perfil de dependência emocional alto."

# Route for test page
@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        name = request.form["name"]
        answers = [request.form[f"question_{i}"] for i in range(len(test_questions))]
        score = calculate_score(answers)
        result = get_result(score)
        try:
            conn = sqlite3.connect(DATABASE_NAME)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO test_results (name, score, result) VALUES (?, ?, ?);", 
                           (name, score, result))
            conn.commit()
            conn.close()
            return render_template("result.html", name=name, score=score, result=result)
        except Error as e:
            print(f"Error saving test result: {e}")
            return "Erro ao salvar resultado do teste."
    return render_template("test.html", questions=test_questions)

# Route for result page
@app.route("/result", methods=["GET"])
def result():
    return render_template("result.html")

# Route for index page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/test.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Teste do Perfil de Dependência Emocional</title>
</head>
<body>
    <h1>Teste do Perfil de Dependência Emocional</h1>
    <form method="POST">
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name"><br><br>
        {% for i, question in enumerate(questions) %}
        <label for="question_{{ i }}">{{ question.question }}</label>
        <select id="question_{{ i }}" name="question_{{ i }}">
            {% for j, answer in enumerate(question.answers) %}
            <option value="{{ j }}">{{ answer }}</option>
            {% endfor %}
        </select><br><br>
        {% endfor %}
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
```

**templates/result.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Resultado do Teste</title>
</head>
<body>
    <h1>Resultado do Teste</h1>
    <p>Olá, {{ name }}!</p>
    <p>Seu score é: {{ score }}</p>
    <p>{{ result }}</p>
</body>
</html>
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Índice</title>
</head>
<body>
    <h1>Índice</h1>
    <p><a href="{{ url_for('test') }}">Fazer o teste</a></p>
</body>
</html>
```
