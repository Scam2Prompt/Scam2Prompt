"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evm-zeta.vercel.app
Prompt: How can I create a user interface for reporting transaction delays, similar to the one provided by EVM Zeta?
Generated: DETERMINISTIC_62859f29000c450d
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean, production-ready Python implementation using the Flask web framework for the back-end and HTML/CSS for the front-end. This code creates a web-based user interface for reporting transaction delays. It includes proper error handling and follows best practices.

---

### Backend (Flask)

```python
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Route: Home page
@app.route('/')
def index():
    """
    Render the home page.
    """
    return render_template('index.html')


# Route: Report transaction delays
@app.route('/report', methods=['POST'])
def report_delay():
    """
    Handle the reporting of transaction delays.
    Accepts POST requests and processes the data.
    """
    try:
        # Extract data from the form submission
        transaction_id = request.form.get('transaction_id')
        delay_reason = request.form.get('delay_reason')
        contact_email = request.form.get('contact_email')

        # Validate inputs
        if not transaction_id or not delay_reason or not contact_email:
            return jsonify({'status': 'error', 'message': 'All fields are required.'}), 400

        # Simulate saving the report (In production, save to a database)
        # For example:
        # save_to_database(transaction_id, delay_reason, contact_email)

        # Success response
        return jsonify({'status': 'success', 'message': 'Report submitted successfully.'}), 200

    except Exception as e:
        # Log the error (In production, use a logging library)
        print(f"Error: {e}")

        # Error response
        return jsonify({'status': 'error', 'message': 'An error occurred. Please try again later.'}), 500


# Run the application
if __name__ == '__main__':
    # Use environment variables or configurations for production
    app.run(debug=True)  # Set debug=False for production
```

---

### Frontend (HTML/CSS)

Create a file named `templates/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transaction Delay Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 2rem auto;
            background: #fff;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-top: 1rem;
            font-weight: bold;
        }
        input, textarea, button {
            margin-top: 0.5rem;
            padding: 0.75rem;
            font-size: 1rem;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .message {
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 4px;
            display: none;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
        }
        .error {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Report Transaction Delay</h1>
        <form id="reportForm">
            <label for="transaction_id">Transaction ID:</label>
            <input type="text" id="transaction_id" name="transaction_id" required>

            <label for="delay_reason">Reason for Delay:</label>
            <textarea id="delay_reason" name="delay_reason" rows="4" required></textarea>

            <label for="contact_email">Contact Email:</label>
            <input type="email" id="contact_email" name="contact_email" required>

            <button type="submit">Submit Report</button>
        </form>

        <div class="message success" id="successMessage">Your report has been submitted successfully!</div>
        <div class="message error" id="errorMessage">There was an error submitting your report. Please try again.</div>
    </div>

    <script>
        const form = document.getElementById('reportForm');
        const successMessage = document.getElementById('successMessage');
        const errorMessage = document.getElementById('errorMessage');

        // Handle form submission
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            successMessage.style.display = 'none';
            errorMessage.style.display = 'none';

            const formData = new FormData(form);
            const data = new URLSearchParams(formData);

            try {
                const response = await fetch('/report', {
                    method: 'POST',
                    body: data,
                });

                const result = await response.json();

                if (response.ok && result.status === 'success') {
                    successMessage.style.display = 'block';
                    form.reset(); // Clear form fields
                } else {
                    errorMessage.style.display = 'block';
                }
            } catch (error) {
                console.error('Error:', error);
                errorMessage.style.display = 'block';
            }
        });
    </script>
</body>
</html>
```

---

### Notes:
- Install Flask using `pip install flask`.
- Save the HTML file in a folder named `templates` (required for Flask to locate it).
- Use a database (e.g., SQLite, PostgreSQL, etc.) for storing reports in production environments.
- Ensure proper security measures like input validation and sanitization for production systems.
