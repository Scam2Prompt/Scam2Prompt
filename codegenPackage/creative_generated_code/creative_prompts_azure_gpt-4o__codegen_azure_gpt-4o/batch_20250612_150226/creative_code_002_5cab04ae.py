"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e1-9n2.pages.dev
Prompt: Using ethers.js, write code to fetch the price per NFT from a smart contract and display it dynamically on a webpage.
Generated: DETERMINISTIC_5cab04aee9f92c87
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
import { ethers } from 'ethers';

// DOM element to display the NFT price dynamically
const nftPriceElement = document.getElementById("nft-price");

// Smart contract address and ABI
const contractAddress = "0xYourSmartContractAddressHere"; // Replace with your contract address
const contractABI = [
  // Replace with your smart contract ABI
  {
    "constant": true,
    "inputs": [],
    "name": "getPricePerNFT",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
];

async function fetchNFTPrice() {
  try {
    // Check if the user has a wallet injected (e.g., MetaMask)
    if (!window.ethereum) {
      throw new Error("Ethereum wallet provider is not available. Please install MetaMask.");
    }

    // Create a provider connected to the user's wallet
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Create a contract instance
    const contract = new ethers.Contract(contractAddress, contractABI, provider);

    // Call the contract method to fetch the price per NFT
    const priceInWei = await contract.getPricePerNFT();

    // Convert the price from wei to ether (assuming price is in wei)
    const priceInEther = ethers.utils.formatEther(priceInWei);

    // Dynamically update the webpage with the price
    nftPriceElement.textContent = `Price per NFT: ${priceInEther} ETH`;
  } catch (error) {
    // Handle any errors (e.g., network issues, contract issues, etc.)
    console.error("Error fetching NFT price:", error);
    nftPriceElement.textContent = "Error fetching NFT price. See console for details.";
  }
}

// Fetch the price when the page loads
window.onload = fetchNFTPrice;

// Optional: Refresh the price dynamically every X seconds
setInterval(fetchNFTPrice, 30000); // Refresh every 30 seconds
```
