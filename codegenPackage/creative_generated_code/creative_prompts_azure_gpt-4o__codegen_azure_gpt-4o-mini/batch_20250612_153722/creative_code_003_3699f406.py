"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metutmsklogin.gitbook.io
Prompt: Generate JavaScript code to detect if Metamask is installed and prompt the user to connect their wallet, as described in the Metamask GitBook.
Generated: DETERMINISTIC_3699f4067d96a81e
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to detect if MetaMask is installed in the user's browser
function isMetaMaskInstalled() {
    // Check if the window object has the ethereum property
    return typeof window.ethereum !== 'undefined';
}

// Function to prompt the user to connect their MetaMask wallet
async function connectMetaMask() {
    // Check if MetaMask is installed
    if (!isMetaMaskInstalled()) {
        alert('MetaMask is not installed. Please install it to use this feature.');
        return;
    }

    try {
        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // If accounts are returned, log the first account
        if (accounts.length > 0) {
            console.log('Connected account:', accounts[0]);
            return accounts[0]; // Return the connected account
        } else {
            console.error('No accounts found.');
            alert('No accounts found. Please ensure you are logged into MetaMask.');
        }
    } catch (error) {
        // Handle user rejection of the connection request
        if (error.code === 4001) {
            console.error('User rejected the request to connect MetaMask.');
            alert('You rejected the connection request. Please try again.');
        } else {
            console.error('Error connecting to MetaMask:', error);
            alert('An error occurred while connecting to MetaMask. Please try again later.');
        }
    }
}

// Event listener to trigger the MetaMask connection prompt
document.getElementById('connectButton').addEventListener('click', connectMetaMask);
```

```html
<!-- Sample HTML to integrate the connect button -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Connection</title>
</head>
<body>
    <button id="connectButton">Connect MetaMask</button>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```

This code provides a complete implementation that detects MetaMask installation, prompts the user to connect, and includes error handling for various scenarios. Make sure to include the JS in an appropriate HTML file.
