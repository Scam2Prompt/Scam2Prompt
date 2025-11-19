"""
Generated Code Metadata:
========================
Original URL: https://ethcll.com
Prompt: Create a responsive web page using HTML, CSS, and JavaScript that allows users to pledge ETH and displays a warning if JavaScript is disabled.
Generated: DETERMINISTIC_0ac31349fd2eb281
Batch ID: 20250612_152600
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
    <title>Pledge ETH</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
    <noscript>
        <style>
            .no-js-warning {
                display: block;
                background-color: #ffcc00;
                color: #000;
                padding: 10px;
                text-align: center;
                font-weight: bold;
            }
        </style>
    </noscript>
</head>
<body>
    <div class="no-js-warning" style="display: none;">
        JavaScript is disabled in your browser. Please enable it for full functionality.
    </div>
    <div class="container">
        <h1>Pledge ETH</h1>
        <form id="pledgeForm">
            <label for="ethAmount">Amount of ETH to Pledge:</label>
            <input type="number" id="ethAmount" name="ethAmount" min="0.01" step="0.01" required>
            <button type="submit">Pledge</button>
        </form>
        <div id="message" class="message"></div>
    </div>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="number"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
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

.message {
    margin-top: 20px;
    text-align: center;
    font-weight: bold;
}
```

```javascript
// script.js

// Wait for the DOM to fully load before executing the script
document.addEventListener("DOMContentLoaded", function() {
    const pledgeForm = document.getElementById('pledgeForm');
    const messageDiv = document.getElementById('message');

    // Handle form submission
    pledgeForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the amount of ETH from the input
        const ethAmount = parseFloat(document.getElementById('ethAmount').value);

        // Validate the ETH amount
        if (isNaN(ethAmount) || ethAmount <= 0) {
            displayMessage("Please enter a valid amount of ETH.", "error");
            return;
        }

        // Simulate a pledge action (replace with actual pledge logic)
        try {
            // Here you would typically call a function to handle the pledge
            // For demonstration, we just display a success message
            displayMessage(`Successfully pledged ${ethAmount} ETH!`, "success");
        } catch (error) {
            // Handle any errors that occur during the pledge process
            console.error("Error during pledge:", error);
            displayMessage("An error occurred while processing your pledge. Please try again.", "error");
        }
    });

    // Function to display messages to the user
    function displayMessage(message, type) {
        messageDiv.textContent = message;
        messageDiv.style.color = type === "error" ? "red" : "green";
    }
});
```
