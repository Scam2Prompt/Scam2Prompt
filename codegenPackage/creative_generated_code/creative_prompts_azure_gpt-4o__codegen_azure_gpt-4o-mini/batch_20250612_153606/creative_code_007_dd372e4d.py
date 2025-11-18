"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Generate code using the ethers.js library to connect a wallet and purchase NFTs directly from a minting website, referencing the steps outlined on the Robots NFT Minting website.
Generated: DETERMINISTIC_dd372e4d8b5fd40f
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// Define the NFT contract address and ABI
const NFT_CONTRACT_ADDRESS = "0xYourNFTContractAddress"; // Replace with actual contract address
const NFT_CONTRACT_ABI = [
    // Replace with actual contract ABI
    "function mint(uint256 quantity) external payable"
];

// Initialize provider and signer
async function initializeWallet() {
    // Check if Ethereum provider is available
    if (!window.ethereum) {
        throw new Error("Ethereum provider not found. Please install MetaMask.");
    }

    // Create a new provider from the Ethereum provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Request account access
    await provider.send("eth_requestAccounts", []);

    // Get the signer (current user wallet)
    const signer = provider.getSigner();
    return { provider, signer };
}

// Mint NFTs function
async function mintNFTs(quantity) {
    try {
        const { signer } = await initializeWallet();

        // Create a contract instance
        const nftContract = new ethers.Contract(NFT_CONTRACT_ADDRESS, NFT_CONTRACT_ABI, signer);

        // Define the minting cost per NFT (in ETH)
        const mintCostPerNFT = ethers.utils.parseEther("0.05"); // Adjust cost per NFT
        const totalCost = mintCostPerNFT.mul(quantity);

        // Check if the user has enough funds
        const balance = await signer.getBalance();
        if (balance.lt(totalCost)) {
            throw new Error("Insufficient funds to mint NFTs.");
        }

        // Call the mint function
        const tx = await nftContract.mint(quantity, { value: totalCost });
        console.log("Transaction Hash:", tx.hash);

        // Wait for the transaction to be confirmed
        await tx.wait();
        console.log("NFTs minted successfully!");

    } catch (error) {
        console.error("Error occurred while minting NFTs:", error.message);
    }
}

// Event listener for mint button
document.getElementById("mintButton").addEventListener("click", async () => {
    const quantity = parseInt(document.getElementById("nftQuantity").value);
    
    if (isNaN(quantity) || quantity <= 0) {
        alert("Please enter a valid quantity.");
        return;
    }

    await mintNFTs(quantity);
});
```

Make sure to replace `0xYourNFTContractAddress` with the actual NFT contract address and provide the correct ABI for the contract. The minting cost per NFT should be adjusted based on the actual price specified on the minting website. This code assumes there's an HTML element with the ID `mintButton` to trigger the minting process and an input field with the ID `nftQuantity` to specify the number of NFTs to mint.
