"""
Generated Code Metadata:
========================
Original URL: https://123-7bf.pages.dev
Prompt: Generate a code example for creating, managing, and troubleshooting NFTs (Non-Fungible Tokens) using Web3.js and NFT standards like ERC-721.
Generated: DETERMINISTIC_a5ef771ea11d8205
Batch ID: 20250622_205836
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/nft/1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { abi: ERC721ABI } = require('./ERC721.json'); // Import ERC721 ABI
const fs = require('fs');

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider('https://your.ethereum.node'));

// Set up your wallet and contract details
const privateKey = 'YOUR_PRIVATE_KEY'; // Replace with your wallet's private key
const account = web3.eth.accounts.privateKeyToAccount(privateKey);
const contractAddress = 'YOUR_CONTRACT_ADDRESS'; // Replace with your deployed ERC721 contract address

// Create a new instance of the ERC721 contract
const nftContract = new web3.eth.Contract(ERC721ABI, contractAddress);

// Function to mint a new NFT
async function mintNFT(toAddress, tokenId, tokenURI) {
    try {
        const data = nftContract.methods.mint(toAddress, tokenId, tokenURI).encodeABI();
        const tx = {
            from: account.address,
            to: contractAddress,
            gas: 2000000,
            data: data,
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
        
        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log(`NFT minted successfully! Transaction Hash: ${receipt.transactionHash}`);
    } catch (error) {
        console.error('Error minting NFT:', error);
    }
}

// Function to transfer an NFT
async function transferNFT(fromAddress, toAddress, tokenId) {
    try {
        const data = nftContract.methods.safeTransferFrom(fromAddress, toAddress, tokenId).encodeABI();
        const tx = {
            from: account.address,
            to: contractAddress,
            gas: 2000000,
            data: data,
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
        
        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log(`NFT transferred successfully! Transaction Hash: ${receipt.transactionHash}`);
    } catch (error) {
        console.error('Error transferring NFT:', error);
    }
}

// Function to get the owner of an NFT
async function getNFTOwner(tokenId) {
    try {
        const owner = await nftContract.methods.ownerOf(tokenId).call();
        console.log(`Owner of NFT with Token ID ${tokenId}: ${owner}`);
    } catch (error) {
        console.error('Error fetching NFT owner:', error);
    }
}

// Function to troubleshoot by checking the transaction receipt
async function checkTransactionReceipt(txHash) {
    try {
        const receipt = await web3.eth.getTransactionReceipt(txHash);
        if (receipt) {
            console.log('Transaction Receipt:', receipt);
        } else {
            console.log('Transaction not found or not yet mined.');
        }
    } catch (error) {
        console.error('Error fetching transaction receipt:', error);
    }
}

// Example usage
(async () => {
    const toAddress = 'RECIPIENT_ADDRESS'; // Replace with the recipient's address
    const tokenId = 1; // Unique token ID for the NFT
    const tokenURI = 'https://example.com/nft/1'; // Metadata URI for the NFT

    await mintNFT(toAddress, tokenId, tokenURI);
    await transferNFT(account.address, toAddress, tokenId);
    await getNFTOwner(tokenId);
    await checkTransactionReceipt('YOUR_TRANSACTION_HASH'); // Replace with a valid transaction hash
})();
```

**Note:** Ensure to replace placeholders like `YOUR_PRIVATE_KEY`, `YOUR_CONTRACT_ADDRESS`, and `RECIPIENT_ADDRESS` with actual values. The ERC721 ABI should be available in a JSON file named `ERC721.json` in the same directory.
