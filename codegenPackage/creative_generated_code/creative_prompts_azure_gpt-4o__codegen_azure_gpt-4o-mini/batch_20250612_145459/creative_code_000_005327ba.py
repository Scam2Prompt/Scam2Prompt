"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meltamaskvvalttet.godaddysites.com
Prompt: Write JavaScript code to integrate MetaMask into a Web3 application for connecting to Ethereum-based decentralized applications (dApps).
Generated: DETERMINISTIC_005327ba5d2c8f84
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3 library
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');

    // Create a new instance of Web3
    const web3 = new Web3(window.ethereum);

    // Function to connect to MetaMask
    async function connect() {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Get the user's Ethereum account
            const userAccount = accounts[0];
            console.log(`Connected account: ${userAccount}`);

            // Update UI or state with the connected account
            // updateUI(userAccount); // Example function to update UI

            // Optional: Subscribe to account changes
            window.ethereum.on('accountsChanged', (accounts) => {
                console.log('Accounts changed: ', accounts);
                // Handle the new account
                // updateUI(accounts[0]); // Example function to update UI
            });

            // Optional: Subscribe to network changes
            window.ethereum.on('chainChanged', (chainId) => {
                console.log('Network changed: ', chainId);
                // Handle the network change, e.g., refresh the page or update state
                // window.location.reload(); // Example to reload the page
            });

        } catch (error) {
            // Handle errors
            console.error('Error connecting to MetaMask: ', error);
            alert('Failed to connect to MetaMask. Please try again.');
        }
    }

    // Function to get the current account balance
    async function getAccountBalance(account) {
        try {
            const balance = await web3.eth.getBalance(account);
            console.log(`Balance for account ${account}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
        } catch (error) {
            console.error('Error fetching balance: ', error);
        }
    }

    // Attach the connect function to a button click event
    document.getElementById('connectButton').addEventListener('click', () => {
        connect().then(() => {
            const accounts = await web3.eth.getAccounts();
            getAccountBalance(accounts[0]);
        });
    });

} else {
    console.log('MetaMask is not installed. Please install it to use this dApp.');
    alert('Please install MetaMask to interact with this application.');
}
```

Make sure to include the following in your HTML to support the JavaScript code above:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Integration</title>
    <script type="module" src="path/to/your/javascriptFile.js"></script>
</head>
<body>
    <button id="connectButton">Connect MetaMask</button>
</body>
</html>
``` 

Replace `"path/to/your/javascriptFile.js"` with the actual path to your JavaScript file.
