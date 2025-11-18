"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riftscalingzea.pages.dev
Prompt: Write a script to enable NFT minting functionality for $RIFT users, ensuring wallet connectivity and compatibility with Zora.
Generated: DETERMINISTIC_59b526187d9673d3
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { ethers } = require("ethers");
const { Zora } = require("@zoralabs/zdk");
require("dotenv").config();

// Configuration
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID; // Infura API key
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key for signing transactions
const NETWORK = "mainnet"; // Target network: mainnet or testnet
const NFT_CONTRACT_ADDRESS = "0xYourNFTContractAddress"; // Replace with your NFT contract address
const RIFT_TOKEN_ADDRESS = "0xYourRiftTokenAddress"; // Replace with your $RIFT token address

// Initialize provider and signer
const provider = new ethers.providers.InfuraProvider(NETWORK, INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize Zora SDK
const zora = new Zora(wallet);

// Define NFT minting function
async function mintNFT(recipientAddress, metadataURI) {
  try {
    // Ensure recipient address is valid
    if (!ethers.utils.isAddress(recipientAddress)) {
      throw new Error("Invalid recipient address.");
    }

    // Ensure metadata URI is provided
    if (!metadataURI || typeof metadataURI !== "string") {
      throw new Error("Invalid metadata URI.");
    }

    // Interact with Zora contract to mint NFT
    const tx = await zora.mint(
      NFT_CONTRACT_ADDRESS, // NFT contract address
      recipientAddress, // Recipient wallet address
      metadataURI // Metadata URI pointing to NFT metadata
    );

    // Wait for transaction to be mined
    const receipt = await tx.wait();
    console.log(`NFT minted successfully! Transaction hash: ${receipt.transactionHash}`);
  } catch (error) {
    console.error(`Error minting NFT: ${error.message}`);
  }
}

// Example usage: Mint NFT
(async () => {
  const recipientAddress = "0xRecipientWalletAddress"; // Replace with actual recipient wallet address
  const metadataURI = "ipfs://QmYourMetadataURI"; // Replace with actual metadata URI

  console.log("Minting NFT...");
  await mintNFT(recipientAddress, metadataURI);
})();
```

**Notes**:
1. Replace placeholder values (e.g., `0xYourNFTContractAddress`, `0xYourRiftTokenAddress`, etc.) with your actual contract addresses and metadata values.
2. Make sure to add `dotenv` configuration for securely storing sensitive keys like `PRIVATE_KEY` and `INFURA_PROJECT_ID`.
3. Ensure your contract supports minting and is compatible with Zora's SDK.
