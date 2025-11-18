"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica18.vercel.app
Prompt: Develop a web interface for selecting a blockchain network (Solana, Ethereum, Polygon) and logging in, similar to the functionality provided by Matrica.
Generated: DETERMINISTIC_5df6bcb0dede6df7
Batch ID: 20250612_153401
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
    <title>Blockchain Network Selector</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <div id="app">
        <h1>Select Blockchain Network</h1>
        <form id="network-form">
            <label for="network">Choose a network:</label>
            <select id="network" required>
                <option value="">--Select a Network--</option>
                <option value="solana">Solana</option>
                <option value="ethereum">Ethereum</option>
                <option value="polygon">Polygon</option>
            </select>
            <br><br>
            <button type="submit">Login</button>
        </form>
        <div id="message"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for better appearance */
body, h1, select, button {
    margin: 0;
    padding: 10px;
}

#app {
    max-width: 400px;
    margin: auto;
    text-align: center;
}

button {
    cursor: pointer;
}
```

```javascript
// script.js

// Function to handle the form submission
document.getElementById('network-form').addEventListener('submit', async function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const network = document.getElementById('network').value; // Get selected network
    const messageDiv = document.getElementById('message'); // Div to display messages
    messageDiv.innerHTML = ''; // Clear any previous messages

    // Validate network selection
    if (!network) {
        displayMessage('Please select a blockchain network.', 'error');
        return;
    }

    try {
        // Logic to handle login for the selected network
        // This is a placeholder for actual integration with wallet providers
        const result = await fakeLogin(network); // Simulate login
        displayMessage(`Logged in to ${network} successfully!`, 'success');
    } catch (error) {
        displayMessage(`Error logging in: ${error.message}`, 'error');
    }
});

// Simulated login function (Replace with actual logic)
async function fakeLogin(network) {
    return new Promise((resolve, reject) => {
        // Simulating a network call
        setTimeout(() => {
            if (network) {
                resolve(true);
            } else {
                reject(new Error('Login failed.'));
            }
        }, 1000);
    });
}

// Function to display messages
function displayMessage(message, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;
    messageDiv.className = type; // Add class for styling
    messageDiv.style.color = type === 'error' ? 'red' : 'green'; // Color based on type
}
```

This code creates a simple web interface where users can select a blockchain network and attempt to log in. The JavaScript simulates a login process with basic error handling and provides feedback to the user.
