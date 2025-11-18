"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Create a secure web form for scam victims to submit details about fraudulent companies, referencing The Legato's user interface design.
Generated: DETERMINISTIC_2fa5cba7843e41c0
Batch ID: 20250612_153712
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
    <meta name="description" content="Secure web form for scam victims to report fraudulent companies.">
    <title>Report Fraudulent Company</title>
    <link rel="stylesheet" href="styles.css"> <!-- Ensure a separate CSS file for styles -->
    <script src="script.js" defer></script> <!-- Ensure to load JS after DOM is ready -->
</head>
<body>
    <div class="container">
        <h1>Report a Fraudulent Company</h1>
        <form id="fraudReportForm" action="/submit-report" method="POST">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required />

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required />

            <label for="companyName">Company Name:</label>
            <input type="text" id="companyName" name="companyName" required />

            <label for="companyWebsite">Company Website:</label>
            <input type="url" id="companyWebsite" name="companyWebsite" required />

            <label for="details">Details of the Scam:</label>
            <textarea id="details" name="details" rows="4" required></textarea>

            <button type="submit">Submit Report</button>
        </form>
        <div id="responseMessage" class="hidden"></div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the container and form elements */
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.hidden {
    display: none;
}

#responseMessage {
    margin-top: 20px;
    text-align: center;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('fraudReportForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(event.target); // Collect form data

    try {
        // Send the form data to the server
        const response = await fetch('/submit-report', {
            method: 'POST',
            body: formData,
        });

        // Check if the response is ok
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json(); // Parse JSON response
        displayMessage('Report submitted successfully!', 'success');
    } catch (error) {
        // Handle errors
        console.error('Error submitting the form:', error);
        displayMessage('There was an error submitting your report. Please try again.', 'error');
    }
});

// Function to display messages to the user
function displayMessage(message, type) {
    const responseMessage = document.getElementById('responseMessage');
    responseMessage.textContent = message;
    responseMessage.className = type; // Apply class based on type (e.g., 'success', 'error')
    responseMessage.classList.remove('hidden'); // Show the message
}
```

### Notes:
- Ensure the backend endpoint `/submit-report` is properly set up to handle form submissions securely.
- Implement CSRF protection in the backend.
- Validate and sanitize user inputs server-side before storing or processing.
- Implement rate limiting on form submissions to prevent abuse.
