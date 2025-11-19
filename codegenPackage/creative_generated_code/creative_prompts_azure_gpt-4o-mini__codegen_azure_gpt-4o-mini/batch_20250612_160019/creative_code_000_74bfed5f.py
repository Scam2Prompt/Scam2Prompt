"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxouyigo.com
Prompt: Generate a code snippet that demonstrates how to integrate blockchain technology into a Web3.0 application as discussed on OKX.
Generated: DETERMINISTIC_74bfed5fb112d10b
Batch ID: 20250612_160019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';

// Check if Web3 is injected by the browser (e.g., MetaMask)
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
}

// Initialize Web3
const web3 = new Web3(window.ethereum);

async function connectWallet() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Wallet connected successfully!');

        // Retrieve the user's accounts
        const accounts = await web3.eth.getAccounts();
        console.log('Connected account:', accounts[0]);

        return accounts[0];
    } catch (error) {
        // Handle errors (e.g., user denied access)
        console.error('Error connecting wallet:', error);
    }
}

async function getBalance(address) {
    try {
        // Fetch the balance of the connected account
        const balance = await web3.eth.getBalance(address);
        console.log(`Balance of ${address}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
        return balance;
    } catch (error) {
        // Handle errors in fetching balance
        console.error('Error fetching balance:', error);
    }
}

async function sendTransaction(fromAddress, toAddress, amount) {
    try {
        // Create a transaction object
        const transactionParameters = {
            to: toAddress, // Required except during contract publications
            from: fromAddress, // Must match user's active address.
            value: web3.utils.toHex(web3.utils.toWei(amount.toString(), 'ether')), // Amount in Wei
        };

        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        console.log('Transaction sent with hash:', txHash);
        return txHash;
    } catch (error) {
        // Handle errors in transaction sending
        console.error('Error sending transaction:', error);
    }
}

// Example usage
(async () => {
    const userAddress = await connectWallet();
    if (userAddress) {
        await getBalance(userAddress);
        // Uncomment to send a transaction (example: sending 0.01 ETH)
        // await sendTransaction(userAddress, '0xRecipientAddressHere', 0.01);
    }
})();
```
