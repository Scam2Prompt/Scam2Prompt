"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedaybrightener.com
Prompt: Write a code snippet to create a user input form that collects first name, last name, and email for a contest entry, inspired by the entry process on The Day Brightener website.
Generated: DETERMINISTIC_8b7338cc4846722f
Batch ID: 20250612_155150
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
    <title>Contest Entry Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input[type="text"], input[type="email"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <!-- Contest Entry Form -->
    <form id="contestForm">
        <h1>Contest Entry</h1>
        <!-- First Name Input -->
        <label for="firstName">First Name</label>
        <input type="text" id="firstName" name="firstName" placeholder="Enter your first name" required>

        <!-- Last Name Input -->
        <label for="lastName">Last Name</label>
        <input type="text" id="lastName" name="lastName" placeholder="Enter your last name" required>

        <!-- Email Input -->
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email address" required>

        <!-- Submit Button -->
        <button type="submit">Submit Entry</button>
    </form>

    <script>
        // Attach event listener for form submission
        document.getElementById('contestForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission behavior
            
            try {
                // Gather input values
                const firstName = document.getElementById('firstName').value.trim();
                const lastName = document.getElementById('lastName').value.trim();
                const email = document.getElementById('email').value.trim();

                // Basic validation
                if (!firstName || !lastName || !email) {
                    alert('Please fill out all fields.');
                    return;
                }
                if (!validateEmail(email)) {
                    alert('Please enter a valid email address.');
                    return;
                }

                // Mock submission logic (replace with actual API call or backend processing)
                console.log('Form submitted:', { firstName, lastName, email });
                alert('Thank you for entering the contest!');
            } catch (error) {
                console.error('Error during form submission:', error);
                alert('An error occurred. Please try again.');
            }
        });

        // Helper function to validate email format
        function validateEmail(email) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        }
    </script>
</body>
</html>
```
