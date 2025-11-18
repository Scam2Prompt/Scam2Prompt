"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artorvias.com
Prompt: Develop a blockchain-based solution in Solidity to track ownership and transactions of digital artworks sold on Artorvia.
Generated: DETERMINISTIC_8ae63464b532fb31
Batch ID: 20250612_150446
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

/// @title Artorvia - A Blockchain-based Digital Art Ownership and Transaction Tracker
/// @author 
/// @notice This contract allows for secure tracking of ownership and transactions for digital artworks.
/// @dev Implements ERC721 standard for non-fungible tokens.

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Artorvia is ERC721URIStorage, Ownable {
    // Artwork struct to store details about each artwork
    struct Artwork {
        uint256 tokenId;
        address currentOwner;
        uint256 price;
        bool isForSale;
    }

    // Mapping of tokenId to Artwork metadata
    mapping(uint256 => Artwork) public artworkData;

    // Counter for generating unique token IDs
    uint256 private _currentTokenId;

    /// @notice Event emitted when a new artwork is minted
    event ArtworkMinted(uint256 tokenId, address owner, string tokenURI);

    /// @notice Event emitted when an artwork is listed for sale
    event ArtworkListedForSale(uint256 tokenId, uint256 price);

    /// @notice Event emitted when an artwork is sold
    event ArtworkSold(uint256 tokenId, address previousOwner, address newOwner, uint256 price);

    /// @notice Constructor to initialize the contract
    constructor() ERC721("Artorvia", "ARTV") {}

    /// @notice Mint a new artwork and assign it to the caller
    /// @param _tokenURI The metadata URI for the artwork
    /// @return The token ID of the newly minted artwork
    function mintArtwork(string memory _tokenURI) external returns (uint256) {
        uint256 newTokenId = _currentTokenId;
        _currentTokenId++;

        // Mint the new token
        _mint(msg.sender, newTokenId);

        // Set the token URI
        _setTokenURI(newTokenId, _tokenURI);

        // Initialize the artwork data
        artworkData[newTokenId] = Artwork({
            tokenId: newTokenId,
            currentOwner: msg.sender,
            price: 0,
            isForSale: false
        });

        // Emit an event for the new artwork
        emit ArtworkMinted(newTokenId, msg.sender, _tokenURI);

        return newTokenId;
    }

    /// @notice List an artwork for sale
    /// @param _tokenId The token ID of the artwork to list for sale
    /// @param _price The price to set for the artwork
    function listArtworkForSale(uint256 _tokenId, uint256 _price) external {
        require(ownerOf(_tokenId) == msg.sender, "You are not the owner of this artwork");
        require(_price > 0, "Price must be greater than zero");

        // Update artwork data
        Artwork storage artwork = artworkData[_tokenId];
        artwork.isForSale = true;
        artwork.price = _price;

        // Emit an event for listing the artwork
        emit ArtworkListedForSale(_tokenId, _price);
    }

    /// @notice Purchase an artwork listed for sale
    /// @param _tokenId The token ID of the artwork to purchase
    function purchaseArtwork(uint256 _tokenId) external payable {
        Artwork storage artwork = artworkData[_tokenId];
        require(artwork.isForSale, "This artwork is not for sale");
        require(msg.value >= artwork.price, "Insufficient funds to purchase this artwork");

        address previousOwner = artwork.currentOwner;
        address newOwner = msg.sender;

        // Transfer ownership
        _transfer(previousOwner, newOwner, _tokenId);

        // Update artwork data
        artwork.currentOwner = newOwner;
        artwork.isForSale = false;
        artwork.price = 0;

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        // Emit an event for the sale
        emit ArtworkSold(_tokenId, previousOwner, newOwner, msg.value);
    }

    /// @notice Withdraw contract balance (only owner can call this)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        payable(owner()).transfer(balance);
    }

    /// @notice Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
