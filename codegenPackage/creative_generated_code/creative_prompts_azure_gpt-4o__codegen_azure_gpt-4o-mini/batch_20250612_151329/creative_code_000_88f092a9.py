"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnvxhjdghdg.pages.dev
Prompt: Write a smart contract in Solidity for an NFT marketplace that supports connecting wallets and purchasing digital art, similar to features described on the Azuki Elementals gallery page.
Generated: DETERMINISTIC_88f092a9c543de3c
Batch ID: 20250612_151329
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NFT Marketplace
/// @notice This contract allows users to mint and purchase NFTs
contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counters for NFT IDs and sold NFTs count
    Counters.Counter private _tokenIdCounter;
    Counters.Counter private _soldCount;

    // Struct to represent each NFT
    struct Art {
        uint256 id;
        address creator;
        string uri;
        uint256 price;
        bool isListed;
    }

    // Mapping from token ID to Art details
    mapping(uint256 => Art) public arts;

    /// @dev Emitted when a new art is created
    event ArtCreated(uint256 indexed id, address indexed creator, string uri, uint256 price);

    /// @dev Emitted when an art is purchased
    event ArtPurchased(uint256 indexed id, address indexed buyer, address indexed previousOwner);

    /// @dev Create an instance of the contract
    constructor() ERC721("NFTMarketplace", "NFTM") {}

    /// @notice Allows the creator to mint a new NFT
    /// @param uri The metadata URI for the NFT
    /// @param price The price for purchasing the NFT
    function createArt(string memory uri, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        _tokenIdCounter.increment();
        uint256 newArtId = _tokenIdCounter.current();
        
        // Create the new art
        arts[newArtId] = Art({
            id: newArtId,
            creator: msg.sender,
            uri: uri,
            price: price,
            isListed: true
        });

        // Mint the NFT
        _mint(msg.sender, newArtId);
        
        emit ArtCreated(newArtId, msg.sender, uri, price);
    }

    /// @notice Allows users to purchase the art
    /// @param artId The ID of the art to purchase
    function purchaseArt(uint256 artId) external payable {
        Art storage art = arts[artId];
        
        // Check if the art is listed and the correct price is sent
        require(art.isListed, "Art is not listed for sale");
        require(msg.value == art.price, "Incorrect value sent");

        // Transfer the NFT to the buyer
        safeTransferFrom(art.creator, msg.sender, artId);

        // Update the art for sale
        art.isListed = false;
        _soldCount.increment();

        // Transfer funds to the creator
        payable(art.creator).transfer(msg.value);

        emit ArtPurchased(artId, msg.sender, art.creator);
    }

    /// @notice Allows the owner to update the price of an art
    /// @param artId The ID of the art to update the price for
    /// @param newPrice The new price for the art
    function updateArtPrice(uint256 artId, uint256 newPrice) external {
        Art storage art = arts[artId];

        require(msg.sender == art.creator, "Only the creator can update the price");
        require(art.isListed, "Art is not listed for sale");
        require(newPrice > 0, "Price must be greater than zero");

        art.price = newPrice;
    }

    /// @notice Returns the total number of sold arts
    /// @return uint256 The count of sold arts
    function getSoldCount() external view returns (uint256) {
        return _soldCount.current();
    }

    /// @notice Returns the details of a specific art
    /// @param artId The ID of the art to retrieve
    /// @return Art The details of the art
    function getArtDetails(uint256 artId) external view returns (Art memory) {
        return arts[artId];
    }
}
```
