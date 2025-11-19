"""
Generated Code Metadata:
========================
Original URL: https://carehelpers.pt
Prompt: "Create a simple web form using HTML and JavaScript to collect client information for a home care services company, inspired by the contact form on the CARE HELPERS website."
Generated: DETERMINISTIC_e42e48682b19a77d
Batch ID: 20250622_205436
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
    <title>Home Care Services Contact Form</title>
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
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Contact Us</h2>
    <form id="contactForm">
        <div class="form-group">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>
            <div class="error" id="nameError"></div>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <div class="error" id="emailError"></div>
        </div>
        <div class="form-group">
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>
            <div class="error" id="phoneError"></div>
        </div>
        <div class="form-group">
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>
            <div class="error" id="messageError"></div>
        </div>
        <button type="submit">Submit</button>
    </form>
</div>

<script>
    // Function to validate the form inputs
    function validateForm(event) {
        event.preventDefault(); // Prevent form submission

        // Clear previous error messages
        document.getElementById('nameError').innerText = '';
        document.getElementById('emailError').innerText = '';
        document.getElementById('phoneError').innerText = '';
        document.getElementById('messageError').innerText = '';

        // Get form values
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const message = document.getElementById('message').value.trim();

        // Validate inputs
        let isValid = true;

        if (name === '') {
            document.getElementById('nameError').innerText = 'Name is required.';
            isValid = false;
        }
        if (email === '') {
            document.getElementById('emailError').innerText = 'Email is required.';
            isValid = false;
        } else if (!validateEmail(email)) {
            document.getElementById('emailError').innerText = 'Invalid email format.';
            isValid = false;
        }
        if (phone === '') {
            document.getElementById('phoneError').innerText = 'Phone number is required.';
            isValid = false;
        }
        if (message === '') {
            document.getElementById('messageError').innerText = 'Message is required.';
            isValid = false;
        }

        // If valid, submit the form (or handle the submission)
        if (isValid) {
            alert('Form submitted successfully!');
            // Here you can add code to send the form data to a server
            // For example, using fetch or XMLHttpRequest
        }
    }

    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Attach the validateForm function to the form's submit event
    document.getElementById('contactForm').addEventListener('submit', validateForm);
</script>

</body>
</html>
```
