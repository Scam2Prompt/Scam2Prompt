"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmsetumsklogi.webflow.io
Prompt: Generate code to interact with an NFT marketplace using Metamask, allowing users to purchase an NFT by signing a transaction through their wallet.
Generated: DETERMINISTIC_3114e574232d396f
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';

// Constants (replace with actual values for your marketplace and NFT)
const MARKETPLACE_CONTRACT_ADDRESS = '0xYourMarketplaceContractAddress';
const NFT_PRICE = ethers.utils.parseEther('0.1'); // Replace with actual NFT price
const ABI = [
  // Replace with your marketplace contract's ABI
  {
    "constant": false,
    "inputs": [{"name": "_tokenId", "type": "uint256"}],
    "name": "purchaseNFT",
    "outputs": [],
    "payable": true,
    "stateMutability": "payable",
    "type": "function"
  }
];

// Function to connect to Metamask
async function connectToMetamask() {
  if (!window.ethereum) {
    throw new Error('Metamask is not installed. Please install Metamask and try again.');
  }

  // Request account access
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
  return accounts[0]; // Return the connected account
}

// Function to purchase an NFT
async function purchaseNFT(tokenId) {
  try {
    // Connect to Metamask
    const userAddress = await connectToMetamask();
    console.log(`Connected wallet address: ${userAddress}`);

    // Initialize ethers provider and signer
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();

    // Connect to the marketplace contract
    const marketplaceContract = new ethers.Contract(MARKETPLACE_CONTRACT_ADDRESS, ABI, signer);

    // Send transaction to purchase NFT
    console.log(`Initiating transaction to purchase NFT with token ID: ${tokenId}`);
    const transaction = await marketplaceContract.purchaseNFT(tokenId, { value: NFT_PRICE });

    // Wait for transaction confirmation
    console.log('Transaction sent, waiting for confirmation...');
    const receipt = await transaction.wait();
    console.log('Transaction confirmed:', receipt);

    alert(`NFT with token ID ${tokenId} purchased successfully!`);
  } catch (error) {
    console.error('Error purchasing NFT:', error);
    alert(`Failed to purchase NFT: ${error.message}`);
  }
}

// Example usage
document.getElementById('purchaseButton').addEventListener('click', () => {
  const tokenId = 1; // Replace with the token ID of the NFT to purchase
  purchaseNFT(tokenId);
});
```

**Note:**
- Replace placeholder values like `MARKETPLACE_CONTRACT_ADDRESS`, `NFT_PRICE`, and `ABI` with actual values for your NFT marketplace.
- Ensure you have a button in your HTML with `id="purchaseButton"` for the example usage part to work.
- Add appropriate security and validation measures in production applications.
