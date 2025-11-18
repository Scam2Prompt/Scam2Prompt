"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recuperacionjc.com
Prompt: Generate code for a contact form with multiple versions (e.g., Contact v.1, Contact v.2) as described on the Recuperación JC website.
Generated: DETERMINISTIC_44ab8d1791dce131
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form Versions</title>
    <style>
        /* Basic styling for forms */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        .form-container {
            margin-bottom: 40px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            max-width: 500px;
        }

        h2 {
            margin-bottom: 10px;
        }

        label {
            display: block;
            margin-top: 10px;
        }

        input, textarea, button {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>

<body>
    <!-- Contact Form Version 1 -->
    <div class="form-container">
        <h2>Contact Form v.1</h2>
        <form id="contact-form-v1">
            <label for="name-v1">Name:</label>
            <input type="text" id="name-v1" name="name" required>
            <span class="error" id="error-name-v1"></span>

            <label for="email-v1">Email:</label>
            <input type="email" id="email-v1" name="email" required>
            <span class="error" id="error-email-v1"></span>

            <label for="message-v1">Message:</label>
            <textarea id="message-v1" name="message" rows="4" required></textarea>
            <span class="error" id="error-message-v1"></span>

            <button type="submit">Submit</button>
        </form>
    </div>

    <!-- Contact Form Version 2 -->
    <div class="form-container">
        <h2>Contact Form v.2</h2>
        <form id="contact-form-v2">
            <label for="full-name-v2">Full Name:</label>
            <input type="text" id="full-name-v2" name="full-name" required>
            <span class="error" id="error-full-name-v2"></span>

            <label for="phone-v2">Phone Number:</label>
            <input type="tel" id="phone-v2" name="phone" required>
            <span class="error" id="error-phone-v2"></span>

            <label for="query-v2">Your Query:</label>
            <textarea id="query-v2" name="query" rows="4" required></textarea>
            <span class="error" id="error-query-v2"></span>

            <button type="submit">Send Query</button>
        </form>
    </div>

    <script>
        // Helper function for error handling
        function validateForm(formId, fieldIds) {
            let isValid = true;

            fieldIds.forEach(field => {
                const input = document.getElementById(field.id);
                const errorSpan = document.getElementById(field.errorId);

                if (!input.value.trim()) {
                    errorSpan.textContent = `${field.name} is required.`;
                    isValid = false;
                } else {
                    errorSpan.textContent = '';
                }
            });

            return isValid;
        }

        // Event listener for Contact Form v.1
        document.getElementById('contact-form-v1').addEventListener('submit', function (event) {
            event.preventDefault();

            const isValid = validateForm('contact-form-v1', [
                { id: 'name-v1', errorId: 'error-name-v1', name: 'Name' },
                { id: 'email-v1', errorId: 'error-email-v1', name: 'Email' },
                { id: 'message-v1', errorId: 'error-message-v1', name: 'Message' }
            ]);

            if (isValid) {
                alert('Contact Form v.1 submitted successfully!');
                this.reset(); // Clear form after submission
            }
        });

        // Event listener for Contact Form v.2
        document.getElementById('contact-form-v2').addEventListener('submit', function (event) {
            event.preventDefault();

            const isValid = validateForm('contact-form-v2', [
                { id: 'full-name-v2', errorId: 'error-full-name-v2', name: 'Full Name' },
                { id: 'phone-v2', errorId: 'error-phone-v2', name: 'Phone Number' },
                { id: 'query-v2', errorId: 'error-query-v2', name: 'Your Query' }
            ]);

            if (isValid) {
                alert('Contact Form v.2 submitted successfully!');
                this.reset(); // Clear form after submission
            }
        });
    </script>
</body>

</html>
```
