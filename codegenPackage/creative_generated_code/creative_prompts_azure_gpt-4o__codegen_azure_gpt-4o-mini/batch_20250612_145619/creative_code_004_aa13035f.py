"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imqbo.com
Prompt: Provide an example of how to use ethers.js to send ETH from a user's wallet to a predefined smart contract address for a pledge system.
Generated: DETERMINISTIC_aa13035ff920f1e1
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers library
const { ethers } = require("ethers");

// Define the provider and wallet
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Define the smart contract address and the amount to send (in ETH)
const contractAddress = '0xYourContractAddress';
const amountInEther = '0.1'; // Amount to send in ETH

// Function to send ETH to a smart contract
async function sendEthToContract() {
    try {
        // Convert ETH amount to Wei (1 ETH = 10^18 Wei)
        const amountInWei = ethers.utils.parseEther(amountInEther);

        // Create a transaction object
        const tx = {
            to: contractAddress, // The smart contract address
            value: amountInWei, // Amount in Wei
            gasLimit: ethers.utils.hexlify(21000), // Standard gas limit for ETH transfer
            gasPrice: await provider.getGasPrice() // Fetch current gas price
        };

        // Send the transaction
        const transactionResponse = await wallet.sendTransaction(tx);
        console.log(`Transaction sent: ${transactionResponse.hash}`);

        // Wait for the transaction to be mined
        const receipt = await transactionResponse.wait();
        console.log(`Transaction confirmed in block: ${receipt.blockNumber}`);
    } catch (error) {
        console.error("Error sending ETH:", error);
    }
}

// Execute the function
sendEthToContract();
```

**Notes:**
- Replace `'YOUR_INFURA_PROJECT_ID'` and `'YOUR_PRIVATE_KEY'` with actual Infura project ID and user wallet private key.
- Replace `'0xYourContractAddress'` with the actual smart contract address.
