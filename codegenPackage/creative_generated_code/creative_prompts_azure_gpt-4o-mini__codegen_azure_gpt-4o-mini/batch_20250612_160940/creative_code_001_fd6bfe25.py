"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintlama.pages.dev
Prompt: Write a smart contract for issuing and trading NFTs on the Cyber Lama platform, considering the project's unique NFT creation process.
Generated: DETERMINISTIC_fd6bfe25d31ac22c
Batch ID: 20250612_160940
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

// Import the required OpenZeppelin contracts for ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// CyberLamaNFT is a smart contract for creating and trading NFTs on the Cyber Lama platform
contract CyberLamaNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking NFT token IDs
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI, address owner);

    // Mapping from token ID to a boolean indicating if it is for sale
    mapping(uint256 => bool) public isForSale;

    // Mapping from token ID to sale price
    mapping(uint256 => uint256) public salePrice;

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("Cyber Lama NFT", "CYBLAMA") {}

    // Function to create a new NFT
    function createNFT(string memory _tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId); // Mint the NFT to the contract owner
        _setTokenURI(tokenId, _tokenURI); // Set the metadata URI for the NFT
        
        emit NFTCreated(tokenId, _tokenURI, msg.sender);
        _tokenIdCounter.increment(); // Increment the token ID counter
    }

    // Function to put an NFT up for sale
    function listForSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner");
        require(price > 0, "Price must be greater than zero");
        
        isForSale[tokenId] = true;
        salePrice[tokenId] = price;
    }

    // Function to remove an NFT from sale
    function removeFromSale(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner");
        
        isForSale[tokenId] = false;
        salePrice[tokenId] = 0;
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        require(isForSale[tokenId], "NFT is not for sale");
        require(msg.value >= salePrice[tokenId], "Insufficient payment");

        address seller = ownerOf(tokenId);
        
        // Transfer the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);
        
        // Transfer the payment to the seller
        payable(seller).transfer(msg.value);

        // Remove NFT from sale after purchase
        isForSale[tokenId] = false;
        salePrice[tokenId] = 0;
    }

    // Function to view the sale status and price of an NFT
    function getNFTDetails(uint256 tokenId) external view returns (bool, uint256) {
        return (isForSale[tokenId], salePrice[tokenId]);
    }
}
```
