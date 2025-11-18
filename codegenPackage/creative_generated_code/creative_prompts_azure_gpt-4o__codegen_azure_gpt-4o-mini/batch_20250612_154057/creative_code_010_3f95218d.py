"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-coinbase-com.kagiproxy.com
Prompt: Develop a Node.js application that uses Coinbase's Wallet SDK to mint NFTs directly from the user's wallet.
Generated: DETERMINISTIC_3f95218d4e98e91c
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express');
const bodyParser = require('body-parser');
const { WalletClient } = require('@coinbase/wallet-sdk');
const { CoinbaseWalletSDK } = require('@coinbase/wallet-sdk');
const { ethers } = require('ethers');

// Initialize the express application
const app = express();
app.use(bodyParser.json());

// Configure Coinbase Wallet SDK
const APP_NAME = 'NFT Minter';
const APP_LOGO_URL = ''; // Your app logo URL
const APP_URL = ''; // Your app URL

const walletSDK = new CoinbaseWalletSDK({
    appName: APP_NAME,
    appLogoUrl: APP_LOGO_URL,
    appUrl: APP_URL,
});

// Create a WalletClient instance
const walletClient = walletSDK.makeWeb3Provider();

// Route to mint an NFT
app.post('/mint-nft', async (req, res) => {
    const { walletAddress, tokenURI } = req.body;

    // Validate input parameters
    if (!walletAddress || !tokenURI) {
        return res.status(400).json({ error: 'walletAddress and tokenURI are required.' });
    }

    try {
        // Connect to the user's wallet
        const provider = new ethers.providers.Web3Provider(walletClient);
        const signer = provider.getSigner(walletAddress);

        // Define the ERC721 minting contract (Replace 'YourNFTContractAddress' and 'YourNFTContractABI' with actual values)
        const nftContractAddress = 'YourNFTContractAddress';
        const nftContractABI = [
            // Minimal ABI for minting function
            "function mint(address to, string memory tokenURI) public returns (uint256)"
        ];
        
        const nftContract = new ethers.Contract(nftContractAddress, nftContractABI, signer);

        // Call the mint function
        const tx = await nftContract.mint(walletAddress, tokenURI);
        await tx.wait(); // Wait for the transaction to be mined

        // Send response back to the client
        res.status(200).json({ message: 'NFT minted successfully', transactionHash: tx.hash });
    } catch (error) {
        console.error('Error minting NFT:', error);
        res.status(500).json({ error: 'Failed to mint NFT. ' + error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Note**: Replace `YourNFTContractAddress` and `YourNFTContractABI` with the actual NFT contract address and ABI. Make sure to install the necessary dependencies using:
```bash
npm install express body-parser @coinbase/wallet-sdk ethers
```
