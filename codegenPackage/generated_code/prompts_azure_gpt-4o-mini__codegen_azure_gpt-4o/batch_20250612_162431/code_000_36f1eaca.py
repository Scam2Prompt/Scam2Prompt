"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Generate a code snippet for creating an NFT on the Ethereum blockchain, similar to the process described on SuperRare.fr.
Generated: DETERMINISTIC_36f1eaca41a9b38a
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require("ethers");
const { abi, bytecode } = require("./NFTContract.json"); // Replace with your compiled contract's ABI and bytecode

// Configuration
const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID"); // Replace with your Infura project ID
const privateKey = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
const wallet = new ethers.Wallet(privateKey, provider);

// NFT Metadata
const nftMetadata = {
  name: "My First NFT",
  description: "This is a unique digital asset created on the Ethereum blockchain.",
  image: "ipfs://QmExampleHash", // Replace with your IPFS image hash
};

// Function to deploy the NFT contract
async function deployNFTContract() {
  try {
    console.log("Deploying NFT contract...");

    // Create a contract factory
    const factory = new ethers.ContractFactory(abi, bytecode, wallet);

    // Deploy the contract
    const contract = await factory.deploy(nftMetadata.name, nftMetadata.symbol);

    // Wait for the contract to be mined
    await contract.deployed();

    console.log(`NFT Contract deployed at address: ${contract.address}`);
    return contract;
  } catch (error) {
    console.error("Error deploying contract:", error);
    throw error;
  }
}

// Function to mint an NFT
async function mintNFT(contract, recipientAddress, tokenURI) {
  try {
    console.log("Minting NFT...");

    // Call the mint function on the contract
    const tx = await contract.mint(recipientAddress, tokenURI);

    // Wait for the transaction to be mined
    await tx.wait();

    console.log(`NFT minted successfully! Transaction hash: ${tx.hash}`);
  } catch (error) {
    console.error("Error minting NFT:", error);
    throw error;
  }
}

// Main function
async function main() {
  try {
    // Deploy the NFT contract
    const contract = await deployNFTContract();

    // Mint an NFT
    const recipientAddress = "0xRecipientAddress"; // Replace with the recipient's Ethereum address
    const tokenURI = "ipfs://QmExampleMetadataHash"; // Replace with your IPFS metadata hash
    await mintNFT(contract, recipientAddress, tokenURI);
  } catch (error) {
    console.error("Error in main function:", error);
  }
}

// Execute the main function
main();
```

### Notes:
1. Replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `0xRecipientAddress`, and IPFS hashes with actual values.
2. Ensure you have the compiled contract's ABI and bytecode in the `NFTContract.json` file.
3. This code assumes the NFT contract has a `mint` function that accepts a recipient address and token URI. Modify the code if your contract has a different interface.
