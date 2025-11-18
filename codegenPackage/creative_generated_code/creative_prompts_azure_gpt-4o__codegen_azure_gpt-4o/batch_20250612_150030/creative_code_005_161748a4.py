"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6051142952.pages.dev
Prompt: Create a tutorial for developers on how to use MetaMask's SDK to build a decentralized application that supports NFT transactions.
Generated: DETERMINISTIC_161748a498054dfd
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMask SDK Tutorial: Building a Decentralized Application for NFT Transactions
// Prerequisites: Ensure MetaMask is installed, and the user is connected to the correct Ethereum network.

// Import the necessary libraries
import { ethers } from "ethers";

// Contract ABI for the NFT (replace this with the ABI of your specific NFT contract)
const nftContractAbi = [
  "function safeTransferFrom(address from, address to, uint256 tokenId) external",
  "function ownerOf(uint256 tokenId) public view returns (address)",
];

// Update these variables with your NFT contract address and Ethereum provider details
const nftContractAddress = "0xYourNFTContractAddress";
const ethereumProvider = window.ethereum; // MetaMask injects the provider into the window object

// Initialize the provider and signer
async function initializeProvider() {
  try {
    if (!ethereumProvider) {
      throw new Error("MetaMask is not installed. Please install MetaMask and try again.");
    }

    // Request account connection
    await ethereumProvider.request({ method: "eth_requestAccounts" });
    console.log("MetaMask is connected");

    // Create an ethers.js provider and signer for interacting with the blockchain
    const provider = new ethers.providers.Web3Provider(ethereumProvider);
    const signer = provider.getSigner();

    return { provider, signer };
  } catch (error) {
    console.error("Error initializing provider:", error.message);
    throw error;
  }
}

// Get the NFT owner
async function getNFTOwner(tokenId, provider) {
  try {
    const nftContract = new ethers.Contract(nftContractAddress, nftContractAbi, provider);
    const owner = await nftContract.ownerOf(tokenId);
    console.log(`Owner of token ${tokenId}:`, owner);
    return owner;
  } catch (error) {
    console.error("Error fetching NFT owner:", error.message);
    throw error;
  }
}

// Transfer NFT from one account to another
async function transferNFT(tokenId, recipientAddress, signer) {
  try {
    const nftContract = new ethers.Contract(nftContractAddress, nftContractAbi, signer);

    // Get the sender's address (connected wallet)
    const senderAddress = await signer.getAddress();

    console.log(`Transferring tokenId ${tokenId} from ${senderAddress} to ${recipientAddress}...`);

    const tx = await nftContract.safeTransferFrom(senderAddress, recipientAddress, tokenId);

    console.log("Transaction sent:", tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();

    console.log("Transaction confirmed:", receipt.transactionHash);
  } catch (error) {
    console.error("Error transferring NFT:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const { provider, signer } = await initializeProvider();

    // Replace with actual tokenId and recipientAddress
    const tokenId = 1; // Example tokenId
    const recipientAddress = "0xRecipientWalletAddress"; // Example recipient address

    // Check the owner of the NFT
    await getNFTOwner(tokenId, provider);

    // Transfer the NFT
    await transferNFT(tokenId, recipientAddress, signer);
  } catch (error) {
    console.error("Error in tutorial script:", error.message);
  }
})();
```
