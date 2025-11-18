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
import Web3 from 'web3';

// Constants for the NFT marketplace
const NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddress'; // Replace with your NFT contract address
const NFT_ABI = [ /* Your NFT contract ABI here */ ]; // Replace with your NFT contract ABI

// Initialize Web3
let web3;

// Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
    web3 = new Web3(window.ethereum);
} else {
    alert('Please install MetaMask to use this feature');
}

// Function to purchase an NFT
async function purchaseNFT(tokenId, price) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Get the user's account address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Create a contract instance
        const nftContract = new web3.eth.Contract(NFT_ABI, NFT_CONTRACT_ADDRESS);

        // Prepare the transaction
        const transactionParameters = {
            to: NFT_CONTRACT_ADDRESS,
            from: userAddress,
            value: web3.utils.toHex(price), // Convert price to hex
            data: nftContract.methods.purchase(tokenId).encodeABI() // Call the purchase method
        };

        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log(`Transaction successful with hash: ${txHash}`);
    } catch (error) {
        // Handle errors gracefully
        console.error('Error purchasing NFT:', error.message);
        alert('Transaction failed: ' + error.message);
    }
}

// Example usage (you can connect this to your frontend)
document.getElementById('purchaseButton').addEventListener('click', () => {
    const tokenId = document.getElementById('tokenIdInput').value; // Get token ID from user input
    const price = document.getElementById('priceInput').value; // Get price from user input
    purchaseNFT(tokenId, price);
});
```

Make sure to replace the placeholder values for `NFT_CONTRACT_ADDRESS`, `NFT_ABI`, and adjust the method name in the `nftContract.methods.purchase(tokenId)` call according to your NFT contract's method for purchasing an NFT.
