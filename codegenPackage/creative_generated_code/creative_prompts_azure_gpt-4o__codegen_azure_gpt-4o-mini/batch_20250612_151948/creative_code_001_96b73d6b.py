"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Generate code for a JavaScript-based Ethereum wallet that interacts with the Ethereum blockchain using Web3.js, as outlined on Ethereum.org.
Generated: DETERMINISTIC_96b73d6b5ea664d8
Batch ID: 20250612_151948
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

// Check if the user has a wallet (like MetaMask) installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask or another Ethereum wallet to use this application.');
}

// Create an instance of Web3
const web3 = new Web3(window.ethereum);

// Function to connect to the Ethereum wallet
async function connectWallet() {
    try {
        // Request account access to allow the user to connect their wallet
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0]; // Return the connected account address
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
        alert('Failed to connect to wallet. Please try again.');
    }
}

// Function to get the balance of an Ethereum address
async function getBalance(address) {
    try {
        const balance = await web3.eth.getBalance(address);
        // Convert balance from Wei to Ether
        return web3.utils.fromWei(balance, 'ether');
    } catch (error) {
        console.error('Error fetching balance:', error);
        alert('Failed to retrieve balance. Please check the address and try again.');
    }
}

// Function to send Ether from one account to another
async function sendEther(fromAddress, toAddress, amount) {
    try {
        // Convert amount to Wei before sending
        const amountWei = web3.utils.toWei(amount.toString(), 'ether');

        const transactionParameters = {
            to: toAddress, // Address to send Ether
            from: fromAddress, // Address to send from
            value: amountWei // Amount in Wei
        };

        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log('Transaction successful with hash:', txHash);
        alert(`Transaction successful! TX Hash: ${txHash}`);
    } catch (error) {
        console.error('Transaction failed:', error);
        alert('Failed to send Ether. Please check the details and try again.');
    }
}

// Example usage
async function main() {
    const account = await connectWallet();
    if (account) {
        const balance = await getBalance(account);
        console.log(`Balance of ${account}: ${balance} ETH`);

        // Example of sending Ether (uncomment to use)
        // const recipientAddress = '0xRecipientAddressHere';
        // const amountToSend = '0.01'; // Amount in ETH
        // await sendEther(account, recipientAddress, amountToSend);
    }
}

// Run the main function on page load
window.onload = main;
```
