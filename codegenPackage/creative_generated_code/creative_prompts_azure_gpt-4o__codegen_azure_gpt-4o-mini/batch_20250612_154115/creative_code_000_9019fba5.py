"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: Write JavaScript code to integrate MetaMask into a web application for interacting with Ethereum-based DApps, ensuring users can connect their wallet and approve transactions directly from the browser.
Generated: DETERMINISTIC_9019fba574302d7d
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('MetaMask is not installed. Please install it to use this feature.');
}

// Function to connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Successfully connected
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        // Handle user rejection or other errors
        console.error('Error connecting to MetaMask:', error);
        alert('Could not connect to MetaMask. Please try again.');
    }
}

// Function to send a transaction
async function sendTransaction(toAddress, amount) {
    // Ensure user is connected
    const fromAddress = await connectMetaMask();
    if (!fromAddress) return;

    // Prepare transaction parameters
    const transactionParameters = {
        to: toAddress, // Required: The address to send to
        from: fromAddress, // Required: The address sending the transaction
        value: window.ethereum.utils.toHex(window.ethereum.utils.toWei(amount.toString(), 'ether')), // Convert amount to Wei
    };

    try {
        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        
        console.log('Transaction sent with hash:', txHash);
        return txHash;
    } catch (error) {
        // Handle any errors during the transaction process
        console.error('Error sending transaction:', error);
        alert('Transaction failed. Please try again.');
    }
}

// Event listener for the 'Connect Wallet' button
document.getElementById('connectButton').addEventListener('click', connectMetaMask);

// Example usage: Send 0.01 ETH to a specific address when a button is clicked
document.getElementById('sendButton').addEventListener('click', () => {
    const toAddress = '0xYourAddressHere'; // Replace with a valid Ethereum address
    const amount = 0.01; // Amount of ETH to send
    sendTransaction(toAddress, amount);
});
```

```html
<!-- Simple HTML structure for connecting wallet and sending transactions -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Integration</title>
</head>
<body>
    <button id="connectButton">Connect Wallet</button>
    <button id="sendButton">Send 0.01 ETH</button>
    <script src="yourScript.js"></script> <!-- Link to the JS code -->
</body>
</html>
```
