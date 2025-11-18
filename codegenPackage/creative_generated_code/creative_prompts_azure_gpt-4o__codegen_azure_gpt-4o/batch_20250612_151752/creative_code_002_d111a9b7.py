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
  <title>Form with CAPTCHA</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 400px;
      margin: auto;
    }
    .error {
      color: red;
    }
  </style>
</head>
<body>
  <h1>Form with Math CAPTCHA</h1>
  <form id="captchaForm">
    <!-- Text input field -->
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <br><br>
    
    <!-- CAPTCHA question -->
    <label id="captchaQuestion"></label>
    <input type="number" id="captchaAnswer" name="captchaAnswer" required>
    <br><br>
    
    <button type="submit">Submit</button>
    <p class="error" id="errorMessage"></p>
  </form>

  <script>
    // Function to generate a random integer between min and max
    function getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    // Generate CAPTCHA question and store the answer
    const num1 = getRandomInt(1, 10); // First random number
    const num2 = getRandomInt(1, 10); // Second random number
    const correctAnswer = num1 + num2; // Correct answer

    // Populate the CAPTCHA question on the form
    const captchaQuestion = document.getElementById('captchaQuestion');
    captchaQuestion.textContent = `What is ${num1} + ${num2}?`;

    // Add event listener for form submission
    const form = document.getElementById('captchaForm');
    const errorMessage = document.getElementById('errorMessage');

    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission
      
      // Get the user's answer
      const userAnswer = parseInt(document.getElementById('captchaAnswer').value, 10);

      // Validate the CAPTCHA answer
      if (userAnswer === correctAnswer) {
        alert('CAPTCHA solved successfully! Form submitted.');
        form.reset(); // Reset the form
        errorMessage.textContent = ''; // Clear error message
      } else {
        errorMessage.textContent = 'Incorrect CAPTCHA. Please try again.';
      }
    });
  </script>
</body>
</html>
```
