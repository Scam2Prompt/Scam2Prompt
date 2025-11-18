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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

/**
 * @title TokenMarketplace
 * @dev A contract to list and query active buy and sell offers for ERC-20 tokens.
 */
contract TokenMarketplace {
    // Struct to represent an offer
    struct Offer {
        address creator; // Address of the offer creator
        address token;   // Address of the ERC-20 token
        uint256 amount;  // Token amount for the offer
        uint256 price;   // Price in wei for the offer
        bool isBuyOffer; // True if it's a buy offer, false if it's a sell offer
        bool isActive;   // True if the offer is active
    }

    // List of all offers
    Offer[] public offers;

    // Event emitted when a new offer is created
    event OfferCreated(
        uint256 offerId,
        address indexed creator,
        address indexed token,
        uint256 amount,
        uint256 price,
        bool isBuyOffer
    );

    // Event emitted when an offer is canceled
    event OfferCanceled(uint256 offerId);

    /**
     * @dev Create a buy or sell offer for a specified ERC-20 token.
     * @param token Address of the ERC-20 token involved in the offer.
     * @param amount The amount of the token involved in the offer.
     * @param price The price in wei for the offer.
     * @param isBuyOffer True if it's a buy offer, false if it's a sell offer.
     */
    function createOffer(address token, uint256 amount, uint256 price, bool isBuyOffer) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(price > 0, "Price must be greater than zero");

        if (!isBuyOffer) {
            // For sell offers, the creator must have approved the token transfer
            require(
                IERC20(token).transferFrom(msg.sender, address(this), amount),
                "Token transfer failed"
            );
        }

        // Create the offer and add it to the list
        offers.push(
            Offer({
                creator: msg.sender,
                token: token,
                amount: amount,
                price: price,
                isBuyOffer: isBuyOffer,
                isActive: true
            })
        );

        emit OfferCreated(offers.length - 1, msg.sender, token, amount, price, isBuyOffer);
    }

    /**
     * @dev Cancel an active offer. Only the creator of the offer can cancel it.
     * @param offerId The ID of the offer to cancel.
     */
    function cancelOffer(uint256 offerId) external {
        require(offerId < offers.length, "Invalid offer ID");
        Offer storage offer = offers[offerId];
        require(offer.isActive, "Offer is not active");
        require(offer.creator == msg.sender, "Only the offer creator can cancel");

        if (!offer.isBuyOffer) {
            // For sell offers, return the tokens back to the creator
            require(
                IERC20(offer.token).transfer(offer.creator, offer.amount),
                "Token transfer failed"
            );
        }

        offer.isActive = false; // Mark the offer as inactive
        emit OfferCanceled(offerId);
    }

    /**
     * @dev Get details of an offer by its ID.
     * @param offerId The ID of the offer to query.
     * @return Offer details.
     */
    function getOffer(uint256 offerId)
        external
        view
        returns (
            address creator,
            address token,
            uint256 amount,
            uint256 price,
            bool isBuyOffer,
            bool isActive
        )
    {
        require(offerId < offers.length, "Invalid offer ID");
        Offer memory offer = offers[offerId];
        return (
            offer.creator,
            offer.token,
            offer.amount,
            offer.price,
            offer.isBuyOffer,
            offer.isActive
        );
    }

    /**
     * @dev Get the total number of offers created.
     * @return The total count of offers.
     */
    function getTotalOffers() external view returns (uint256) {
        return offers.length;
    }
}
```
