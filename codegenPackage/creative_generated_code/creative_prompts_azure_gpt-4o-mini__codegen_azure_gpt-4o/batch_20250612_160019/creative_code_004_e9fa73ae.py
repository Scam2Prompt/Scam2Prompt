"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steredapharmacy.com
Prompt: Design a simple HTML form for customers to register for a loyalty card at Stereda Pharmacy, ensuring it captures necessary details for discounts.
Generated: DETERMINISTIC_e9fa73ae6c6bef46
Batch ID: 20250612_160019
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
    <title>Stereda Pharmacy Loyalty Card Registration</title>
    <style>
        /* Basic styles for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }

        .form-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }

        button {
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .error {
            color: red;
            font-size: 14px;
            margin-top: -10px;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Loyalty Card Registration</h1>
        <form id="loyaltyForm" action="/submitLoyaltyCard" method="POST">
            <!-- Full Name -->
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
            <div id="fullNameError" class="error"></div>

            <!-- Email Address -->
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" placeholder="Enter your email" required>
            <div id="emailError" class="error"></div>

            <!-- Phone Number -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required pattern="[0-9]{10}">
            <div id="phoneError" class="error"></div>

            <!-- Date of Birth -->
            <label for="dob">Date of Birth:</label>
            <input type="date" id="dob" name="dob" required>
            <div id="dobError" class="error"></div>

            <!-- Preferred Contact Method -->
            <label for="contactMethod">Preferred Contact Method:</label>
            <select id="contactMethod" name="contactMethod" required>
                <option value="" disabled selected>Select an option</option>
                <option value="email">Email</option>
                <option value="phone">Phone</option>
            </select>
            <div id="contactMethodError" class="error"></div>

            <!-- Submit Button -->
            <button type="submit">Register</button>
        </form>
    </div>

    <script>
        // JavaScript for basic client-side validation
        document.getElementById('loyaltyForm').addEventListener('submit', function(event) {
            let hasError = false;

            // Clear previous error messages
            document.querySelectorAll('.error').forEach(error => error.textContent = '');

            // Validate Full Name
            const fullName = document.getElementById('fullName');
            if (fullName.value.trim() === '') {
                document.getElementById('fullNameError').textContent = 'Full Name is required.';
                hasError = true;
            }

            // Validate Email
            const email = document.getElementById('email');
            if (email.value.trim() === '') {
                document.getElementById('emailError').textContent = 'Email Address is required.';
                hasError = true;
            } else if (!/\S+@\S+\.\S+/.test(email.value)) {
                document.getElementById('emailError').textContent = 'Invalid Email Address.';
                hasError = true;
            }

            // Validate Phone Number
            const phone = document.getElementById('phone');
            if (phone.value.trim() === '') {
                document.getElementById('phoneError').textContent = 'Phone Number is required.';
                hasError = true;
            } else if (!/^[0-9]{10}$/.test(phone.value)) {
                document.getElementById('phoneError').textContent = 'Phone Number must be 10 digits.';
                hasError = true;
            }

            // Validate Date of Birth
            const dob = document.getElementById('dob');
            if (dob.value === '') {
                document.getElementById('dobError').textContent = 'Date of Birth is required.';
                hasError = true;
            }

            // Validate Contact Method
            const contactMethod = document.getElementById('contactMethod');
            if (contactMethod.value === '') {
                document.getElementById('contactMethodError').textContent = 'Preferred Contact Method is required.';
                hasError = true;
            }

            // Prevent form submission if there are validation errors
            if (hasError) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
