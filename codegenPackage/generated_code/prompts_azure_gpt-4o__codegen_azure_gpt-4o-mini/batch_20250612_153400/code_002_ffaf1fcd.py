"""
Generated Code Metadata:
========================
Original URL: https://presales-friend.pages.dev
Prompt: Develop a registration form for a PWA, ensuring that users who register within a specified timeframe (e.g., 48 hours) are flagged for inclusion in a special event or feature.
Generated: DETERMINISTIC_ffaf1fcd343e05b6
Batch ID: 20250612_153400
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
    <title>Registration Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Registration Form</h1>
        <form id="registrationForm">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <button type="submit">Register</button>
        </form>
        <div id="message"></div>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('registrationForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Get the current timestamp
            const registrationTime = new Date().getTime();

            // Create a user object
            const user = {
                username,
                email,
                password,
                registrationTime
            };

            try {
                // Simulate sending data to a server
                const response = await fetch('/api/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(user)
                });

                // Check for server response
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const result = await response.json();

                // Check if the user registered within the last 48 hours
                const currentTime = new Date().getTime();
                const timeDifference = currentTime - registrationTime;
                const isEligibleForEvent = timeDifference <= 48 * 60 * 60 * 1000; // 48 hours in milliseconds

                // Display success message
                document.getElementById('message').innerText = result.message;

                if (isEligibleForEvent) {
                    document.getElementById('message').innerText += ' You are eligible for the special event!';
                }
            } catch (error) {
                // Handle errors gracefully
                console.error('Error during registration:', error);
                document.getElementById('message').innerText = 'Registration failed. Please try again later.';
            }
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 400px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
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

#message {
    margin-top: 15px;
    text-align: center;
    color: red;
}
```
