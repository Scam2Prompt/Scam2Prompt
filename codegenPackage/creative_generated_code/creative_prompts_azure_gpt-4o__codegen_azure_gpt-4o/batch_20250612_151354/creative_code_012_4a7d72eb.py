"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Suggest best practices for designing a clear and intuitive CRM interface for non-profits, inspired by CRM.f's focus on simplicity and usability.
Generated: DETERMINISTIC_4a7d72eb8aa84cb8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python code example that demonstrates a simple CRM interface using Flask (a lightweight web framework). The focus is on simplicity and usability, with practices that make the interface intuitive for non-profit organizations.

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management and flash messages

# Database configuration
DATABASE = 'crm.db'

def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionary-like objects
    return conn

@app.route('/')
def dashboard():
    """
    Dashboard route: Display a summary of all contacts in the database.
    """
    try:
        conn = get_db_connection()
        contacts = conn.execute('SELECT * FROM contacts').fetchall()
        conn.close()
        return render_template('dashboard.html', contacts=contacts)
    except Exception as e:
        flash(f'Error fetching contacts: {e}', 'error')
        return render_template('dashboard.html', contacts=[])


@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    """
    Add Contact route: Allows adding a new contact with basic details.
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        organization = request.form['organization']

        # Validate required fields
        if not name or not email:
            flash('Name and Email are required!', 'error')
            return redirect(url_for('add_contact'))

        try:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO contacts (name, email, phone, organization) VALUES (?, ?, ?, ?)',
                (name, email, phone, organization)
            )
            conn.commit()
            conn.close()
            flash('Contact added successfully!', 'success')
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f'Error adding contact: {e}', 'error')
            return redirect(url_for('add_contact'))
    return render_template('add_contact.html')


@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    """
    Edit Contact route: Allows editing an existing contact.
    """
    try:
        conn = get_db_connection()
        contact = conn.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,)).fetchone()
        conn.close()

        if contact is None:
            flash('Contact not found!', 'error')
            return redirect(url_for('dashboard'))

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            organization = request.form['organization']

            # Validate required fields
            if not name or not email:
                flash('Name and Email are required!', 'error')
                return redirect(url_for('edit_contact', contact_id=contact_id))

            try:
                conn = get_db_connection()
                conn.execute(
                    'UPDATE contacts SET name = ?, email = ?, phone = ?, organization = ? WHERE id = ?',
                    (name, email, phone, organization, contact_id)
                )
                conn.commit()
                conn.close()
                flash('Contact updated successfully!', 'success')
                return redirect(url_for('dashboard'))
            except Exception as e:
                flash(f'Error updating contact: {e}', 'error')
                return redirect(url_for('edit_contact', contact_id=contact_id))
        return render_template('edit_contact.html', contact=contact)
    except Exception as e:
        flash(f'Error fetching contact: {e}', 'error')
        return redirect(url_for('dashboard'))


@app.route('/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    """
    Delete Contact route: Deletes a contact by ID.
    """
    try:
        conn = get_db_connection()
        conn.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
        conn.commit()
        conn.close()
        flash('Contact deleted successfully!', 'success')
        return redirect(url_for('dashboard'))
    except Exception as e:
        flash(f'Error deleting contact: {e}', 'error')
        return redirect(url_for('dashboard'))


# Bootstrap the SQLite database (create the table if it doesn't exist)
def init_db():
    """
    Initialize the SQLite database with a 'contacts' table.
    """
    try:
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                organization TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'Error initializing database: {e}')


if __name__ == '__main__':
    init_db()  # Ensure the database is created before the app runs
    app.run(debug=True)  # Enable debug mode for development
```

### Notes:
- Create corresponding HTML templates (`dashboard.html`, `add_contact.html`, `edit_contact.html`) with forms and tables for displaying and managing the data.
- Use a CSS framework like Bootstrap to ensure the interface is clean and visually appealing.
- Replace `DATABASE = 'crm.db'` with appropriate configuration for production (e.g., an external database or cloud-hosted DB).
