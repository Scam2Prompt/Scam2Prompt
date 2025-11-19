"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foxyline.com
Prompt: How can I integrate a contact form using HTML and JavaScript for a business inquiry page like FOXYLINE.COM?
Generated: DETERMINISTIC_6c423f68ddaed680
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
    <title>Business Inquiry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f8f8;
        }
        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .contact-form h2 {
            margin-bottom: 20px;
            font-size: 24px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-group textarea {
            resize: vertical;
            min-height: 100px;
        }
        .form-group .error {
            color: red;
            font-size: 14px;
        }
        .submit-btn {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #0056b3;
        }
        .success-message {
            color: green;
        }
    </style>
</head>
<body>
    <div class="contact-form">
        <h2>Contact Us</h2>
        <form id="businessInquiryForm">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
                <span class="error" id="nameError"></span>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                <span class="error" id="emailError"></span>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" required></textarea>
                <span class="error" id="messageError"></span>
            </div>
            <button type="submit" class="submit-btn">Submit</button>
            <p class="success-message" id="successMessage" style="display: none;">Thank you for your inquiry! We'll get back to you soon.</p>
        </form>
    </div>

    <script>
        // Get form and elements
        const form = document.getElementById('businessInquiryForm');
        const nameInput = document.getElementById('name');
        const emailInput = document.getElementById('email');
        const messageInput = document.getElementById('message');
        const nameError = document.getElementById('nameError');
        const emailError = document.getElementById('emailError');
        const messageError = document.getElementById('messageError');
        const successMessage = document.getElementById('successMessage');

        /**
         * Validates the input fields.
         * @returns {boolean} - Returns true if all fields are valid, otherwise false.
         */
        function validateForm() {
            let isValid = true;

            // Reset error messages
            nameError.textContent = '';
            emailError.textContent = '';
            messageError.textContent = '';

            // Name validation
            if (nameInput.value.trim() === '') {
                nameError.textContent = 'Name is required.';
                isValid = false;
            }

            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (emailInput.value.trim() === '') {
                emailError.textContent = 'Email is required.';
                isValid = false;
            } else if (!emailRegex.test(emailInput.value.trim())) {
                emailError.textContent = 'Please enter a valid email address.';
                isValid = false;
            }

            // Message validation
            if (messageInput.value.trim() === '') {
                messageError.textContent = 'Message is required.';
                isValid = false;
            }

            return isValid;
        }

        /**
         * Handles form submission.
         * @param {Event} event - The form submission event.
         */
        form.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent form from being submitted traditionally

            if (validateForm()) {
                // Display success message
                successMessage.style.display = 'block';

                // Optionally, send the form data to a server via an API call
                // Example:
                // fetch('/submit-form', {
                //     method: 'POST',
                //     headers: { 'Content-Type': 'application/json' },
                //     body: JSON.stringify({
                //         name: nameInput.value,
                //         email: emailInput.value,
                //         message: messageInput.value,
                //     }),
                // }).then(response => {
                //     if (response.ok) {
                //         console.log('Form submitted successfully');
                //     } else {
                //         console.error('Error submitting form');
                //     }
                // }).catch(error => console.error('Network error:', error));
                
                // Clear form fields after submission
                form.reset();
            }
        });
    </script>
</body>
</html>
```
