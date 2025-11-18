"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Build a simple Flask application that allows users to input their expenses and generates a downloadable expense report, inspired by Cashflow Routine's focus on transparency.
Generated: DETERMINISTIC_eced4e3b6911eb7e
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import os
import csv
from io import StringIO

app = Flask(__name__)

# Set up a list to store expenses in memory
expenses = []

@app.route('/')
def home():
    """
    Render the home page where users can input their expenses.
    """
    return render_template('index.html')

@app.route('/add-expense', methods=['POST'])
def add_expense():
    """
    Handle the submission of a new expense. Expects 'name', 'amount', and 'date' fields in the form.
    """
    try:
        # Retrieve form data
        name = request.form.get('name')
        amount = request.form.get('amount')
        date = request.form.get('date')

        # Validate input
        if not name or not amount or not date:
            return jsonify({'error': 'All fields are required.'}), 400

        # Add the expense to the list
        expenses.append({'name': name, 'amount': float(amount), 'date': date})

        return redirect(url_for('home'))
    except ValueError:
        return jsonify({'error': 'Invalid amount format.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download-report', methods=['GET'])
def download_report():
    """
    Generate a CSV report of expenses and make it downloadable.
    """
    try:
        # Prepare CSV data
        csv_file = StringIO()
        writer = csv.DictWriter(csv_file, fieldnames=['Name', 'Amount', 'Date'])
        writer.writeheader()
        writer.writerows(expenses)

        # Reset file pointer to the beginning
        csv_file.seek(0)

        return send_file(
            csv_file,
            mimetype='text/csv',
            as_attachment=True,
            download_name='expense_report.csv'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# HTML template (index.html) for the home page
@app.route('/templates/index.html')
def index_template():
    """
    Serve the index.html template with relevant information.
    """
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Expense Tracker</title>
    </head>
    <body>
        <h1>Expense Tracker</h1>
        <form method="POST" action="/add-expense">
            <label for="name">Expense Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="amount">Amount:</label><br>
            <input type="number" step="0.01" id="amount" name="amount"><br>
            <label for="date">Date:</label><br>
            <input type="date" id="date" name="date"><br><br>
            <button type="submit">Add Expense</button>
        </form>
        <br>
        <a href="/download-report">Download Expense Report</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    # Set the debug flag to False for production environments
    app.run(debug=False)
```
