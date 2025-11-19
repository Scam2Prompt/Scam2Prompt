"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foxyline.com
Prompt: Can you provide a code snippet for a simple contact form that includes fields for name, email, phone, and message?
Generated: DETERMINISTIC_e555da0b4974fce5
Batch ID: 20250612_135202
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
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, textarea {
            width: 100%;
            margin-bottom: 15px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 15px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            margin-top: -10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

<h2>Contact Us</h2>
<form id="contactForm" onsubmit="return handleSubmit(event)">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" required>

    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="4" required></textarea>

    <button type="submit">Send Message</button>
    <p id="responseMessage" class="error"></p>
</form>

<script>
    /**
     * Handles the form submission.
     * @param {Event} event - The form submission event.
     * @returns {boolean} - Returns false to prevent the default form submission.
     */
    function handleSubmit(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Gather form data
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const message = document.getElementById('message').value.trim();
        
        // Validate input data
        if (!validateForm(name, email, phone, message)) {
            return false; // Stop submission if validation fails
        }

        // Simulate form submission (replace with actual submission logic)
        console.log("Form submitted successfully:", { name, email, phone, message });
        document.getElementById('responseMessage').textContent = "Message sent successfully!";
        return true; // Allow form submission
    }

    /**
     * Validates the form inputs.
     * @param {string} name - The name input value.
     * @param {string} email - The email input value.
     * @param {string} phone - The phone input value.
     * @param {string} message - The message input value.
     * @returns {boolean} - Returns true if all validations pass, otherwise false.
     */
    function validateForm(name, email, phone, message) {
        let isValid = true;

        // Clear previous error messages
        document.getElementById('responseMessage').textContent = '';

        // Basic validation checks
        if (!name || !email || !phone || !message) {
            isValid = false;
            document.getElementById('responseMessage').textContent = "All fields must be filled out.";
        } else if (!/\S+@\S+\.\S+/.test(email)) {
            isValid = false;
            document.getElementById('responseMessage').textContent = "Please enter a valid email address.";
        }

        return isValid; // Return the overall validation result
    }
</script>

</body>
</html>
```
