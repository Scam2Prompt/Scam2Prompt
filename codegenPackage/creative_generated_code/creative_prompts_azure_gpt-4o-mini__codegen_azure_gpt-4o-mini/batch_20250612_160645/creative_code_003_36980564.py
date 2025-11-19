"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-pandorabuild.pages.dev
Prompt: Generate a registration form in HTML for users to sign up for updates from Pandora Labs.
Generated: DETERMINISTIC_3698056412767757
Batch ID: 20250612_160645
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
    <title>Registration Form - Pandora Labs</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external stylesheet -->
</head>
<body>
    <div class="container">
        <h1>Sign Up for Updates from Pandora Labs</h1>
        <form id="registrationForm" action="/submit" method="POST">
            <label for="firstName">First Name:</label>
            <input type="text" id="firstName" name="firstName" required>
            
            <label for="lastName">Last Name:</label>
            <input type="text" id="lastName" name="lastName" required>
            
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required minlength="8">

            <label for="confirmPassword">Confirm Password:</label>
            <input type="password" id="confirmPassword" name="confirmPassword" required minlength="8">
            
            <button type="submit">Register</button>
        </form>
        
        <p id="successMessage" style="display:none; color: green;">Registration successful! Check your email for updates.</p>
        <p id="errorMessage" style="display:none; color: red;">An error occurred. Please try again later.</p>
    </div>

    <script>
        // Handle form submission
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Validate password match
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            if (password !== confirmPassword) {
                alert('Passwords do not match. Please try again.');
                return;
            }

            // Simulate form submission (replace with actual AJAX call or form submission)
            const formData = new FormData(this);

            // Example AJAX request
            fetch('/submit', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Show success message
                document.getElementById('successMessage').style.display = 'block';
                this.reset(); // Reset form fields
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                document.getElementById('errorMessage').style.display = 'block';
            });
        });
    </script>
</body>
</html>
```
