"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Create an HTML form with a math-based CAPTCHA system that ensures users verify they are not bots before submitting data.
Generated: DETERMINISTIC_d111a9b792a1285f
Batch ID: 20250612_151752
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

    <h1>Contact Form</h1>
    <form id="contactForm" onsubmit="return validateForm(event)">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <div id="captchaContainer">
            <p id="captchaQuestion"></p>
            <input type="number" id="captchaAnswer" name="captchaAnswer" required placeholder="Your answer">
        </div>
        
        <button type="submit">Submit</button>
        <p class="error" id="errorMessage"></p>
    </form>

    <script>
        // Function to generate a random math question for the CAPTCHA
        function generateCaptcha() {
            const num1 = Math.floor(Math.random() * 10);
            const num2 = Math.floor(Math.random() * 10);
            document.getElementById('captchaQuestion').innerText = `What is ${num1} + ${num2}?`;
            return num1 + num2; // Return the correct answer
        }

        // Store the correct answer in a variable
        let correctAnswer = generateCaptcha();

        // Form validation function
        function validateForm(event) {
            event.preventDefault(); // Prevent form submission for validation
            
            const userAnswer = parseInt(document.getElementById('captchaAnswer').value);
            const errorMessage = document.getElementById('errorMessage');

            // Check if the user's answer matches the correct answer
            if (userAnswer !== correctAnswer) {
                errorMessage.innerText = "Incorrect answer. Please try again.";
                correctAnswer = generateCaptcha(); // Regenerate CAPTCHA
            } else {
                errorMessage.innerText = ""; // Clear error message
                alert("Form submitted successfully!"); // Simulate successful submission
                document.getElementById('contactForm').reset(); // Reset form fields
                correctAnswer = generateCaptcha(); // Regenerate CAPTCHA for next use
            }
        }
    </script>
</body>
</html>
```
