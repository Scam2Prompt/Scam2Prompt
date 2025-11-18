"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-24m.pages.dev
Prompt: Generate code using Web3.js or ethers.js to connect a wallet and participate in the $DOGEVERSE presale on Ethereum, Solana, or BNB Chain. Include functionality for swapping ETH, BNB, or MATIC for $DOGEVERSE tokens.
Generated: DETERMINISTIC_57e069217a8d7596
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';

// Constants for the presale
const PRESALE_CONTRACT_ADDRESS = 'YOUR_PRESALE_CONTRACT_ADDRESS';
const DOGEVERSE_TOKEN_ADDRESS = 'YOUR_DOGEVERSE_TOKEN_ADDRESS';
const NETWORK = 'ethereum'; // Change to 'bsc' for BNB Chain or 'solana' for Solana
const TOKEN_AMOUNT = ethers.utils.parseEther('1'); // Amount of DOGEVERSE tokens to purchase

// Initialize provider and signer
async function initialize() {
    // Check if the user has a wallet installed
    if (typeof window.ethereum === 'undefined') {
        alert('Please install MetaMask!');
        return;
    }

    // Request wallet connection
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();

    // Connect to the wallet
    await provider.send("eth_requestAccounts", []);
    console.log("Wallet connected!");
    return signer;
}

// Swap ETH/BNB/MATIC for $DOGEVERSE tokens
async function swapForDogeverse(signer) {
    try {
        // Create a contract instance of the presale
        const presaleContract = new ethers.Contract(PRESALE_CONTRACT_ADDRESS, [
            // Presale contract ABI
            'function buyTokens(address beneficiary) payable'
        ], signer);

        // Execute the transaction
        const tx = await presaleContract.buyTokens(signer.getAddress(), { value: TOKEN_AMOUNT });
        console.log("Transaction sent:", tx.hash);

        // Wait for transaction confirmation
        await tx.wait();
        console.log("Transaction confirmed!");

    } catch (error) {
        console.error("An error occurred during the transaction:", error.message);
        alert("Transaction failed: " + error.message);
    }
}

// Main function to execute the entire process
async function main() {
    const signer = await initialize();
    if (!signer) return;

    await swapForDogeverse(signer);
}

// Run the main function
main();
```

**Note:** Replace `YOUR_PRESALE_CONTRACT_ADDRESS` and `YOUR_DOGEVERSE_TOKEN_ADDRESS` with the actual contract addresses. Adjust `TOKEN_AMOUNT` based on the required amount of DOGEVERSE tokens and ensure that the ABI matches your presale contract's.
