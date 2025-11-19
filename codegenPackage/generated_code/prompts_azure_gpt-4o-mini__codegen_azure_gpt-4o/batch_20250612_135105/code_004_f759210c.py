"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Develop a web form for clients to request HVAC cleaning services, ensuring it captures necessary details as outlined by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_f759210cf71df072
Batch ID: 20250612_135105
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
    <title>HVAC Cleaning Service Request</title>
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
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-top: 10px;
            font-weight: bold;
        }
        input, textarea, select, button {
            margin-top: 5px;
            padding: 10px;
            font-size: 16px;
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
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>HVAC Cleaning Service Request</h1>
        <form id="hvacForm">
            <!-- Full Name -->
            <label for="fullName">Full Name</label>
            <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
            <span class="error" id="nameError"></span>

            <!-- Email -->
            <label for="email">Email</label>
            <input type="email" id="email" name="email" placeholder="Enter your email address" required>
            <span class="error" id="emailError"></span>

            <!-- Phone Number -->
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
            <span class="error" id="phoneError"></span>

            <!-- Address -->
            <label for="address">Address</label>
            <textarea id="address" name="address" rows="3" placeholder="Enter your address" required></textarea>
            <span class="error" id="addressError"></span>

            <!-- Preferred Date -->
            <label for="preferredDate">Preferred Service Date</label>
            <input type="date" id="preferredDate" name="preferredDate" required>
            <span class="error" id="dateError"></span>

            <!-- Service Type -->
            <label for="serviceType">Service Type</label>
            <select id="serviceType" name="serviceType" required>
                <option value="">Select a service</option>
                <option value="ductCleaning">Duct Cleaning</option>
                <option value="ventCleaning">Vent Cleaning</option>
                <option value="fullSystemCleaning">Full System Cleaning</option>
            </select>
            <span class="error" id="serviceError"></span>

            <!-- Additional Notes -->
            <label for="notes">Additional Notes (Optional)</label>
            <textarea id="notes" name="notes" rows="4" placeholder="Enter any additional details"></textarea>

            <!-- Submit Button -->
            <button type="submit">Submit Request</button>
        </form>
    </div>

    <script>
        // Form validation and submission
        document.getElementById('hvacForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Clear previous error messages
            document.querySelectorAll('.error').forEach(error => error.textContent = '');

            // Validate form fields
            let isValid = true;

            const fullName = document.getElementById('fullName').value.trim();
            if (!fullName) {
                document.getElementById('nameError').textContent = 'Full name is required.';
                isValid = false;
            }

            const email = document.getElementById('email').value.trim();
            if (!email || !/^\S+@\S+\.\S+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Valid email is required.';
                isValid = false;
            }

            const phone = document.getElementById('phone').value.trim();
            if (!phone || !/^\d{10}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Valid 10-digit phone number is required.';
                isValid = false;
            }

            const address = document.getElementById('address').value.trim();
            if (!address) {
                document.getElementById('addressError').textContent = 'Address is required.';
                isValid = false;
            }

            const preferredDate = document.getElementById('preferredDate').value;
            if (!preferredDate) {
                document.getElementById('dateError').textContent = 'Preferred service date is required.';
                isValid = false;
            }

            const serviceType = document.getElementById('serviceType').value;
            if (!serviceType) {
                document.getElementById('serviceError').textContent = 'Please select a service type.';
                isValid = false;
            }

            // If all fields are valid, submit the form data
            if (isValid) {
                const formData = {
                    fullName,
                    email,
                    phone,
                    address,
                    preferredDate,
                    serviceType,
                    notes: document.getElementById('notes').value.trim()
                };

                // Simulate form submission (replace with actual API call in production)
                console.log('Form submitted successfully:', formData);
                alert('Your request has been submitted successfully!');
                document.getElementById('hvacForm').reset(); // Reset the form
            }
        });
    </script>
</body>
</html>
```
