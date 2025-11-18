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

/**
 * @title NFTTradingPlatform
 * @dev A smart contract to simulate NFT trading options inspired by Crypto Dezire's platform.
 */
contract NFTTradingPlatform {
    // Struct to represent an NFT listing
    struct NFT {
        uint256 id;           // Unique identifier for the NFT
        address owner;        // Current owner of the NFT
        uint256 price;        // Price of the NFT in wei
        bool isListed;        // Is the NFT currently listed for sale
    }

    // Map NFT ID to its details
    mapping(uint256 => NFT) private nfts;

    // Event to notify when an NFT is listed for sale
    event NFTListed(uint256 indexed nftId, address indexed owner, uint256 price);

    // Event to notify when an NFT is purchased
    event NFTPurchased(uint256 indexed nftId, address indexed newOwner, uint256 price);

    // Event to notify when an NFT is delisted
    event NFTDelisted(uint256 indexed nftId, address indexed owner);

    // Modifier to check if the caller is the NFT owner
    modifier onlyOwner(uint256 nftId) {
        require(nfts[nftId].owner == msg.sender, "Caller is not the NFT owner");
        _;
    }

    // Modifier to ensure the NFT is listed for sale
    modifier isListed(uint256 nftId) {
        require(nfts[nftId].isListed, "NFT is not listed for sale");
        _;
    }

    /**
     * @notice Lists an NFT for sale
     * @param nftId The ID of the NFT
     * @param price The price of the NFT in wei
     */
    function listNFT(uint256 nftId, uint256 price) external onlyOwner(nftId) {
        require(price > 0, "Price must be greater than zero");
        nfts[nftId].price = price;
        nfts[nftId].isListed = true;

        emit NFTListed(nftId, msg.sender, price);
    }

    /**
     * @notice Purchases a listed NFT
     * @param nftId The ID of the NFT
     */
    function purchaseNFT(uint256 nftId) external payable isListed(nftId) {
        NFT memory nft = nfts[nftId];

        require(msg.value == nft.price, "Incorrect payment amount");
        require(nft.owner != msg.sender, "Caller already owns the NFT");

        // Transfer payment to the current owner
        payable(nft.owner).transfer(msg.value);

        // Update ownership
        nfts[nftId].owner = msg.sender;
        nfts[nftId].isListed = false;

        emit NFTPurchased(nftId, msg.sender, nft.price);
    }

    /**
     * @notice Delists an NFT
     * @param nftId The ID of the NFT
     */
    function delistNFT(uint256 nftId) external onlyOwner(nftId) {
        require(nfts[nftId].isListed, "NFT is not listed for sale");

        nfts[nftId].isListed = false;

        emit NFTDelisted(nftId, msg.sender);
    }

    /**
     * @notice Adds a new NFT to the platform
     * @param nftId The ID of the NFT
     */
    function addNFT(uint256 nftId) external {
        require(nfts[nftId].owner == address(0), "NFT already exists");

        nfts[nftId] = NFT({
            id: nftId,
            owner: msg.sender,
            price: 0,
            isListed: false
        });
    }

    /**
     * @notice Fetches NFT details
     * @param nftId The ID of the NFT
     * @return id, owner, price, isListed
     */
    function getNFTDetails(uint256 nftId)
        external
        view
        returns (
            uint256 id,
            address owner,
            uint256 price,
            bool isListed
        )
    {
        NFT memory nft = nfts[nftId];
        return (nft.id, nft.owner, nft.price, nft.isListed);
    }
}
```
