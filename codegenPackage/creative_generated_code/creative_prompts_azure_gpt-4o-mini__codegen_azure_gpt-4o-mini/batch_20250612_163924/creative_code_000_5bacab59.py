"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oberbank-ag.myfreesites.net
Prompt: Generate a code snippet for a web form that collects user addresses for prize winners, ensuring it includes age verification and validation features.
Generated: DETERMINISTIC_5bacab59f1780f1f
Batch ID: 20250612_163924
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
    <title>Prize Winners Address Collection</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
        }
        input, select {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            margin: 5px 0;
        }
    </style>
</head>
<body>

    <h2>Prize Winner Address Collection</h2>
    <form id="winnerForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required placeholder="Enter your name">

        <label for="age">Age:</label>
        <input type="number" id="age" name="age" min="1" required placeholder="Enter your age">

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required placeholder="Enter your address">

        <label for="city">City:</label>
        <input type="text" id="city" name="city" required placeholder="Enter your city">

        <label for="state">State:</label>
        <input type="text" id="state" name="state" required placeholder="Enter your state">

        <label for="zip">ZIP Code:</label>
        <input type="text" id="zip" name="zip" required pattern="\d{5}" placeholder="Enter your ZIP code (5 digits)">

        <button type="submit">Submit</button>

        <div id="errorContainer" class="error" style="display:none;"></div>
    </form>

    <script>
        document.getElementById('winnerForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Clear previous error messages
            const errorContainer = document.getElementById('errorContainer');
            errorContainer.innerHTML = '';
            errorContainer.style.display = 'none';

            // Get form values
            const name = document.getElementById('name').value.trim();
            const age = parseInt(document.getElementById('age').value.trim(), 10);
            const address = document.getElementById('address').value.trim();
            const city = document.getElementById('city').value.trim();
            const state = document.getElementById('state').value.trim();
            const zip = document.getElementById('zip').value.trim();

            // Validate age (must be 18 or older)
            if (age < 18) {
                errorContainer.innerHTML += 'You must be at least 18 years old.<br>';
                errorContainer.style.display = 'block';
                return; // Exit if validation fails
            }

            // Validate ZIP Code format (5 digits)
            const zipPattern = /^\d{5}$/;
            if (!zipPattern.test(zip)) {
                errorContainer.innerHTML += 'ZIP code must be 5 digits.<br>';
                errorContainer.style.display = 'block';
                return; // Exit if validation fails
            }

            // If all validations pass, simulate form submission
            console.log('Form submitted successfully:', {
                name,
                age,
                address,
                city,
                state,
                zip
            });

            // Optionally clear the form or redirect
            // this.reset();
            // window.location.href = 'success.html';
        });
    </script>
</body>
</html>
```
