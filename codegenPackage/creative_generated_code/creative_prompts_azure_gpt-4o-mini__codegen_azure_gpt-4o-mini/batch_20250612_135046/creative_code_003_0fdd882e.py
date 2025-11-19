"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io
Prompt: Provide an example of how to implement Snaps to enhance the features of a MetaMask wallet.
Generated: DETERMINISTIC_0fdd882e6de0f0f5
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";

// Define a function to initialize MetaMask and enable the wallet
async function initMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error("MetaMask is not installed. Please install it to use this feature.");
    }

    // Request account access if needed
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Create a provider and signer
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();

    return { provider, signer };
}

// Define a function to send a transaction
async function sendTransaction(signer, toAddress, amount) {
    try {
        // Convert amount to wei
        const txAmount = ethers.utils.parseEther(amount);

        // Create transaction object
        const tx = {
            to: toAddress,
            value: txAmount,
            gasLimit: 21000, // Set a default gas limit
        };

        // Send transaction and wait for confirmation
        const transactionResponse = await signer.sendTransaction(tx);
        console.log(`Transaction sent: ${transactionResponse.hash}`);

        // Wait for transaction to be mined
        await transactionResponse.wait();
        console.log(`Transaction confirmed in block: ${transactionResponse.blockNumber}`);
    } catch (error) {
        // Handle any errors that occur during the transaction
        console.error("Transaction failed:", error.message);
    }
}

// Define a function to fetch the current balance of an Ethereum address
async function fetchBalance(signer, address) {
    try {
        const balance = await signer.provider.getBalance(address);
        console.log(`Balance of ${address}: ${ethers.utils.formatEther(balance)} ETH`);
        return balance;
    } catch (error) {
        console.error("Failed to fetch balance:", error.message);
    }
}

// Example usage of the functions
(async () => {
    try {
        const { provider, signer } = await initMetaMask();

        // Example: Fetch balance of the connected account
        const account = await signer.getAddress();
        await fetchBalance(signer, account);

        // Example: Send 0.01 ETH to a specified address
        const recipientAddress = "0xRecipientAddressHere"; // Replace with actual address
        await sendTransaction(signer, recipientAddress, "0.01");
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
})();
```

Make sure to replace `"0xRecipientAddressHere"` with the actual Ethereum address to which you want to send Ether.
