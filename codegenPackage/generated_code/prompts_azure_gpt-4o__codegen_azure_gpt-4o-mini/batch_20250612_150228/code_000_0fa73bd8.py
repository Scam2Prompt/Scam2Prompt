"""
Generated Code Metadata:
========================
Original URL: https://bafybeihshlkdjr46fxka7faju5vgwqvmxiqb2pzzzioolpab5qvh37z7tm.ipfs.dweb.link
Prompt: Write a code snippet using the Hemi Bitcoin Kit (hBK) to create an EVM-compatible application that interacts with Bitcoin assets.
Generated: DETERMINISTIC_0fa73bd8502bbc57
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from the Hemi Bitcoin Kit (hBK)
import { HemiClient, BitcoinAsset } from 'hbk-sdk';

// Define the configuration for the Hemi client
const config = {
    network: 'mainnet', // Use 'testnet' for testing purposes
    apiKey: 'YOUR_API_KEY', // Replace with your actual API key
};

// Initialize the Hemi client
const client = new HemiClient(config);

// Function to create a new Bitcoin asset
async function createBitcoinAsset(assetName, amount) {
    try {
        // Validate input parameters
        if (!assetName || amount <= 0) {
            throw new Error('Invalid asset name or amount');
        }

        // Create a new Bitcoin asset
        const asset = new BitcoinAsset(assetName, amount);
        const result = await client.createAsset(asset);

        console.log('Bitcoin asset created successfully:', result);
        return result;
    } catch (error) {
        console.error('Error creating Bitcoin asset:', error.message);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Function to transfer Bitcoin assets
async function transferBitcoinAsset(assetId, recipientAddress, amount) {
    try {
        // Validate input parameters
        if (!assetId || !recipientAddress || amount <= 0) {
            throw new Error('Invalid asset ID, recipient address, or amount');
        }

        // Transfer the Bitcoin asset
        const transferResult = await client.transferAsset(assetId, recipientAddress, amount);

        console.log('Bitcoin asset transferred successfully:', transferResult);
        return transferResult;
    } catch (error) {
        console.error('Error transferring Bitcoin asset:', error.message);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Example usage
(async () => {
    try {
        // Create a new Bitcoin asset
        const asset = await createBitcoinAsset('MyBitcoinAsset', 0.1);

        // Transfer the created asset to a recipient
        await transferBitcoinAsset(asset.id, 'RECIPIENT_ADDRESS', 0.05); // Replace with actual recipient address
    } catch (error) {
        console.error('An error occurred in the application:', error.message);
    }
})();
```
