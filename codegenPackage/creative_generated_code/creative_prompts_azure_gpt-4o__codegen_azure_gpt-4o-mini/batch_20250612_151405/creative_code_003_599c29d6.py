"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp.busta.gg
Prompt: Provide an example of JavaScript code to enable wallet connection (e.g., MetaMask) for a dApp like the one on Busta.gg.
Generated: DETERMINISTIC_599c29d6b0455665
Batch ID: 20250612_151405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
const Web3 = require('web3'); // For interacting with the Ethereum blockchain

// Function to initialize the web3 instance and connect to MetaMask
async function connectWallet() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        alert('Please install MetaMask to use this dApp!');
        return;
    }

    // Create a new Web3 instance with the injected provider
    const web3 = new Web3(window.ethereum);

    try {
        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's accounts
        const accounts = await web3.eth.getAccounts();

        // Display the connected account
        console.log('Connected account:', accounts[0]);

        // Set the network ID
        const networkId = await web3.eth.net.getId();
        console.log('Connected to network ID:', networkId);
        
        // Additional setup can be done here (e.g., contract initialization)

    } catch (error) {
        // Handle errors (e.g., user denied account access)
        console.error('An error occurred while connecting to MetaMask:', error.message);
        alert('Error connecting to wallet: ' + error.message);
    }
}

// Event listener for a button to connect the wallet
document.getElementById('connect-button').addEventListener('click', connectWallet);
```

```html
<!-- HTML Button to trigger wallet connection -->
<button id="connect-button">Connect Wallet</button>
```

```css
/* Add some basic styles for the button */
#connect-button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #f0c14b;
    border: 1px solid #a88734;
    cursor: pointer;
}

#connect-button:hover {
    background-color: #ddb347;
}
```
