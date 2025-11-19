"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viafuar.com
Prompt: Generate a code snippet to create an event registration form for the Tuzla Boat Show, including fields for name, email, and boat type.
Generated: DETERMINISTIC_906522c74a59e8d6
Batch ID: 20250612_161700
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
    <title>Tuzla Boat Show Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Tuzla Boat Show Registration</h1>
    <form id="registrationForm" action="submit_registration.php" method="POST">
        <!-- Name input field -->
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required placeholder="Enter your name">

        <!-- Email input field -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required placeholder="Enter your email">

        <!-- Boat type selection -->
        <label for="boatType">Boat Type:</label>
        <select id="boatType" name="boatType" required>
            <option value="">Select a boat type</option>
            <option value="sailboat">Sailboat</option>
            <option value="motorboat">Motorboat</option>
            <option value="yacht">Yacht</option>
            <option value="other">Other</option>
        </select>

        <!-- Submit button -->
        <button type="submit">Register</button>
    </form>

    <script>
        // Add event listener for form submission
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            // Perform client-side validation if needed
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const boatType = document.getElementById('boatType').value;

            // Check if any fields are empty (additional client-side validation)
            if (!name || !email || !boatType) {
                alert('Please fill in all fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
