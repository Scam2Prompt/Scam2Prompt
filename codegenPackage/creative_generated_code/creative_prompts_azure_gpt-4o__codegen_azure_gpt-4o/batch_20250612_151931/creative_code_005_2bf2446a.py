"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wenwen.pages.dev
Prompt: Develop a Web3-based application that immortalizes "wen culture" by minting NFTs of community-generated content related to WEN.
Generated: DETERMINISTIC_2bf2446a7046d0f2
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready code for a Web3-based application that mints NFTs with community-generated content related to "wen culture." The application uses the `ethers.js` library and a Solidity smart contract for the NFT minting logic.

### Solidity Smart Contract (`WenNFT.sol`)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title WenNFT
 * @dev A contract for minting NFTs featuring community-generated content related to "wen culture."
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WenNFT is ERC721URIStorage, Ownable {
    uint256 private _tokenIdCounter;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    constructor() ERC721("WenCultureNFT", "WEN") {
        _tokenIdCounter = 1; // Start token IDs at 1
    }

    /**
     * @dev Mint new NFT with `tokenURI`.
     * @param to Address to mint the NFT to.
     * @param tokenURI URI pointing to metadata of the NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter;
        _tokenIdCounter++;

        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit NFTMinted(to, tokenId, tokenURI);
    }
}
```

### Node.js Backend (`mint-nft.js`)

```javascript
const { ethers } = require("ethers");
require("dotenv").config(); // Load environment variables

// Load contract ABI and bytecode (compiled Solidity output)
const contractABI = require("./WenNFT.json").abi;

// Configuration
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL); // RPC URL (e.g., Infura or Alchemy)
const privateKey = process.env.PRIVATE_KEY; // Wallet private key (used by the owner to mint NFTs)
const contractAddress = process.env.CONTRACT_ADDRESS; // Deployed contract address

// Initialize wallet and contract
const wallet = new ethers.Wallet(privateKey, provider);
const contract = new ethers.Contract(contractAddress, contractABI, wallet);

/**
 * Mint NFT with community-generated content related to "wen culture."
 * @param {string} recipientAddress - Recipient's wallet address.
 * @param {string} metadataURI - URI pointing to NFT metadata.
 */
async function mintNFT(recipientAddress, metadataURI) {
  try {
    console.log("Minting NFT...");
    const tx = await contract.mintNFT(recipientAddress, metadataURI);
    console.log("Transaction sent:", tx.hash);

    // Wait for transaction confirmation
    const receipt = await tx.wait();
    console.log("NFT minted successfully:", receipt);
  } catch (error) {
    console.error("Error minting NFT:", error);
  }
}

// Example usage
const recipient = "0xRecipientAddressHere"; // Replace with actual recipient address
const metadataURI = "ipfs://QmExampleMetadataHash"; // Replace with actual IPFS hash or URL

mintNFT(recipient, metadataURI);
```

### `.env` File

```plaintext
RPC_URL=<Your_RPC_URL>                # E.g., Infura/Alchemy endpoint
PRIVATE_KEY=<Your_Private_Key>        # Owner's private key
CONTRACT_ADDRESS=<Deployed_Contract_Address>
```

### Notes:
- Make sure OpenZeppelin contracts are installed (`npm install @openzeppelin/contracts`).
- Deploy the Solidity contract using Hardhat or Truffle, and use the deployed contract address in the `.env` file.
- Metadata for the NFT (e.g., JSON files pointing to IPFS) should be generated and uploaded separately.
- This code assumes proper RPC and wallet setup.
