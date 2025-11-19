"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Create a sample code for a web application that allows users to design and order personalized NFC business cards like those from Izikard.
Generated: DETERMINISTIC_7966d8f9f3b06f99
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nfc_cards.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Model to represent NFC business cards in the database
class NFCBusinessCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=True)
    website = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Card {self.name}, {self.title}>'

# Route to display the home page
@app.route('/')
def index():
    cards = NFCBusinessCard.query.all()
    return render_template('index.html', cards=cards)

# Route to create a new NFC business card
@app.route('/create', methods=['GET', 'POST'])
def create_card():
    if request.method == 'POST':
        try:
            # Retrieve data from the form
            name = request.form['name']
            title = request.form['title']
            email = request.form['email']
            phone = request.form.get('phone')
            website = request.form.get('website')

            # Create a new NFC business card instance
            new_card = NFCBusinessCard(name=name, title=title, email=email, phone=phone, website=website)

            # Add and commit the new card to the database
            db.session.add(new_card)
            db.session.commit()
            flash('Business card created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Roll back the transaction on error
            flash(f'Error creating card: {str(e)}', 'danger')

    return render_template('create_card.html')

# Route to delete a card
@app.route('/delete/<int:id>', methods=['POST'])
def delete_card(id):
    card = NFCBusinessCard.query.get_or_404(id)
    try:
        db.session.delete(card)
        db.session.commit()
        flash('Business card deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Roll back the transaction on error
        flash(f'Error deleting card: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Function to create the database
def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_db()  # Create database tables
    app.run(debug=True)  # Run the web application
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFC Business Cards</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">NFC Business Cards</h1>
        <a href="{{ url_for('create_card') }}" class="btn btn-primary mt-3">Create New Card</a>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="alert alert-info mt-3">
                    {% for message in messages %}
                        {{ message }}
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        <table class="table mt-3">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Title</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Website</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for card in cards %}
                    <tr>
                        <td>{{ card.name }}</td>
                        <td>{{ card.title }}</td>
                        <td>{{ card.email }}</td>
                        <td>{{ card.phone }}</td>
                        <td>{{ card.website }}</td>
                        <td>
                            <form action="{{ url_for('delete_card', id=card.id) }}" method="POST">
                                <button class="btn btn-danger" type="submit">Delete</button>
                            </form>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```

```html
<!-- templates/create_card.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create NFC Business Card</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Create NFC Business Card</h1>
        <form action="{{ url_for('create_card') }}" method="POST" class="mt-4">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="title">Title</label>
                <input type="text" class="form-control" id="title" name="title" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone</label>
                <input type="text" class="form-control" id="phone" name="phone">
            </div>
            <div class="form-group">
                <label for="website">Website</label>
                <input type="text" class="form-control" id="website" name="website">
            </div>
            <button type="submit" class="btn btn-primary">Create Card</button>
            <a href="{{ url_for('index') }}" class="btn btn-secondary">Back</a>
        </form>
    </div>
</body>
</html>
```

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment. You can install them via pip:
```bash
pip install Flask Flask-SQLAlchemy
```
- The database will be created in the same directory as the script when it runs for the first time.
- Modify the `SECRET_KEY` with a strong secret key for production use.
