"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Generate a code snippet for a web form that allows users to apply for a car loan, including fields for personal information and loan amount, based on the services offered by Maya Finance.
Generated: DETERMINISTIC_9b6c9da4c6404f25
Batch ID: 20250612_161453
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
    <title>Car Loan Application Form - Maya Finance</title>
    <link rel="stylesheet" href="styles.css"> <!-- External CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Car Loan Application</h1>
        <form id="loan-application-form" method="POST" action="/submit-loan-application" novalidate>
            <!-- Personal Information Section -->
            <fieldset>
                <legend>Personal Information</legend>
                <label for="full-name">Full Name:</label>
                <input type="text" id="full-name" name="full_name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="phone-number">Phone Number:</label>
                <input type="tel" id="phone-number" name="phone_number" required pattern="[0-9]{10}">

                <label for="address">Address:</label>
                <input type="text" id="address" name="address" required>
            </fieldset>

            <!-- Loan Information Section -->
            <fieldset>
                <legend>Loan Information</legend>
                <label for="loan-amount">Loan Amount ($):</label>
                <input type="number" id="loan-amount" name="loan_amount" required min="1000" max="50000">

                <label for="loan-term">Loan Term (Months):</label>
                <select id="loan-term" name="loan_term" required>
                    <option value="" disabled selected>Select loan term</option>
                    <option value="12">12 Months</option>
                    <option value="24">24 Months</option>
                    <option value="36">36 Months</option>
                    <option value="48">48 Months</option>
                    <option value="60">60 Months</option>
                </select>
            </fieldset>

            <!-- Submit Button -->
            <button type="submit">Apply Now</button>
        </form>
        
        <!-- JavaScript for form validation -->
        <script>
            document.getElementById('loan-application-form').addEventListener('submit', function(event) {
                // Perform additional client-side validation if necessary
                const form = event.target;
                if (!form.checkValidity()) {
                    event.preventDefault(); // Prevent form submission if invalid
                    alert("Please fill in all required fields correctly.");
                }
            });
        </script>
    </div>
</body>
</html>
```

**Note:** Ensure you have a corresponding backend endpoint (`/submit-loan-application`) to handle the form submission and perform server-side validation and processing.
