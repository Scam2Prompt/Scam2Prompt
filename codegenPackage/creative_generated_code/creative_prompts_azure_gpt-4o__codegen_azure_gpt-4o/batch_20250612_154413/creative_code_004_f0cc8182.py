"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.seedify.cloud
Prompt: Write JavaScript code to create a CAPTCHA system that asks users to solve math problems before submitting a form, similar to the verification process on seedify.cloud.
Generated: DETERMINISTIC_f0cc8182f6ef3289
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CAPTCHA System: Math problem verification for a form submission

// Generate a random integer within a specified range
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Generate a random math problem for CAPTCHA
function generateCaptcha() {
    const num1 = getRandomInt(1, 20); // Random number between 1 and 20
    const num2 = getRandomInt(1, 20); // Random number between 1 and 20
    const operator = ['+', '-', '*'][getRandomInt(0, 2)]; // Random operator (+, -, *)

    // Compute the correct answer based on the selected operator
    let correctAnswer;
    switch (operator) {
        case '+':
            correctAnswer = num1 + num2;
            break;
        case '-':
            correctAnswer = num1 - num2;
            break;
        case '*':
            correctAnswer = num1 * num2;
            break;
    }

    return {
        question: `${num1} ${operator} ${num2}`, // Math problem as a string
        answer: correctAnswer                      // Correct answer for verification
    };
}

// Setup CAPTCHA on the form
function setupCaptcha() {
    const captcha = generateCaptcha(); // Generate a new CAPTCHA
    const form = document.getElementById('myForm'); // Form element
    const captchaContainer = document.getElementById('captchaContainer'); // CAPTCHA container
    const captchaInput = document.getElementById('captchaInput'); // Input field for CAPTCHA answer

    // Display the CAPTCHA question
    captchaContainer.textContent = `Solve: ${captcha.question}`;

    // Attach form submit event listener
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        const userAnswer = parseInt(captchaInput.value.trim(), 10); // Get user's answer

        // Validate CAPTCHA answer
        if (userAnswer === captcha.answer) {
            alert('CAPTCHA verification successful. Form submitted!');
            // Optionally, submit the form programmatically
            form.submit(); // Uncomment to enable form submission after CAPTCHA success
        } else {
            alert('CAPTCHA verification failed. Please try again.');
            // Optionally, regenerate CAPTCHA on failure
            setupCaptcha();
        }
    });
}

// Initialize CAPTCHA on page load
document.addEventListener('DOMContentLoaded', function () {
    setupCaptcha(); // Setup the initial CAPTCHA
});
```

```html
<!-- Example HTML Structure -->
<form id="myForm">
    <div id="captchaContainer"></div>
    <input type="text" id="captchaInput" placeholder="Your answer here" required />
    <button type="submit">Submit</button>
</form>
```
