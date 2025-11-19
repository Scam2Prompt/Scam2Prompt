"""
Generated Code Metadata:
========================
Original URL: https://telos-4ji.pages.dev
Prompt: Write a Solidity smart contract for deploying an NFT marketplace on Telos EVM, incorporating Telos' fixed-rate gas fee system to prevent front-running.
Generated: DETERMINISTIC_536e9ab243865f2f
Batch ID: 20250612_152018
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMarketplace contract for deploying an NFT marketplace on Telos EVM
contract NFTMarketplace is Ownable, ERC721URIStorage {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public listingFee; // Fee for listing an NFT

    // Struct to represent an NFT listing
    struct Listing {
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to Listing
    mapping(uint256 => Listing) public listings;

    // Event emitted when an NFT is listed
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to initialize the contract
    constructor(uint256 _listingFee) ERC721("TelosNFT", "TNFT") {
        listingFee = _listingFee; // Set the listing fee
    }

    // Function to mint a new NFT
    function mintNFT(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _tokenIdCounter.increment(); // Increment the token ID counter
        _mint(msg.sender, tokenId); // Mint the NFT
        _setTokenURI(tokenId, tokenURI); // Set the token URI
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external payable {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(msg.value == listingFee, "Incorrect listing fee");

        listings[tokenId] = Listing(msg.sender, price, true); // Create a new listing
        emit NFTListed(tokenId, msg.sender, price); // Emit the listing event
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId]; // Get the listing

        require(listing.isActive, "NFT is not for sale");
        require(msg.value == listing.price, "Incorrect price");

        // Transfer the NFT to the buyer
        _transfer(listing.seller, msg.sender, tokenId);
        // Transfer the sale amount to the seller
        payable(listing.seller).transfer(msg.value);

        // Mark the listing as inactive
        listings[tokenId].isActive = false;
        emit NFTSold(tokenId, msg.sender, listing.price); // Emit the sale event
    }

    // Function to withdraw the listing fee (only for the owner)
    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance); // Transfer the balance to the owner
    }

    // Function to update the listing fee (only for the owner)
    function updateListingFee(uint256 newFee) external onlyOwner {
        listingFee = newFee; // Update the listing fee
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
