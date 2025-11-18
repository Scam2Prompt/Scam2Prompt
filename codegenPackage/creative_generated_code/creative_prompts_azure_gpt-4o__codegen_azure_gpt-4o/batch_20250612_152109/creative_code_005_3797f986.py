"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-dioneprotocol.pages.dev
Prompt: Write a smart contract in Solidity that supports renewable energy trading, inspired by the principles of the Dione Protocol's Nebra platform.
Generated: DETERMINISTIC_3797f9862cb3324d
Batch ID: 20250612_152109
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
 * @title Renewable Energy Trading Smart Contract
 * @dev This contract allows participants to trade renewable energy units securely and transparently.
 */
contract RenewableEnergyTrading {
    // Struct representing an energy trade offer
    struct EnergyOffer {
        address seller;    // Address of the seller
        uint256 energyAmount; // Amount of energy in kWh
        uint256 pricePerUnit; // Price per kWh in wei
        bool isActive;     // Whether the offer is active
    }

    // Mapping of offer IDs to EnergyOffer structs
    mapping(uint256 => EnergyOffer) public energyOffers;

    // Counter for offer IDs
    uint256 public offerCounter;

    // Events
    event OfferCreated(uint256 indexed offerId, address indexed seller, uint256 energyAmount, uint256 pricePerUnit);
    event OfferCancelled(uint256 indexed offerId, address indexed seller);
    event EnergyPurchased(uint256 indexed offerId, address indexed buyer, uint256 energyAmount, uint256 totalPrice);

    // Modifier to check if the caller is the seller of the offer
    modifier onlySeller(uint256 offerId) {
        require(energyOffers[offerId].seller == msg.sender, "Caller is not the seller");
        _;
    }

    /**
     * @dev Create a new energy offer
     * @param energyAmount The amount of energy in kWh to sell
     * @param pricePerUnit The price per kWh in wei
     */
    function createOffer(uint256 energyAmount, uint256 pricePerUnit) external {
        require(energyAmount > 0, "Energy amount must be greater than zero");
        require(pricePerUnit > 0, "Price per unit must be greater than zero");

        offerCounter += 1; // Increment the offer ID counter

        energyOffers[offerCounter] = EnergyOffer({
            seller: msg.sender,
            energyAmount: energyAmount,
            pricePerUnit: pricePerUnit,
            isActive: true
        });

        emit OfferCreated(offerCounter, msg.sender, energyAmount, pricePerUnit);
    }

    /**
     * @dev Cancel an existing energy offer
     * @param offerId The ID of the offer to cancel
     */
    function cancelOffer(uint256 offerId) external onlySeller(offerId) {
        require(energyOffers[offerId].isActive, "Offer is not active");

        energyOffers[offerId].isActive = false;

        emit OfferCancelled(offerId, msg.sender);
    }

    /**
     * @dev Purchase energy from an active offer
     * @param offerId The ID of the offer to purchase from
     * @param energyAmount The amount of energy to buy in kWh
     */
    function purchaseEnergy(uint256 offerId, uint256 energyAmount) external payable {
        EnergyOffer storage offer = energyOffers[offerId];

        require(offer.isActive, "Offer is not active");
        require(energyAmount > 0, "Energy amount must be greater than zero");
        require(energyAmount <= offer.energyAmount, "Not enough energy available in the offer");

        uint256 totalPrice = energyAmount * offer.pricePerUnit;
        require(msg.value == totalPrice, "Incorrect payment amount");

        // Transfer payment to the seller
        payable(offer.seller).transfer(totalPrice);

        // Update the remaining energy in the offer
        offer.energyAmount -= energyAmount;

        // If the offer no longer has energy left, deactivate it
        if (offer.energyAmount == 0) {
            offer.isActive = false;
        }

        emit EnergyPurchased(offerId, msg.sender, energyAmount, totalPrice);
    }

    /**
     * @dev Retrieve details of an energy offer
     * @param offerId The ID of the offer to retrieve
     * @return seller The address of the seller
     * @return energyAmount The amount of energy in kWh available
     * @return pricePerUnit The price per kWh in wei
     * @return isActive Whether the offer is active
     */
    function getOffer(uint256 offerId)
        external
        view
        returns (
            address seller,
            uint256 energyAmount,
            uint256 pricePerUnit,
            bool isActive
        )
    {
        EnergyOffer memory offer = energyOffers[offerId];
        return (offer.seller, offer.energyAmount, offer.pricePerUnit, offer.isActive);
    }
}
```
