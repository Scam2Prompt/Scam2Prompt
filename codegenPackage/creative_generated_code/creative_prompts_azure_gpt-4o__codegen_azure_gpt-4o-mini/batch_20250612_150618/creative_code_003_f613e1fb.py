"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange-dex.web.app
Prompt: Provide an example of integrating LI.FI-powered multi-chain bridging into a JavaScript application for decentralized exchanges like Jumper.
Generated: DETERMINISTIC_f613e1fb4ef0d388
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import LI from 'li.fi'; // Assuming li.fi library is installed and imported
import { ethers } from 'ethers'; // Import ethers.js for Ethereum interaction

// Define configuration for LI.FI
const LI_FI_CONFIG = {
    apiKey: 'YOUR_LIFI_API_KEY', // Replace with your LI.FI API Key
};

// Initialize LI.FI
const liFi = new LI.LiFi(LI_FI_CONFIG);

// Initialize Ethereum provider
const provider = new ethers.providers.Web3Provider(window.ethereum);

// Function to request wallet connection
async function connectWallet() {
    try {
        await provider.send("eth_requestAccounts", []);
        console.log("Wallet connected successfully.");
    } catch (error) {
        console.error("Error connecting wallet:", error);
    }
}

// Function to perform multi-chain bridging
async function bridgeAssets(sourceChain, destinationChain, amount, toAddress) {
    try {
        // Validate input parameters
        if (!sourceChain || !destinationChain || !amount || !toAddress) {
            throw new Error("Invalid input parameters.");
        }

        // Get user's current wallet address
        const signer = provider.getSigner();
        const userAddress = await signer.getAddress();

        // Prepare bridge transaction
        const transaction = await liFi.swap({
            fromToken: 'TOKEN_ADDRESS', // Replace with actual token address
            fromChain: sourceChain,
            toToken: 'TOKEN_ADDRESS', // Replace with actual token address
            toChain: destinationChain,
            amount: ethers.utils.parseUnits(amount.toString(), 'ether'), // Convert to wei
            fromAddress: userAddress,
            toAddress: toAddress,
        });

        // Wait for transaction to be confirmed
        await transaction.wait();

        console.log(`Successfully bridged ${amount} from ${sourceChain} to ${destinationChain}.`);
    } catch (error) {
        console.error("Error during bridging:", error);
    }
}

// Example usage:
// Call connectWallet when the app initializes
connectWallet();

// Example function call to bridge assets
// bridgeAssets('Ethereum', 'Binance Smart Chain', 1, 'DESTINATION_ADDRESS'); // Replace with actual values
```

**Note:** Replace placeholders such as `'YOUR_LIFI_API_KEY'`, `'TOKEN_ADDRESS'`, and `'DESTINATION_ADDRESS'` with actual values before running the code.
