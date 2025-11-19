"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esofa.edu.pe
Prompt: Develop a simple HTML form for prospective students to inquire about the admission process at the Escuela de Suboficiales de la Fuerza Aérea del Perú, including validation for required fields.
Generated: DETERMINISTIC_6d0d361d0cf80008
Batch ID: 20250612_162220
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
    <title>Admission Inquiry Form</title>

    <!-- Link to CSS styles -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 500px;
            margin: 0 auto;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea, button {
            width: 100%;
            padding: 8px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
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
            font-size: 0.8em;
        }
    </style>
</head>
<body>
    <h1>Admission Inquiry Form</h1>
    <p>Please fill out the form below to inquire about the admission process.</p>
    
    <!-- Admission Inquiry Form -->
    <form id="admissionForm">
        <!-- Full Name Field -->
        <label for="fullName">Full Name *</label>
        <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
        <span class="error" id="fullNameError"></span>
        
        <!-- Email Field -->
        <label for="email">Email Address *</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
        <span class="error" id="emailError"></span>

        <!-- Phone Number Field -->
        <label for="phone">Phone Number *</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required pattern="[0-9]{9}">
        <span class="error" id="phoneError"></span>

        <!-- Message Field -->
        <label for="message">Message</label>
        <textarea id="message" name="message" placeholder="Enter your inquiry or message" rows="4"></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
    </form>
    
    <!-- JavaScript for Form Validation -->
    <script>
        const form = document.getElementById('admissionForm');

        form.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent form submission
            
            let isValid = true;

            // Validate Full Name
            const fullName = document.getElementById('fullName');
            const fullNameError = document.getElementById('fullNameError');
            fullNameError.textContent = '';
            if (fullName.value.trim() === '') {
                fullNameError.textContent = 'Full Name is required.';
                isValid = false;
            }

            // Validate Email
            const email = document.getElementById('email');
            const emailError = document.getElementById('emailError');
            emailError.textContent = '';
            const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,6}$/;
            if (!emailPattern.test(email.value.trim())) {
                emailError.textContent = 'Please enter a valid email address.';
                isValid = false;
            }

            // Validate Phone Number
            const phone = document.getElementById('phone');
            const phoneError = document.getElementById('phoneError');
            phoneError.textContent = '';
            const phonePattern = /^[0-9]{9}$/;
            if (!phonePattern.test(phone.value.trim())) {
                phoneError.textContent = 'Phone number must be 9 digits.';
                isValid = false;
            }

            // If all validations pass, submit the form
            if (isValid) {
                alert('Inquiry submitted successfully!');
                form.reset(); // Reset the form
            }
        });
    </script>
</body>
</html>
```
