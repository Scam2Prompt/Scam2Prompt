"""
Generated Code Metadata:
========================
Original URL: https://bids-sea.io
Prompt: Create a function in Solidity to mint NFTs programmatically, following the steps outlined on the Bids Sea Community site (wallet setup, collection creation, NFT addition, and sale).
Generated: DETERMINISTIC_82cf7afcb6f36ec7
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NFTMintingContract
/// @dev This contract allows the minting of NFTs programmatically.
contract NFTMintingContract is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to sale price
    mapping(uint256 => uint256) private _tokenSalePrices;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed owner, uint256 salePrice);

    // Event emitted when an NFT is put up for sale
    event NFTPutUpForSale(uint256 indexed tokenId, uint256 salePrice);

    // Constructor to set the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @dev Function to mint a new NFT
    /// @param to The address that will receive the minted NFT
    /// @param salePrice The sale price of the NFT
    function mintNFT(address to, uint256 salePrice) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(salePrice > 0, "Sale price must be greater than zero");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(to, tokenId);

        // Set the sale price for the minted NFT
        _tokenSalePrices[tokenId] = salePrice;

        emit NFTMinted(tokenId, to, salePrice);
    }

    /// @dev Function to put an NFT up for sale
    /// @param tokenId The ID of the NFT to put up for sale
    /// @param salePrice The new sale price of the NFT
    function putNFTUpForSale(uint256 tokenId, uint256 salePrice) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only the owner can put it up for sale");
        require(salePrice > 0, "Sale price must be greater than zero");

        // Update the sale price for the NFT
        _tokenSalePrices[tokenId] = salePrice;

        emit NFTPutUpForSale(tokenId, salePrice);
    }

    /// @dev Function to get the sale price of an NFT
    /// @param tokenId The ID of the NFT
    /// @return The sale price of the NFT
    function getSalePrice(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "NFT does not exist");
        return _tokenSalePrices[tokenId];
    }

    /// @dev Function to buy an NFT
    /// @param tokenId The ID of the NFT to buy
    function buyNFT(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist");
        uint256 salePrice = _tokenSalePrices[tokenId];
        require(msg.value >= salePrice, "Insufficient funds sent");

        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "Owner cannot buy their own NFT");

        // Transfer the NFT to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Transfer the sale price to the seller
        payable(owner).transfer(salePrice);

        // Refund excess funds sent
        if (msg.value > salePrice) {
            payable(msg.sender).transfer(msg.value - salePrice);
        }
    }
}
```
