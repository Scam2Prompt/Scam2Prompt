"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sembradordevidaac.org
Prompt: How can I implement a contact form in HTML that allows users to reach out to Sembrador de Vida for more information?
Generated: DETERMINISTIC_da00ac720dbdfc6d
Batch ID: 20250612_135557
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
    <title>Contact Form - Sembrador de Vida</title>
    <style>
        /* Basic styling for the contact form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .form-container {
            background-color: #fff;
            max-width: 600px;
            margin: 2rem auto;
            padding: 1.5rem;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .form-container h1 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: #555;
        }
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }
        .form-group textarea {
            resize: vertical;
            min-height: 100px;
        }
        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #007BFF;
        }
        .form-submit {
            text-align: center;
        }
        .form-submit button {
            padding: 0.8rem 1.5rem;
            background-color: #007BFF;
            border: none;
            border-radius: 4px;
            color: #fff;
            font-size: 1rem;
            cursor: pointer;
        }
        .form-submit button:hover {
            background-color: #0056b3;
        }
        .error-message,
        .success-message {
            text-align: center;
            margin-top: 1rem;
            font-size: 0.9rem;
        }
        .error-message {
            color: #d9534f;
        }
        .success-message {
            color: #5cb85c;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Contact Sembrador de Vida</h1>
        <form id="contactForm">
            <!-- Full Name -->
            <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
            </div>
            <!-- Email -->
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Enter your email address" required>
            </div>
            <!-- Message -->
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" placeholder="Write your message here" required></textarea>
            </div>
            <!-- Submit Button -->
            <div class="form-submit">
                <button type="submit">Send Message</button>
            </div>
            <!-- Display Success or Error Messages -->
            <div id="formStatus" class="success-message" style="display: none;"></div>
            <div id="formError" class="error-message" style="display: none;"></div>
        </form>
    </div>

    <script>
        /**
         * Handle form submission
         */
        document.getElementById('contactForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the default form submission

            // Get form values
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Error handling for required fields
            if (!fullName || !email || !message) {
                document.getElementById('formError').style.display = 'block';
                document.getElementById('formError').textContent = 'All fields are required!';
                return;
            }

            // Simulate sending form data (adjust for actual implementation).
            // Normally, here you'd send the form data via AJAX to a server-side endpoint.
            fetch('/submit-contact-form', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ fullName, email, message }),
            })
                .then((response) => {
                    // Check if the response was successful
                    if (response.ok) {
                        document.getElementById('formStatus').style.display = 'block';
                        document.getElementById('formStatus').textContent =
                            'Your message has been sent successfully!';
                        document.getElementById('formError').style.display = 'none';
                    } else {
                        throw new Error('Failed to send your message. Please try again.');
                    }
                })
                .catch((error) => {
                    document.getElementById('formError').style.display = 'block';
                    document.getElementById('formError').textContent = error.message;
                    document.getElementById('formStatus').style.display = 'none';
                });
        });
    </script>
</body>
</html>
```
