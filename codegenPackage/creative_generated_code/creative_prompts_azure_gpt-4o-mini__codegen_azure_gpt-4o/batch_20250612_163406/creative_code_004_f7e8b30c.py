"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autocarescosme.com
Prompt: Construct a sample HTML form for users to inquire about renting classic vehicles from Autocares Cosme, ensuring it captures all necessary information for the booking process.
Generated: DETERMINISTIC_f7e8b30c74729fb1
Batch ID: 20250612_163406
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
    <title>Classic Vehicle Rental Inquiry</title>

    <!-- External CSS for styling -->
    <style>
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

        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16);
            max-width: 400px;
            width: 100%;
        }

        h1 {
            text-align: center;
            font-size: 1.5em;
            margin-bottom: 20px;
        }

        label {
            font-weight: bold;
            margin-bottom: 5px;
            display: block;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        input[type="submit"] {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }

        .error-message {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>

<body>
    <form id="rentalInquiryForm" action="/submit-inquiry" method="POST" novalidate>
        <!-- Heading -->
        <h1>Classic Vehicle Rental Inquiry</h1>

        <!-- Full Name Field -->
        <label for="fullName">Full Name:</label>
        <input type="text" id="fullName" name="fullName" required>
        <span class="error-message" id="fullNameError"></span>

        <!-- Email Field -->
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required>
        <span class="error-message" id="emailError"></span>

        <!-- Phone Number Field -->
        <label for="phoneNumber">Phone Number:</label>
        <input type="tel" id="phoneNumber" name="phoneNumber" pattern="[0-9]{10}" required>
        <span class="error-message" id="phoneError">Please enter a valid 10-digit phone number.</span>

        <!-- Vehicle Type Dropdown -->
        <label for="vehicleType">Select Vehicle Type:</label>
        <select id="vehicleType" name="vehicleType" required>
            <option value="">-- Please Select --</option>
            <option value="classic-car">Classic Car</option>
            <option value="vintage-bus">Vintage Bus</option>
            <option value="motorcycle">Motorcycle</option>
        </select>
        <span class="error-message" id="vehicleTypeError"></span>

        <!-- Rental Date Field -->
        <label for="rentalDate">Desired Rental Date:</label>
        <input type="date" id="rentalDate" name="rentalDate" required>
        <span class="error-message" id="rentalDateError"></span>

        <!-- Additional Comments Field -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4"></textarea>

        <!-- Submit Button -->
        <input type="submit" value="Submit Inquiry">
    </form>

    <!-- JavaScript for Basic Validation -->
    <script>
        document.getElementById('rentalInquiryForm').addEventListener('submit', function (event) {
            // Clear previous error messages
            document.querySelectorAll('.error-message').forEach(span => span.textContent = '');

            // Basic validation
            let isValid = true;

            const fullName = document.getElementById('fullName');
            if (!fullName.value.trim()) {
                document.getElementById('fullNameError').textContent = 'Full name is required.';
                isValid = false;
            }

            const email = document.getElementById('email');
            if (!email.value.trim() || !email.validity.valid) {
                document.getElementById('emailError').textContent = 'Valid email address is required.';
                isValid = false;
            }

            const phoneNumber = document.getElementById('phoneNumber');
            if (!phoneNumber.value.trim() || !phoneNumber.validity.valid) {
                document.getElementById('phoneError').textContent = 'Valid phone number is required.';
                isValid = false;
            }

            const vehicleType = document.getElementById('vehicleType');
            if (!vehicleType.value.trim()) {
                document.getElementById('vehicleTypeError').textContent = 'Please select a vehicle type.';
                isValid = false;
            }

            const rentalDate = document.getElementById('rentalDate');
            if (!rentalDate.value.trim()) {
                document.getElementById('rentalDateError').textContent = 'Rental date is required.';
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>

</html>
```
