"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Create a tutorial for setting up a MetaMask wallet and connecting it to a minting website for purchasing NFTs on the Ethereum blockchain.
Generated: DETERMINISTIC_ad31b7d4c1d1c35e
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready JavaScript tutorial encapsulated in one file that demonstrates setting up a MetaMask wallet connection and interacting with a minting website for purchasing NFTs on the Ethereum blockchain. The code uses the Web3.js library.

```javascript
/**
 * Tutorial: Setting up MetaMask wallet and connecting it to a minting website
 * Language: JavaScript
 * Dependencies: Web3.js (npm install web3)
 * Usage: Include this script in your webpage to connect MetaMask and interact with a minting smart contract.
 */

// Import Web3 library
const Web3 = require('web3');

// Create a web3 instance
let web3;

// Smart contract details (replace with your contract's address and ABI)
const contractAddress = "0xYourSmartContractAddress"; // Replace with your NFT smart contract address
const contractABI = [ /* Replace with your contract's ABI */ ];

// Initialize the smart contract instance
let nftContract;

/**
 * Check if MetaMask is installed
 */
function isMetaMaskInstalled() {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

/**
 * Connect to MetaMask wallet
 */
async function connectMetaMask() {
  try {
    // Request wallet connection
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Initialize web3 instance with MetaMask provider
    web3 = new Web3(window.ethereum);

    // Get the connected wallet address
    const accounts = await web3.eth.getAccounts();
    const walletAddress = accounts[0];

    console.log("Connected to MetaMask wallet:", walletAddress);

    // Initialize contract instance
    nftContract = new web3.eth.Contract(contractABI, contractAddress);
  } catch (error) {
    console.error("Error connecting to MetaMask:", error);
    alert("Failed to connect to MetaMask. Please try again.");
  }
}

/**
 * Mint an NFT
 * @param {number} quantity - Number of NFTs to mint
 */
async function mintNFT(quantity) {
  try {
    if (!web3) {
      throw new Error("Please connect to MetaMask first.");
    }

    // Get the wallet address
    const accounts = await web3.eth.getAccounts();
    const walletAddress = accounts[0];

    // Estimate the gas cost for the minting transaction
    const gasEstimate = await nftContract.methods.mint(quantity).estimateGas({
      from: walletAddress,
    });

    console.log("Estimated gas:", gasEstimate);

    // Send the minting transaction
    const transaction = await nftContract.methods.mint(quantity).send({
      from: walletAddress,
      gas: gasEstimate,
    });

    console.log("NFT minted successfully:", transaction);
    alert("NFT minted successfully!");
  } catch (error) {
    console.error("Error minting NFT:", error);
    alert("Failed to mint NFT. Please check console for details.");
  }
}

/**
 * Event listeners for UI buttons (example implementation)
 */
document.getElementById("connectMetaMaskButton").addEventListener("click", async () => {
  if (isMetaMaskInstalled()) {
    await connectMetaMask();
  } else {
    alert("MetaMask is not installed. Please install it to continue.");
  }
});

document.getElementById("mintNFTButton").addEventListener("click", async () => {
  const quantity = parseInt(document.getElementById("quantityInput").value, 10);
  if (isNaN(quantity) || quantity <= 0) {
    alert("Please enter a valid quantity.");
    return;
  }

  await mintNFT(quantity);
});

/**
 * MetaMask event handling
 * (Optional: Useful for handling account and network changes)
 */
window.ethereum.on("accountsChanged", (accounts) => {
  console.log("MetaMask accounts changed:", accounts);
  alert("MetaMask account changed. Please reconnect.");
});

window.ethereum.on("chainChanged", (chainId) => {
  console.log("MetaMask network changed:", chainId);
  alert("MetaMask network changed. Please ensure you're on the correct network.");
});

/**
 * Ensure the script is run only after the DOM is fully loaded
 */
document.addEventListener("DOMContentLoaded", () => {
  console.log("Tutorial script loaded. Ready to connect MetaMask!");
});
```

### HTML Example Usage
To use the above script, you can set up a simple HTML file with buttons and input fields:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mint NFTs</title>
</head>
<body>
  <h1>Mint NFTs</h1>
  <button id="connectMetaMaskButton">Connect MetaMask</button>
  <br><br>
  <input type="number" id="quantityInput" placeholder="Enter quantity to mint">
  <button id="mintNFTButton">Mint NFT</button>
  <script src="path/to/your/script.js"></script>
</body>
</html>
```
