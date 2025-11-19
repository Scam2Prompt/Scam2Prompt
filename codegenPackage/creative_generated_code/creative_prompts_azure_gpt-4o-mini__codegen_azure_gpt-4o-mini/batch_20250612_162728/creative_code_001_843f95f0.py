"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mhfgy-722.com
Prompt: What are the best practices for integrating reCAPTCHA into a website for user verification?
Generated: DETERMINISTIC_843f95f0682d2899
Batch ID: 20250612_162728
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/recaptcha/api.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.google.com/recaptcha/api/siteverify?secret=${RECAPTCHA_SECRET_KEY}&response=${recaptchaResponse}`;": {
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
<!-- HTML Code for reCAPTCHA Integration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>reCAPTCHA Integration Example</title>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
</head>
<body>
    <h1>User Registration</h1>
    <form id="registrationForm" action="/submit" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        
        <!-- reCAPTCHA widget -->
        <div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY"></div>
        <br>

        <button type="submit">Register</button>
    </form>

    <script>
        // Function to handle form submission
        document.getElementById('registrationForm').onsubmit = async function(event) {
            event.preventDefault(); // Prevent default form submission
            
            // Get the reCAPTCHA response
            const recaptchaResponse = grecaptcha.getResponse();
            if (recaptchaResponse.length === 0) {
                alert("Please complete the reCAPTCHA");
                return; // Exit if reCAPTCHA is not completed
            }

            // Prepare form data
            const formData = new FormData(this);
            formData.append('g-recaptcha-response', recaptchaResponse);

            try {
                // Send form data to the server
                const response = await fetch('/submit', {
                    method: 'POST',
                    body: formData
                });

                // Check for a successful response
                if (response.ok) {
                    const data = await response.json();
                    // Handle success (e.g., display a success message)
                    alert(data.message || 'Registration successful!');
                } else {
                    // Handle server errors
                    const errorData = await response.json();
                    alert(errorData.message || 'An error occurred during registration.');
                }
            } catch (error) {
                // Handle network errors
                console.error('Error:', error);
                alert('A network error occurred. Please try again later.');
            }
        };
    </script>
</body>
</html>
```

```javascript
// Node.js code for server-side reCAPTCHA validation
const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('node-fetch');
const app = express();

// Middleware to parse JSON and URL-encoded data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Your reCAPTCHA secret key
const RECAPTCHA_SECRET_KEY = 'YOUR_SECRET_KEY';

// Route to handle form submission
app.post('/submit', async (req, res) => {
    const recaptchaResponse = req.body['g-recaptcha-response'];

    // Verify reCAPTCHA response
    const verificationUrl = `https://www.google.com/recaptcha/api/siteverify?secret=${RECAPTCHA_SECRET_KEY}&response=${recaptchaResponse}`;
    
    try {
        const verificationResponse = await fetch(verificationUrl, {
            method: 'POST'
        });

        const verificationData = await verificationResponse.json();

        if (!verificationData.success) {
            return res.status(400).json({ message: 'reCAPTCHA verification failed. Please try again.' });
        }

        // Proceed with registration logic (e.g., save user to database)
        // ...

        return res.status(200).json({ message: 'Registration successful!' });
    } catch (error) {
        console.error('Verification Error:', error);
        return res.status(500).json({ message: 'Internal server error. Please try again later.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
