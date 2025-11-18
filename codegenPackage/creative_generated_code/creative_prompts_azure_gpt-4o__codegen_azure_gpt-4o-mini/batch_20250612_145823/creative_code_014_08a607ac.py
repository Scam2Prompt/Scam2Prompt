"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Write a step-by-step guide for deploying an NFT on the MDEX NFT marketplace using the Polygon network.
Generated: DETERMINISTIC_08a607ac3f1347d5
Batch ID: 20250612_145823
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://polygon-rpc.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/metadata.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Step 1: Import necessary libraries
const Web3 = require('web3');
const { abi: NFTAbi } = require('./NFTContract.json'); // Adjust the path to your NFT contract ABI
const { abi: MarketplaceAbi } = require('./MarketplaceContract.json'); // Adjust the path to your marketplace contract ABI

// Step 2: Set up Web3 and connect to the Polygon network
const polygonUrl = 'https://polygon-rpc.com'; // Polygon RPC URL
const web3 = new Web3(new Web3.providers.HttpProvider(polygonUrl));

// Step 3: Define contract addresses
const nftContractAddress = '0xYourNFTContractAddress'; // Replace with your NFT contract address
const marketplaceContractAddress = '0xYourMarketplaceContractAddress'; // Replace with MDEX marketplace contract address

// Step 4: Set up contract instances
const nftContract = new web3.eth.Contract(NFTAbi, nftContractAddress);
const marketplaceContract = new web3.eth.Contract(MarketplaceAbi, marketplaceContractAddress);

// Step 5: Define the function to mint and list an NFT
async function mintAndListNFT(account, metadataURI, price) {
    try {
        // Step 5.1: Mint the NFT
        const mintTx = await nftContract.methods.mint(account, metadataURI).send({ from: account });
        console.log('NFT minted:', mintTx);

        // Step 5.2: Get the tokenId of the newly minted NFT
        const tokenId = mintTx.events.Transfer.returnValues.tokenId;

        // Step 5.3: Approve the marketplace to spend the NFT
        await nftContract.methods.approve(marketplaceContractAddress, tokenId).send({ from: account });

        // Step 5.4: List the NFT on the marketplace
        const listTx = await marketplaceContract.methods.listNFT(nftContractAddress, tokenId, web3.utils.toWei(price, 'ether')).send({ from: account });
        console.log('NFT listed on marketplace:', listTx);
    } catch (error) {
        console.error('Error in minting or listing NFT:', error);
    }
}

// Step 6: Execute the minting and listing function
const account = '0xYourWalletAddress'; // Replace with your wallet address
const metadataURI = 'https://example.com/metadata.json'; // Replace with your NFT metadata URI
const price = '0.1'; // Set the price in Ether

// Call the function to mint and list the NFT
mintAndListNFT(account, metadataURI, price);
```

**Notes:**
- Replace placeholder values such as `0xYourNFTContractAddress`, `0xYourMarketplaceContractAddress`, and `0xYourWalletAddress` with actual values.
- Ensure `NFTContract.json` and `MarketplaceContract.json` contain the correct ABI definitions for your contracts.
- The above code assumes you have already deployed your NFT contract and the MDEX marketplace contract on the Polygon network.
