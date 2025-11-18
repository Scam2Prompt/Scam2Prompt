"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-en.pages.dev
Prompt: Write a script using Web3.js to connect a user's MetaMask wallet to a decentralized betting platform, referencing the wallet connection functionality described on Blockchain Bets.
Generated: DETERMINISTIC_16e75be00b6c0db3
Batch ID: 20250612_153420
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

// Function to connect user's MetaMask wallet to the betting platform
async function connectWallet() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            // Create a new instance of Web3 using the provider from MetaMask
            const web3 = new Web3(window.ethereum);

            // Request account access from the user
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Log the connected account
            console.log('Connected account:', accounts[0]);

            // Return the Web3 instance and connected account
            return { web3, account: accounts[0] };
        } else {
            console.error('MetaMask is not installed. Please install it to use this feature.');
            alert('MetaMask is not installed. Please install it to use this feature.');
        }
    } catch (error) {
        // Handle errors (e.g., user denied access)
        console.error('Error connecting to MetaMask:', error.message);
        alert(`Error connecting to MetaMask: ${error.message}`);
    }
}

// Example usage
document.getElementById('connectButton').addEventListener('click', async () => {
    const { web3, account } = await connectWallet();
    if (web3 && account) {
        // Proceed with further functionalities of the betting platform
        console.log('Web3 and account ready for betting operations');
    }
});
```

### HTML Button Example
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Betting Platform</title>
</head>
<body>
    <button id="connectButton">Connect MetaMask Wallet</button>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```

### Notes:
- Ensure to replace `path/to/your/script.js` with the actual path to your JavaScript file containing the Web3.js code.
- This code assumes you have Web3.js installed and available in your project.
