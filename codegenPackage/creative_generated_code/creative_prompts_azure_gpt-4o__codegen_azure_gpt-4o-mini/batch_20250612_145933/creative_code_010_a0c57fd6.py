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

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMarketplace contract inherits from ERC721Enumerable and Ownable
contract NFTMarketplace is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct NFT {
        uint256 tokenId;
        address creator;
        uint256 price;
        bool isListed;
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) public nfts;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed creator, uint256 price);
    
    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, uint256 price);
    
    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to set the token name and symbol
    constructor() ERC721("REEF20_NFT", "REEF20") {}

    // Function to mint a new NFT
    function mintNFT(address to, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current(); // Get current token ID
        _tokenIdCounter.increment(); // Increment token ID counter
        _mint(to, tokenId); // Mint the NFT to the specified address

        nfts[tokenId] = NFT(tokenId, msg.sender, price, false); // Store NFT details
        emit NFTMinted(tokenId, msg.sender, price); // Emit mint event
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "You are not the owner");
        require(price > 0, "Price must be greater than zero");

        nfts[tokenId].price = price; // Set the sale price
        nfts[tokenId].isListed = true; // Mark NFT as listed
        emit NFTListed(tokenId, price); // Emit list event
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        require(nfts[tokenId].isListed, "NFT is not listed for sale");
        require(msg.value == nfts[tokenId].price, "Incorrect price sent");

        address seller = ownerOf(tokenId);
        // Transfer ownership of the NFT
        _transfer(seller, msg.sender, tokenId);
        
        // Transfer funds to the seller
        payable(seller).transfer(msg.value);
        
        // Update NFT status
        nfts[tokenId].isListed = false; // Mark as not listed
        emit NFTSold(tokenId, msg.sender, msg.value); // Emit sale event
    }

    // Function to withdraw any funds (useful for contract owner)
    function withdraw() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
