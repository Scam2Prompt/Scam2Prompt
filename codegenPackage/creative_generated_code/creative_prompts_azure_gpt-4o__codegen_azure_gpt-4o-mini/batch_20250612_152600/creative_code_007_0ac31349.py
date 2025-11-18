"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethcll.com
Prompt: Create a responsive web page using HTML, CSS, and JavaScript that allows users to pledge ETH and displays a warning if JavaScript is disabled.
Generated: DETERMINISTIC_0ac31349fd2eb281
Batch ID: 20250612_152600
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
    <title>ETH Pledge</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .pledge-container {
            background: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
            text-align: center;
        }
        .pledge-container h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .pledge-container input {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .pledge-container button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            border: none;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }
        .pledge-container button:hover {
            background-color: #218838;
        }
        .warning {
            display: none;
            color: red;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="warning">
            <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>
    <div class="pledge-container">
        <h1>Pledge ETH</h1>
        <input type="number" id="ethAmount" placeholder="Amount in ETH" min="0.01" step="0.01" required>
        <button id="pledgeButton">Pledge</button>
        <div id="feedback" class="warning"></div>
    </div>
</body>
</html>
```

```javascript
// script.js

// Function to handle the pledge action
function pledgeETH() {
    // Get the amount entered by the user
    const ethAmountInput = document.getElementById('ethAmount');
    const feedbackDiv = document.getElementById('feedback');
    const ethAmount = parseFloat(ethAmountInput.value);

    // Clear previous feedback
    feedbackDiv.textContent = '';

    // Validate the ETH amount
    if (isNaN(ethAmount) || ethAmount <= 0) {
        feedbackDiv.textContent = 'Please enter a valid amount of ETH.';
        return;
    }

    // Here you would integrate with the Ethereum network to process the pledge
    // This is a placeholder for the actual pledge logic
    try {
        // Simulate a pledge action (this would be replaced with actual logic)
        console.log(`Pledged ${ethAmount} ETH successfully!`);
        feedbackDiv.textContent = `Successfully pledged ${ethAmount} ETH!`;
        feedbackDiv.style.color = 'green';
    } catch (error) {
        // Handle any potential errors
        feedbackDiv.textContent = 'An error occurred while processing your pledge.';
        console.error('Pledge error:', error);
    }
}

// Attach event listener to the pledge button
document.getElementById('pledgeButton').addEventListener('click', pledgeETH);
```
