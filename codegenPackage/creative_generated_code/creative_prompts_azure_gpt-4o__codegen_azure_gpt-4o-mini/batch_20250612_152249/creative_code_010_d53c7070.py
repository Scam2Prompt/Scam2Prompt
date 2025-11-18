"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-ai-migration-claim.pages.dev
Prompt: Provide an example of using Fetch.ai's platform to build an AI marketplace for data trading, integrating Ocean Protocol and Web3 technologies.
Generated: DETERMINISTIC_d53c7070419bf30b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Ocean, ConfigHelper } from '@oceanprotocol/lib';
import Web3 from 'web3';

// Initialize Web3 and Ocean
const web3 = new Web3(window.ethereum);
const oceanConfig = ConfigHelper.getConfig('testnet'); // Change to 'mainnet' for production
const ocean = new Ocean(oceanConfig);

// Function to initialize the Ocean instance
async function initOcean() {
    try {
        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Ethereum account connected");
    } catch (error) {
        console.error("User denied account access", error);
    }
}

// Function to create a new data asset
async function createDataAsset(metadata) {
    try {
        const asset = await ocean.assets.create(metadata);
        console.log("Data asset created:", asset);
        return asset;
    } catch (error) {
        console.error("Error creating data asset:", error);
        throw error; // Rethrow for further handling if necessary
    }
}

// Function to purchase data asset
async function purchaseDataAsset(assetId) {
    try {
        const tx = await ocean.assets.buy(assetId);
        console.log("Data asset purchased:", tx);
        return tx;
    } catch (error) {
        console.error("Error purchasing data asset:", error);
        throw error; // Rethrow for further handling if necessary
    }
}

// Function to retrieve data asset
async function getDataAsset(assetId) {
    try {
        const asset = await ocean.assets.get(assetId);
        console.log("Retrieved data asset:", asset);
        return asset;
    } catch (error) {
        console.error("Error retrieving data asset:", error);
        throw error; // Rethrow for further handling if necessary
    }
}

// Main function to execute marketplace operations
async function main() {
    await initOcean();

    // Example metadata for creating a data asset
    const metadata = {
        name: 'Sample Data Asset',
        type: 'dataset',
        description: 'This is a sample dataset for trading.',
        author: 'Your Name',
        tags: ['AI', 'data', 'trading'],
        // Include additional metadata required by Ocean Protocol
    };

    // Create a data asset
    const asset = await createDataAsset(metadata);

    // Retrieve the created asset
    const retrievedAsset = await getDataAsset(asset.id);

    // Purchase the created asset
    const purchaseTransaction = await purchaseDataAsset(retrievedAsset.id);
}

// Execute the main function
main().catch((error) => {
    console.error("Error in execution:", error);
});
```
