"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Generate a code snippet for a web form that allows users to request a consultation with a personal injury law firm, including fields for name, contact information, and type of accident (e.g., car, motorcycle, pedestrian).
Generated: DETERMINISTIC_effa119fb6c093f9
Batch ID: 20250612_163423
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
    <title>Consultation Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to a CSS file for styling -->
</head>
<body>
    <h1>Request a Consultation</h1>
    <form id="consultationForm" action="/submit-consultation" method="POST">
        <!-- Name Field -->
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required placeholder="John Doe">
        
        <!-- Email Field -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required placeholder="johndoe@example.com">
        
        <!-- Phone Number Field -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required placeholder="(555) 555-5555">

        <!-- Type of Accident Selection -->
        <label for="accidentType">Type of Accident:</label>
        <select id="accidentType" name="accidentType" required>
            <option value="">Select an accident type</option>
            <option value="car">Car Accident</option>
            <option value="motorcycle">Motorcycle Accident</option>
            <option value="pedestrian">Pedestrian Accident</option>
            <option value="other">Other</option>
        </select>

        <!-- Error Message Display -->
        <div id="error-message" style="color:red;display:none;"></div>

        <!-- Submit Button -->
        <button type="submit">Request Consultation</button>
    </form>

    <script>
        // Form submission event listener
        document.getElementById('consultationForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Simple client-side validation
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const accidentType = document.getElementById('accidentType').value;

            // Check for empty fields
            if (!name || !email || !phone || !accidentType) {
                document.getElementById('error-message').innerText = 'Please fill in all fields.';
                document.getElementById('error-message').style.display = 'block';
                return;
            }

            // Form is valid, proceed with submission
            this.submit();
        });
    </script>
</body>
</html>
```
