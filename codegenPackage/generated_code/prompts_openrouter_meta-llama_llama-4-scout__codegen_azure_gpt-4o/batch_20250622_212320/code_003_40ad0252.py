"""
Generated Code Metadata:
========================
Original URL: https://gorodshansona.ru
Prompt: "Generate a smart contract using Solidity that utilizes Immutable X for instant and fee-less NFT trading on Ethereum."
Generated: DETERMINISTIC_40ad0252ba936116
Batch ID: 20250622_212320
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

/**
 * @title ImmutableX NFT Trading Smart Contract
 * @dev This contract integrates with Immutable X for instant and fee-less NFT trading on Ethereum.
 * @notice Ensure you have the Immutable X SDK and API properly configured for off-chain order matching.
 */
contract ImmutableXNFTTrading {
    // Immutable X's ERC721 bridge address (replace with the actual address for your environment)
    address public immutableXBridge;

    // Event emitted when an NFT is listed for trading
    event NFTListed(address indexed owner, address indexed tokenAddress, uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(address indexed buyer, address indexed tokenAddress, uint256 indexed tokenId, uint256 price);

    // Struct to represent an NFT listing
    struct NFTListing {
        address owner;
        address tokenAddress;
        uint256 tokenId;
        uint256 price;
        bool isActive;
    }

    // Mapping to store NFT listings
    mapping(uint256 => NFTListing) public listings;

    // Counter for listing IDs
    uint256 public listingCounter;

    /**
     * @dev Constructor to set the Immutable X bridge address.
     * @param _immutableXBridge The address of the Immutable X ERC721 bridge.
     */
    constructor(address _immutableXBridge) {
        require(_immutableXBridge != address(0), "Invalid Immutable X bridge address");
        immutableXBridge = _immutableXBridge;
    }

    /**
     * @dev Function to list an NFT for trading.
     * @param tokenAddress The address of the ERC721 token contract.
     * @param tokenId The ID of the token to list.
     * @param price The price of the NFT in wei.
     */
    function listNFT(address tokenAddress, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(tokenAddress != address(0), "Invalid token address");

        // Ensure the caller is the owner of the NFT
        require(IERC721(tokenAddress).ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");

        // Approve the Immutable X bridge to transfer the NFT
        IERC721(tokenAddress).approve(immutableXBridge, tokenId);

        // Create a new listing
        listingCounter++;
        listings[listingCounter] = NFTListing({
            owner: msg.sender,
            tokenAddress: tokenAddress,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        emit NFTListed(msg.sender, tokenAddress, tokenId, price);
    }

    /**
     * @dev Function to purchase an NFT.
     * @param listingId The ID of the listing to purchase.
     */
    function purchaseNFT(uint256 listingId) external payable {
        NFTListing storage listing = listings[listingId];

        require(listing.isActive, "Listing is not active");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Transfer payment to the seller
        payable(listing.owner).transfer(msg.value);

        // Transfer the NFT to the buyer via Immutable X bridge
        IERC721(listing.tokenAddress).transferFrom(listing.owner, msg.sender, listing.tokenId);

        // Mark the listing as inactive
        listing.isActive = false;

        emit NFTPurchased(msg.sender, listing.tokenAddress, listing.tokenId, listing.price);
    }

    /**
     * @dev Function to cancel an NFT listing.
     * @param listingId The ID of the listing to cancel.
     */
    function cancelListing(uint256 listingId) external {
        NFTListing storage listing = listings[listingId];

        require(listing.isActive, "Listing is not active");
        require(listing.owner == msg.sender, "Caller is not the owner of the listing");

        // Mark the listing as inactive
        listing.isActive = false;

        emit NFTListed(msg.sender, listing.tokenAddress, listing.tokenId, 0);
    }
}

// Interface for ERC721 token standard
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function approve(address to, uint256 tokenId) external;
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```
