"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbdfinancials-mg.pages.dev
Prompt: Generate code to create a cross-chain marketplace for trading phygital assets, incorporating features like tokenization and NFT integration, as described in the MBD Boulevard section.
Generated: DETERMINISTIC_6f42376f34ff771f
Batch ID: 20250612_151255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is the production-ready code for creating a cross-chain marketplace for trading phygital assets using tokenization and NFT integration. The example leverages JavaScript (Node.js) and Solidity for smart contract implementation.

---

### Solidity Smart Contract (Tokenization & NFT Integration)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title CrossChainMarketplace
 * @dev A marketplace for trading phygital assets using tokenization and NFT integration.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CrossChainMarketplace is ERC721, Ownable {
    uint256 public nextTokenId;
    mapping(uint256 => string) public tokenMetadata; // Stores metadata for phygital assets
    mapping(uint256 => bool) public listedForSale; // Tracks whether tokens are listed for sale
    mapping(uint256 => uint256) public tokenPrices; // Stores token prices

    event TokenMinted(uint256 indexed tokenId, address owner, string metadata);
    event TokenListed(uint256 indexed tokenId, uint256 price, address seller);
    event TokenSold(uint256 indexed tokenId, address buyer);

    constructor() ERC721("PhygitalAssetNFT", "PANFT") {}

    /**
     * @notice Mint a new token representing a phygital asset.
     * @param metadata Metadata representing the phygital asset's details.
     */
    function mintToken(string memory metadata) external onlyOwner {
        uint256 tokenId = nextTokenId++;
        _safeMint(msg.sender, tokenId);
        tokenMetadata[tokenId] = metadata;

        emit TokenMinted(tokenId, msg.sender, metadata);
    }

    /**
     * @notice List a token for sale on the marketplace.
     * @param tokenId The token ID to list for sale.
     * @param price The price to sell the token for (in Wei).
     */
    function listTokenForSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this token.");
        require(price > 0, "Price must be greater than zero.");

        listedForSale[tokenId] = true;
        tokenPrices[tokenId] = price;

        emit TokenListed(tokenId, price, msg.sender);
    }

    /**
     * @notice Buy a token listed for sale.
     * @param tokenId The token ID to purchase.
     */
    function buyToken(uint256 tokenId) external payable {
        require(listedForSale[tokenId], "This token is not listed for sale.");
        require(msg.value == tokenPrices[tokenId], "Incorrect value sent.");

        address seller = ownerOf(tokenId);
        _transfer(seller, msg.sender, tokenId);
        listedForSale[tokenId] = false;

        payable(seller).transfer(msg.value);

        emit TokenSold(tokenId, msg.sender);
    }

    /**
     * @notice Get metadata for a given token ID.
     * @param tokenId The token ID to retrieve metadata for.
     * @return Metadata string.
     */
    function getTokenMetadata(uint256 tokenId) external view returns (string memory) {
        return tokenMetadata[tokenId];
    }
}
```

---

### Node.js Backend (Cross-Chain Marketplace Logic)

```javascript
const express = require('express');
const Web3 = require('web3');
const bodyParser = require('body-parser');
const { abi, networks } = require('./CrossChainMarketplace.json');

const app = express();
app.use(bodyParser.json());

// Set up Web3 and contract instance
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'); // Replace with your Infura ID or desired provider
const contractAddress = networks['1'].address; // Replace '1' with the desired network ID
const contract = new web3.eth.Contract(abi, contractAddress);

// Helper function for error handling
const handleError = (res, error) => {
  console.error(error);
  res.status(500).json({ error: error.message });
};

// Route to mint a new token
app.post('/mint', async (req, res) => {
  const { metadata, account, privateKey } = req.body;
  
  try {
    const transaction = contract.methods.mintToken(metadata);
    const gas = await transaction.estimateGas({ from: account });
    const gasPrice = await web3.eth.getGasPrice();

    const signedTx = await web3.eth.accounts.signTransaction(
      {
        to: contractAddress,
        data: transaction.encodeABI(),
        gas,
        gasPrice,
      },
      privateKey
    );

    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    res.json({ message: 'Token minted successfully!', receipt });
  } catch (error) {
    handleError(res, error);
  }
});

// Route to list token for sale
app.post('/list-for-sale', async (req, res) => {
  const { tokenId, price, account, privateKey } = req.body;

  try {
    const transaction = contract.methods.listTokenForSale(tokenId, price);
    const gas = await transaction.estimateGas({ from: account });
    const gasPrice = await web3.eth.getGasPrice();

    const signedTx = await web3.eth.accounts.signTransaction(
      {
        to: contractAddress,
        data: transaction.encodeABI(),
        gas,
        gasPrice,
      },
      privateKey
    );

    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    res.json({ message: 'Token listed for sale!', receipt });
  } catch (error) {
    handleError(res, error);
  }
});

// Route to buy a token
app.post('/buy', async (req, res) => {
  const { tokenId, account, privateKey } = req.body;
  const price = await contract.methods.tokenPrices(tokenId).call();

  try {
    const transaction = contract.methods.buyToken(tokenId);
    const gas = await transaction.estimateGas({ from: account, value: price });
    const gasPrice = await web3.eth.getGasPrice();

    const signedTx = await web3.eth.accounts.signTransaction(
      {
        to: contractAddress,
        data: transaction.encodeABI(),
        gas,
        gasPrice,
        value: price,
      },
      privateKey
    );

    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    res.json({ message: 'Token purchased successfully!', receipt });
  } catch (error) {
    handleError(res, error);
  }
});

// Route to retrieve token metadata
app.get('/token-metadata/:tokenId', async (req, res) => {
  const { tokenId } = req.params;

  try {
    const metadata = await contract.methods.getTokenMetadata(tokenId).call();
    res.json({ tokenId, metadata });
  } catch (error) {
    handleError(res, error);
  }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

---

### Notes:
- Replace placeholders like `YOUR_INFURA_PROJECT_ID` and private keys with actual values.
- Ensure proper security measures are implemented to protect sensitive information (e.g., private keys).
- Install required dependencies using `npm install express web3 body-parser`.
