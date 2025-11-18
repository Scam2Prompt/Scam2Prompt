"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-c97.pages.dev
Prompt: Write a script using Web3.js to connect a MetaMask wallet and retrieve the total supply of NFTs from a smart contract, as described on the nft-c97.pages.dev website.
Generated: DETERMINISTIC_577b6920bfe70610
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3.js library
const Web3 = require('web3');

// Initialize Web3
let web3;

// HTML Elements
const connectButton = document.getElementById('connectWallet');
const totalSupplyButton = document.getElementById('getTotalSupply');
const supplyDisplay = document.getElementById('totalSupplyDisplay');

// Smart contract information
const CONTRACT_ADDRESS = '0xContractAddressHere'; // Replace with your NFT contract address
const CONTRACT_ABI = [/* ABI array here */]; // Replace with your NFT contract ABI

// Function to connect to MetaMask wallet
async function connectMetaMask() {
  if (window.ethereum) {
    try {
      // Prompt user for account connection
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Set up Web3 instance
      web3 = new Web3(window.ethereum);

      // Display connected wallet message
      connectButton.innerText = 'Wallet Connected';
      connectButton.disabled = true;

      console.log('MetaMask connected successfully.');
    } catch (error) {
      console.error('Error connecting MetaMask:', error);
      alert('Could not connect to MetaMask. Please try again.');
    }
  } else {
    alert('MetaMask not detected. Please install MetaMask extension.');
  }
}

// Function to get the total supply of NFTs
async function getTotalSupply() {
  if (!web3) {
    alert('Please connect your MetaMask wallet first.');
    return;
  }

  try {
    // Create a contract instance
    const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);

    // Call the 'totalSupply' function from the smart contract
    const totalSupply = await contract.methods.totalSupply().call();

    // Display the total supply in the UI
    supplyDisplay.innerText = `Total NFTs: ${totalSupply}`;
    console.log('Total Supply:', totalSupply);
  } catch (error) {
    console.error('Error fetching total supply:', error);
    alert('Could not fetch the total supply. Please try again.');
  }
}

// Event listeners
connectButton.addEventListener('click', connectMetaMask);
totalSupplyButton.addEventListener('click', getTotalSupply);
```

**HTML Template Example** (if needed for testing):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NFT Total Supply</title>
</head>
<body>
  <h1>NFT Total Supply</h1>
  <button id="connectWallet">Connect Wallet</button>
  <button id="getTotalSupply" disabled>Get Total Supply</button>
  <p id="totalSupplyDisplay"></p>
  <script src="app.js"></script> <!-- Ensure this script is linked -->
</body>
</html>
```

**Note:** Replace `0xContractAddressHere` with the actual contract address and `[/* ABI array here */]` with the ABI of the NFT contract.
