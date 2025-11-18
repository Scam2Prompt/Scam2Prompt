"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Create a function in JavaScript to verify the user's wallet balance using the MetaMask Chrome extension and display it in a web application.
Generated: DETERMINISTIC_6ecd4f037562edb0
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check the user's wallet balance using MetaMask
async function checkWalletBalance() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        return;
    }

    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's account address
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length === 0) {
            console.error('No accounts found. Please ensure you are logged into MetaMask.');
            return;
        }

        const account = accounts[0];

        // Fetch the balance of the user's wallet in Wei
        const balanceWei = await window.ethereum.request({
            method: 'eth_getBalance',
            params: [account, 'latest']
        });

        // Convert the balance from Wei to Ether
        const balanceEther = parseFloat(window.ethereum.utils.fromWei(balanceWei, 'ether'));

        // Display the balance on the web application
        displayBalance(account, balanceEther);
    } catch (error) {
        console.error('Failed to retrieve wallet balance:', error);
    }
}

// Function to display the wallet balance in the web application
function displayBalance(account, balance) {
    const balanceDisplayElement = document.getElementById('wallet-balance');
    if (balanceDisplayElement) {
        balanceDisplayElement.textContent = `Account: ${account} \nBalance: ${balance} ETH`;
    } else {
        console.error('Display element for balance not found.');
    }
}

// Example usage: Call the checkWalletBalance function when the window loads
window.onload = () => {
    checkWalletBalance();
};
```

```html
<!-- HTML structure for displaying the wallet balance -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallet Balance Checker</title>
</head>
<body>
    <h1>Wallet Balance Checker</h1>
    <pre id="wallet-balance">Checking balance...</pre>

    <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```
