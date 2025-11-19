"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jnanbarta.com
Prompt: Generate a code snippet to create a contact form similar to the one on the Jnanbarta website, including fields for first name, last name, phone number, email, address, and a message.
Generated: DETERMINISTIC_6f5661f757293828
Batch ID: 20250612_155606
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
            margin: 20px;
        }
        form {
            display: flex;
            flex-direction: column;
            max-width: 400px;
        }
        label {
            margin: 10px 0 5px;
        }
        input, textarea {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            margin-top: 10px;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

<h1>Contact Us</h1>

<form id="contactForm">
    <label for="firstName">First Name</label>
    <input type="text" id="firstName" name="firstName" required>

    <label for="lastName">Last Name</label>
    <input type="text" id="lastName" name="lastName" required>

    <label for="phone">Phone Number</label>
    <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}">

    <label for="email">Email</label>
    <input type="email" id="email" name="email" required>

    <label for="address">Address</label>
    <input type="text" id="address" name="address" required>

    <label for="message">Message</label>
    <textarea id="message" name="message" rows="4" required></textarea>

    <button type="submit">Send Message</button>
</form>

<script>
    // Handle form submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        const formData = new FormData(this);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Send form data to server
        fetch('/submit-contact-form', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            alert('Message sent successfully!');
            this.reset(); // Reset form fields
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert('There was an error sending your message. Please try again.');
        });
    });
</script>

</body>
</html>
```
