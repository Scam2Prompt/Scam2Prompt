"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.kim
Prompt: Write a smart contract in Solidity that mimics the functionality of creating buy, sell, and trade offers for Ethereum-based assets, including ETH, ERC-20, and ERC-721 tokens, as described on ethereum.kim.
Generated: DETERMINISTIC_0e719a4c3d42bc52
Batch ID: 20250612_151811
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

// Importing necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define a struct for TradeOffer
struct TradeOffer {
    address assetAddress; // Address of the asset (ERC20 or ERC721)
    uint256 assetId; // Asset ID for ERC721 (0 if ERC20)
    address seller; // Seller's address
    uint256 price; // Price in ETH (for ERC20, price in token amount)
    bool isActive; // Status of the offer
}

// Main contract
contract AssetMarketplace is Ownable {
    // State variable to store trade offers
    mapping(uint256 => TradeOffer) public offers;
    uint256 public offerCount; // Counter for offers

    // Event emitted when a new offer is created
    event OfferCreated(uint256 offerId, address indexed seller, address assetAddress, uint256 price, bool isERC721);
    
    // Event emitted when an offer is filled
    event OfferFilled(uint256 offerId, address indexed buyer);

    // Function to create a new trade offer
    function createOffer(address assetAddress, uint256 assetId, uint256 price) external {
        require(price > 0, "Price must be greater than 0");

        // Increment the offer count for unique offer ID
        offerCount++;

        // Create and store the offer
        offers[offerCount] = TradeOffer({
            assetAddress: assetAddress,
            assetId: assetId,
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit OfferCreated(offerCount, msg.sender, assetAddress, price, assetId != 0);
    }

    // Function to fill a trade offer
    function fillOffer(uint256 offerId) external payable {
        TradeOffer storage offer = offers[offerId];

        require(offer.isActive, "Offer is not active");
        require(msg.value == offer.price, "Incorrect ETH amount sent");

        // Transfer ETH to the seller
        payable(offer.seller).transfer(msg.value);

        // Handle ERC20 or ERC721 transfer
        if (offer.assetId == 0) {
            // ERC20 Asset
            require(IERC20(offer.assetAddress).transferFrom(offer.seller, msg.sender, offer.price), "Transfer failed");
        } else {
            // ERC721 Asset
            require(IERC721(offer.assetAddress).ownerOf(offer.assetId) == offer.seller, "Seller is not the owner");
            IERC721(offer.assetAddress).safeTransferFrom(offer.seller, msg.sender, offer.assetId);
        }

        // Mark the offer as inactive
        offer.isActive = false;

        emit OfferFilled(offerId, msg.sender);
    }

    // Function to cancel an offer
    function cancelOffer(uint256 offerId) external {
        TradeOffer storage offer = offers[offerId];

        require(offer.seller == msg.sender, "Only the seller can cancel the offer");
        require(offer.isActive, "Offer is not active");

        offer.isActive = false; // Mark the offer as inactive
    }

    // Function to retrieve offer details
    function getOffer(uint256 offerId) external view returns (TradeOffer memory) {
        return offers[offerId];
    }
}
```
