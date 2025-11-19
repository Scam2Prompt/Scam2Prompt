"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Write Python code to create an online donation system for a non-profit organization, including features for tracking donations and generating financial reports, inspired by the "موقع جمع التبرعات" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_d52a4d089c2e0514
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Donation model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Donation {self.donor_name}, Amount: {self.amount}>'

# Create the database
with app.app_context():
    db.create_all()

# Route to handle donations
@app.route('/donate', methods=['POST'])
def donate():
    try:
        data = request.get_json()
        donor_name = data.get('donor_name')
        amount = data.get('amount')

        if not donor_name or not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({'error': 'Invalid input'}), 400

        new_donation = Donation(donor_name=donor_name, amount=amount)
        db.session.add(new_donation)
        db.session.commit()

        logging.info(f'Donation received: {donor_name} donated {amount}')
        return jsonify({'message': 'Donation successful'}), 201

    except Exception as e:
        logging.error(f'Error processing donation: {e}')
        return jsonify({'error': 'Internal server error'}), 500

# Route to generate financial reports
@app.route('/reports', methods=['GET'])
def generate_report():
    try:
        donations = Donation.query.all()
        total_donations = sum(donation.amount for donation in donations)
        report = {
            'total_donations': total_donations,
            'donation_count': len(donations),
            'donations': [{'donor_name': d.donor_name, 'amount': d.amount, 'date': d.date} for d in donations]
        }
        return jsonify(report), 200

    except Exception as e:
        logging.error(f'Error generating report: {e}')
        return jsonify({'error': 'Internal server error'}), 500

# Route to render the donation form (for web interface)
@app.route('/')
def index():
    return render_template('donation_form.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (donation_form.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donation Form</title>
</head>
<body>
    <h1>Donate to Our Cause</h1>
    <form id="donationForm">
        <label for="donor_name">Your Name:</label>
        <input type="text" id="donor_name" name="donor_name" required>
        <br>
        <label for="amount">Donation Amount:</label>
        <input type="number" id="amount" name="amount" required min="0.01" step="0.01">
        <br>
        <button type="submit">Donate</button>
    </form>

    <script>
        document.getElementById('donationForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const donorName = document.getElementById('donor_name').value;
            const amount = parseFloat(document.getElementById('amount').value);

            fetch('/donate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ donor_name: donorName, amount: amount })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                if (data.message) {
                    document.getElementById('donationForm').reset();
                }
            })
            .catch(error => {
                alert('Error: ' + error);
            });
        });
    </script>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- The database is set to SQLite for simplicity; you can change it to any other database as needed.
- The HTML form allows users to submit their donations directly from a web interface.
