"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubalife.me
Prompt: Design a simple web form using HTML and JavaScript to allow users to inquire about services at TUBA SPA, including their contact details and preferred service.
Generated: DETERMINISTIC_8ee3eda7aa5d7caf
Batch ID: 20250612_161520
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
    <title>TUBA SPA Inquiry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        .form-container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .form-container h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        .form-group textarea {
            resize: vertical;
        }

        .form-group button {
            display: block;
            width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            font-size: 16px;
        }

        .form-group button:hover {
            background-color: #45a049;
        }

        .error {
            color: red;
            font-size: 14px;
        }

        .success {
            color: green;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>TUBA SPA Inquiry Form</h2>
        <form id="spaForm">
            <!-- Form Group for Name -->
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" placeholder="Enter your full name" required>
                <span class="error" id="nameError"></span>
            </div>

            <!-- Form Group for Email -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email address" required>
                <span class="error" id="emailError"></span>
            </div>

            <!-- Form Group for Phone Number -->
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" pattern="[0-9]{10}" required>
                <span class="error" id="phoneError"></span>
            </div>

            <!-- Form Group for Preferred Service -->
            <div class="form-group">
                <label for="service">Preferred Service:</label>
                <select id="service" name="service" required>
                    <option value="">Select a service</option>
                    <option value="massage">Massage</option>
                    <option value="facial">Facial</option>
                    <option value="manicure">Manicure</option>
                    <option value="pedicure">Pedicure</option>
                </select>
                <span class="error" id="serviceError"></span>
            </div>

            <!-- Form Group for Additional Comments -->
            <div class="form-group">
                <label for="comments">Additional Comments:</label>
                <textarea id="comments" name="comments" rows="4" placeholder="Enter any additional comments"></textarea>
            </div>

            <!-- Submit Button -->
            <div class="form-group">
                <button type="submit">Submit Inquiry</button>
                <span class="success" id="formSuccess"></span>
            </div>
        </form>
    </div>

    <script>
        // JavaScript code for form validation and submission handling
        document.getElementById('spaForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission
            
            // Clear previous error messages and success message
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('phoneError').textContent = '';
            document.getElementById('serviceError').textContent = '';
            document.getElementById('formSuccess').textContent = '';
            
            // Form field values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const service = document.getElementById('service').value;

            let isValid = true;

            // Validate name
            if (!name) {
                document.getElementById('nameError').textContent = 'Name is required.';
                isValid = false;
            }

            // Validate email
            if (!email || !email.includes('@')) {
                document.getElementById('emailError').textContent = 'Valid email is required.';
                isValid = false;
            }

            // Validate phone
            if (!phone || !/^\d{10}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Valid 10-digit phone number is required.';
                isValid = false;
            }

            // Validate service selection
            if (!service) {
                document.getElementById('serviceError').textContent = 'Please select a service.';
                isValid = false;
            }

            // Handle form submission if validation is successful
            if (isValid) {
                // In a real application, you would send the form data to a server here
                document.getElementById('formSuccess').textContent = 'Your inquiry has been submitted successfully!';
                document.getElementById('spaForm').reset(); // Reset the form
            }
        });
    </script>
</body>
</html>
```
