"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: Generate a code snippet for a web form that allows users to request a custom cue quote, including fields for name, email, subject, and message, similar to the quote request process on Cohen Cues.
Generated: DETERMINISTIC_dbc3d7a4830a8155
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Cue Quote Request</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        .form-container {
            max-width: 600px;
            margin: 50px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }

        textarea {
            resize: vertical;
        }

        .error {
            color: red;
            font-size: 14px;
        }

        button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Request a Custom Cue Quote</h1>
        <form id="quoteForm">
            <!-- Name field -->
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
                <div class="error" id="nameError"></div>
            </div>

            <!-- Email field -->
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                <div class="error" id="emailError"></div>
            </div>

            <!-- Subject field -->
            <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" name="subject" required>
                <div class="error" id="subjectError"></div>
            </div>

            <!-- Message field -->
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="5" required></textarea>
                <div class="error" id="messageError"></div>
            </div>

            <!-- Submit button -->
            <button type="submit">Submit Request</button>
        </form>
    </div>

    <script>
        // JavaScript for form validation and submission
        document.getElementById('quoteForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form from submitting normally

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('subjectError').textContent = '';
            document.getElementById('messageError').textContent = '';

            // Validate form fields
            let isValid = true;

            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();

            if (!name) {
                document.getElementById('nameError').textContent = 'Name is required.';
                isValid = false;
            }

            if (!email) {
                document.getElementById('emailError').textContent = 'Email is required.';
                isValid = false;
            } else if (!/\S+@\S+\.\S+/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address.';
                isValid = false;
            }

            if (!subject) {
                document.getElementById('subjectError').textContent = 'Subject is required.';
                isValid = false;
            }

            if (!message) {
                document.getElementById('messageError').textContent = 'Message is required.';
                isValid = false;
            }

            // If all fields are valid, simulate form submission
            if (isValid) {
                alert('Your request has been submitted successfully!');
                // Here, you can add code to send the form data to a server using AJAX or fetch API
                document.getElementById('quoteForm').reset(); // Reset the form
            }
        });
    </script>
</body>
</html>
```
