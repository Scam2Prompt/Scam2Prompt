"""
Generated Code Metadata:
========================
Original URL: https://btcdzv.com
Prompt: Generate a basic HTML structure for a Bitcoin pledge service that requires JavaScript to function properly.
Generated: DETERMINISTIC_67af0f04f39761d9
Batch ID: 20250622_210145
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
    <title>Bitcoin Pledge Service</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript file -->
</head>
<body>
    <header>
        <h1>Bitcoin Pledge Service</h1>
        <p>Join us in supporting the Bitcoin community!</p>
    </header>

    <main>
        <section id="pledge-form">
            <h2>Pledge Your Support</h2>
            <form id="pledgeForm">
                <label for="name">Your Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="amount">Pledge Amount (BTC):</label>
                <input type="number" id="amount" name="amount" step="0.0001" min="0.0001" required>

                <button type="submit">Submit Pledge</button>
            </form>
            <div id="responseMessage"></div> <!-- Placeholder for response messages -->
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Bitcoin Pledge Service. All rights reserved.</p>
    </footer>
</body>
</html>
```

```javascript
// script.js

// Function to handle the pledge form submission
document.getElementById('pledgeForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Retrieve form data
    const name = document.getElementById('name').value;
    const amount = parseFloat(document.getElementById('amount').value);

    // Validate the input
    if (!name || amount <= 0) {
        displayMessage('Please enter a valid name and pledge amount.', 'error');
        return;
    }

    // Simulate a pledge submission (replace with actual API call)
    submitPledge(name, amount)
        .then(response => {
            displayMessage(`Thank you, ${name}! Your pledge of ${amount} BTC has been recorded.`, 'success');
        })
        .catch(error => {
            displayMessage('An error occurred while processing your pledge. Please try again later.', 'error');
            console.error('Pledge submission error:', error);
        });
});

// Function to simulate pledge submission (mock API call)
function submitPledge(name, amount) {
    return new Promise((resolve, reject) => {
        // Simulate a successful submission with a timeout
        setTimeout(() => {
            // Randomly simulate success or failure
            Math.random() > 0.2 ? resolve() : reject(new Error('Submission failed'));
        }, 1000);
    });
}

// Function to display messages to the user
function displayMessage(message, type) {
    const responseMessage = document.getElementById('responseMessage');
    responseMessage.textContent = message;
    responseMessage.className = type; // Set class for styling based on message type
}
```

```css
/* styles.css */

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #0070f3;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Form styling */
#pledge-form {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Input and button styling */
input[type="text"],
input[type="number"],
button {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Button styling */
button {
    background: #0070f3;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #005bb5;
}

/* Response message styling */
#responseMessage {
    margin-top: 20px;
    font-weight: bold;
}

/* Error message styling */
.error {
    color: red;
}

/* Success message styling */
.success {
    color: green;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px;
    background: #0070f3;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
