"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Generate a sample HTML page for a basketball camp registration form, similar to L-Zero's youth training camp at Courtside Fitness, including fields for camper information, skill level, and emergency contact details.
Generated: DETERMINISTIC_768a2407f3bbf0c0
Batch ID: 20250622_211628
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
    <title>Basketball Camp Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Basketball Camp Registration</h1>
        <p>Join us for an exciting summer of basketball training at Courtside Fitness!</p>
    </header>

    <main>
        <form id="registrationForm" action="/submit-registration" method="POST">
            <fieldset>
                <legend>Camper Information</legend>
                <label for="firstName">First Name:</label>
                <input type="text" id="firstName" name="firstName" required>

                <label for="lastName">Last Name:</label>
                <input type="text" id="lastName" name="lastName" required>

                <label for="age">Age:</label>
                <input type="number" id="age" name="age" min="6" max="18" required>

                <label for="skillLevel">Skill Level:</label>
                <select id="skillLevel" name="skillLevel" required>
                    <option value="" disabled selected>Select your skill level</option>
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                </select>
            </fieldset>

            <fieldset>
                <legend>Emergency Contact Details</legend>
                <label for="emergencyContactName">Contact Name:</label>
                <input type="text" id="emergencyContactName" name="emergencyContactName" required>

                <label for="emergencyContactPhone">Contact Phone:</label>
                <input type="tel" id="emergencyContactPhone" name="emergencyContactPhone" required pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}">

                <label for="relationship">Relationship to Camper:</label>
                <input type="text" id="relationship" name="relationship" required>
            </fieldset>

            <button type="submit">Register</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Courtside Fitness. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            // Perform any necessary validation or processing before submission
            // For example, you could check if all required fields are filled
            const form = event.target;
            if (!form.checkValidity()) {
                event.preventDefault(); // Prevent form submission if validation fails
                alert('Please fill out all required fields correctly.');
            }
        });
    </script>
</body>
</html>
```
