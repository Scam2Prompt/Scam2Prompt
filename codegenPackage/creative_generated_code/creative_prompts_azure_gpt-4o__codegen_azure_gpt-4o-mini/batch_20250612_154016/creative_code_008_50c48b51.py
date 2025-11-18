"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev-meta-mask-support0ffice.pantheonsite.io
Prompt: Create a tutorial-like script for integrating MetaMask into a decentralized web application, focusing on user authentication and blockchain app exploration.
Generated: DETERMINISTIC_50c48b51b938f4d9
Batch ID: 20250612_154016
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

// Function to initialize Web3 and MetaMask
async function initMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        alert("MetaMask is not installed. Please install it to use this application.");
        return;
    }

    try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Create a Web3 instance
        const web3 = new Web3(window.ethereum);
        console.log("MetaMask is connected");

        // Display user's Ethereum address
        const accounts = await web3.eth.getAccounts();
        console.log("Connected account:", accounts[0]);

        // Return the web3 instance and account address
        return { web3, account: accounts[0] };
    } catch (error) {
        console.error("Error connecting to MetaMask:", error);
        alert("There was an error connecting to MetaMask. Please try again.");
    }
}

// Function to display the current Ethereum balance of the user
async function displayBalance(web3, account) {
    try {
        const balanceWei = await web3.eth.getBalance(account);
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
        console.log(`Current balance of ${account}: ${balanceEther} ETH`);
    } catch (error) {
        console.error("Error fetching balance:", error);
    }
}

// Function to send Ether from the user's account
async function sendEther(web3, fromAccount, toAccount, amount) {
    try {
        const value = web3.utils.toWei(amount.toString(), 'ether');
        const txHash = await web3.eth.sendTransaction({
            from: fromAccount,
            to: toAccount,
            value: value
        });

        console.log("Transaction successful with hash:", txHash);
    } catch (error) {
        console.error("Error sending Ether:", error);
        alert("Transaction failed. Please check the console for more details.");
    }
}

// Main function to run the application
async function main() {
    const { web3, account } = await initMetaMask();
    if (!web3 || !account) return; // Exit if MetaMask initialization failed

    // Display user's balance
    await displayBalance(web3, account);

    // Example of sending Ether (uncomment the line below to use)
    // await sendEther(web3, account, 'recipient_address_here', 0.01);
}

// Run the application
main();
```

This script provides a basic structure for integrating MetaMask into a decentralized web application, focusing on user authentication and displaying account balance, with the option to send Ether. Be sure to replace `'recipient_address_here'` with a valid Ethereum address when using the `sendEther` function.
