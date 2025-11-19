"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpncg.edu.mx
Prompt: Develop a simple HTML form for parents to contact the Colegio Panamericano, ensuring it captures essential details like name, phone number, and message.
Generated: DETERMINISTIC_530564cebc60b72c
Batch ID: 20250612_155153
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
    <meta name="description" content="Contact form for Colegio Panamericano">
    <title>Contact Colegio Panamericano</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f9f9f9;
        }

        .contact-form {
            width: 100%;
            max-width: 400px;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .contact-form h1 {
            font-size: 24px;
            margin-bottom: 20px;
            text-align: center;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }

        .form-group textarea {
            resize: vertical;
            height: 100px;
        }

        .form-group .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }

        .submit-btn {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .submit-btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>
    <form class="contact-form" id="contactForm">
        <h1>Contact Colegio Panamericano</h1>

        <!-- Name Field -->
        <div class="form-group">
            <label for="name">Name *</label>
            <input type="text" id="name" name="name" placeholder="Enter your name" required>
            <span class="error" id="nameError"></span>
        </div>

        <!-- Phone Number Field -->
        <div class="form-group">
            <label for="phone">Phone Number *</label>
            <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
            <span class="error" id="phoneError"></span>
        </div>

        <!-- Message Field -->
        <div class="form-group">
            <label for="message">Message *</label>
            <textarea id="message" name="message" placeholder="Write your message here" required></textarea>
            <span class="error" id="messageError"></span>
        </div>

        <!-- Submit Button -->
        <button type="submit" class="submit-btn">Send Message</button>
    </form>

    <script>
        // Simple client-side form validation
        document.getElementById('contactForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission for validation
            let hasError = false;

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('phoneError').textContent = '';
            document.getElementById('messageError').textContent = '';

            // Validate Name
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('nameError').textContent = 'Name is required.';
                hasError = true;
            }

            // Validate Phone Number
            const phone = document.getElementById('phone').value.trim();
            if (phone === '') {
                document.getElementById('phoneError').textContent = 'Phone number is required.';
                hasError = true;
            } else if (!/^\d{10}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Enter a valid 10-digit phone number.';
                hasError = true;
            }

            // Validate Message
            const message = document.getElementById('message').value.trim();
            if (message === '') {
                document.getElementById('messageError').textContent = 'Message is required.';
                hasError = true;
            }

            // If no errors, submit the form (example: send to server or display confirmation)
            if (!hasError) {
                alert('Thank you for your message! We will get back to you shortly.');
                // Here you can add code to actually submit the form (e.g., via AJAX or form submission)
                // Example: this.submit();
            }
        });
    </script>
</body>

</html>
```
