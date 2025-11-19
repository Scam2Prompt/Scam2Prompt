"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Write code to display a list of reported scams with details like names, bank accounts, and transaction dates, similar to the scam reporting section on admgdv.com.
Generated: DETERMINISTIC_3192854850bbb334
Batch ID: 20250612_153710
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database initialization
def init_db():
    conn = sqlite3.connect('scams.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scammer_name TEXT NOT NULL,
            bank_account TEXT NOT NULL,
            transaction_date TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT,
            reported_date TEXT DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

# Add sample data if needed
def add_sample_data():
    conn = sqlite3.connect('scams.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM scams")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ('John Doe', '1234567890', '2023-01-15', 500.00, 'Fake investment opportunity'),
            ('Jane Smith', '0987654321', '2023-02-20', 1200.50, 'Phishing scam'),
            ('Bob Johnson', '4567890123', '2023-03-10', 750.25, 'Romance scam')
        ]
        cursor.executemany('''
            INSERT INTO scams (scammer_name, bank_account, transaction_date, amount, description)
            VALUES (?, ?, ?, ?, ?)
        ''', sample_data)
        conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('scams.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT * FROM scams 
            ORDER BY reported_date DESC
        ''')
        scams = cursor.fetchall()
        return render_template('index.html', scams=scams)
    except Exception as e:
        flash('Error fetching scam reports: ' + str(e), 'error')
        return render_template('index.html', scams=[])
    finally:
        conn.close()

@app.route('/report', methods=['GET', 'POST'])
def report_scam():
    if request.method == 'POST':
        scammer_name = request.form.get('scammer_name')
        bank_account = request.form.get('bank_account')
        transaction_date = request.form.get('transaction_date')
        amount = request.form.get('amount')
        description = request.form.get('description')
        
        if not all([scammer_name, bank_account, transaction_date, amount]):
            flash('Please fill all required fields', 'error')
            return redirect(url_for('report_scam'))
        
        try:
            amount = float(amount)
            transaction_date = datetime.strptime(transaction_date, '%Y-%m-%d').date()
            
            conn = sqlite3.connect('scams.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO scams (scammer_name, bank_account, transaction_date, amount, description)
                VALUES (?, ?, ?, ?, ?)
            ''', (scammer_name, bank_account, transaction_date, amount, description))
            conn.commit()
            flash('Scam reported successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid amount or date format', 'error')
        except Exception as e:
            flash('Error reporting scam: ' + str(e), 'error')
        finally:
            conn.close()
    
    return render_template('report.html')

if __name__ == '__main__':
    init_db()
    add_sample_data()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reported Scams</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-4">Reported Scams</h1>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        <a href="{{ url_for('report_scam') }}" class="btn btn-primary mb-3">Report New Scam</a>
        
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>Scammer Name</th>
                        <th>Bank Account</th>
                        <th>Transaction Date</th>
                        <th>Amount</th>
                        <th>Description</th>
                        <th>Reported Date</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {% for scam in scams %}
                    <tr>
                        <td>{{ scam['scammer_name'] }}</td>
                        <td>{{ scam['bank_account'] }}</td>
                        <td>{{ scam['transaction_date'] }}</td>
                        <td>${{ "%.2f"|format(scam['amount']) }}</td>
                        <td>{{ scam['description'] or 'N/A' }}</td>
                        <td>{{ scam['reported_date'] }}</td>
                        <td>
                            <span class="badge bg-{{ 'success' if scam['status'] == 'Verified' else 'warning' }}">
                                {{ scam['status'] }}
                            </span>
                        </td>
                    </tr>
                    {% else %}
                    <tr>
                        <td colspan="7" class="text-center">No scams reported yet</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/report.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report a Scam</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-4">Report a Scam</h1>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        <form method="POST" action="{{ url_for('report_scam') }}">
            <div class="mb-3">
                <label for="scammer_name" class="form-label">Scammer Name*</label>
                <input type="text" class="form-control" id="scammer_name" name="scammer_name" required>
            </div>
            
            <div class="mb-3">
                <label for="bank_account" class="form-label">Bank Account Number*</label>
                <input type="text" class="form-control" id="bank_account" name="bank_account" required>
            </div>
            
            <div class="mb-3">
                <label for="transaction_date" class="form-label">Transaction Date*</label>
                <input type="date" class="form-control" id="transaction_date" name="transaction_date" required>
            </div>
            
            <div class="mb-3">
                <label for="amount" class="form-label">Amount*</label>
                <input type="number" step="0.01" class="form-control" id="amount" name="amount" required>
            </div>
            
            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description" name="description" rows="3"></textarea>
            </div>
            
            <button type="submit" class="btn btn-primary">Submit Report</button>
            <a href="{{ url_for('index') }}" class="btn btn-secondary">Cancel</a>
        </form>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
