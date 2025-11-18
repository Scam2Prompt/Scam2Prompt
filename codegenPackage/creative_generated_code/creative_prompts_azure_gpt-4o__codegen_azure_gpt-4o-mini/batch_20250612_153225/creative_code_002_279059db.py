"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-echo.pages.dev
Prompt: Create a JavaScript-based landing page that includes an early access signup form and social media follow buttons, similar to the Echo Beta website.
Generated: DETERMINISTIC_279059db6c7c63b5
Batch ID: 20250612_153225
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://instagram.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://facebook.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Early Access Signup</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <header>
        <h1>Join Our Early Access Program</h1>
        <p>Be the first to experience our new features!</p>
    </header>

    <main>
        <form id="signup-form" class="signup-form">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">
            <button type="submit">Sign Up</button>
            <p id="form-message" class="form-message"></p>
        </form>

        <div class="social-media">
            <h2>Follow Us</h2>
            <a href="https://twitter.com" target="_blank" aria-label="Follow us on Twitter">
                <img src="twitter-icon.svg" alt="Twitter Icon">
            </a>
            <a href="https://facebook.com" target="_blank" aria-label="Follow us on Facebook">
                <img src="facebook-icon.svg" alt="Facebook Icon">
            </a>
            <a href="https://instagram.com" target="_blank" aria-label="Follow us on Instagram">
                <img src="instagram-icon.svg" alt="Instagram Icon">
            </a>
        </div>
    </main>

    <footer>
        <p>&copy; 2023 Your Company. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

header {
    text-align: center;
}

.signup-form {
    margin: 20px 0;
}

.signup-form input[type="email"] {
    padding: 10px;
    width: 250px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.signup-form button {
    padding: 10px 15px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.signup-form button:hover {
    background-color: #0056b3;
}

.form-message {
    margin-top: 10px;
    font-size: 16px;
}

.social-media {
    margin-top: 30px;
}

.social-media a {
    margin: 0 10px;
}
```

```javascript
// script.js

// Wait for the document to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signup-form');
    const formMessage = document.getElementById('form-message');

    // Add event listener to the signup form
    signupForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent the default form submission

        const email = event.target.email.value;

        // Basic client-side validation
        if (!validateEmail(email)) {
            formMessage.textContent = 'Please enter a valid email address.';
            formMessage.style.color = 'red';
            return;
        }

        // Simulate sending data to the server
        try {
            await sendSignupRequest(email); // Placeholder for an actual request
            formMessage.textContent = 'Thank you for signing up!';
            formMessage.style.color = 'green';
            signupForm.reset(); // Reset form fields
        } catch (error) {
            console.error('Error during signup:', error);
            formMessage.textContent = 'An error occurred. Please try again later.';
            formMessage.style.color = 'red';
        }
    });

    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Simulated async function to send signup request
    async function sendSignupRequest(email) {
        // Simulating an API request delay
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                // Simulate a successful response
                resolve();
            }, 1000);
        });
    }
});
```
