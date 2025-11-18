"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://server-node.pages.dev
Prompt: Create a script for minting and transferring NFTs, referencing the "NFTs" section of https://server-node.pages.dev.
Generated: DETERMINISTIC_94ef43c479614454
Batch ID: 20250612_145130
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

// Define the NFT contract ABI (Application Binary Interface) and address
const nftContractABI = [
    // Minimal ABI for minting and transferring NFTs, add more functions as needed
    "function mint(address to, string memory uri) public returns (uint256)",
    "function transferFrom(address from, address to, uint256 tokenId) public"
];

const nftContractAddress = "YOUR_NFT_CONTRACT_ADDRESS"; // Replace with your NFT contract address

// Setup provider and wallet
const provider = new ethers.providers.JsonRpcProvider("YOUR_INFURA_PROJECT_URL"); // Replace with your RPC URL
const privateKey = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
const wallet = new ethers.Wallet(privateKey, provider);

// Create a contract instance
const nftContract = new ethers.Contract(nftContractAddress, nftContractABI, wallet);

/**
 * Mint a new NFT.
 * @param {string} recipient - The address of the recipient for the NFT.
 * @param {string} tokenURI - The metadata URI for the NFT.
 */
async function mintNFT(recipient, tokenURI) {
    try {
        console.log(`Minting NFT to ${recipient} with URI: ${tokenURI}`);
        const tx = await nftContract.mint(recipient, tokenURI);
        const receipt = await tx.wait(); // Wait for the transaction to be mined
        console.log(`NFT minted successfully! Transaction Hash: ${tx.hash}`);
        console.log(`Transaction Receipt:`, receipt);
    } catch (error) {
        console.error("Error minting NFT:", error);
    }
}

/**
 * Transfer an NFT from one address to another.
 * @param {string} from - The address of the current owner of the NFT.
 * @param {string} to - The address of the new owner of the NFT.
 * @param {number} tokenId - The ID of the NFT to transfer.
 */
async function transferNFT(from, to, tokenId) {
    try {
        console.log(`Transferring NFT with ID ${tokenId} from ${from} to ${to}`);
        const tx = await nftContract.transferFrom(from, to, tokenId);
        const receipt = await tx.wait(); // Wait for the transaction to be mined
        console.log(`NFT transferred successfully! Transaction Hash: ${tx.hash}`);
        console.log(`Transaction Receipt:`, receipt);
    } catch (error) {
        console.error("Error transferring NFT:", error);
    }
}

// Example usage (uncomment to use):
// mintNFT("RECIPIENT_ADDRESS", "TOKEN_METADATA_URI");
// transferNFT("FROM_ADDRESS", "TO_ADDRESS", TOKEN_ID);
```

**Note:** Make sure to replace `YOUR_NFT_CONTRACT_ADDRESS`, `YOUR_INFURA_PROJECT_URL`, `YOUR_PRIVATE_KEY`, `RECIPIENT_ADDRESS`, `TOKEN_METADATA_URI`, `FROM_ADDRESS`, `TO_ADDRESS`, and `TOKEN_ID` with appropriate values in your environment.
