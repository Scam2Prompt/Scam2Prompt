"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://servicosgm.online
Prompt: Generate a code snippet to handle "Página não encontrada" errors in a web application.
Generated: DETERMINISTIC_477af825d867dd23
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Define a custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle "Página não encontrada" errors gracefully.
    Returns a JSON response with an appropriate error message and status code.
    """
    error_response = {
        "error": "Página não encontrada",
        "message": "A página que você está procurando não existe.",
        "status_code": 404
    }
    return jsonify(error_response), 404

@app.route("/")
def home():
    """
    A simple route to test the application.
    """
    return "Bem-vindo à aplicação!"

# Run the Flask application, enabling debugging for development
if __name__ == "__main__":
    app.run(debug=True)
```
