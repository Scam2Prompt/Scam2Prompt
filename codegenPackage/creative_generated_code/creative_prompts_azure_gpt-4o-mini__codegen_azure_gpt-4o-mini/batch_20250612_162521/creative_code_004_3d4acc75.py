"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acknowledgment.netlify.app
Prompt: How can I create a reset button for a contact form that clears all input fields effectively?
Generated: DETERMINISTIC_3d4acc75c1e9b32f
Batch ID: 20250612_162521
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
    <title>Contact Form with Reset Button</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        label {
            margin-bottom: 5px;
            display: block;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"],
        input[type="reset"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="reset"] {
            background-color: #f44336; /* Red color for reset button */
        }
        input[type="submit"]:hover,
        input[type="reset"]:hover {
            opacity: 0.8;
        }
    </style>
</head>
<body>

    <h2>Contact Us</h2>
    <form id="contactForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="4" required></textarea>

        <input type="submit" value="Submit">
        <input type="reset" value="Reset" id="resetButton">
    </form>

    <script>
        // Attach an event listener to the reset button
        document.getElementById('resetButton').addEventListener('click', function (event) {
            // Confirm reset action with the user
            if (!confirm('Are you sure you want to clear all fields?')) {
                // Prevent the default reset action if the user cancels
                event.preventDefault();
            }
        });

        // Optional: Prevent form submission for demonstration purposes
        document.getElementById('contactForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission
            alert('Form submitted!'); // Placeholder for form submission logic
        });
    </script>

</body>
</html>
```
