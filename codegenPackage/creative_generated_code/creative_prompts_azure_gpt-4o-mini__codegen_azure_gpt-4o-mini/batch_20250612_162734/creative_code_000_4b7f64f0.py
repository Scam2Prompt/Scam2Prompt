"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://public-metamask-com--cdn.bravesites.com
Prompt: How can I implement MetaMask login for my decentralized application (dApp) to enhance user security and simplify authentication?
Generated: DETERMINISTIC_4b7f64f03af47d8b
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Ensure the user has MetaMask installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this feature.');
} else {
    // Create a Web3 instance
    const web3 = new Web3(window.ethereum);

    // Function to connect to MetaMask
    async function connectMetaMask() {
        try {
            // Request account access from the user
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Set the user's account (the first one returned)
            const userAccount = accounts[0];
            console.log(`Connected account: ${userAccount}`);
            document.getElementById('accountDisplay').innerText = `Connected: ${userAccount}`;
        } catch (error) {
            // Handle errors (user rejected connection, etc.)
            console.error('User denied account access or error occurred', error);
            alert('Connection to MetaMask was denied or encountered an error. Please try again.');
        }
    }

    // Function to display the current account's balance
    async function displayBalance() {
        const userAccount = document.getElementById('accountDisplay').innerText.split(' ')[1];
        try {
            // Fetch the balance of the account
            const balance = await web3.eth.getBalance(userAccount);
            const etherBalance = web3.utils.fromWei(balance, 'ether');
            console.log(`Balance of ${userAccount}: ${etherBalance} ETH`);
            document.getElementById('balanceDisplay').innerText = `Balance: ${etherBalance} ETH`;
        } catch (error) {
            console.error('Error fetching balance', error);
            alert('Failed to retrieve account balance.');
        }
    }

    // Setup event listeners for buttons
    document.getElementById('connectButton').addEventListener('click', async () => {
        await connectMetaMask();
        await displayBalance();
    });
}
```

### HTML for reference
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Login</title>
</head>
<body>
    <h1>Connect to MetaMask</h1>
    <button id="connectButton">Connect MetaMask</button>
    <p id="accountDisplay">Connected: None</p>
    <p id="balanceDisplay">Balance: 0 ETH</p>
    <script src="path/to/your/javascript.js"></script>
</body>
</html>
```

### Note:
- Ensure to replace `"path/to/your/javascript.js"` with the correct path where the JavaScript code is saved.
