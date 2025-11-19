"""
Generated Code Metadata:
========================
Original URL: https://wormhole.vercel.app
Prompt: Provide an example of how to check the balance of an account using MetaMask in a DApp, based on the information from Wormhole.
Generated: DETERMINISTIC_10a5198d9ebc1ad4
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Initialize Web3 instance
let web3;

// Function to initialize Web3 and check for MetaMask
async function initWeb3() {
    if (window.ethereum) {
        // Use MetaMask's provider
        web3 = new Web3(window.ethereum);
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
        } catch (error) {
            console.error("User denied account access:", error);
            return;
        }
    } else {
        console.error("MetaMask is not installed. Please install it to use this DApp.");
        return;
    }
}

// Function to get the balance of the connected account
async function getAccountBalance() {
    try {
        // Get the list of accounts
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            console.error("No accounts found. Please connect your wallet.");
            return;
        }

        // Get the balance of the first account
        const balance = await web3.eth.getBalance(accounts[0]);
        
        // Convert balance from Wei to Ether
        const balanceInEther = web3.utils.fromWei(balance, 'ether');
        
        console.log(`Account: ${accounts[0]}`);
        console.log(`Balance: ${balanceInEther} ETH`);
    } catch (error) {
        console.error("Error fetching account balance:", error);
    }
}

// Main function to run the DApp
async function main() {
    await initWeb3();
    await getAccountBalance();
}

// Run the main function
main();
```
