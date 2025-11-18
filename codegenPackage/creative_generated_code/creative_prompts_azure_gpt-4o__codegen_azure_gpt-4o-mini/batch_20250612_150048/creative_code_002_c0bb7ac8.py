"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-cryptodezire.com
Prompt: Generate code to simulate NFT trading options using Ethereum's programming language, incorporating features inspired by Crypto Dezire's platform.
Generated: DETERMINISTIC_c0bb7ac85b545adf
Batch ID: 20250612_150048
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

// Importing required OpenZeppelin libraries for ERC721 implementation and access control
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMarketplace contract to simulate NFT trading options
contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    mapping(uint256 => uint256) private _prices; // Mapping to track NFT prices
    mapping(uint256 => address) private _creators; // Mapping to track NFT creators
    mapping(uint256 => bool) private _listed; // Mapping to track if an NFT is listed for sale

    // Events
    event NFTCreated(uint256 indexed tokenId, address indexed creator);
    event NFTListed(uint256 indexed tokenId, uint256 price);
    event NFTUnlisted(uint256 indexed tokenId);
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("CryptoDezireNFT", "CDNFT") {}

    // Function to create a new NFT
    function createNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _tokenIdCounter.increment(); // Increment the token ID counter
        _mint(msg.sender, tokenId); // Mint the NFT to the creator
        _creators[tokenId] = msg.sender; // Set the creator of the NFT
        emit NFTCreated(tokenId, msg.sender); // Emit an event for NFT creation
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(price > 0, "Price must be greater than zero");
        
        _prices[tokenId] = price; // Set the NFT price
        _listed[tokenId] = true; // Mark the NFT as listed
        emit NFTListed(tokenId, price); // Emit an event for NFT listing
    }

    // Function to unlist an NFT
    function unlistNFT(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(_listed[tokenId], "NFT is not listed");

        delete _prices[tokenId]; // Remove the price
        _listed[tokenId] = false; // Mark the NFT as unlisted
        emit NFTUnlisted(tokenId); // Emit an event for NFT unlisting
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        require(_listed[tokenId], "NFT is not listed for sale");
        require(msg.value == _prices[tokenId], "Incorrect price");

        address seller = ownerOf(tokenId); // Get the seller's address
        _transfer(seller, msg.sender, tokenId); // Transfer the NFT from seller to buyer
        payable(seller).transfer(msg.value); // Transfer the payment to the seller

        delete _prices[tokenId]; // Remove the price
        _listed[tokenId] = false; // Mark the NFT as unlisted
        emit NFTSold(tokenId, msg.sender, msg.value); // Emit an event for NFT sale
    }

    // Function to get the price of an NFT
    function getNFTPrice(uint256 tokenId) external view returns (uint256) {
        require(_listed[tokenId], "NFT is not listed for sale");
        return _prices[tokenId]; // Return the price of the NFT
    }

    // Function to check if an NFT is listed
    function isNFTListed(uint256 tokenId) external view returns (bool) {
        return _listed[tokenId]; // Return whether the NFT is listed
    }
}
```
