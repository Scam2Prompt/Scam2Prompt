"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.kim
Prompt: Write a Solidity contract that supports listing and querying active buy and sell offers for ERC-20 tokens, similar to the functionality described on ethereum.kim.
Generated: DETERMINISTIC_fcb8e678a6bcd42b
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Struct to define a buy or sell offer
struct Offer {
    address token;
    address owner;
    uint256 amount;
    uint256 price; // Price in wei per token
    bool isActive; // Status of the offer
}

// Contract for managing buy and sell offers for ERC-20 tokens
contract TokenMarket is Ownable {
    // Mapping of offers by their IDs
    mapping(uint256 => Offer) private offers;
    // Counter for the offer IDs
    uint256 private offerIdCounter;

    // Event emitted when a new offer is created
    event OfferCreated(uint256 offerId, address indexed token, address indexed owner, uint256 amount, uint256 price);
    // Event emitted when an offer is cancelled
    event OfferCancelled(uint256 offerId);
    // Event emitted when an offer is completed
    event OfferCompleted(uint256 offerId, address indexed buyer);

    // Create a new offer
    function createOffer(address token, uint256 amount, uint256 price) external {
        require(amount > 0, "Amount must be greater than zero");
        require(price > 0, "Price must be greater than zero");

        // Transfer tokens from the offer creator to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Increment offer ID counter and create the offer
        uint256 newOfferId = offerIdCounter++;
        offers[newOfferId] = Offer({
            token: token,
            owner: msg.sender,
            amount: amount,
            price: price,
            isActive: true
        });

        emit OfferCreated(newOfferId, token, msg.sender, amount, price);
    }

    // Cancel an active offer
    function cancelOffer(uint256 offerId) external {
        Offer storage offer = offers[offerId];
        require(offer.isActive, "Offer is not active");
        require(offer.owner == msg.sender, "Only the owner can cancel the offer");

        // Mark offer as inactive and return tokens
        offer.isActive = false;
        IERC20(offer.token).transfer(offer.owner, offer.amount);

        emit OfferCancelled(offerId);
    }

    // Complete an offer by buying tokens
    function completeOffer(uint256 offerId) external payable {
        Offer storage offer = offers[offerId];
        require(offer.isActive, "Offer is not active");
        require(msg.value == offer.price * offer.amount, "Incorrect payment amount");

        // Transfer tokens to buyer and funds to seller
        IERC20(offer.token).transfer(msg.sender, offer.amount);
        payable(offer.owner).transfer(msg.value);

        // Mark offer as inactive
        offer.isActive = false;

        emit OfferCompleted(offerId, msg.sender);
    }

    // Query active offers
    function getActiveOffers(uint256 startIndex, uint256 endIndex) external view returns (Offer[] memory) {
        require(startIndex < endIndex, "Invalid index range");
        require(endIndex <= offerIdCounter, "Index out of bounds");

        // Create an array to hold active offers
        Offer[] memory activeOffers = new Offer[](endIndex - startIndex);
        uint256 index = 0;

        // Iterate through the offers and collect active ones
        for (uint256 i = startIndex; i < endIndex; i++) {
            if (offers[i].isActive) {
                activeOffers[index] = offers[i];
                index++;
            }
        }

        return activeOffers;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
