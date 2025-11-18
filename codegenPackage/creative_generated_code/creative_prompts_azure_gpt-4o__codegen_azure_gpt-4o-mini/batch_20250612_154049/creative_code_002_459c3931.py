"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://horizondapp.com
Prompt: Generate code to enable JavaScript-based functionality for a web application that interacts with blockchain networks, similar to CoinHorizon.
Generated: DETERMINISTIC_459c39314954d5f6
Batch ID: 20250612_154049
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
// Import necessary functions for handling Ethereum addresses
import { isAddress } from 'web3-utils';

// Initialize Web3 instance
let web3;

// Check if the browser has an Ethereum provider
if (window.ethereum) {
    // Request account access if needed
    window.ethereum.request({ method: 'eth_requestAccounts'})
        .then(() => {
            // Create a new Web3 instance
            web3 = new Web3(window.ethereum);
            console.log("Web3 successfully initialized!");
        })
        .catch((error) => {
            console.error("User denied account access or error occurred:", error);
        });
} else {
    console.error("No Ethereum provider detected. Please install MetaMask.");
}

/**
 * Function to get the balance of an Ethereum address
 * @param {string} address - The Ethereum address to check the balance for
 * @returns {Promise<string>} - The balance in Ether, or an error message
 */
async function getBalance(address) {
    // Validate the Ethereum address
    if (!isAddress(address)) {
        throw new Error("Invalid Ethereum address.");
    }
    
    try {
        const balanceWei = await web3.eth.getBalance(address);
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
        return balanceEther;
    } catch (error) {
        console.error("Error fetching balance:", error);
        throw new Error("Failed to fetch balance.");
    }
}

/**
 * Function to send Ether from one address to another
 * @param {string} from - The sender's Ethereum address
 * @param {string} to - The receiver's Ethereum address
 * @param {string} amount - The amount of Ether to send (in Ether)
 * @returns {Promise<string>} - The transaction hash or an error message
 */
async function sendEther(from, to, amount) {
    // Validate the Ethereum addresses
    if (!isAddress(from) || !isAddress(to)) {
        throw new Error("Invalid Ethereum address provided.");
    }

    // Convert amount to Wei
    const amountWei = web3.utils.toWei(amount, 'ether');

    try {
        const transactionHash = await web3.eth.sendTransaction({
            from: from,
            to: to,
            value: amountWei
        });
        return transactionHash.transactionHash;
    } catch (error) {
        console.error("Error sending Ether:", error);
        throw new Error("Transaction failed.");
    }
}

/**
 * Function to listen for new blocks on the blockchain
 */
function listenForNewBlocks() {
    if (!web3) {
        console.error("Web3 is not initialized. Cannot listen for new blocks.");
        return;
    }

    web3.eth.subscribe('newBlockHeaders', (error, blockHeader) => {
        if (error) {
            console.error("Error subscribing to new blocks:", error);
            return;
        }
        console.log("New block received. Block number:", blockHeader.number);
    });
}

// Example usage
async function main() {
    const address = '0xYourEthereumAddressHere';
    try {
        const balance = await getBalance(address);
        console.log(`Balance of ${address}: ${balance} Ether`);

        const transactionHash = await sendEther(address, '0xRecipientAddressHere', '0.01');
        console.log(`Transaction successful with hash: ${transactionHash}`);
    } catch (error) {
        console.error("Error in main function:", error);
    }

    listenForNewBlocks();
}

// Run the main function to demonstrate functionality
main();
```
