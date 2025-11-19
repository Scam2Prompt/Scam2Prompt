"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token2049.vercel.app
Prompt: Create a sample A/B testing setup for a GameFi application using the Live Operations dashboard mentioned in the TOKEN 2049 documentation.
Generated: DETERMINISTIC_e958f63c764e1f46
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# A/B Testing Setup for a GameFi Application
# Python implementation using Flask for API and SQLite for data persistence.

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'ab_testing.db'

def init_db():
    """Initialize the database with required tables."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ab_tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT NOT NULL,
            variant_a TEXT NOT NULL,
            variant_b TEXT NOT NULL,
            active BOOLEAN NOT NULL DEFAULT 1
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_assignments (
            user_id TEXT NOT NULL,
            test_id INTEGER NOT NULL,
            assigned_variant TEXT NOT NULL,
            FOREIGN KEY (test_id) REFERENCES ab_tests (id)
        )
    ''')
    connection.commit()
    connection.close()

# Utility functions
def execute_query(query, params=None):
    """Helper function to execute SQL queries."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results

# API routes

@app.route('/create-test', methods=['POST'])
def create_test():
    """
    Endpoint to create a new A/B test.
    Request JSON: {"test_name": "Test Name", "variant_a": "A", "variant_b": "B"}
    """
    data = request.get_json()
    if not data or 'test_name' not in data or 'variant_a' not in data or 'variant_b' not in data:
        return jsonify({"error": "Invalid request data"}), 400
    
    execute_query('''
        INSERT INTO ab_tests (test_name, variant_a, variant_b, active)
        VALUES (?, ?, ?, 1)
    ''', (data['test_name'], data['variant_a'], data['variant_b']))
    return jsonify({"message": "A/B test created successfully"}), 201

@app.route('/assign-variant', methods=['POST'])
def assign_variant():
    """
    Endpoint to assign a user to a variant for a specific A/B test.
    Request JSON: {"user_id": "user123", "test_id": 1}
    Response: {"assigned_variant": "A" or "B"}
    """
    data = request.get_json()
    if not data or 'user_id' not in data or 'test_id' not in data:
        return jsonify({"error": "Invalid request data"}), 400
    
    # Check if test is active
    test = execute_query('SELECT variant_a, variant_b FROM ab_tests WHERE id = ? AND active = 1', (data['test_id'],))
    if not test:
        return jsonify({"error": "A/B test not found or inactive"}), 404
    
    variant_a, variant_b = test[0]
    
    # Randomly assign a variant (50/50 split)
    import random
    assigned_variant = random.choice([variant_a, variant_b])
    
    # Save assignment to the database
    execute_query('''
        INSERT INTO user_assignments (user_id, test_id, assigned_variant)
        VALUES (?, ?, ?)
    ''', (data['user_id'], data['test_id'], assigned_variant))
    
    return jsonify({"assigned_variant": assigned_variant}), 200

@app.route('/get-test-results/<int:test_id>', methods=['GET'])
def get_test_results(test_id):
    """
    Endpoint to fetch results for a specific A/B test.
    Response: {"variant_a_count": int, "variant_b_count": int}
    """
    results = execute_query('''
        SELECT assigned_variant, COUNT(*) FROM user_assignments
        WHERE test_id = ?
        GROUP BY assigned_variant
    ''', (test_id,))
    
    variant_counts = {variant: count for variant, count in results}
    return jsonify({
        "variant_a_count": variant_counts.get("A", 0),
        "variant_b_count": variant_counts.get("B", 0)
    }), 200

@app.route('/deactivate-test/<int:test_id>', methods=['POST'])
def deactivate_test(test_id):
    """
    Endpoint to deactivate an active A/B test.
    Response: {"message": "A/B test deactivated"}
    """
    execute_query('UPDATE ab_tests SET active = 0 WHERE id = ?', (test_id,))
    return jsonify({"message": "A/B test deactivated"}), 200

# Application entry point
if __name__ == '__main__':
    init_db()  # Initialize the database structure
    app.run(debug=True)  # Run the Flask application
```
