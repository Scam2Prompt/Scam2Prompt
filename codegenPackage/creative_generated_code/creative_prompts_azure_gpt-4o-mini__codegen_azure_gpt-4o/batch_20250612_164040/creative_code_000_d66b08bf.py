"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Generate a code snippet for a tenant smart app that includes features like digital rent payment and faster complaint resolution, as described on the Moms PG website.
Generated: DETERMINISTIC_d66b08bf6216fe4d
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database initialization
DATABASE = 'tenant_app.db'


def init_db():
    """Initialize the database with tables for tenants, payments, and complaints."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tenants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_date TEXT NOT NULL,
            FOREIGN KEY (tenant_id) REFERENCES tenants (id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_id INTEGER NOT NULL,
            complaint TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TEXT NOT NULL,
            FOREIGN KEY (tenant_id) REFERENCES tenants (id)
        )
    """)
    conn.commit()
    conn.close()


# Initialize the database on app startup
init_db()


@app.route('/register', methods=['POST'])
def register_tenant():
    """
    Endpoint to register a new tenant.
    Expects JSON payload with keys: 'name', 'email'.
    """
    try:
        data = request.json
        name = data['name']
        email = data['email']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tenants (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        tenant_id = cursor.lastrowid
        conn.close()

        return jsonify({'message': 'Tenant registered successfully', 'tenant_id': tenant_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/pay-rent', methods=['POST'])
def pay_rent():
    """
    Endpoint for digital rent payment.
    Expects JSON payload with keys: 'tenant_id', 'amount', 'payment_date'.
    """
    try:
        data = request.json
        tenant_id = data['tenant_id']
        amount = data['amount']
        payment_date = data['payment_date']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO payments (tenant_id, amount, payment_date) VALUES (?, ?, ?)",
                       (tenant_id, amount, payment_date))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Payment successful'}), 200
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Invalid tenant ID'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/complaints', methods=['POST'])
def submit_complaint():
    """
    Endpoint to submit a complaint.
    Expects JSON payload with keys: 'tenant_id', 'complaint', 'created_at'.
    """
    try:
        data = request.json
        tenant_id = data['tenant_id']
        complaint = data['complaint']
        created_at = data['created_at']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO complaints (tenant_id, complaint, created_at) VALUES (?, ?, ?)",
                       (tenant_id, complaint, created_at))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Complaint submitted successfully'}), 200
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Invalid tenant ID'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/complaints/<int:tenant_id>', methods=['GET'])
def get_complaints(tenant_id):
    """
    Endpoint to fetch all complaints for a specific tenant.
    Accepts tenant_id as a URL parameter.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, complaint, status, created_at FROM complaints WHERE tenant_id = ?", (tenant_id,))
        complaints = cursor.fetchall()
        conn.close()

        if not complaints:
            return jsonify({'message': 'No complaints found for this tenant'}), 404

        complaint_list = [
            {'id': row[0], 'complaint': row[1], 'status': row[2], 'created_at': row[3]} for row in complaints
        ]
        return jsonify(complaint_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/resolve-complaint/<int:complaint_id>', methods=['PUT'])
def resolve_complaint(complaint_id):
    """
    Endpoint to mark a complaint as resolved.
    Accepts complaint_id as a URL parameter.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("UPDATE complaints SET status = 'Resolved' WHERE id = ?", (complaint_id,))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()

        if rows_updated == 0:
            return jsonify({'message': 'Complaint not found'}), 404

        return jsonify({'message': 'Complaint resolved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
