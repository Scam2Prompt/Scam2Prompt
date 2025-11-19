"""
Generated Code Metadata:
========================
Original URL: https://gravity-cq3.pages.dev
Prompt: Provide an example of using Gravity's EVM-compatible features to enable seamless interactions between dApps and wallets.
Generated: DETERMINISTIC_97fd76c256268add
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// Define the Gravity contract address and ABI
const GRAVITY_CONTRACT_ADDRESS = "0xYourGravityContractAddress"; // Replace with actual address
const GRAVITY_CONTRACT_ABI = [
    // Add the ABI of the Gravity contract here
];

// Initialize provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Create a contract instance
const gravityContract = new ethers.Contract(GRAVITY_CONTRACT_ADDRESS, GRAVITY_CONTRACT_ABI, signer);

/**
 * Function to send a transaction to the Gravity contract
 * @param {string} recipient - The address of the recipient
 * @param {number} amount - The amount to send
 */
async function sendTransaction(recipient, amount) {
    try {
        // Request account access if needed
        await provider.send("eth_requestAccounts", []);

        // Prepare the transaction
        const tx = await gravityContract.sendTokens(recipient, ethers.utils.parseEther(amount.toString()));

        // Wait for the transaction to be mined
        const receipt = await tx.wait();

        console.log("Transaction successful with hash:", receipt.transactionHash);
    } catch (error) {
        console.error("Transaction failed:", error);
    }
}

/**
 * Function to check the balance of a specific address
 * @param {string} address - The address to check the balance for
 */
async function checkBalance(address) {
    try {
        const balance = await gravityContract.balanceOf(address);
        console.log(`Balance of ${address}:`, ethers.utils.formatEther(balance));
    } catch (error) {
        console.error("Failed to fetch balance:", error);
    }
}

// Example usage
(async () => {
    const recipientAddress = "0xRecipientAddress"; // Replace with actual recipient address
    const amountToSend = 1; // Amount in Ether

    // Send transaction
    await sendTransaction(recipientAddress, amountToSend);

    // Check balance
    await checkBalance(recipientAddress);
})();
```
