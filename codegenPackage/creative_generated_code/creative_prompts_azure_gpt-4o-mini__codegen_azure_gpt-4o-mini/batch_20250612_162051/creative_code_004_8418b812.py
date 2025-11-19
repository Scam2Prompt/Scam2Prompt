"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.efeotokurtarma.com.tr
Prompt: Illustrate how to implement a contact form in HTML that connects users to a towing service like Efem Oto Çekici, ensuring it highlights 24/7 support.
Generated: DETERMINISTIC_8418b8128ec43128
Batch ID: 20250612_162051
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
    <title>Contact Us - Efem Oto Çekici</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
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
        }
        input[type="text"], input[type="email"], textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #218838;
        }
        .support-info {
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
            color: #d9534f;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Contact Us</h1>
    <form id="contactForm" method="POST" action="submit_form.php">
        <div class="form-group">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required aria-required="true" placeholder="Enter your full name">
        </div>
        
        <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required aria-required="true" placeholder="Enter your email address">
        </div>

        <div class="form-group">
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required aria-required="true" placeholder="Enter your message here..."></textarea>
        </div>

        <button type="submit">Send Message</button>
    </form>

    <div class="support-info">
        We offer 24/7 support for all your towing needs!
    </div>
</div>

<script>
    // Form submission event handler
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        // Prevent the default form submission
        event.preventDefault();

        // Validate form fields
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        if (name && email && message) {
            this.submit(); // Submit form if validation is successful
        } else {
            alert('Please fill in all fields.');
        }
    });
</script>

</body>
</html>
```

**Note:** Make sure to create a `submit_form.php` file on the server side to handle the form submissions appropriately and securely. This code serves as a client-side implementation of the contact form.
