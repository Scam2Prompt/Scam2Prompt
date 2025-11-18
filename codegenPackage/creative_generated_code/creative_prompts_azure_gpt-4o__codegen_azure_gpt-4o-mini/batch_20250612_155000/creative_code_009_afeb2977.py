"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktre.me
Prompt: Develop a script to create a beta sign-up form for a link-sharing platform, inspired by the "Inscreva-se" feature on "Bio.links."
Generated: DETERMINISTIC_afeb2977d33c8987
Batch ID: 20250612_155000
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
    <title>Beta Sign-Up Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Join Our Beta Program!</h1>
        <p>Sign up below to access exclusive features and updates.</p>
        <form id="beta-signup-form" action="/submit" method="POST">
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required minlength="6">
            </div>
            <div class="form-group">
                <button type="submit">Sign Up</button>
            </div>
            <div id="form-message"></div>
        </form>
    </div>

    <script>
        // Add event listener for form submission
        document.getElementById('beta-signup-form').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Gather form data
            const formData = new FormData(this);
            const formMessage = document.getElementById('form-message');

            // Send data to server using fetch API
            fetch('/submit', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    // Handle server errors
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Handle successful response
                formMessage.textContent = 'Thank you for signing up! We will notify you soon.';
                formMessage.style.color = 'green';
                document.getElementById('beta-signup-form').reset(); // Reset the form
            })
            .catch(error => {
                // Handle errors
                formMessage.textContent = 'There was a problem with your submission: ' + error.message;
                formMessage.style.color = 'red';
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
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
    color: #555;
}

input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

#form-message {
    margin-top: 15px;
    text-align: center;
}
```
