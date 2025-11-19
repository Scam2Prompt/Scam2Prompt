"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: How can I use Fortmatic to build web3 dApps without requiring users to install extensions?
Generated: DETERMINISTIC_d7e514f1ce48a8ee
Batch ID: 20250612_164205
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/fortmatic/dist/fortmatic.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/web3/1.3.5/web3.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import Fortmatic from 'fortmatic';

// Set up Fortmatic
const fortmaticApiKey = 'YOUR_FORTMATIC_API_KEY'; // Replace with your Fortmatic API key
const fm = new Fortmatic(fortmaticApiKey);
const web3 = new Web3(fm.getProvider());

// Function to connect to Fortmatic and create a Web3 instance
async function connectWallet() {
    try {
        // Request account access if needed
        await fm.user.login();
        console.log('Connected to Fortmatic!');

        // Get the user's Ethereum accounts
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please ensure you have an account in Fortmatic.');
        }

        // Log the user's account
        console.log('User account:', accounts[0]);
        return accounts[0]; // Return the first account
    } catch (error) {
        console.error('Error connecting to Fortmatic:', error);
        alert(`Error connecting to wallet: ${error.message}`);
    }
}

// Function to send a transaction
async function sendTransaction(toAddress, amount) {
    try {
        const fromAddress = await connectWallet(); // Ensure the user is connected
        const tx = {
            from: fromAddress,
            to: toAddress,
            value: web3.utils.toWei(amount, 'ether'), // Convert amount to Wei
            gas: 21000, // Gas limit
        };

        // Send the transaction
        const receipt = await web3.eth.sendTransaction(tx);
        console.log('Transaction receipt:', receipt);
        alert('Transaction successful!');
    } catch (error) {
        console.error('Error sending transaction:', error);
        alert(`Transaction failed: ${error.message}`);
    }
}

// Example usage
document.getElementById('connectButton').onclick = connectWallet; // Connect wallet on button click
document.getElementById('sendButton').onclick = () => {
    const toAddress = document.getElementById('toAddress').value; // Get recipient address
    const amount = document.getElementById('amount').value; // Get amount to send
    sendTransaction(toAddress, amount); // Send transaction
};
```

### HTML Structure (for reference)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fortmatic Web3 dApp</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.3.5/web3.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/fortmatic/dist/fortmatic.js"></script>
    <script src="app.js" defer></script> <!-- Include the above JavaScript -->
</head>
<body>
    <h1>Fortmatic Web3 dApp</h1>
    <button id="connectButton">Connect Wallet</button>
    <br />
    <input type="text" id="toAddress" placeholder="Recipient Address" />
    <input type="text" id="amount" placeholder="Amount in ETH" />
    <button id="sendButton">Send Transaction</button>
</body>
</html>
``` 

### Notes:
- Replace `YOUR_FORTMATIC_API_KEY` with your actual Fortmatic API key.
- This code assumes you will include it in a suitable HTML file as shown.
- Make sure to handle sensitive information like API keys securely in a real application.
