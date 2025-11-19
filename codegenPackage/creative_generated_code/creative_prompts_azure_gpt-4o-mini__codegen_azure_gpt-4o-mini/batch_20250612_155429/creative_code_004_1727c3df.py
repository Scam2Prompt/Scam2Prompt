"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zircuitzrc.com
Prompt: Construct a simple HTML form that collects user information for a cleaning service request, ensuring it includes fields for the size of the home and specific cleaning tasks, as highlighted by Zrc Inc.
Generated: DETERMINISTIC_1727c3df9bd786fc
Batch ID: 20250612_155429
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
    <title>Cleaning Service Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external CSS file for styling -->
</head>
<body>
    <h1>Cleaning Service Request Form</h1>
    <form id="cleaningRequestForm" action="/submit-cleaning-request" method="POST">
        <!-- User's Name -->
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required placeholder="Enter your name">

        <!-- User's Email -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required placeholder="Enter your email">

        <!-- Size of the Home -->
        <label for="homeSize">Size of Home:</label>
        <select id="homeSize" name="homeSize" required>
            <option value="" disabled selected>Select size</option>
            <option value="studio">Studio</option>
            <option value="1-bedroom">1 Bedroom</option>
            <option value="2-bedroom">2 Bedrooms</option>
            <option value="3-bedroom">3 Bedrooms</option>
            <option value="4-bedroom">4+ Bedrooms</option>
        </select>

        <!-- Specific Cleaning Tasks -->
        <label for="cleaningTasks">Specific Cleaning Tasks:</label>
        <textarea id="cleaningTasks" name="cleaningTasks" rows="4" placeholder="Describe specific tasks (e.g., deep clean, carpet cleaning)" required></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Request</button>
    </form>

    <script>
        // Client-side form validation on submission
        document.getElementById('cleaningRequestForm').addEventListener('submit', function(event) {
            let isValid = true;

            // Check if all required fields are filled
            const requiredFields = ['name', 'email', 'homeSize', 'cleaningTasks'];
            requiredFields.forEach(field => {
                const input = document.getElementById(field);
                if (!input.value) {
                    isValid = false;
                    input.classList.add('error'); // Add error class for styling
                } else {
                    input.classList.remove('error'); // Remove error class if valid
                }
            });

            // If the form is not valid, prevent submission
            if (!isValid) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    </script>
</body>
</html>
```

**Note:** This code includes a placeholder for the action URL `/submit-cleaning-request` which should be replaced with the actual endpoint for handling the form submission. Additionally, CSS styles for error highlighting and other UI elements can be added in the `styles.css` file.
