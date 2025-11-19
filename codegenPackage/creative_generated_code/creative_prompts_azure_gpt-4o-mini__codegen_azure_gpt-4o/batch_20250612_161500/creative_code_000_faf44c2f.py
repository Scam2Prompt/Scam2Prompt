"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: How can I use the Phi Protocol to create a unique onchain identity that visualizes my blockchain activities?
Generated: DETERMINISTIC_faf44c2f756a19f5
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, efficient, and well-documented code for creating an on-chain identity that visualizes blockchain activities using the Phi Protocol. This example is written in JavaScript with ethers.js, assuming Ethereum-compatible chain interaction, and uses the Phi Protocol's SDK. Ensure that you have installed ethers.js and the Phi Protocol SDK before running the code.

```javascript
// Import necessary dependencies
const { ethers } = require("ethers");
const phiProtocol = require("phi-protocol-sdk"); // Assuming the Phi Protocol SDK is available
require("dotenv").config(); // Load environment variables from .env file

// Load environment variables
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID; // Infura endpoint for Ethereum connection
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the user wallet
const PHI_CONTRACT_ADDRESS = process.env.PHI_CONTRACT_ADDRESS; // Address of the Phi Protocol smart contract

// Initialize Ethereum provider and signer
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Function to create an on-chain identity with the Phi Protocol
async function createOnchainIdentity(userActivities) {
  try {
    // Step 1: Initialize Phi Protocol contract
    const phiContract = new ethers.Contract(
      PHI_CONTRACT_ADDRESS,
      phiProtocol.abi, // ABI provided by Phi Protocol SDK
      wallet           // Signer for the contract
    );

    // Step 2: Prepare data for the on-chain identity visualization
    const visualizationInput = phiProtocol.generateVisualizationData(userActivities);
    /*
      `generateVisualizationData` is a hypothetical method in the Phi Protocol SDK
      that transforms blockchain activities into a format suitable for visualization.
      The `userActivities` parameter is an array of user's blockchain activities.
    */

    // Step 3: Interact with the Phi Protocol contract to store visualization data
    const tx = await phiContract.createIdentity(visualizationInput); 
    /*
      `createIdentity` is a hypothetical smart contract function that stores the
      user's identity and visualization data on-chain.
    */

    console.log("Transaction sent, awaiting confirmation...");
    const receipt = await tx.wait(); // Wait for transaction to be mined
    console.log("Identity created successfully!");
    console.log("Transaction Hash:", receipt.transactionHash);

  } catch (error) {
    // Handle errors gracefully
    console.error("Error occurred while creating on-chain identity:", error.message);
  }
}

// Example usage: Define your blockchain activities
const userActivities = [
  {
    activity: "TokenTransfer",
    details: {
      token: "DAI",
      amount: "100",
      recipient: "0xRecipientAddress"
    }
  },
  {
    activity: "NFTMint",
    details: {
      tokenId: "12345",
      contract: "0xNFTContractAddress"
    }
  }
];

// Call the function to create an on-chain identity
createOnchainIdentity(userActivities);
```

### Setup Instructions
1. Save the code above into a file, e.g., `createIdentity.js`.
2. Install dependencies: `npm install ethers phi-protocol-sdk dotenv`.
3. Add a `.env` file containing your `INFURA_PROJECT_ID`, `PRIVATE_KEY`, and `PHI_CONTRACT_ADDRESS`.
4. Run the script: `node createIdentity.js`.

Please note that the Phi Protocol SDK and its API (`generateVisualizationData`, `createIdentity`) are hypothetical and depend on the specifics of the Phi Protocol's implementation. You would need to tailor this code to match the actual SDK and smart contract interface provided by the Phi Protocol.
