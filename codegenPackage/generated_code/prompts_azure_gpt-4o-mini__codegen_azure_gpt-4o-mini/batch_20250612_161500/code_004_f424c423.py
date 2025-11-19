"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: Write a code example for a web form that collects customer details for printing services, ensuring it includes fields for items like brochures and roll-ups, as mentioned on Detalj Reklam's site.
Generated: DETERMINISTIC_f424c423a115bff5
Batch ID: 20250612_161500
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
    <title>Customer Details Form for Printing Services</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Customer Details for Printing Services</h1>
    <form id="printingForm" action="/submit" method="POST">
        <!-- Customer Information Section -->
        <fieldset>
            <legend>Customer Information</legend>
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>
        </fieldset>

        <!-- Printing Services Section -->
        <fieldset>
            <legend>Printing Services</legend>
            <label for="brochures">Brochures:</label>
            <input type="number" id="brochures" name="brochures" min="0" value="0">
            
            <label for="rollUps">Roll-Ups:</label>
            <input type="number" id="rollUps" name="rollUps" min="0" value="0">
            
            <label for="businessCards">Business Cards:</label>
            <input type="number" id="businessCards" name="businessCards" min="0" value="0">
        </fieldset>

        <!-- Additional Comments Section -->
        <fieldset>
            <legend>Additional Comments</legend>
            <textarea id="comments" name="comments" rows="4" cols="50" placeholder="Any additional requests or comments..."></textarea>
        </fieldset>

        <!-- Submit Button -->
        <button type="submit">Submit</button>
    </form>

    <script>
        // Form submission handler
        document.getElementById('printingForm').addEventListener('submit', function(event) {
            // Validate form data before submission
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();

            if (!name || !email || !phone) {
                alert('Please fill in all required fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
