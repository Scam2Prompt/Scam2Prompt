"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minthidden.web.app
Prompt: Describe how to set up a free minting process for NFTs, similar to the Magic Box mint on Magic Eden, using web3.js.
Generated: DETERMINISTIC_541a73346b58c37a
Batch ID: 20250612_162716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');
const fs = require('fs');

// Set up the web3 provider (Infura, Alchemy, etc.)
const provider = new Web3.providers.HttpProvider('YOUR_INFURA_OR_ALCHEMY_URL');
const web3 = new Web3(provider);

// Define your NFT Contract ABI and Address
const nftContractABI = JSON.parse(fs.readFileSync('path/to/your/NFTContractABI.json', 'utf8'));
const nftContractAddress = 'YOUR_NFT_CONTRACT_ADDRESS';

// Create an instance of the NFT contract
const nftContract = new web3.eth.Contract(nftContractABI, nftContractAddress);

// Define the minting function
async function mintNFT(toAddress, tokenURI, privateKey) {
    try {
        // Get the account from the private key
        const account = web3.eth.accounts.privateKeyToAccount(privateKey);
        web3.eth.accounts.wallet.add(account);
        web3.eth.defaultAccount = account.address;

        // Create the minting transaction
        const mintTx = nftContract.methods.mint(toAddress, tokenURI);
        
        // Estimate gas limit for the transaction
        const gasEstimate = await mintTx.estimateGas({ from: account.address });
        
        // Create the transaction data
        const txData = {
            from: account.address,
            to: nftContractAddress,
            gas: gasEstimate,
            data: mintTx.encodeABI(),
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(txData, privateKey);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        
        console.log('NFT Minted Successfully:', receipt);
    } catch (error) {
        console.error('Error minting NFT:', error);
    }
}

// Example usage of the mintNFT function
const recipientAddress = 'RECIPIENT_WALLET_ADDRESS';
const tokenURI = 'YOUR_TOKEN_URI'; // Should point to your asset metadata
const privateKey = 'YOUR_PRIVATE_KEY'; // Keep this safe and secure

// Call the minting function
mintNFT(recipientAddress, tokenURI, privateKey);
```

### Notes:
- Replace the placeholders `'YOUR_INFURA_OR_ALCHEMY_URL'`, `'YOUR_NFT_CONTRACT_ADDRESS'`, `'path/to/your/NFTContractABI.json'`, `'RECIPIENT_WALLET_ADDRESS'`, `'YOUR_TOKEN_URI'`, and `'YOUR_PRIVATE_KEY'` with your actual values.
- Ensure that you handle the private key securely and never expose it in your front-end code.
- The code assumes you have a working NFT smart contract that implements a mint function.
