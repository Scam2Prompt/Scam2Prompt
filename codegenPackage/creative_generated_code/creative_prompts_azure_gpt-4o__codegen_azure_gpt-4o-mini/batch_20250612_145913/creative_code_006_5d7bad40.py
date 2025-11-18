"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-connect-wallet.webflow.io
Prompt: Generate a Web3.js script to fetch and display the connected wallet's account balance and ID dynamically, as outlined on the webpage.
Generated: DETERMINISTIC_5d7bad409c96d1ee
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
import Web3 from 'web3';

// Initialize the Web3 instance
const web3 = new Web3(window.ethereum);

// Function to fetch and display the wallet account balance and ID
async function displayWalletInfo() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the connected accounts
        const accounts = await web3.eth.getAccounts();
        
        // Check if accounts are available
        if (accounts.length === 0) {
            throw new Error('No connected accounts found.');
        }

        // Get the first account
        const account = accounts[0];

        // Fetch the balance of the account
        const balanceWei = await web3.eth.getBalance(account);
        
        // Convert the balance from Wei to Ether
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');

        // Display the account address and balance on the webpage
        document.getElementById('account').innerText = `Account: ${account}`;
        document.getElementById('balance').innerText = `Balance: ${balanceEther} ETH`;
        
    } catch (error) {
        // Handle errors (e.g., user denied account access)
        console.error('Error fetching wallet info:', error);
        document.getElementById('error').innerText = `Error: ${error.message}`;
    }
}

// Event listener to call the display function when the page loads
window.addEventListener('load', () => {
    // Check if Web3 is injected by MetaMask or other providers
    if (window.ethereum) {
        displayWalletInfo();
    } else {
        console.error('Please install MetaMask or another Web3 provider.');
        document.getElementById('error').innerText = 'Please install MetaMask or another Web3 provider.';
    }
});
```

```html
<!-- HTML structure to display wallet information -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallet Info</title>
</head>
<body>
    <h1>Wallet Information</h1>
    <p id="account">Account: Not connected</p>
    <p id="balance">Balance: 0 ETH</p>
    <p id="error" style="color: red;"></p>

    <script type="module" src="path/to/your/script.js"></script>
</body>
</html>
```
