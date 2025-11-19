"""
Generated Code Metadata:
========================
Original URL: https://sharon-robinson-662.pages.dev
Prompt: Create an HTML page that includes a call-to-action for a best friends discount, using the content from the provided webpage.
Generated: DETERMINISTIC_9a69402b9db8d6b6
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Best Friends Discount</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Best Friends Discount</h1>
    </header>
    <main>
        <section class="cta">
            <h2>Share the Love, Get Rewarded!</h2>
            <p>Refer a friend and receive a special discount on your next purchase!</p>
            <button id="cta-button">Get Your Discount Code</button>
            <div id="cta-form-container" style="display: none;">
                <form id="cta-form">
                    <label for="friend-email">Enter your friend's email:</label>
                    <input type="email" id="friend-email" required>
                    <button id="cta-submit">Send</button>
                </form>
                <p id="cta-success" style="display: none;">Success! Your friend has been notified.</p>
                <p id="cta-error" style="display: none; color: red;"></p>
            </div>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

.cta {
    max-width: 500px;
    margin: 2em auto;
    padding: 1em;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.cta h2 {
    margin-top: 0;
}

#cta-button {
    background-color: #4CAF50;
    color: #fff;
    padding: 1em 2em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#cta-button:hover {
    background-color: #3e8e41;
}

#cta-form-container {
    margin-top: 1em;
}

#cta-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#cta-form label {
    margin-bottom: 0.5em;
}

#cta-form input {
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
}

#cta-submit {
    background-color: #4CAF50;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#cta-submit:hover {
    background-color: #3e8e41;
}

#cta-success, #cta-error {
    margin-top: 0.5em;
}
```

```javascript
// script.js

const ctaButton = document.getElementById('cta-button');
const ctaFormContainer = document.getElementById('cta-form-container');
const ctaForm = document.getElementById('cta-form');
const friendEmailInput = document.getElementById('friend-email');
const ctaSubmit = document.getElementById('cta-submit');
const ctaSuccess = document.getElementById('cta-success');
const ctaError = document.getElementById('cta-error');

ctaButton.addEventListener('click', () => {
    ctaFormContainer.style.display = 'block';
});

ctaForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const friendEmail = friendEmailInput.value.trim();
    if (friendEmail) {
        // Replace with your actual API endpoint or email sending logic
        // For demonstration purposes, we'll just simulate a successful submission
        try {
            // Send email or API call here
            ctaSuccess.style.display = 'block';
            ctaError.style.display = 'none';
            ctaFormContainer.style.display = 'none';
            friendEmailInput.value = '';
        } catch (error) {
            ctaError.textContent = 'Error sending email. Please try again.';
            ctaError.style.display = 'block';
            ctaSuccess.style.display = 'none';
        }
    } else {
        ctaError.textContent = 'Please enter a valid email address.';
        ctaError.style.display = 'block';
    }
});
```
