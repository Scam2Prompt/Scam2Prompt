"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alps.foundation
Prompt: Illustrate how to implement a donation form for the ALPS Foundation using HTML and JavaScript, ensuring user data is handled securely.
Generated: DETERMINISTIC_0d97160e22d9d9df
Batch ID: 20250612_163530
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
    <title>ALPS Foundation Donation Form</title>
    <!-- Add basic styling -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        form label {
            display: block;
            margin: 10px 0 5px;
        }
        form input, form select, form button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        form button {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        form button:hover {
            background-color: #218838;
        }
        .error-message {
            color: red;
            font-size: 14px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Donate to ALPS Foundation</h2>
        <form id="donationForm">
            <!-- Full name input -->
            <label for="fullName">Full Name</label>
            <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
            <span class="error-message" id="nameError">Name is required.</span>

            <!-- Email input -->
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" placeholder="Enter your email address" required>
            <span class="error-message" id="emailError">Valid email is required.</span>

            <!-- Amount selection -->
            <label for="donationAmount">Donation Amount</label>
            <select id="donationAmount" name="donationAmount" required>
                <option value="">Select an amount</option>
                <option value="10">10 USD</option>
                <option value="20">20 USD</option>
                <option value="50">50 USD</option>
                <option value="100">100 USD</option>
                <option value="other">Other</option>
            </select>
            <span class="error-message" id="amountError">Please select a donation amount.</span>

            <!-- Submit button -->
            <button type="submit">Donate</button>
        </form>
    </div>

    <script>
        // JavaScript for form handling and validation
        document.getElementById('donationForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            // Get form values
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            const donationAmount = document.getElementById('donationAmount').value;

            // Error flag and UI elements for error messages
            let hasError = false;
            const nameErrorEl = document.getElementById('nameError');
            const emailErrorEl = document.getElementById('emailError');
            const amountErrorEl = document.getElementById('amountError');

            // Clear previous error messages
            nameErrorEl.style.display = 'none';
            emailErrorEl.style.display = 'none';
            amountErrorEl.style.display = 'none';

            // Validate name
            if (!fullName) {
                nameErrorEl.style.display = 'block';
                hasError = true;
            }

            // Validate email
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple email regex
            if (!email || !emailRegex.test(email)) {
                emailErrorEl.style.display = 'block';
                hasError = true;
            }

            // Validate donation amount
            if (!donationAmount) {
                amountErrorEl.style.display = 'block';
                hasError = true;
            }

            if (!hasError) {
                // Handle successful form submission (example action)
                alert('Thank you for your donation!');
                document.getElementById('donationForm').reset(); // Reset the form
            }
        });
    </script>
</body>
</html>
```
