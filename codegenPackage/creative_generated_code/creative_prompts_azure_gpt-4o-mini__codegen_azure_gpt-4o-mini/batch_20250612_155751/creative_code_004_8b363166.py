"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecbc.online
Prompt: Design a simple HTML form for users to donate to ECBC Radio, ensuring it captures their name and email as mentioned on the website.
Generated: DETERMINISTIC_8b3631665bc94d3a
Batch ID: 20250612_155751
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
    <title>ECBC Radio Donation Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file for styling -->
</head>
<body>
    <header>
        <h1>Support ECBC Radio</h1>
        <p>Your contribution helps us continue to provide quality programming.</p>
    </header>

    <main>
        <form id="donationForm" action="/submit-donation" method="POST">
            <!-- Input for the user's name -->
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your name">

            <!-- Input for the user's email -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">

            <!-- Submit button for the form -->
            <button type="submit">Donate</button>
        </form>
    </main>

    <footer>
        <p>Thank you for supporting ECBC Radio!</p>
    </footer>

    <script>
        // Client-side validation to ensure form data is valid before submission
        document.getElementById('donationForm').addEventListener('submit', function(event) {
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');

            // Check if name is empty
            if (nameInput.value.trim() === '') {
                alert('Please enter your name.');
                event.preventDefault(); // Prevent form submission
                return;
            }

            // Check if email is valid
            if (!validateEmail(emailInput.value)) {
                alert('Please enter a valid email address.');
                event.preventDefault(); // Prevent form submission
                return;
            }
        });

        // Function to validate email format
        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex
            return re.test(String(email).toLowerCase());
        }
    </script>
</body>
</html>
```
