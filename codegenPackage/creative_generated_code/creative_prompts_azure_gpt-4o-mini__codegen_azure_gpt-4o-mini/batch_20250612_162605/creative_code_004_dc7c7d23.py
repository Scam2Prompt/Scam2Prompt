"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamusklogy.godaddysites.com
Prompt: Explain how to use MetaMask for securely managing crypto assets in a Web3 environment.
Generated: DETERMINISTIC_dc7c7d233f959289
Batch ID: 20250612_162605
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

// This function initializes a connection to MetaMask
async function initializeMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Create a new instance of Web3
        const web3 = new Web3(window.ethereum);
        
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("MetaMask is connected");
            return web3;
        } catch (error) {
            // Handle error if user denies account access
            console.error("User denied account access:", error);
        }
    } else {
        console.error("MetaMask is not installed. Please install it to use this application.");
    }
}

// Function to get the connected user's Ethereum address
async function getUserAddress(web3) {
    const accounts = await web3.eth.getAccounts();
    if (accounts.length > 0) {
        return accounts[0]; // Return the first account address
    } else {
        throw new Error("No accounts found. Please connect your MetaMask wallet.");
    }
}

// Function to get the current balance of the user's account
async function getBalance(web3, address) {
    try {
        const balanceWei = await web3.eth.getBalance(address);
        // Convert Wei to Ether
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
        return balanceEther;
    } catch (error) {
        console.error("Failed to fetch balance:", error);
        throw error;
    }
}

// Function to send Ether from the user's account
async function sendEther(web3, fromAddress, toAddress, amount) {
    try {
        const transactionParameters = {
            to: toAddress, // The address to send to
            from: fromAddress, // The address sending the funds
            value: web3.utils.toHex(web3.utils.toWei(amount, 'ether')), // Amount in Wei
        };

        // Send the transaction
        await web3.eth.sendTransaction(transactionParameters);
        console.log(`Transaction successful: Sent ${amount} ETH to ${toAddress}`);
    } catch (error) {
        console.error("Transaction failed:", error);
        throw error;
    }
}

// Main function to manage user interactions
async function main() {
    const web3 = await initializeMetaMask();
    if (!web3) return; // Exit if web3 is not initialized

    try {
        const userAddress = await getUserAddress(web3);
        console.log(`Connected Address: ${userAddress}`);

        const balance = await getBalance(web3, userAddress);
        console.log(`Current Balance: ${balance} ETH`);

        // Example of sending Ether (uncomment to use)
        // await sendEther(web3, userAddress, 'RECEIVER_ADDRESS_HERE', '0.01');

    } catch (error) {
        console.error("Error in main function:", error);
    }
}

// Run the main function when the script is executed
main();
```

**Note:** For the `sendEther` function, replace `'RECEIVER_ADDRESS_HERE'` with the actual Ethereum address of the recipient when you decide to send Ether. This code is structured for educational purposes and should be tested in a safe environment before deploying in production.
