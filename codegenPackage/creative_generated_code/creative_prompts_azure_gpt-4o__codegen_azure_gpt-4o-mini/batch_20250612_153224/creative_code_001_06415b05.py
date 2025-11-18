"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Generate code to create a contact form for a handyman service website, allowing users to input their name, email, and service request (e.g., plumbing, electrical work, or appliance repair). Include validation for phone numbers like `620 365 080`.
Generated: DETERMINISTIC_06415b0594e23a2e
Batch ID: 20250612_153224
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
    <title>Contact Form - Handyman Service</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f9f9f9;
        }
        form {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 15px;
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
            margin-bottom: 15px;
        }
    </style>
</head>
<body>

<h1>Contact Us</h1>
<form id="contactForm" method="POST" action="/submit">
    <div id="errorMessage" class="error"></div>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="phone">Phone (e.g., 620 365 080):</label>
    <input type="text" id="phone" name="phone" required pattern="^\d{3} \d{3} \d{3}$" title="Format: 620 365 080">
    
    <label for="service">Service Request:</label>
    <textarea id="service" name="service" rows="4" required></textarea>

    <button type="submit">Submit</button>
</form>

<script>
    // Function to validate the form input before submission
    document.getElementById('contactForm').onsubmit = function(event) {
        const errorMessage = document.getElementById('errorMessage');
        errorMessage.textContent = ''; // Clear previous error messages

        const phonePattern = /^\d{3} \d{3} \d{3}$/;
        const phoneInput = document.getElementById('phone').value;

        // Validate phone number format
        if (!phonePattern.test(phoneInput)) {
            errorMessage.textContent = 'Phone number must be in the format: 620 365 080.';
            event.preventDefault(); // Prevent form submission
            return false;
        }

        // Further validation can be added here as needed

        return true; // Allow form submission if validation passes
    }
</script>

</body>
</html>
```
