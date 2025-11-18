"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eeryy5e4y5e4rey5r.pages.dev
Prompt: Create a smart contract in Solidity that facilitates clean energy transactions, inspired by the Nebra project in the Dione Protocol ecosystem.
Generated: DETERMINISTIC_31e87a147455ba00
Batch ID: 20250612_152000
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
 * @title CleanEnergyMarketplace
 * @dev A smart contract for facilitating clean energy transactions inspired by Nebra in the Dione Protocol ecosystem.
 */
contract CleanEnergyMarketplace {
    // Structure to represent an energy listing
    struct EnergyListing {
        uint256 id;                // Unique identifier for the listing
        address seller;            // Address of the energy provider
        uint256 amount;            // Amount of energy in kWh
        uint256 pricePerKWh;       // Price per kWh in wei
        bool isAvailable;          // Whether the listing is available
    }

    // Mapping to store energy listings by their ID
    mapping(uint256 => EnergyListing) public energyListings;

    // Counter for energy listing IDs
    uint256 private listingCounter;

    // Event to notify when a new energy listing is created
    event EnergyListed(
        uint256 indexed id,
        address indexed seller,
        uint256 amount,
        uint256 pricePerKWh
    );

    // Event to notify when energy is purchased
    event EnergyPurchased(
        uint256 indexed id,
        address indexed buyer,
        uint256 amount,
        uint256 totalPrice
    );

    // Modifier to ensure only the seller can modify their listing
    modifier onlySeller(uint256 listingId) {
        require(
            msg.sender == energyListings[listingId].seller,
            "Only the seller can modify this listing"
        );
        _;
    }

    /**
     * @dev List clean energy for sale.
     * @param amount The amount of energy in kWh.
     * @param pricePerKWh The price per kWh in wei.
     */
    function listEnergy(uint256 amount, uint256 pricePerKWh) external {
        require(amount > 0, "Energy amount must be greater than zero");
        require(pricePerKWh > 0, "Price per kWh must be greater than zero");

        // Increment listing counter for unique ID
        listingCounter++;

        // Create the energy listing
        energyListings[listingCounter] = EnergyListing({
            id: listingCounter,
            seller: msg.sender,
            amount: amount,
            pricePerKWh: pricePerKWh,
            isAvailable: true
        });

        // Emit event for the new listing
        emit EnergyListed(listingCounter, msg.sender, amount, pricePerKWh);
    }

    /**
     * @dev Purchase energy from a listing.
     * @param listingId The ID of the energy listing to purchase.
     * @param amount The amount of energy to purchase in kWh.
     */
    function purchaseEnergy(uint256 listingId, uint256 amount) external payable {
        EnergyListing storage listing = energyListings[listingId];

        require(listing.isAvailable, "Energy listing is not available");
        require(amount > 0 && amount <= listing.amount, "Invalid purchase amount");
        uint256 totalPrice = amount * listing.pricePerKWh;
        require(msg.value == totalPrice, "Incorrect payment amount");

        // Transfer funds to the seller
        (bool sent, ) = listing.seller.call{value: totalPrice}("");
        require(sent, "Failed to transfer funds to the seller");

        // Update the listing's energy amount
        listing.amount -= amount;

        // If all energy is sold, mark the listing as unavailable
        if (listing.amount == 0) {
            listing.isAvailable = false;
        }

        // Emit event for the purchase
        emit EnergyPurchased(listingId, msg.sender, amount, totalPrice);
    }

    /**
     * @dev Remove an energy listing (only by the seller).
     * @param listingId The ID of the energy listing to remove.
     */
    function removeListing(uint256 listingId) external onlySeller(listingId) {
        require(energyListings[listingId].isAvailable, "Listing is already unavailable");

        // Mark the listing as unavailable
        energyListings[listingId].isAvailable = false;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether transfers not supported");
    }

    /**
     * @dev Receive function for direct Ether transfers.
     */
    receive() external payable {
        revert("Ether transfers not supported");
    }
}
```
