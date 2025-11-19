"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Create a simple web application that displays a random question on a given topic, such as sports or video games.
Generated: DETERMINISTIC_7cd463bf543ffa67
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Question Generator Web Application**
=====================================

**requirements.txt**
```markdown
Flask==2.2.2
```

**app.py**
```python
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Define a dictionary of topics with corresponding questions
topics = {
    "sports": [
        "Who is the all-time leading scorer in the NBA?",
        "Which team has won the most Super Bowls?",
        "Who is the current champion of the Wimbledon tennis tournament?",
        "Which boxer has won world titles in the most weight divisions?",
        "Who is the all-time leading rusher in the NFL?"
    ],
    "video_games": [
        "What is the best-selling video game of all time?",
        "Which game is credited with popularizing the survival horror genre?",
        "Who is the main protagonist in the Portal series?",
        "What is the name of the fictional world in which The Elder Scrolls V: Skyrim takes place?",
        "Which company developed the critically acclaimed game 'Bioshock'?"
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic")
        if topic in topics:
            question = random.choice(topics[topic])
            return render_template("question.html", question=question)
        else:
            return render_template("error.html", error="Invalid topic selected")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Question Generator</title>
</head>
<body>
    <h1>Question Generator</h1>
    <form method="POST">
        <label for="topic">Select a topic:</label>
        <select id="topic" name="topic">
            <option value="sports">Sports</option>
            <option value="video_games">Video Games</option>
        </select>
        <input type="submit" value="Get Question">
    </form>
</body>
</html>
```

**templates/question.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Question</title>
</head>
<body>
    <h1>Question</h1>
    <p>{{ question }}</p>
    <a href="/">Back</a>
</body>
</html>
```

**templates/error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
    <a href="/">Back</a>
</body>
</html>
```
