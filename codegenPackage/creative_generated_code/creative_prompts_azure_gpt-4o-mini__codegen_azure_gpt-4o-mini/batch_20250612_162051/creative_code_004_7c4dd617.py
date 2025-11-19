"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Design a simple HTML form that collects user information for a digital course on architecture and interior design offered by Nyiku Design.
Generated: DETERMINISTIC_7c4dd61781cbf8d6
Batch ID: 20250612_162051
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
    <title>Nyiku Design Course Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Nyiku Design: Architecture and Interior Design Course</h1>
    </header>

    <main>
        <form id="registrationForm" action="/submit" method="POST">
            <fieldset>
                <legend>User Information</legend>

                <label for="firstName">First Name:</label>
                <input type="text" id="firstName" name="firstName" required>

                <label for="lastName">Last Name:</label>
                <input type="text" id="lastName" name="lastName" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}" title="Must be 10 digits">

                <label for="experienceLevel">Experience Level:</label>
                <select id="experienceLevel" name="experienceLevel" required>
                    <option value="" disabled selected>Select your experience level</option>
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                </select>

                <label for="comments">Additional Comments:</label>
                <textarea id="comments" name="comments" rows="4" cols="50" placeholder="Any other information..."></textarea>

                <input type="submit" value="Register">
            </fieldset>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Nyiku Design. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handling
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            // Perform any necessary validation or processing before submission
            // This could include additional client-side validation if needed
            console.log('Form submitted!');
        });
    </script>
</body>
</html>
```
