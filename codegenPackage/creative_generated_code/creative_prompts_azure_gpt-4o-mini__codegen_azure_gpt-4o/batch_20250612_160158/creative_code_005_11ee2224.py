"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitfxt.com
Prompt: Develop a simple HTML form for user registration on Profitfxt Limited, ensuring it meets their security standards.
Generated: DETERMINISTIC_11ee2224a5844e2c
Batch ID: 20250612_160158
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
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>User Registration - Profitfxt Limited</title>
    <link rel="stylesheet" href="styles.css">
    <script src="scripts.js" defer></script>
</head>

<body>
    <main>
        <section>
            <h1>User Registration - Profitfxt Limited</h1>
            <form id="registrationForm" action="/register" method="POST">
                <!-- Full Name -->
                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="fullName" required minlength="2" maxlength="100"
                    pattern="[a-zA-Z\s]+" title="Only letters and spaces are allowed.">

                <!-- Email Address -->
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required maxlength="100">

                <!-- Password -->
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required minlength="8"
                    title="Password must be at least 8 characters long.">

                <!-- Confirm Password -->
                <label for="confirmPassword">Confirm Password:</label>
                <input type="password" id="confirmPassword" name="confirmPassword" required minlength="8"
                    title="Password must be at least 8 characters long.">

                <!-- Submit Button -->
                <button type="submit">Register</button>
            </form>
        </section>
    </main>

    <script>
        /**
         * Validate form before submission
         */
        document.getElementById('registrationForm').addEventListener('submit', function (event) {
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            // Check if passwords match
            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>

</html>
```
