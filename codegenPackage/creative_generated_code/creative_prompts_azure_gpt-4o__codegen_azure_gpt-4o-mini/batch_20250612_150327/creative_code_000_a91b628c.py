"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmaskextensio.livejournal.com
Prompt: Write code to interact with Ethereum-based dApps using the MetaMask Wallet Extension. Include steps for connecting the wallet and sending a transaction.
Generated: DETERMINISTIC_a91b628c59feab88
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers library for Ethereum interactions
import { ethers } from "ethers";

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to use this application.');
}

// Function to connect to MetaMask wallet
async function connectWallet() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected wallet address:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Error connecting to MetaMask:', error);
        throw new Error('Failed to connect to MetaMask');
    }
}

// Function to send a transaction
async function sendTransaction(toAddress, amountInEther) {
    try {
        // Ensure the user is connected to their wallet
        const signer = new ethers.providers.Web3Provider(window.ethereum).getSigner();

        // Create the transaction parameters
        const transaction = {
            to: toAddress,
            value: ethers.utils.parseEther(amountInEther), // Convert Ether to Wei
            gasLimit: ethers.utils.hexlify(21000), // Standard gas limit for ETH transfer
        };

        // Send the transaction
        const txResponse = await signer.sendTransaction(transaction);
        console.log('Transaction sent:', txResponse);

        // Wait for the transaction to be mined
        const txReceipt = await txResponse.wait();
        console.log('Transaction mined:', txReceipt);
    } catch (error) {
        console.error('Error sending transaction:', error);
        throw new Error('Transaction failed');
    }
}

// Example usage
(async () => {
    const walletAddress = await connectWallet(); // Connect to wallet
    const recipientAddress = '0xRecipientAddressHere'; // Change to the recipient address
    const amount = '0.01'; // Amount of Ether to send

    // Send Ether to the recipient
    await sendTransaction(recipientAddress, amount);
})();
```

### Note:
- Replace `'0xRecipientAddressHere'` with the actual recipient address where you want to send Ether.
- Ensure that the user has sufficient funds in their MetaMask wallet to send the specified amount.
