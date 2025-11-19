"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Develop a smart contract using Ethereum's Solidity language to facilitate the buying and selling of NFTs, including features like royalty payments to artists.
Generated: DETERMINISTIC_0fe65bcfca46cb97
Batch ID: 20250622_212427
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
 * @title NFTMarketplace
 * @dev A smart contract for buying and selling NFTs with royalty payments to artists.
 */
contract NFTMarketplace {
    // Struct to represent an NFT
    struct NFT {
        uint256 id;
        address payable creator;
        address payable currentOwner;
        uint256 price;
        uint256 royaltyPercentage; // Royalty percentage (e.g., 5 for 5%)
    }

    // Mapping to store NFTs by their ID
    mapping(uint256 => NFT) public nfts;

    // Counter for NFT IDs
    uint256 private nextNFTId;

    // Event emitted when an NFT is created
    event NFTCreated(
        uint256 indexed id,
        address indexed creator,
        uint256 price,
        uint256 royaltyPercentage
    );

    // Event emitted when an NFT is sold
    event NFTSold(
        uint256 indexed id,
        address indexed buyer,
        uint256 price,
        uint256 royaltyPaid
    );

    /**
     * @dev Create a new NFT.
     * @param price The price of the NFT in wei.
     * @param royaltyPercentage The royalty percentage for the creator.
     */
    function createNFT(uint256 price, uint256 royaltyPercentage) external {
        require(price > 0, "Price must be greater than zero");
        require(
            royaltyPercentage >= 0 && royaltyPercentage <= 100,
            "Royalty percentage must be between 0 and 100"
        );

        // Create the NFT
        NFT memory newNFT = NFT({
            id: nextNFTId,
            creator: payable(msg.sender),
            currentOwner: payable(msg.sender),
            price: price,
            royaltyPercentage: royaltyPercentage
        });

        // Store the NFT in the mapping
        nfts[nextNFTId] = newNFT;

        // Emit the NFT creation event
        emit NFTCreated(nextNFTId, msg.sender, price, royaltyPercentage);

        // Increment the NFT ID counter
        nextNFTId++;
    }

    /**
     * @dev Buy an NFT.
     * @param nftId The ID of the NFT to buy.
     */
    function buyNFT(uint256 nftId) external payable {
        // Ensure the NFT exists
        NFT storage nft = nfts[nftId];
        require(nft.price > 0, "NFT does not exist");
        require(msg.value == nft.price, "Incorrect payment amount");

        // Calculate royalty payment
        uint256 royalty = (msg.value * nft.royaltyPercentage) / 100;

        // Pay the creator their royalty
        nft.creator.transfer(royalty);

        // Pay the current owner the remaining amount
        nft.currentOwner.transfer(msg.value - royalty);

        // Update the current owner of the NFT
        nft.currentOwner = payable(msg.sender);

        // Emit the NFT sold event
        emit NFTSold(nftId, msg.sender, msg.value, royalty);
    }

    /**
     * @dev Update the price of an NFT.
     * @param nftId The ID of the NFT to update.
     * @param newPrice The new price of the NFT in wei.
     */
    function updateNFTPrice(uint256 nftId, uint256 newPrice) external {
        // Ensure the NFT exists
        NFT storage nft = nfts[nftId];
        require(nft.price > 0, "NFT does not exist");
        require(msg.sender == nft.currentOwner, "Only the owner can update the price");
        require(newPrice > 0, "Price must be greater than zero");

        // Update the price
        nft.price = newPrice;
    }

    /**
     * @dev Get details of an NFT.
     * @param nftId The ID of the NFT to retrieve.
     * @return id The ID of the NFT.
     * @return creator The creator of the NFT.
     * @return currentOwner The current owner of the NFT.
     * @return price The price of the NFT.
     * @return royaltyPercentage The royalty percentage for the creator.
     */
    function getNFT(uint256 nftId)
        external
        view
        returns (
            uint256 id,
            address creator,
            address currentOwner,
            uint256 price,
            uint256 royaltyPercentage
        )
    {
        // Ensure the NFT exists
        NFT storage nft = nfts[nftId];
        require(nft.price > 0, "NFT does not exist");

        // Return the NFT details
        return (
            nft.id,
            nft.creator,
            nft.currentOwner,
            nft.price,
            nft.royaltyPercentage
        );
    }
}
```
