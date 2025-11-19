"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Write a code snippet to create a user input form that collects first name, last name, and email for a contest entry, inspired by the entry process on The Day Brightener website.
Generated: DETERMINISTIC_8b7338cc4846722f
Batch ID: 20250612_155150
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
    <title>Contest Entry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        .form-container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 25px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #333;
        }
        input[type="text"],
        input[type="email"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }
        input:focus {
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 5px rgba(52,152,219,0.5);
        }
        .submit-btn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }
        .submit-btn:hover {
            background-color: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
        .success-message {
            display: none;
            background-color: #2ecc71;
            color: white;
            padding: 15px;
            border-radius: 4px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Contest Entry Form</h1>
        <form id="contestForm">
            <div class="form-group">
                <label for="firstName">First Name</label>
                <input type="text" id="firstName" name="firstName" required>
                <div class="error" id="firstNameError">Please enter your first name</div>
            </div>
            
            <div class="form-group">
                <label for="lastName">Last Name</label>
                <input type="text" id="lastName" name="lastName" required>
                <div class="error" id="lastNameError">Please enter your last name</div>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required>
                <div class="error" id="emailError">Please enter a valid email address</div>
            </div>
            
            <button type="submit" class="submit-btn">Submit Entry</button>
        </form>
        
        <div class="success-message" id="successMessage">
            Thank you for your contest entry! Good luck!
        </div>
    </div>

    <script>
        document.getElementById('contestForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.style.display = 'none');
            
            // Get form values
            const firstName = document.getElementById('firstName').value.trim();
            const lastName = document.getElementById('lastName').value.trim();
            const email = document.getElementById('email').value.trim();
            
            let isValid = true;
            
            // Validate first name
            if (!firstName) {
                document.getElementById('firstNameError').style.display = 'block';
                isValid = false;
            }
            
            // Validate last name
            if (!lastName) {
                document.getElementById('lastNameError').style.display = 'block';
                isValid = false;
            }
            
            // Validate email
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email || !emailRegex.test(email)) {
                document.getElementById('emailError').style.display = 'block';
                isValid = false;
            }
            
            // If form is valid, show success message
            if (isValid) {
                document.getElementById('contestForm').style.display = 'none';
                document.getElementById('successMessage').style.display = 'block';
                
                // In a real application, you would send the data to a server here
                // For example:
                // const formData = { firstName, lastName, email };
                // fetch('/api/contest-entry', {
                //     method: 'POST',
                //     headers: { 'Content-Type': 'application/json' },
                //     body: JSON.stringify(formData)
                // })
                // .then(response => response.json())
                // .then(data => console.log('Success:', data))
                // .catch(error => console.error('Error:', error));
            }
        });
    </script>
</body>
</html>
```
