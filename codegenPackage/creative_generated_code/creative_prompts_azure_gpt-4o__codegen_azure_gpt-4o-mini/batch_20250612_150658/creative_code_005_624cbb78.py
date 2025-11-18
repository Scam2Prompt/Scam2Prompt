"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: How can I use MetaMask’s API to manage multiple accounts and assets in a Web3 application? Provide example code.
Generated: DETERMINISTIC_624cbb78a834d34d
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to use this app.');
}

// Create a new instance of Web3 with the provider from MetaMask
const web3 = new Web3(window.ethereum);

// Function to request account access
async function requestAccountAccess() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts;
    } catch (error) {
        console.error('Error requesting account access:', error);
    }
}

// Function to get the current account
async function getCurrentAccount() {
    const accounts = await requestAccountAccess();
    return accounts[0]; // Return the first account
}

// Function to retrieve balance of the specified account
async function getAccountBalance(account) {
    try {
        // Get balance in Wei and convert to Ether
        const balanceWei = await web3.eth.getBalance(account);
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
        return balanceEther;
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
}

// Function to manage multiple accounts
async function manageMultipleAccounts() {
    try {
        const accounts = await requestAccountAccess();
        console.log('Accounts:', accounts);

        // Retrieve and log balances for each account
        for (const account of accounts) {
            const balance = await getAccountBalance(account);
            console.log(`Balance of ${account}: ${balance} Ether`);
        }
    } catch (error) {
        console.error('Error managing multiple accounts:', error);
    }
}

// Function to send Ether from one account to another
async function sendEther(fromAccount, toAccount, amount) {
    try {
        // Convert the amount to Wei
        const amountWei = web3.utils.toWei(amount.toString(), 'ether');

        // Send the transaction
        const transactionHash = await web3.eth.sendTransaction({
            from: fromAccount,
            to: toAccount,
            value: amountWei,
        });

        console.log('Transaction successful with hash:', transactionHash);
    } catch (error) {
        console.error('Error sending Ether:', error);
    }
}

// Example usage of the functions
(async () => {
    const currentAccount = await getCurrentAccount();
    console.log('Current Account:', currentAccount);

    // Manage multiple accounts and log their balances
    await manageMultipleAccounts();

    // Example: Sending Ether (uncomment to execute)
    // await sendEther(currentAccount, 'RECEIVER_ACCOUNT_ADDRESS', 0.01);
})();
```
