"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reef-io.pages.dev
Prompt: Write a guide for deploying a REEF-20 NFT marketplace on Reef chain, including example code for minting and trading NFTs.
Generated: DETERMINISTIC_a0c57fd64a320302
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title REEF-20 NFT Marketplace
 * @dev Contract for minting and trading NFTs on the Reef chain.
 *      This example demonstrates a basic implementation of an NFT marketplace.
 */

// Importing OpenZeppelin's ERC721 contract
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ReefNFTMarketplace is ERC721, Ownable {
    // Struct to represent an NFT listed for sale
    struct ListedNFT {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isListed;
    }

    // Mapping to store NFTs listed for sale
    mapping(uint256 => ListedNFT) public listedNFTs;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    // Counter to generate unique token IDs
    uint256 private _tokenIdCounter;

    constructor() ERC721("ReefNFT", "REEF") {}

    /**
     * @dev Mint a new NFT
     * @param to Address to receive the newly minted NFT
     */
    function mintNFT(address to) external onlyOwner {
        require(to != address(0), "Invalid address");

        // Increment token ID counter
        _tokenIdCounter += 1;

        // Mint the NFT
        _mint(to, _tokenIdCounter);

        emit NFTMinted(to, _tokenIdCounter);
    }

    /**
     * @dev List an NFT for sale
     * @param tokenId ID of the NFT to list
     * @param price Price of the NFT in Wei
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        require(price > 0, "Price must be greater than zero");

        // Transfer the NFT to the contract for escrow
        transferFrom(msg.sender, address(this), tokenId);

        // Store NFT listing data
        listedNFTs[tokenId] = ListedNFT({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isListed: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Buy a listed NFT
     * @param tokenId ID of the NFT to purchase
     */
    function buyNFT(uint256 tokenId) external payable {
        ListedNFT memory nft = listedNFTs[tokenId];
        require(nft.isListed, "NFT is not listed for sale");
        require(msg.value >= nft.price, "Insufficient payment");

        // Remove the NFT from listing
        listedNFTs[tokenId].isListed = false;

        // Transfer payment to the seller
        (bool sent, ) = nft.seller.call{value: nft.price}("");
        require(sent, "Failed to send Ether");

        // Transfer the NFT to the buyer
        _transfer(address(this), msg.sender, tokenId);

        emit NFTPurchased(tokenId, msg.sender, nft.seller, nft.price);
    }

    /**
     * @dev Withdraw funds from the contract (owner only)
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool sent, ) = msg.sender.call{value: balance}("");
        require(sent, "Failed to withdraw funds");
    }

    /**
     * @dev Fallback function to accept Ether
     */
    receive() external payable {}
}
```

### Deployment Guide:
1. Install dependencies: `npm install @openzeppelin/contracts`.
2. Compile the contract using Hardhat or Truffle.
3. Deploy the contract on Reef chain:
   - Use a deployment script to deploy the contract.
   - Example deployment script in JavaScript:
```javascript
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contract with account:", deployer.address);

  const ReefNFTMarketplace = await ethers.getContractFactory("ReefNFTMarketplace");
  const marketplace = await ReefNFTMarketplace.deploy();

  console.log("Contract deployed to address:", marketplace.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
}
```
4. Interact with the contract using a client like Web3.js or ethers.js to call mint, list, and buy functions.
