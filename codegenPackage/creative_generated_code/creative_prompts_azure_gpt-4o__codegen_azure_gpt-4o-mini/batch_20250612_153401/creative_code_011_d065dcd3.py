"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleph-zero.pages.dev
Prompt: Provide code for deploying an NFT marketplace on Aleph Zero, leveraging its scalability and privacy features for secure transactions.
Generated: DETERMINISTIC_d065dcd3fdf21558
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// NFTMarketplace.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title NFTMarketplace
 * @dev A simple NFT marketplace that allows users to mint and trade NFTs
 */
contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for minting unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an NFT
    struct NFT {
        uint256 id;
        string name;
        string uri;
        address owner;
        uint256 price;
        bool forSale;
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) public nfts;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed id, string name, string uri, address indexed owner, uint256 price);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed id, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed id, address indexed buyer, address indexed seller, uint256 price);

    constructor() ERC721("NFTMarketplace", "NFTM") {}

    /**
     * @dev Mint a new NFT
     * @param name The name of the NFT
     * @param uri The metadata URI for the NFT
     * @param price The sale price of the NFT
     */
    function mintNFT(string memory name, string memory uri, uint256 price) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        nfts[tokenId] = NFT(tokenId, name, uri, msg.sender, price, true);
        _mint(msg.sender, tokenId);

        emit NFTCreated(tokenId, name, uri, msg.sender, price);
    }

    /**
     * @dev List an NFT for sale
     * @param tokenId The ID of the NFT to list
     * @param price The price to list the NFT for
     */
    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can list their NFT");
        require(price > 0, "Price must be greater than zero");

        nfts[tokenId].price = price;
        nfts[tokenId].forSale = true;

        emit NFTListed(tokenId, price);
    }

    /**
     * @dev Purchase an NFT
     * @param tokenId The ID of the NFT to purchase
     */
    function purchaseNFT(uint256 tokenId) public payable {
        NFT memory nft = nfts[tokenId];
        require(nft.forSale, "NFT is not for sale");
        require(msg.value >= nft.price, "Insufficient funds sent");

        address seller = nft.owner;

        // Transfer the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);
        
        // Transfer the funds to the seller
        payable(seller).transfer(msg.value);

        // Update the NFT details
        nfts[tokenId].owner = msg.sender;
        nfts[tokenId].forSale = false;

        emit NFTSold(tokenId, msg.sender, seller, nft.price);
    }

    /**
     * @dev Retrieve NFT details by token ID
     * @param tokenId The ID of the NFT
     * @return The details of the NFT
     */
    function getNFT(uint256 tokenId) public view returns (NFT memory) {
        require(_exists(tokenId), "NFT does not exist");
        return nfts[tokenId];
    }
}
```

### Deployment Script (deploy.js)

```javascript
// deploy.js
const { ethers } = require("hardhat");

async function main() {
    // Compile the contract
    await hre.run('compile');

    // Get the contract factory
    const NFTMarketplace = await ethers.getContractFactory("NFTMarketplace");

    // Deploy the contract
    const nftMarketplace = await NFTMarketplace.deploy();

    // Wait for the deployment to be confirmed
    await nftMarketplace.deployed();

    console.log("NFTMarketplace deployed to:", nftMarketplace.address);
}

// Handle errors during deployment
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

### Notes:
- This code uses OpenZeppelin's ERC721 implementation for creating the NFT standard.
- Ensure you have the necessary environment setup, including `Node.js`, `Hardhat`, and the OpenZeppelin Contracts library.
- Adjust the contract settings as needed to deploy on Aleph Zero, including its specific blockchain parameters.
