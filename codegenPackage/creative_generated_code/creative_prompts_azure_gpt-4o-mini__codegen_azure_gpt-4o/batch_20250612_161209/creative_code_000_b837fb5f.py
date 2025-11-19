"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Generate a code snippet for a web form that collects user information for insurance quotes, including fields for name, phone number, email, and specific details for auto insurance like driving experience and vehicle model.
Generated: DETERMINISTIC_b837fb5ffbafd161
Batch ID: 20250612_161209
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
    <title>Insurance Quote Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 600px;
            margin: 0 auto;
        }
        label {
            display: block;
            margin-top: 10px;
            font-weight: bold;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .error-message {
            color: red;
            font-size: 0.9em;
        }
        .success-message {
            color: green;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>Insurance Quote Form</h1>
    <form id="insuranceForm">
        <!-- Full Name Input -->
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
        
        <!-- Phone Number Input -->
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required pattern="[0-9]{10}">
        
        <!-- Email Address Input -->
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email address" required>
        
        <!-- Driving Experience Input -->
        <label for="drivingExperience">Driving Experience (in years)</label>
        <input type="number" id="drivingExperience" name="drivingExperience" placeholder="Enter years of driving experience" required min="0">
        
        <!-- Vehicle Model Input -->
        <label for="vehicleModel">Vehicle Model</label>
        <input type="text" id="vehicleModel" name="vehicleModel" placeholder="Enter your vehicle model" required>
        
        <!-- Submit Button -->
        <button type="submit">Get Quote</button>

        <!-- Success/Error Messages -->
        <div id="message" class="success-message" style="display: none;">Form submitted successfully!</div>
        <div id="error-message" class="error-message" style="display: none;">Failed to submit the form. Please check your entries.</div>
    </form>

    <script>
        // JavaScript to handle form submission
        document.getElementById('insuranceForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
            
            const messageElement = document.getElementById("message");
            const errorMessageElement = document.getElementById("error-message");

            try {
                // Simulate form processing
                const formData = {
                    name: document.getElementById('name').value.trim(),
                    phone: document.getElementById('phone').value.trim(),
                    email: document.getElementById('email').value.trim(),
                    drivingExperience: document.getElementById('drivingExperience').value.trim(),
                    vehicleModel: document.getElementById('vehicleModel').value.trim(),
                };

                // Validate inputs (example validation: check non-empty fields)
                for (const field in formData) {
                    if (!formData[field]) {
                        throw new Error(`Field '${field}' cannot be empty.`);
                    }
                }

                // Clear any error messages
                errorMessageElement.style.display = "none";

                // Show success message
                messageElement.style.display = "block";

                console.log("Form Data Submitted Successfully:", formData);
            } catch (error) {
                // Handle errors and display the error message
                messageElement.style.display = "none";
                errorMessageElement.textContent = error.message;
                errorMessageElement.style.display = "block";
            }
        });
    </script>
</body>
</html>
```
