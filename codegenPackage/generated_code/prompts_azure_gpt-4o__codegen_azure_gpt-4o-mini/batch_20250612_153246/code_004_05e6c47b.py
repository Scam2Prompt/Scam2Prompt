"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Develop an HTML form for dealers to sign up for the Sundance Spas Retail Advantage program, including fields for first name, last name, company name, zip code, country, and email.
Generated: DETERMINISTIC_05e6c47b01deaa28
Batch ID: 20250612_153246
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
    <title>Sundance Spas Retail Advantage Program Sign Up</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Sundance Spas Retail Advantage Program Sign Up</h1>
    <form id="dealerSignUpForm" action="/submit" method="POST" novalidate>
        <!-- First Name Field -->
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" name="firstName" required>
        
        <!-- Last Name Field -->
        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" name="lastName" required>
        
        <!-- Company Name Field -->
        <label for="companyName">Company Name:</label>
        <input type="text" id="companyName" name="companyName" required>
        
        <!-- Zip Code Field -->
        <label for="zipCode">Zip Code:</label>
        <input type="text" id="zipCode" name="zipCode" required pattern="\d{5}">
        
        <!-- Country Field -->
        <label for="country">Country:</label>
        <select id="country" name="country" required>
            <option value="" disabled selected>Select your country</option>
            <option value="USA">USA</option>
            <option value="Canada">Canada</option>
            <option value="Other">Other</option>
        </select>
        
        <!-- Email Field -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <!-- Submit Button -->
        <button type="submit">Sign Up</button>
    </form>

    <script>
        // Form submission handler
        document.getElementById('dealerSignUpForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Validate form fields
            if (this.checkValidity()) {
                // If valid, submit the form data
                const formData = new FormData(this);
                fetch(this.action, {
                    method: this.method,
                    body: formData,
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Handle success (e.g., show a success message)
                    alert('Sign up successful! Thank you for joining the Sundance Spas Retail Advantage program.');
                })
                .catch(error => {
                    // Handle errors (e.g., show an error message)
                    console.error('There was a problem with the fetch operation:', error);
                    alert('There was an error during sign up. Please try again later.');
                });
            } else {
                // If invalid, show validation errors
                alert('Please fill out all required fields correctly.');
            }
        });
    </script>
</body>
</html>
```
