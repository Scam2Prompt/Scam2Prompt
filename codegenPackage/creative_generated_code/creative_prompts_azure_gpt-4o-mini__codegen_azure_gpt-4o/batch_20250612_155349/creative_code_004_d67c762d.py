"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnasecure.com
Prompt: Illustrate how to implement a user registration form in HTML for potential POSP agents on ApnaSecure, including fields for name, age, and contact information.
Generated: DETERMINISTIC_d67c762df19fe9c3
Batch ID: 20250612_155349
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
    <title>POSP Agent Registration - ApnaSecure</title>
    <!-- External CSS for styling -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>POSP Agent Registration</h1>
        <p>Please fill out the form below to register as a POSP agent.</p>
        <form id="registrationForm" action="submit_registration.php" method="POST">
            <!-- Full Name -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required maxlength="100" placeholder="Enter your full name">
            
            <!-- Age -->
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required min="18" max="65" placeholder="Enter your age">
            
            <!-- Contact Information -->
            <label for="contact">Contact Information:</label>
            <input type="tel" id="contact" name="contact" required pattern="[0-9]{10}" maxlength="10" placeholder="Enter your 10-digit phone number">
            
            <!-- Submit Button -->
            <button type="submit">Register</button>
        </form>
    </div>
    <!-- Inline JavaScript for basic form validation -->
    <script>
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            // Basic validation for numeric fields
            const age = document.getElementById('age').value;
            const contact = document.getElementById('contact').value;

            if (age < 18 || age > 65) {
                alert('Age must be between 18 and 65.');
                event.preventDefault();
                return;
            }

            if (!/^\d{10}$/.test(contact)) {
                alert('Contact number must be a 10-digit number.');
                event.preventDefault();
                return;
            }

            // Form is valid, proceed with submission
            alert('Thank you for registering!');
        });
    </script>
</body>
</html>
```
