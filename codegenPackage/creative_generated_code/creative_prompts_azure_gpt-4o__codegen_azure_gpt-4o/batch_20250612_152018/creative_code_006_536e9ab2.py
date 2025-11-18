"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telos-4ji.pages.dev
Prompt: Write a Solidity smart contract for deploying an NFT marketplace on Telos EVM, incorporating Telos' fixed-rate gas fee system to prevent front-running.
Generated: DETERMINISTIC_536e9ab243865f2f
Batch ID: 20250612_152018
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

/**
 * @title NFTMarketplace
 * @dev A simple NFT marketplace deployed on Telos EVM.
 *      Incorporates Telos' unique fixed-rate gas fee system to prevent front-running.
 */
contract NFTMarketplace {
    // State variables
    address public owner;
    uint256 public listingFee; // Fixed fee for listing an NFT
    uint256 public marketplaceFeePercentage; // Percentage fee on sales
    uint256 private constant FIXED_GAS_RATE = 1 * 10**6; // Example fixed gas fee in wei (Telos EVM specific)

    // Struct to represent an NFT for sale
    struct NFT {
        address payable seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool isSold;
    }

    // Mapping to store NFTs for sale
    mapping(uint256 => NFT) public marketplaceNFTs;

    // Counter for marketplace NFT IDs
    uint256 public nftCounter;

    // Events
    event NFTListed(
        uint256 indexed nftId,
        address indexed seller,
        address indexed nftContract,
        uint256 tokenId,
        uint256 price
    );
    event NFTSold(
        uint256 indexed nftId,
        address indexed buyer,
        address indexed nftContract,
        uint256 tokenId,
        uint256 price
    );

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier validateGasFee() {
        // Ensure the transaction is sent with the fixed-rate gas fee
        require(msg.value >= FIXED_GAS_RATE, "Insufficient gas fee sent");
        _;
    }

    // Constructor
    constructor(uint256 _listingFee, uint256 _marketplaceFeePercentage) {
        owner = msg.sender;
        listingFee = _listingFee;
        marketplaceFeePercentage = _marketplaceFeePercentage;
    }

    /**
     * @dev List an NFT for sale on the marketplace.
     * @param nftContract Address of the ERC721 contract.
     * @param tokenId Token ID of the NFT.
     * @param price Price of the NFT in wei.
     */
    function listNFT(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) external payable validateGasFee {
        require(msg.value >= listingFee + FIXED_GAS_RATE, "Insufficient listing fee sent");
        require(price > 0, "Price must be greater than zero");

        // Transfer the listing fee to the owner
        payable(owner).transfer(listingFee);

        // Increment NFT counter
        nftCounter++;

        // Add NFT to the marketplace
        marketplaceNFTs[nftCounter] = NFT(
            payable(msg.sender),
            nftContract,
            tokenId,
            price,
            false
        );

        emit NFTListed(nftCounter, msg.sender, nftContract, tokenId, price);
    }

    /**
     * @dev Purchase an NFT from the marketplace.
     * @param nftId ID of the NFT in the marketplace.
     */
    function purchaseNFT(uint256 nftId) external payable validateGasFee {
        NFT storage nft = marketplaceNFTs[nftId];
        require(!nft.isSold, "NFT has already been sold");
        require(msg.value >= nft.price + FIXED_GAS_RATE, "Insufficient funds sent");

        // Calculate marketplace fee
        uint256 marketplaceFee = (nft.price * marketplaceFeePercentage) / 100;

        // Transfer payment to the seller
        nft.seller.transfer(nft.price - marketplaceFee);

        // Transfer the marketplace fee to the owner
        payable(owner).transfer(marketplaceFee);

        // Mark the NFT as sold
        nft.isSold = true;

        // Transfer the NFT ownership to the buyer
        IERC721(nft.nftContract).safeTransferFrom(
            nft.seller,
            msg.sender,
            nft.tokenId
        );

        emit NFTSold(nftId, msg.sender, nft.nftContract, nft.tokenId, nft.price);
    }

    /**
     * @dev Update the listing fee.
     * @param _newListingFee New fixed listing fee in wei.
     */
    function updateListingFee(uint256 _newListingFee) external onlyOwner {
        require(_newListingFee > 0, "Listing fee must be greater than zero");
        listingFee = _newListingFee;
    }

    /**
     * @dev Update the marketplace fee percentage.
     * @param _newMarketplaceFeePercentage New marketplace fee percentage.
     */
    function updateMarketplaceFeePercentage(uint256 _newMarketplaceFeePercentage) external onlyOwner {
        require(_newMarketplaceFeePercentage >= 0, "Fee percentage cannot be negative");
        marketplaceFeePercentage = _newMarketplaceFeePercentage;
    }

    /**
     * @dev Withdraw any funds accidentally sent to the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner).transfer(balance);
    }
}

// Interface for ERC721
interface IERC721 {
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
}
```
