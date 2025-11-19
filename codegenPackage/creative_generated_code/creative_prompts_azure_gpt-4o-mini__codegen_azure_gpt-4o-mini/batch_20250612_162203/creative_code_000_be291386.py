"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bengonbase-xyz.pages.dev
Prompt: Generate a code snippet for connecting a wallet to the $BENG token on the Base blockchain.
Generated: DETERMINISTIC_be2913867fdbabf9
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import { ethers } from "ethers";

// Token contract address on the Base blockchain
const BENG_TOKEN_ADDRESS = "0xYourBENGTokenAddressHere"; // Replace with actual contract address

// ABI for the ERC20 token contract
const BENG_TOKEN_ABI = [
    "function balanceOf(address owner) view returns (uint256)",
    "function transfer(address to, uint256 amount) returns (bool)"
];

// Function to connect wallet and interact with $BENG token
async function connectWalletAndInteract() {
    try {
        // Check for wallet provider
        if (!window.ethereum) {
            throw new Error("MetaMask not detected. Please install it.");
        }

        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];

        // Create a provider and signer
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Create a contract instance
        const bengTokenContract = new ethers.Contract(BENG_TOKEN_ADDRESS, BENG_TOKEN_ABI, signer);

        // Example: Get the balance of the connected wallet for $BENG token
        const balance = await bengTokenContract.balanceOf(userAddress);
        console.log(`Balance of $BENG token: ${ethers.utils.formatUnits(balance, 18)}`);

        // Example: Transfer $BENG tokens (uncomment to use)
        // const recipientAddress = "0xRecipientAddressHere"; // Replace with actual recipient address
        // const amountToSend = ethers.utils.parseUnits("1.0", 18); // Sending 1.0 $BENG tokens
        // const tx = await bengTokenContract.transfer(recipientAddress, amountToSend);
        // await tx.wait(); // Wait for transaction to be mined
        // console.log(`Successfully transferred ${ethers.utils.formatUnits(amountToSend, 18)} $BENG to ${recipientAddress}`);

    } catch (error) {
        // Handle errors appropriately
        console.error("Error connecting to wallet or interacting with $BENG token: ", error.message);
    }
}

// Call the function to connect wallet
connectWalletAndInteract();
```
