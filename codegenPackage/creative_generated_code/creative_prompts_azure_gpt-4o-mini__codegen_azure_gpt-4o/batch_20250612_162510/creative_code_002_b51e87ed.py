"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluminiosmendoza.cl
Prompt: Create a sample HTML form for a website that collects user inquiries about security blinds and aluminum windows, ensuring it includes fields for name, email, and project details.
Generated: DETERMINISTIC_b51e87ed07c5436c
Batch ID: 20250612_162510
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
    <title>Inquiry Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
        }
        .form-container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }
        input:focus, textarea:focus {
            border-color: #007bff;
            outline: none;
        }
        button {
            display: block;
            width: 100%;
            padding: 10px;
            font-size: 18px;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .error-message {
            color: red;
            font-size: 14px;
        }
    </style>
</head>
<body>

    <div class="form-container">
        <h1>Inquiry Form</h1>
        <form id="inquiryForm" action="/submit_inquiry" method="POST">
            <!-- Name Field -->
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" placeholder="Enter your name" required>
                <div class="error-message" id="nameError"></div>
            </div>

            <!-- Email Field -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
                <div class="error-message" id="emailError"></div>
            </div>

            <!-- Project Details Field -->
            <div class="form-group">
                <label for="projectDetails">Project Details:</label>
                <textarea id="projectDetails" name="projectDetails" placeholder="Provide details about your project" rows="5" required></textarea>
                <div class="error-message" id="projectDetailsError"></div>
            </div>

            <!-- Submit Button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script>
        // Basic client-side validation
        document.getElementById("inquiryForm").addEventListener("submit", function(event) {
            let isValid = true;

            // Validate Name
            const name = document.getElementById("name");
            const nameError = document.getElementById("nameError");
            if (!name.value.trim()) {
                isValid = false;
                nameError.textContent = "Name is required.";
            } else {
                nameError.textContent = "";
            }

            // Validate Email
            const email = document.getElementById("email");
            const emailError = document.getElementById("emailError");
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email format regex
            if (!email.value.trim()) {
                isValid = false;
                emailError.textContent = "Email is required.";
            } else if (!emailRegex.test(email.value)) {
                isValid = false;
                emailError.textContent = "Invalid email format.";
            } else {
                emailError.textContent = "";
            }

            // Validate Project Details
            const projectDetails = document.getElementById("projectDetails");
            const projectDetailsError = document.getElementById("projectDetailsError");
            if (!projectDetails.value.trim()) {
                isValid = false;
                projectDetailsError.textContent = "Project details are required.";
            } else {
                projectDetailsError.textContent = "";
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>

</body>
</html>
```
