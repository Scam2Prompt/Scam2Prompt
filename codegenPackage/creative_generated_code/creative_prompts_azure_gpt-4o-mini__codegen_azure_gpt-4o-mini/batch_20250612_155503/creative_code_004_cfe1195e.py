"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thresholdsummer.org
Prompt: Design a simple HTML form for collecting attendee information for the 2025 Threshold Summer Meeting, ensuring it includes fields for contact details and payment preferences.
Generated: DETERMINISTIC_cfe1195ecefdd43a
Batch ID: 20250612_155503
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
    <title>Threshold Summer Meeting 2025 Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>2025 Threshold Summer Meeting Registration</h1>
    <form id="registrationForm" action="/submit" method="POST"> <!-- Form submission action -->
        <!-- Attendee Contact Information Section -->
        <fieldset>
            <legend>Contact Information</legend>

            <label for="firstName">First Name:</label>
            <input type="text" id="firstName" name="firstName" required>

            <label for="lastName">Last Name:</label>
            <input type="text" id="lastName" name="lastName" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required>
        </fieldset>

        <!-- Payment Preferences Section -->
        <fieldset>
            <legend>Payment Preferences</legend>

            <label for="paymentMethod">Payment Method:</label>
            <select id="paymentMethod" name="paymentMethod" required>
                <option value="">Select a payment method</option>
                <option value="creditCard">Credit Card</option>
                <option value="paypal">PayPal</option>
                <option value="bankTransfer">Bank Transfer</option>
            </select>

            <label for="amount">Amount to Pay:</label>
            <input type="number" id="amount" name="amount" min="0" required>

            <label for="comments">Additional Comments:</label>
            <textarea id="comments" name="comments" rows="4"></textarea>
        </fieldset>

        <!-- Submit Button -->
        <button type="submit">Register</button>
    </form>

    <script>
        // Form submission event handling
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            // Perform basic validation
            const email = document.getElementById('email').value;
            if (!validateEmail(email)) {
                alert('Please enter a valid email address.');
                event.preventDefault(); // Prevent form submission
            }
        });

        // Email validation function
        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple regex for email validation
            return re.test(String(email).toLowerCase());
        }
    </script>
</body>
</html>
```
