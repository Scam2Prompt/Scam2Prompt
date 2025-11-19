"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poohclaim.pages.dev
Prompt: Explain how to set up a MetaMask wallet for purchasing $POOH tokens, including any necessary code for connecting to the Ethereum network.
Generated: DETERMINISTIC_771a82bf412195c5
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';

// Function to initialize MetaMask connection
async function initMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Create a new instance of Web3 with the provider from MetaMask
        const web3 = new Web3(window.ethereum);
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("MetaMask connected");
            return web3;
        } catch (error) {
            console.error("User denied account access:", error);
            throw new Error("User denied account access to MetaMask.");
        }
    } else {
        console.error("MetaMask is not installed.");
        throw new Error("Please install MetaMask to use this feature.");
    }
}

// Function to purchase $POOH tokens
async function buyPoohTokens(tokenAddress, amountInEther) {
    const web3 = await initMetaMask();
    
    // Define the transaction details
    const transactionParameters = {
        to: tokenAddress, // The address of the $POOH token contract
        from: window.ethereum.selectedAddress, // The user's MetaMask account
        value: web3.utils.toWei(amountInEther, 'ether'), // Convert Ether to Wei
        gas: '2000000', // Estimate a reasonable gas limit
    };

    // Sending the transaction
    try {
        const txHash = await web3.eth.sendTransaction(transactionParameters);
        console.log("Transaction successful with hash:", txHash);
    } catch (error) {
        console.error("Transaction failed:", error);
        throw new Error("Transaction failed. Please check your MetaMask.");
    }
}

// Example usage: Set the token address and amount to purchase
const poohTokenAddress = '0xYourPoohTokenAddress'; // Replace with actual $POOH token contract address
const amountToBuy = '0.01'; // Amount in Ether to purchase $POOH tokens

// Uncomment the following line to execute the purchase (in a real application, do this on a button click or event)
// buyPoohTokens(poohTokenAddress, amountToBuy);
```
