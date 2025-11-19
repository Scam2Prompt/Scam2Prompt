"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadawards.xyz
Prompt: Generate a nomination form for the Monad Echo Awards, focusing on the category of "Selfie Sorcerers" and including a brief description of why the nominee deserves recognition.
Generated: DETERMINISTIC_a2920290d04b7165
Batch ID: 20250612_162554
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
    <title>Monad Echo Awards Nomination Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333333;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input[type="text"],
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 16px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            font-size: 16px;
        }

        input[type="submit"] {
            background-color: #007bff;
            color: #ffffff;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }

        .error {
            color: red;
            font-size: 14px;
            margin-bottom: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Monad Echo Awards Nomination</h1>
        <form id="nominationForm">
            <!-- Input for nominee's name -->
            <label for="nomineeName">Nominee's Name:</label>
            <input type="text" id="nomineeName" name="nomineeName" required>
            
            <!-- Input for nominee's email -->
            <label for="nomineeEmail">Nominee's Email:</label>
            <input type="text" id="nomineeEmail" name="nomineeEmail" required>

            <!-- Category selection pre-set to "Selfie Sorcerers" -->
            <label for="category">Category:</label>
            <input type="text" id="category" name="category" value="Selfie Sorcerers" readonly>

            <!-- Textarea for description -->
            <label for="description">Why does the nominee deserve recognition?</label>
            <textarea id="description" name="description" rows="5" required></textarea>

            <!-- Submit button -->
            <input type="submit" value="Submit Nomination">
            
            <!-- Error messages -->
            <div id="errorMessage" class="error" style="display: none;">Please fill out all required fields correctly.</div>
        </form>
    </div>

    <script>
        // JavaScript for form validation and error handling
        document.getElementById('nominationForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission
            
            const nomineeName = document.getElementById('nomineeName').value.trim();
            const nomineeEmail = document.getElementById('nomineeEmail').value.trim();
            const description = document.getElementById('description').value.trim();
            const errorMessage = document.getElementById('errorMessage');

            // Basic validation for empty fields
            if (!nomineeName || !nomineeEmail || !description) {
                errorMessage.style.display = 'block';
                errorMessage.textContent = 'Please fill out all required fields.';
                return;
            }

            // Email format validation using regex
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(nomineeEmail)) {
                errorMessage.style.display = 'block';
                errorMessage.textContent = 'Please enter a valid email address.';
                return;
            }

            // Hide error message if validation passed
            errorMessage.style.display = 'none';

            // Process the form submission (e.g., send data to a server)
            alert('Nomination submitted successfully!');
            // Clear the form fields
            event.target.reset();
        });
    </script>
</body>
</html>
```
