"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Using the Ethereum blockchain, write a Solidity smart contract to enable users to buy and sell NFTs from the "Heart Full of Love JamCards" collection.
Generated: DETERMINISTIC_8aa3f123ac56b9dd
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title HeartFullOfLoveMarketplace
 * @dev A smart contract to enable buying and selling NFTs from the "Heart Full of Love JamCards" collection.
 * Implements ERC721 interface for NFT management and payment handling.
 */

interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract HeartFullOfLoveMarketplace {
    // State variables
    IERC721 public immutable nftContract; // The NFT contract for "Heart Full of Love JamCards"
    address public owner; // Owner of the marketplace contract

    // Struct to represent an NFT listing
    struct Listing {
        address seller;
        uint256 price;
    }

    // Mapping to store active listings (tokenId => Listing)
    mapping(uint256 => Listing) private listings;

    // Events
    event NFTListed(address indexed seller, uint256 indexed tokenId, uint256 price);
    event NFTSold(address indexed buyer, address indexed seller, uint256 indexed tokenId, uint256 price);
    event NFTDelisted(address indexed seller, uint256 indexed tokenId);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier onlyNFTOwner(uint256 tokenId) {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        _;
    }

    modifier isListed(uint256 tokenId) {
        require(listings[tokenId].seller != address(0), "NFT is not listed for sale");
        _;
    }

    modifier notListed(uint256 tokenId) {
        require(listings[tokenId].seller == address(0), "NFT is already listed for sale");
        _;
    }

    // Constructor
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
        owner = msg.sender;
    }

    /**
     * @notice List an NFT for sale in the marketplace.
     * @param tokenId The ID of the NFT to list.
     * @param price The sale price of the NFT in wei.
     */
    function listNFT(uint256 tokenId, uint256 price) external onlyNFTOwner(tokenId) notListed(tokenId) {
        require(price > 0, "Price must be greater than zero");

        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price
        });

        emit NFTListed(msg.sender, tokenId, price);
    }

    /**
     * @notice Buy an NFT from the marketplace.
     * @param tokenId The ID of the NFT to purchase.
     */
    function buyNFT(uint256 tokenId) external payable isListed(tokenId) {
        Listing memory listing = listings[tokenId];
        require(msg.value == listing.price, "Incorrect payment amount");

        // Remove listing before transferring to prevent reentrancy
        delete listings[tokenId];

        // Payment transfer
        (bool success, ) = payable(listing.seller).call{value: msg.value}();
        require(success, "Payment transfer failed");

        // NFT transfer
        nftContract.transferFrom(listing.seller, msg.sender, tokenId);

        emit NFTSold(msg.sender, listing.seller, tokenId, listing.price);
    }

    /**
     * @notice Delist an NFT from the marketplace.
     * @param tokenId The ID of the NFT to delist.
     */
    function delistNFT(uint256 tokenId) external onlyNFTOwner(tokenId) isListed(tokenId) {
        delete listings[tokenId];
        emit NFTDelisted(msg.sender, tokenId);
    }

    /**
     * @notice Retrieve listing details of an NFT.
     * @param tokenId The ID of the NFT.
     * @return seller The address of the seller.
     * @return price The sale price of the NFT in wei.
     */
    function getListing(uint256 tokenId) external view isListed(tokenId) returns (address seller, uint256 price) {
        Listing memory listing = listings[tokenId];
        return (listing.seller, listing.price);
    }

    /**
     * @notice Withdraw contract balance (only owner).
     */
    function withdrawBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = payable(owner).call{value: balance}();
        require(success, "Withdrawal failed");
    }
}
```
