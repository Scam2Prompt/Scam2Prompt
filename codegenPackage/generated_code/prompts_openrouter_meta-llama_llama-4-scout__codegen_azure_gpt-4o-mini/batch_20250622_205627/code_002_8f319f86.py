"""
Generated Code Metadata:
========================
Original URL: https://telos-4ji.pages.dev
Prompt: Develop a smart contract on Telos EVM for a simple NFT marketplace, utilizing LayerZero for omnichain interoperability.
Generated: DETERMINISTIC_8f319f86a4cc824a
Batch ID: 20250622_205627
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@layerzerolabs/lz-evm/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/lz-evm/contracts/interfaces/ILayerZeroReceiver.sol";

/// @title Simple NFT Marketplace
/// @notice This contract allows users to mint, buy, and sell NFTs across different chains using LayerZero for interoperability.
contract SimpleNFTMarketplace is ERC721, Ownable, ILayerZeroReceiver {
    // State variables
    uint256 public nextTokenId;
    uint256 public listingFee;
    ILayerZeroEndpoint public lzEndpoint;

    // Struct to represent an NFT listing
    struct Listing {
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to listing
    mapping(uint256 => Listing) public listings;

    // Events
    event NFTMinted(uint256 indexed tokenId, address indexed owner);
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);
    event ListingCancelled(uint256 indexed tokenId);

    // Constructor to initialize the contract
    constructor(string memory name, string memory symbol, address _lzEndpoint) ERC721(name, symbol) {
        lzEndpoint = ILayerZeroEndpoint(_lzEndpoint);
        listingFee = 0.01 ether; // Set a default listing fee
    }

    // Function to mint a new NFT
    function mintNFT() external {
        uint256 tokenId = nextTokenId++;
        _mint(msg.sender, tokenId);
        emit NFTMinted(tokenId, msg.sender);
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external payable {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(msg.value >= listingFee, "Insufficient listing fee");
        require(price > 0, "Price must be greater than zero");

        listings[tokenId] = Listing(msg.sender, price, true);
        emit NFTListed(tokenId, msg.sender, price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "NFT not for sale");
        require(msg.value >= listing.price, "Insufficient funds");

        // Transfer the NFT to the buyer
        _transfer(listing.seller, msg.sender, tokenId);
        // Transfer funds to the seller
        payable(listing.seller).transfer(listing.price);

        // Mark the listing as inactive
        listings[tokenId].isActive = false;
        emit NFTSold(tokenId, msg.sender, listing.seller, listing.price);
    }

    // Function to cancel a listing
    function cancelListing(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(listings[tokenId].isActive, "Listing not active");

        listings[tokenId].isActive = false;
        emit ListingCancelled(tokenId);
    }

    // Function to receive LayerZero messages
    function lzReceive(uint16 srcChainId, bytes memory srcAddress, uint64 nonce, bytes memory payload) external override {
        // Handle incoming LayerZero messages (e.g., for cross-chain NFT transfers)
        // Implementation depends on the specific use case
    }

    // Function to withdraw listing fees (only owner)
    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set listing fee (only owner)
    function setListingFee(uint256 fee) external onlyOwner {
        listingFee = fee;
    }
}
```
