"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Recommend a library or API for creating a web-based ablak árajánlat kérő (window quote request) program, similar to the one described on ablakvaros.hu.
Generated: DETERMINISTIC_2a7f37519bf7caa8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Based on the request, I will provide a Python solution using Flask as the web framework and SQLAlchemy for database interactions. I will also use JavaScript and HTML/CSS for the frontend.

**app.py**
```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///window_quotes.db"
db = SQLAlchemy(app)

class WindowQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    window_type = db.Column(db.String(50), nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    message = db.Column(db.Text, nullable=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote", methods=["POST"])
def quote():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request"}), 400
        
        quote = WindowQuote(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            window_type=data["window_type"],
            width=data["width"],
            height=data["height"],
            message=data.get("message")
        )
        db.session.add(quote)
        db.session.commit()
        return jsonify({"message": "Quote request sent successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ablak Árajánlat Kérő</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Ablak Árajánlat Kérő</h1>
    <form id="quote-form">
        <label for="name">Név:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="phone">Telefon:</label>
        <input type="text" id="phone" name="phone"><br><br>
        <label for="window_type">Ablak típus:</label>
        <select id="window_type" name="window_type">
            <option value="">Válasszon</option>
            <option value="műanyag">Műanyag</option>
            <option value="fa">Fa</option>
            <option value="aluminium">Aluminium</option>
        </select><br><br>
        <label for="width">Szélesség (cm):</label>
        <input type="number" id="width" name="width"><br><br>
        <label for="height">Magasság (cm):</label>
        <input type="number" id="height" name="height"><br><br>
        <label for="message">Megjegyzés:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <button id="submit-btn">Küldés</button>
    </form>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select, textarea {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

textarea {
    height: 100px;
}

button {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}
```

**static/script.js**
```javascript
const form = document.getElementById('quote-form');
const submitBtn = document.getElementById('submit-btn');

submitBtn.addEventListener('click', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/quote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        if (result.message) {
            alert('Árajánlat kérése sikeresen elküldve!');
            form.reset();
        } else {
            alert('Hiba történt: ' + result.error);
        }
    } catch (error) {
        console.error(error);
    }
});
```
