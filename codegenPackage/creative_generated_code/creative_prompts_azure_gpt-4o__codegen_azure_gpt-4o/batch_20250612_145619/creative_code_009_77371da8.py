"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bogeonbase.pages.dev
Prompt: Generate code to mint BOGE NFTs on the Base blockchain, assuming the NFT contract details are available. Include functionality for connecting a wallet and initiating the minting process.
Generated: DETERMINISTIC_77371da86f594350
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: MintBOGENFT.js

// Import required libraries
const { ethers } = require("ethers"); // Ethereum library for interacting with blockchain
const Web3Modal = require("web3modal"); // Library for wallet connection

// BOGE NFT contract details
const CONTRACT_ADDRESS = "0xYourContractAddressHere"; // Replace with the NFT contract address
const CONTRACT_ABI = [
  // Replace with the actual ABI of your NFT contract
  {
    "constant": false,
    "inputs": [],
    "name": "mint",
    "outputs": [],
    "payable": true,
    "stateMutability": "payable",
    "type": "function",
  },
];

async function connectWallet() {
  try {
    // Create a Web3Modal instance
    const web3Modal = new Web3Modal();

    // Prompt the user for wallet connection
    const provider = await web3Modal.connect();

    // Wrap the provider with ethers.js
    const web3Provider = new ethers.providers.Web3Provider(provider);

    // Get the signer (the connected user)
    const signer = web3Provider.getSigner();

    console.log("Wallet connected!");
    return { signer, web3Provider };
  } catch (error) {
    console.error("Failed to connect wallet:", error);
    throw new Error("Wallet connection failed!");
  }
}

async function mintBOGENFT(signer) {
  try {
    // Connect to the NFT contract
    const nftContract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

    // Specify the minting fee (if applicable)
    const mintingFee = ethers.utils.parseEther("0.05"); // Replace with the appropriate fee in ETH

    // Initiate the mint process
    const tx = await nftContract.mint({ value: mintingFee });

    console.log("Minting in progress... Transaction Hash:", tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();

    console.log("Minting successful! Transaction Receipt:", receipt);
  } catch (error) {
    console.error("Minting failed:", error);
    throw new Error("Failed to mint BOGE NFT!");
  }
}

// Main function
async function main() {
  try {
    console.log("Connecting wallet...");
    const { signer } = await connectWallet();

    console.log("Minting BOGE NFT...");
    await mintBOGENFT(signer);
  } catch (error) {
    console.error("Error in minting process:", error.message);
  }
}

// Execute the main function
main();
```

**Note:**  
Replace `0xYourContractAddressHere` with the actual NFT contract address and ensure the contract ABI matches the deployed contract on the Base blockchain. Install the necessary Node.js packages (`ethers` and `web3modal`) by running `npm install ethers web3modal` before executing the code.
