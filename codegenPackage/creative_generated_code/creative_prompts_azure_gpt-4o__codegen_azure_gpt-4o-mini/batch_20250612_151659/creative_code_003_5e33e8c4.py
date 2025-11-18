"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resume.khtain.com
Prompt: Provide an example of integrating Web3.js into a JavaScript application, ensuring compatibility with Cool-Web3 features.
Generated: DETERMINISTIC_5e33e8c4074771d7
Batch ID: 20250612_151659
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
import CoolWeb3 from 'cool-web3'; // Assuming Cool-Web3 is a compatible library

// Check if the browser has MetaMask installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this application');
    throw new Error('MetaMask not found');
}

// Initialize Web3 and Cool-Web3
const web3 = new Web3(window.ethereum);
const coolWeb3 = new CoolWeb3(web3);

// Function to connect to MetaMask
async function connectWallet() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Wallet connected');
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
        throw new Error('Wallet connection failed');
    }
}

// Function to get the current account
async function getCurrentAccount() {
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
        console.error('No accounts found');
        throw new Error('No accounts found');
    }
    return accounts[0];
}

// Function to get balance of the current account
async function getBalance() {
    try {
        const account = await getCurrentAccount();
        const balance = await web3.eth.getBalance(account);
        console.log(`Balance of ${account}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
}

// Function to send a transaction
async function sendTransaction(toAddress, amountInEther) {
    try {
        const account = await getCurrentAccount();
        const amountInWei = web3.utils.toWei(amountInEther, 'ether');
        
        const transactionParameters = {
            to: toAddress,
            from: account,
            value: amountInWei,
        };

        // Send transaction using Cool-Web3
        const txHash = await coolWeb3.eth.sendTransaction(transactionParameters);
        console.log('Transaction successful with hash:', txHash);
    } catch (error) {
        console.error('Transaction failed:', error);
    }
}

// Example usage
(async () => {
    await connectWallet(); // Connect wallet
    await getBalance(); // Get account balance

    // Uncomment the following line to send a transaction
    // await sendTransaction('0xRecipientAddressHere', '0.01'); // Replace with actual recipient address
})();
```
