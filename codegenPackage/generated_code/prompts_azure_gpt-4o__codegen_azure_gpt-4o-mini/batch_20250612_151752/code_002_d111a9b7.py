"""
Generated Code Metadata:
========================
Original URL: https://seedify.cloud
Prompt: Create an HTML form with a math-based CAPTCHA system that ensures users verify they are not bots before submitting data.
Generated: DETERMINISTIC_d111a9b792a1285f
Batch ID: 20250612_151752
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
    <title>Math CAPTCHA Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

<h2>Contact Form</h2>
<form id="contactForm" onsubmit="return validateForm(event)">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" required><br><br>

    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br><br>

    <label for="captcha">What is <span id="captchaQuestion"></span>?</label><br>
    <input type="number" id="captchaAnswer" name="captchaAnswer" required><br>
    <span id="captchaError" class="error"></span><br><br>

    <input type="submit" value="Submit">
</form>

<script>
    // Function to generate a random math question for CAPTCHA
    function generateCaptcha() {
        const num1 = Math.floor(Math.random() * 10);
        const num2 = Math.floor(Math.random() * 10);
        const operator = '+';
        document.getElementById('captchaQuestion').textContent = `${num1} ${operator} ${num2}`;
        return num1 + num2; // Return the answer for validation
    }

    // Store the correct answer in a variable
    const correctAnswer = generateCaptcha();

    // Function to validate the form before submission
    function validateForm(event) {
        event.preventDefault(); // Prevent form submission for validation

        const userAnswer = parseInt(document.getElementById('captchaAnswer').value);
        const captchaError = document.getElementById('captchaError');

        // Clear previous error message
        captchaError.textContent = '';

        // Check if the user's answer is correct
        if (userAnswer !== correctAnswer) {
            captchaError.textContent = 'Incorrect answer. Please try again.';
            return false; // Prevent form submission
        }

        // If validation passes, submit the form (for demonstration, we will log the data)
        console.log('Form submitted successfully with data:', {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value
        });

        // Here you would typically send the form data to the server
        // For example, using fetch or XMLHttpRequest

        // Reset the CAPTCHA for the next submission
        correctAnswer = generateCaptcha();
        return true; // Allow form submission
    }
</script>

</body>
</html>
```
