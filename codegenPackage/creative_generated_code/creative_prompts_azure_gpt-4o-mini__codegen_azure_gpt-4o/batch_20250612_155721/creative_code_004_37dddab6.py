"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mateimsklogi-usa.godaddysites.com
Prompt: Provide an example of using the MetaMask library to send Ether from one wallet to another in a Node.js application.
Generated: DETERMINISTIC_37dddab6f4390399
Batch ID: 20250612_155721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
const { ethers } = require("ethers");

// Function to send Ether using MetaMask
async function sendEther(senderPrivateKey, recipientAddress, amountInEther) {
    try {
        // Connect to the Ethereum network via MetaMask provider
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Request MetaMask to connect (if not already connected)
        await provider.send("eth_requestAccounts", []);

        // Create a wallet instance using the sender's private key
        const wallet = new ethers.Wallet(senderPrivateKey, provider);

        // Validate recipient address
        if (!ethers.utils.isAddress(recipientAddress)) {
            throw new Error("Invalid recipient address");
        }

        // Convert Ether amount to wei
        const amountInWei = ethers.utils.parseEther(amountInEther);

        // Create the transaction object
        const tx = {
            to: recipientAddress, // Recipient address
            value: amountInWei,   // Amount in wei
            gasPrice: await provider.getGasPrice(), // Fetch current gas price
            gasLimit: ethers.utils.hexlify(21000)   // Gas limit for standard transfers
        };

        // Sign and send the transaction
        const transactionResponse = await wallet.sendTransaction(tx);

        console.log("Transaction sent! Waiting for confirmation...");
        console.log("Transaction hash:", transactionResponse.hash);

        // Wait for confirmation
        const receipt = await transactionResponse.wait();

        console.log("Transaction confirmed!");
        console.log("Receipt:", receipt);

        return receipt; // Return transaction receipt for further processing
    } catch (error) {
        // Handle and log errors
        console.error("Error while sending Ether:", error.message);
        throw error; // Rethrow error for higher-level handling if required
    }
}

// Example usage
(async () => {
    try {
        // Replace with actual values
        const senderPrivateKey = "0xYOUR_PRIVATE_KEY"; // Sender's private key (never expose in production!)
        const recipientAddress = "0xRECIPIENT_ADDRESS"; // Recipient's Ethereum address
        const amountInEther = "0.01"; // Amount to send

        // Call the function to send Ether
        const receipt = await sendEther(senderPrivateKey, recipientAddress, amountInEther);
        console.log("Transaction successful! Receipt:", receipt);
    } catch (error) {
        console.error("Failed to send Ether:", error.message);
    }
})();
```
