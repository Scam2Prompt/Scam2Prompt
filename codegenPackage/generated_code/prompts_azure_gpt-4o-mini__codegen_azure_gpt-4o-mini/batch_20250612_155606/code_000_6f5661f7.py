"""
Generated Code Metadata:
========================
Original URL: https://jnanbarta.com
Prompt: Generate a code snippet to create a contact form similar to the one on the Jnanbarta website, including fields for first name, last name, phone number, email, address, and a message.
Generated: DETERMINISTIC_6f5661f757293828
Batch ID: 20250612_155606
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
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #5cb85c;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #4cae4c;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Contact Us</h2>
    <form id="contactForm" onsubmit="return handleSubmit(event)">
        <div class="form-group">
            <label for="firstName">First Name</label>
            <input type="text" id="firstName" name="firstName" required>
        </div>
        <div class="form-group">
            <label for="lastName">Last Name</label>
            <input type="text" id="lastName" name="lastName" required>
        </div>
        <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" required>
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="address">Address</label>
            <input type="text" id="address" name="address" required>
        </div>
        <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" name="message" rows="4" required></textarea>
        </div>
        <button type="submit">Submit</button>
    </form>
</div>

<script>
    /**
     * Handles the form submission.
     * @param {Event} event - The submit event.
     * @returns {boolean} - Returns false to prevent default form submission.
     */
    function handleSubmit(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        const formData = {
            firstName: document.getElementById('firstName').value,
            lastName: document.getElementById('lastName').value,
            phone: document.getElementById('phone').value,
            email: document.getElementById('email').value,
            address: document.getElementById('address').value,
            message: document.getElementById('message').value,
        };

        // Validate form data (basic validation)
        if (!validateFormData(formData)) {
            alert('Please fill in all fields correctly.');
            return false;
        }

        // Simulate form submission (replace with actual API call)
        console.log('Form submitted successfully:', formData);
        alert('Thank you for your message! We will get back to you soon.');

        // Reset the form
        document.getElementById('contactForm').reset();
        return false; // Prevent default form submission
    }

    /**
     * Validates the form data.
     * @param {Object} data - The form data to validate.
     * @returns {boolean} - Returns true if valid, false otherwise.
     */
    function validateFormData(data) {
        // Check if all fields are filled
        return Object.values(data).every(value => value.trim() !== '');
    }
</script>

</body>
</html>
```
