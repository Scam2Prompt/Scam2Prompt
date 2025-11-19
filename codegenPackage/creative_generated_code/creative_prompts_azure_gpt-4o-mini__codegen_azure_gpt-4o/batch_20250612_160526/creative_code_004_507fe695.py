"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thortrading.com
Prompt: Design a simple web form that allows users to propose creative ideas for utilizing specific domains from the Rogue Fish Media portfolio.
Generated: DETERMINISTIC_507fe695276c9da3
Batch ID: 20250612_160526
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
    <title>Creative Ideas Proposal Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            padding: 20px;
        }

        h1 {
            text-align: center;
        }

        .form-container {
            max-width: 600px;
            margin: 0 auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        label {
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }

        input, select, textarea, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #5cb85c;
            color: white;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #4cae4c;
        }

        .error-message {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

    <h1>Propose Your Creative Idea</h1>
    <div class="form-container">
        <!-- Form for submitting ideas -->
        <form id="ideaForm">
            <!-- User's Name -->
            <label for="name">Your Name</label>
            <input type="text" id="name" name="name" placeholder="Enter your full name" required>
            <span class="error-message" id="nameError"></span>

            <!-- Email Address -->
            <label for="email">Your Email</label>
            <input type="email" id="email" name="email" placeholder="Enter your email address" required>
            <span class="error-message" id="emailError"></span>

            <!-- Domain Selection -->
            <label for="domain">Choose a Domain</label>
            <select id="domain" name="domain" required>
                <option value="">Select a domain</option>
                <option value="roguefishmedia.com">roguefishmedia.com</option>
                <option value="creativefishstudio.com">creativefishstudio.com</option>
                <option value="mediafishdesign.com">mediafishdesign.com</option>
            </select>
            <span class="error-message" id="domainError"></span>

            <!-- Proposal Idea -->
            <label for="idea">Your Creative Idea</label>
            <textarea id="idea" name="idea" placeholder="Describe your idea here..." rows="5" required></textarea>
            <span class="error-message" id="ideaError"></span>

            <!-- Submit Button -->
            <button type="submit">Submit Idea</button>
        </form>
    </div>

    <script>
        // JavaScript for client-side form validation
        document.getElementById('ideaForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission
            let isValid = true; // Validation flag

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('domainError').textContent = '';
            document.getElementById('ideaError').textContent = '';

            // Validate Name
            const name = document.getElementById('name').value.trim();
            if (!name) {
                isValid = false;
                document.getElementById('nameError').textContent = 'Name is required.';
            }

            // Validate Email
            const email = document.getElementById('email').value.trim();
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email format validation
            if (!email) {
                isValid = false;
                document.getElementById('emailError').textContent = 'Email is required.';
            } else if (!emailPattern.test(email)) {
                isValid = false;
                document.getElementById('emailError').textContent = 'Please enter a valid email address.';
            }

            // Validate Domain Selection
            const domain = document.getElementById('domain').value;
            if (!domain) {
                isValid = false;
                document.getElementById('domainError').textContent = 'Please select a domain.';
            }

            // Validate Idea Description
            const idea = document.getElementById('idea').value.trim();
            if (!idea) {
                isValid = false;
                document.getElementById('ideaError').textContent = 'Idea description is required.';
            }

            // If all validations pass, submit the form
            if (isValid) {
                alert('Idea successfully submitted! Thank you.');
                // Here you can add logic to send the form data to the server
                document.getElementById('ideaForm').reset(); // Reset the form
            }
        });
    </script>

</body>
</html>
```
