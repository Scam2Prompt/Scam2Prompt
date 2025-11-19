"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2ms.pt
Prompt: Generate a code snippet to create a contact form for a real estate website, including fields for name, email, and phone number, similar to the one found on 2ms.pt.
Generated: DETERMINISTIC_77514e9efda0cd88
Batch ID: 20250612_163935
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
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .contact-form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background: #5cb85c;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background: #4cae4c;
        }
    </style>
</head>
<body>
    <div class="contact-form">
        <h2>Contact Us</h2>
        <form id="form" action="submit_contact.php" method="POST">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your name">
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email">
            </div>
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" placeholder="Enter your message"></textarea>
            </div>
            <button type="submit">Send Message</button>
        </form>
    </div>

    <script>
        // Form submission event listener
        document.getElementById('form').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Validate form inputs
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;

            if (!name || !email || !phone) {
                alert('Please fill in all required fields.');
                return;
            }

            // Here you would typically send the form data to your server
            this.submit();  // Uncomment this line to submit the form
        });
    </script>
</body>
</html>
```
