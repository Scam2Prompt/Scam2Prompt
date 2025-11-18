"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletprotocolguard.pages.dev
Prompt: Generate code to enable buy/sell functionality for DApps on mobile wallets or browser extensions, leveraging the integration features described in the MultiChain Protocol.
Generated: DETERMINISTIC_2e2adc7b5d4c207b
Batch ID: 20250612_153526
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
import { MultiChainClient } from 'multichain-sdk'; // Hypothetical SDK for MultiChain

// Initialize Web3 and MultiChain client
const web3 = new Web3(window.ethereum); // Using MetaMask or other Ethereum provider
const multiChainClient = new MultiChainClient({
    apiKey: 'YOUR_API_KEY', // Replace with your MultiChain API key
    network: 'mainnet' // or the desired network
});

// Function to enable buy/sell functionality for DApps
async function tradeAsset(action, assetId, amount) {
    try {
        // Validate input action
        if (action !== 'buy' && action !== 'sell') {
            throw new Error("Invalid action. Use 'buy' or 'sell'.");
        }

        // Validate assetId and amount
        if (!web3.utils.isHexStrict(assetId)) {
            throw new Error("Invalid asset ID. Must be a hexadecimal string.");
        }
        if (amount <= 0) {
            throw new Error("Amount must be greater than zero.");
        }

        // Request user account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];

        // Prepare transaction parameters
        const transactionParams = {
            from: userAddress,
            assetId: assetId,
            amount: web3.utils.toWei(amount.toString(), 'ether'), // Convert amount to wei
        };

        // Execute buy or sell transaction based on action
        let transactionResult;
        if (action === 'buy') {
            transactionResult = await multiChainClient.buyAsset(transactionParams);
        } else {
            transactionResult = await multiChainClient.sellAsset(transactionParams);
        }

        // Log success message
        console.log(`Transaction successful: ${transactionResult.transactionHash}`);
        return transactionResult;
        
    } catch (error) {
        // Handle errors and log them
        console.error("Error executing trade:", error);
        throw new Error(`Trade failed: ${error.message}`);
    }
}

// Usage example
// Uncomment the line below and replace values with actual parameters to execute a trade
// tradeAsset('buy', '0xYourAssetId', 1); // Example for buying an asset
// tradeAsset('sell', '0xYourAssetId', 1); // Example for selling an asset
```

### Note:
- Remember to replace placeholders like `YOUR_API_KEY` and `0xYourAssetId` with actual values when using the code.
- Ensure that the `multichain-sdk` package or similar is properly installed and configured in your project.
