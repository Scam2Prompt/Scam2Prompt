"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defie.me
Prompt: Generate code to enable JavaScript-based wallet integration (e.g., MetaMask) for an Ethereum DeFi application.
Generated: DETERMINISTIC_d8debddf9c4f0ed2
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ethereum Wallet Integration for DeFi Application

// Check if the browser has Ethereum provider (like MetaMask)
if (typeof window.ethereum !== 'undefined') {
    console.log('Ethereum wallet is available.');

    // Function to request account access
    async function connectWallet() {
        try {
            // Request account access from the user
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
            return accounts[0]; // Return the connected account address
        } catch (error) {
            // Handle errors (e.g., user denied access)
            console.error('Error connecting to wallet:', error);
            throw new Error('Wallet connection failed. Please check if you have a wallet installed or authorized.');
        }
    }

    // Function to get the current Ethereum network
    async function getNetwork() {
        try {
            const networkId = await window.ethereum.request({ method: 'net_version' });
            console.log('Current Network ID:', networkId);
            return networkId; // Return the network ID
        } catch (error) {
            console.error('Error fetching network ID:', error);
            throw new Error('Failed to fetch network information.');
        }
    }

    // Function to send a transaction
    async function sendTransaction(to, amount) {
        try {
            const transactionParameters = {
                to: to, // Address to send the transaction to
                from: window.ethereum.selectedAddress, // Uses the selected account
                value: window.ethereum.utils.toHex(window.ethereum.utils.toWei(amount.toString(), 'ether')), // Amount in wei
            };

            // Send the transaction
            const txHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });
            console.log('Transaction sent. Hash:', txHash);
            return txHash; // Return the transaction hash
        } catch (error) {
            console.error('Transaction error:', error);
            throw new Error('Transaction failed. Please check your inputs and try again.');
        }
    }

    // Example usage
    document.getElementById('connect-wallet-button').addEventListener('click', async () => {
        try {
            const account = await connectWallet();
            const network = await getNetwork();
            console.log('Connected to account:', account, 'on network:', network);
        } catch (error) {
            alert(error.message); // Display error to the user
        }
    });

    // Send transaction example
    document.getElementById('send-transaction-button').addEventListener('click', async () => {
        const recipientAddress = document.getElementById('recipient-address').value;
        const amount = document.getElementById('amount').value;
        
        try {
            const txHash = await sendTransaction(recipientAddress, amount);
            alert('Transaction successful! Hash: ' + txHash);
        } catch (error) {
            alert(error.message); // Display error to the user
        }
    });

} else {
    console.log('Please install an Ethereum wallet like MetaMask.');
    alert('Ethereum wallet not found. Please install MetaMask or another wallet extension.');
}
```

This code snippet sets up an Ethereum wallet integration using JavaScript, enabling users to connect their wallets, request network information, and send transactions. The code includes error handling and user notifications for a smooth experience. Make sure to adapt the button IDs and HTML structure according to your application design.
