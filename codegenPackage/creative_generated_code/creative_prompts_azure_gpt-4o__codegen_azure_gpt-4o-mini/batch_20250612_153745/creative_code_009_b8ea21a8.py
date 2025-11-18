"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meitamskkextnion.webflow.io
Prompt: Create a JavaScript function that uses MetaMask to connect to a dApp and display the user's wallet balance in real-time.
Generated: DETERMINISTIC_b8ea21a8594c530d
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure that the code runs after the DOM has fully loaded
document.addEventListener("DOMContentLoaded", async () => {
    // Function to check if MetaMask is installed
    const isMetaMaskInstalled = () => {
        return typeof window.ethereum !== 'undefined';
    };

    // Function to connect to MetaMask and get the user's wallet address
    const connectToMetaMask = async () => {
        if (!isMetaMaskInstalled()) {
            alert("MetaMask is not installed. Please install it to use this dApp.");
            return null;
        }

        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the first account
        } catch (error) {
            console.error("User denied account access or error occurred:", error);
            return null;
        }
    };

    // Function to get the user's wallet balance
    const getWalletBalance = async (account) => {
        if (!account) {
            console.error("No account provided for balance retrieval.");
            return null;
        }

        try {
            // Get the balance in Wei
            const balanceWei = await window.ethereum.request({
                method: 'eth_getBalance',
                params: [account, 'latest']
            });
            // Convert balance from Wei to Ether
            const balance = parseFloat(balanceWei) / Math.pow(10, 18);
            return balance;
        } catch (error) {
            console.error("Error fetching balance:", error);
            return null;
        }
    };

    // Function to update the displayed balance on the webpage
    const updateBalanceDisplay = (balance) => {
        const balanceDisplay = document.getElementById("balanceDisplay");
        if (balanceDisplay) {
            balanceDisplay.innerText = `Wallet Balance: ${balance} ETH`;
        }
    };

    // Main function to handle MetaMask connection and balance display
    const init = async () => {
        const account = await connectToMetaMask();
        if (account) {
            const balance = await getWalletBalance(account);
            if (balance !== null) {
                updateBalanceDisplay(balance);
            }
        }
    };

    // Button to trigger the connection and balance retrieval
    const connectButton = document.getElementById("connectButton");
    if (connectButton) {
        connectButton.addEventListener("click", init);
    }
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Wallet Balance</title>
</head>
<body>
    <h1>Connect to MetaMask</h1>
    <button id="connectButton">Connect MetaMask</button>
    <p id="balanceDisplay">Wallet Balance: 0 ETH</p>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```
