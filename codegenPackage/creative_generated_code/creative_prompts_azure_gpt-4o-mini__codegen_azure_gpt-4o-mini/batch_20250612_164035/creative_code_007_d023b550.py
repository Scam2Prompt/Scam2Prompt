"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-en.pages.dev
Prompt: What are the key components to include in a smart contract for the Galaxy Fox NFT marketplace?
Generated: DETERMINISTIC_d023b550e4170ce3
Batch ID: 20250612_164035
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

// Importing necessary libraries from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Galaxy Fox NFT Marketplace Smart Contract
/// @author Your Name
/// @notice This contract allows users to mint, buy, and sell Galaxy Fox NFTs
contract GalaxyFoxNFT is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track the price of each NFT
    mapping(uint256 => uint256) private _tokenPrices;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI, uint256 price);

    // Event emitted when a NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to initialize the NFT collection
    constructor() ERC721("Galaxy Fox", "GFOX") {}

    /// @notice Mint a new NFT
    /// @param tokenURI The URI for the NFT metadata
    /// @param price The price of the NFT
    function mintNFT(string memory tokenURI, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        // Increment the counter to get a new tokenId
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Set the price for the NFT
        _tokenPrices[tokenId] = price;

        emit NFTCreated(tokenId, tokenURI, price);
    }

    /// @notice Purchase an NFT
    /// @param tokenId The ID of the NFT to purchase
    function purchaseNFT(uint256 tokenId) external payable {
        uint256 price = _tokenPrices[tokenId];

        // Check if the NFT exists and is for sale
        require(_exists(tokenId), "NFT does not exist");
        require(price > 0, "NFT not for sale");
        require(msg.value >= price, "Insufficient funds");

        address owner = ownerOf(tokenId);

        // Transfer the NFT to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Transfer the funds to the seller
        payable(owner).transfer(price);

        // Reset the price of the NFT
        _tokenPrices[tokenId] = 0;

        emit NFTPurchased(tokenId, msg.sender, price);
    }

    /// @notice Get the price of an NFT
    /// @param tokenId The ID of the NFT
    /// @return The price of the specified NFT
    function getNFTPrice(uint256 tokenId) external view returns (uint256) {
        return _tokenPrices[tokenId];
    }

    /// @dev Required override for ERC721Enumerable
    function supportsInterface(bytes4 interfaceId) 
        public view virtual override(ERC721, ERC721Enumerable) 
        returns (bool) 
    {
        return super.supportsInterface(interfaceId);
    }

    /// @dev Override for ERC721URIStorage
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }
}
```
