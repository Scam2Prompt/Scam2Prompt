"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Generate a JavaScript code snippet that interacts with decentralized applications (DApps) through the MetaMask Chrome extension.
Generated: DETERMINISTIC_84a5f6ae0582b730
Batch ID: 20250612_135144
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
    console.error('MetaMask is not installed. Please install it to interact with DApps.');
} else {
    // Initialize Web3
    const Web3 = require('web3');
    const web3 = new Web3(window.ethereum); // Use the MetaMask provider

    // Function to connect to MetaMask
    async function connectMetaMask() {
        try {
            // Request account access if needed
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            const userAccount = accounts[0];
            console.log('Connected account:', userAccount);
            return userAccount;
        } catch (error) {
            console.error('User denied account access or other error:', error);
        }
    }

    // Function to get the current balance of the connected account
    async function getBalance(account) {
        try {
            const balance = await web3.eth.getBalance(account);
            console.log('Account balance:', web3.utils.fromWei(balance, 'ether'), 'ETH');
        } catch (error) {
            console.error('Error fetching balance:', error);
        }
    }

    // Function to send Ether from one account to another
    async function sendEther(fromAccount, toAccount, amount) {
        try {
            const transactionParameters = {
                to: toAccount, // The recipient's address
                from: fromAccount, // The sender's address
                value: web3.utils.toHex(web3.utils.toWei(amount, 'ether')), // Amount in Wei
                gas: '2000000', // Optional gas limit
            };

            // Sending the transaction
            const txHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });

            console.log('Transaction sent with hash:', txHash);
            return txHash;
        } catch (error) {
            console.error('Transaction failed:', error);
        }
    }

    // Main function to execute the DApp interaction
    async function main() {
        const userAccount = await connectMetaMask();
        if (userAccount) {
            await getBalance(userAccount);
            // Example: Sending 0.01 ETH to a recipient address
            const recipientAddress = '0xRecipientAddressHere'; // Replace with your recipient's address
            await sendEther(userAccount, recipientAddress, '0.01');
        }
    }

    // Execute the main function
    main();
}
```
