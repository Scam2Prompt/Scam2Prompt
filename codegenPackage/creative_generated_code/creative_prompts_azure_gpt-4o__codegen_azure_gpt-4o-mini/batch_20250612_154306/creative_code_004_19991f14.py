"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-news.com
Prompt: Write a smart contract in Solidity to facilitate energy trading and microgrid management on Ethereum, referencing the use cases described in revolutionizing energy trading with Ethereum.
Generated: DETERMINISTIC_19991f147c5f13fe
Batch ID: 20250612_154306
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

contract EnergyTrading {
    // Struct to represent an energy offer
    struct EnergyOffer {
        address seller;
        uint256 amount; // Amount of energy in kWh
        uint256 price;  // Price per kWh in wei
        bool isActive;  // Status of the offer
    }

    // Mapping to store energy offers by their unique ID
    mapping(uint256 => EnergyOffer) public energyOffers;

    // Counter for unique offer IDs
    uint256 public offerCount;

    // Event emitted when a new energy offer is created
    event OfferCreated(uint256 offerId, address indexed seller, uint256 amount, uint256 price);

    // Event emitted when an energy offer is purchased
    event OfferPurchased(uint256 offerId, address indexed buyer, uint256 amount);

    // Modifier to check if the offer is active
    modifier isOfferActive(uint256 _offerId) {
        require(energyOffers[_offerId].isActive, "Energy offer is not active");
        _;
    }

    // Function to create a new energy offer
    function createEnergyOffer(uint256 _amount, uint256 _price) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_price > 0, "Price must be greater than zero");

        // Increment offer count and create a new offer
        offerCount++;
        energyOffers[offerCount] = EnergyOffer(msg.sender, _amount, _price, true);

        emit OfferCreated(offerCount, msg.sender, _amount, _price);
    }

    // Function to purchase energy from an active offer
    function purchaseEnergy(uint256 _offerId, uint256 _amount) external payable isOfferActive(_offerId) {
        EnergyOffer storage offer = energyOffers[_offerId];

        // Check if the requested amount is available
        require(_amount <= offer.amount, "Requested amount exceeds available energy");
        // Check if sufficient Ether is sent
        require(msg.value >= offer.price * _amount, "Insufficient payment");

        // Update the offer's remaining amount
        offer.amount -= _amount;

        // If the offer is fully consumed, deactivate it
        if (offer.amount == 0) {
            offer.isActive = false;
        }

        // Transfer funds to the seller
        payable(offer.seller).transfer(msg.value);

        emit OfferPurchased(_offerId, msg.sender, _amount);
    }

    // Function to retrieve details of an energy offer
    function getOfferDetails(uint256 _offerId) external view returns (EnergyOffer memory) {
        require(_offerId > 0 && _offerId <= offerCount, "Invalid offer ID");
        return energyOffers[_offerId];
    }

    // Function to deactivate an energy offer (for seller)
    function deactivateOffer(uint256 _offerId) external isOfferActive(_offerId) {
        require(energyOffers[_offerId].seller == msg.sender, "Only seller can deactivate the offer");
        energyOffers[_offerId].isActive = false;
    }
}
```
