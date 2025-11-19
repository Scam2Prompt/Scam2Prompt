"""
Generated Code Metadata:
========================
Original URL: https://ethereum.kim
Prompt: Write a Solidity contract that supports listing and querying active buy and sell offers for ERC-20 tokens, similar to the functionality described on ethereum.kim.
Generated: DETERMINISTIC_fcb8e678a6bcd42b
Batch ID: 20250612_151811
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for managing buy and sell offers for ERC20 tokens
contract TokenMarketplace is Ownable {
    // Struct to represent a buy or sell offer
    struct Offer {
        address token; // Address of the ERC20 token
        address seller; // Address of the seller (for sell offers)
        address buyer; // Address of the buyer (for buy offers)
        uint256 amount; // Amount of tokens for the offer
        uint256 price; // Price per token in wei
        bool isActive; // Status of the offer
    }

    // Mapping to store offers by their ID
    mapping(uint256 => Offer) public offers;
    // Counter for offer IDs
    uint256 public offerCount;

    // Event emitted when a new offer is created
    event OfferCreated(uint256 indexed offerId, address indexed token, address indexed seller, uint256 amount, uint256 price);
    // Event emitted when an offer is canceled
    event OfferCanceled(uint256 indexed offerId);
    // Event emitted when an offer is accepted
    event OfferAccepted(uint256 indexed offerId, address indexed buyer);

    // Function to create a new sell offer
    function createSellOffer(address token, uint256 amount, uint256 price) external {
        require(amount > 0, "Amount must be greater than zero");
        require(price > 0, "Price must be greater than zero");
        
        // Transfer tokens from seller to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Create the offer
        offers[offerCount] = Offer({
            token: token,
            seller: msg.sender,
            buyer: address(0),
            amount: amount,
            price: price,
            isActive: true
        });

        emit OfferCreated(offerCount, token, msg.sender, amount, price);
        offerCount++;
    }

    // Function to cancel an active offer
    function cancelOffer(uint256 offerId) external {
        Offer storage offer = offers[offerId];
        require(offer.isActive, "Offer is not active");
        require(offer.seller == msg.sender, "Only the seller can cancel the offer");

        // Mark the offer as inactive
        offer.isActive = false;

        // Transfer tokens back to the seller
        IERC20(offer.token).transfer(offer.seller, offer.amount);

        emit OfferCanceled(offerId);
    }

    // Function to accept a sell offer
    function acceptOffer(uint256 offerId) external payable {
        Offer storage offer = offers[offerId];
        require(offer.isActive, "Offer is not active");
        require(msg.value == offer.price * offer.amount, "Incorrect payment amount");

        // Mark the offer as inactive
        offer.isActive = false;
        offer.buyer = msg.sender;

        // Transfer tokens to the buyer
        IERC20(offer.token).transfer(msg.sender, offer.amount);
        // Transfer payment to the seller
        payable(offer.seller).transfer(msg.value);

        emit OfferAccepted(offerId, msg.sender);
    }

    // Function to query an offer by ID
    function getOffer(uint256 offerId) external view returns (Offer memory) {
        return offers[offerId];
    }

    // Function to withdraw any accidentally sent ERC20 tokens to the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
