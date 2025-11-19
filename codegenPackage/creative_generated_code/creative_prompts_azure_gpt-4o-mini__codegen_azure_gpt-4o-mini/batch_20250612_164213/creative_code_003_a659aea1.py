"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacerealestatevt.com
Prompt: Develop a simple web form using HTML and JavaScript that allows users to sign up for market updates from Pace Real Estate in Northern Vermont.
Generated: DETERMINISTIC_a659aea18619ac2d
Batch ID: 20250612_164213
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
    <title>Pace Real Estate - Sign Up for Market Updates</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Pace Real Estate</h1>
        <h2>Sign Up for Market Updates</h2>
    </header>
    
    <main>
        <form id="signup-form" novalidate>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <span class="error" id="name-error"></span>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <span class="error" id="email-error"></span>

            <button type="submit">Sign Up</button>
        </form>

        <div id="success-message" class="hidden">
            <p>Thank you for signing up! You will receive market updates shortly.</p>
        </div>
    </main>

    <footer>
        <p>&copy; 2023 Pace Real Estate. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the page */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

header {
    text-align: center;
}

form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: auto;
}

label {
    margin: 10px 0 5px;
}

input {
    padding: 10px;
    margin-bottom: 20px;
}

button {
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.error {
    color: red;
    font-size: 0.9em;
}

.hidden {
    display: none;
}

#success-message {
    text-align: center;
    margin-top: 20px;
}
```

```javascript
// script.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('signup-form');
    const successMessage = document.getElementById('success-message');
    
    // Form submission event listener
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        document.getElementById('name-error').textContent = '';
        document.getElementById('email-error').textContent = '';

        // Get form values
        const name = form.name.value.trim();
        const email = form.email.value.trim();

        // Validate inputs
        let isValid = true;

        if (name === '') {
            document.getElementById('name-error').textContent = 'Name is required.';
            isValid = false;
        }

        if (email === '' || !validateEmail(email)) {
            document.getElementById('email-error').textContent = 'A valid email is required.';
            isValid = false;
        }

        // If valid, simulate server request
        if (isValid) {
            // Simulate a successful response
            simulateServerResponse()
                .then(() => {
                    form.reset(); // Reset form fields
                    successMessage.classList.remove('hidden'); // Show success message
                })
                .catch((error) => {
                    console.error('Error during submission:', error);
                    alert('An error occurred. Please try again later.');
                });
        }
    });

    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Simulates a server response for signup
    function simulateServerResponse() {
        return new Promise((resolve, reject) => {
            // Simulate network delay
            setTimeout(() => {
                // Simulate a successful response
                resolve();
            }, 1000);
        });
    }
});
```
