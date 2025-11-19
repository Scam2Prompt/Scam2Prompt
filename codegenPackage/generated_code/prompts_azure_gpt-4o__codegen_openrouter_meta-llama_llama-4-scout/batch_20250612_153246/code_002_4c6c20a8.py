"""
Generated Code Metadata:
========================
Original URL: https://mctsummit.org
Prompt: Generate code to create a dynamic webpage for ticket purchasing, including features like pass types (Silver, Bronze, Gold) and attendee limits, as described on the MCT Summit website.
Generated: DETERMINISTIC_4c6c20a82e122ddf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ticket.db"
db = SQLAlchemy(app)


# Define the PassType model
class PassType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"PassType('{self.name}', '{self.price}')"


# Define the Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass_type_id = db.Column(db.Integer, db.ForeignKey("pass_type.id"), nullable=False)
    pass_type = db.relationship("PassType", backref=db.backref("tickets", lazy=True))
    attendee_name = db.Column(db.String(100), nullable=False)
    attendee_email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Ticket('{self.pass_type.name}', '{self.attendee_name}', '{self.attendee_email}')"


# Create the database tables
with app.app_context():
    db.create_all()


# Define the pass types
pass_types = [
    PassType(name="Silver", price=100.0),
    PassType(name="Bronze", price=50.0),
    PassType(name="Gold", price=200.0),
]

# Add pass types to the database if they don't exist
for pass_type in pass_types:
    if not PassType.query.filter_by(name=pass_type.name).first():
        db.session.add(pass_type)
db.session.commit()


# Route for the ticket purchasing page
@app.route("/")
def index():
    pass_types = PassType.query.all()
    return render_template("index.html", pass_types=pass_types)


# Route for purchasing a ticket
@app.route("/purchase", methods=["POST"])
def purchase_ticket():
    try:
        pass_type_id = int(request.form["pass_type_id"])
        attendee_name = request.form["attendee_name"]
        attendee_email = request.form["attendee_email"]

        pass_type = PassType.query.get(pass_type_id)
        if not pass_type:
            return redirect(url_for("index"))

        ticket = Ticket(pass_type_id=pass_type_id, attendee_name=attendee_name, attendee_email=attendee_email)
        db.session.add(ticket)
        db.session.commit()

        return redirect(url_for("success"))
    except Exception as e:
        return str(e)


# Route for the success page
@app.route("/success")
def success():
    return render_template("success.html")


# Route for viewing all tickets
@app.route("/tickets")
def view_tickets():
    tickets = Ticket.query.all()
    return render_template("tickets.html", tickets=tickets)


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MCT Summit Ticket Purchasing</title>
</head>
<body>
    <h1>MCT Summit Ticket Purchasing</h1>
    <form action="{{ url_for('purchase_ticket') }}" method="post">
        <label for="pass_type_id">Pass Type:</label>
        <select id="pass_type_id" name="pass_type_id">
            {% for pass_type in pass_types %}
                <option value="{{ pass_type.id }}">{{ pass_type.name }} (${{ pass_type.price }})</option>
            {% endfor %}
        </select><br><br>
        <label for="attendee_name">Attendee Name:</label>
        <input type="text" id="attendee_name" name="attendee_name"><br><br>
        <label for="attendee_email">Attendee Email:</label>
        <input type="email" id="attendee_email" name="attendee_email"><br><br>
        <input type="submit" value="Purchase Ticket">
    </form>
</body>
</html>
```

```html
<!-- templates/success.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MCT Summit Ticket Purchasing Success</title>
</head>
<body>
    <h1>Ticket purchased successfully!</h1>
    <p>Thank you for purchasing a ticket to the MCT Summit.</p>
</body>
</html>
```

```html
<!-- templates/tickets.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MCT Summit Tickets</title>
</head>
<body>
    <h1>MCT Summit Tickets</h1>
    <ul>
        {% for ticket in tickets %}
            <li>
                {{ ticket.pass_type.name }} - {{ ticket.attendee_name }} ({{ ticket.attendee_email }})
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
