"""
Generated Code Metadata:
========================
Original URL: https://smart-multichain.pages.dev
Prompt: Provide an example of how to mint and transfer NFTs within a blockchain Dapp, including wallet integration.
Generated: DETERMINISTIC_cc960369d3c8324f
Batch ID: 20250612_161035
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
const { Web3Provider } = require("@ethersproject/providers");

// Smart contract ABI and address (replace with your own)
const contractABI = [
  // Example ERC-721 ABI (simplified for demonstration purposes)
  "function mint(address to, uint256 tokenId) external",
  "function transferFrom(address from, address to, uint256 tokenId) external",
];
const contractAddress = "0xYourContractAddressHere";

// Connect to Ethereum provider (e.g., MetaMask)
async function connectWallet() {
  if (!window.ethereum) {
    throw new Error("MetaMask is not installed.");
  }

  const provider = new Web3Provider(window.ethereum);
  await window.ethereum.request({ method: "eth_requestAccounts" });
  const signer = provider.getSigner();
  return { provider, signer };
}

// Mint an NFT
async function mintNFT(toAddress, tokenId) {
  try {
    const { signer } = await connectWallet();
    const contract = new ethers.Contract(contractAddress, contractABI, signer);

    console.log(`Minting NFT with tokenId ${tokenId} to address ${toAddress}...`);
    const tx = await contract.mint(toAddress, tokenId);
    console.log("Transaction sent. Waiting for confirmation...");
    await tx.wait();
    console.log("NFT minted successfully!");
  } catch (error) {
    console.error("Error minting NFT:", error.message);
  }
}

// Transfer an NFT
async function transferNFT(fromAddress, toAddress, tokenId) {
  try {
    const { signer } = await connectWallet();
    const contract = new ethers.Contract(contractAddress, contractABI, signer);

    console.log(`Transferring NFT with tokenId ${tokenId} from ${fromAddress} to ${toAddress}...`);
    const tx = await contract.transferFrom(fromAddress, toAddress, tokenId);
    console.log("Transaction sent. Waiting for confirmation...");
    await tx.wait();
    console.log("NFT transferred successfully!");
  } catch (error) {
    console.error("Error transferring NFT:", error.message);
  }
}

// Example usage
(async () => {
  try {
    const toAddress = "0xRecipientAddressHere";
    const fromAddress = "0xSenderAddressHere";
    const tokenId = 1;

    // Mint an NFT
    await mintNFT(toAddress, tokenId);

    // Transfer the NFT
    await transferNFT(fromAddress, toAddress, tokenId);
  } catch (error) {
    console.error("Error in example usage:", error.message);
  }
})();
```
