"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chain-dioneprotoclcom.pages.dev
Prompt: Create a smart contract in Solidity for facilitating clean energy transactions, inspired by the Nebra project within the Dione Ecosystem.
Generated: DETERMINISTIC_f9537c17e78cefd8
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
pragma solidity ^0.8.17;

/**
 * @title CleanEnergyMarketplace
 * @dev A decentralized smart contract for facilitating clean energy transactions.
 */
contract CleanEnergyMarketplace {
    // ============================
    // Structs and Enums
    // ============================

    struct EnergyListing {
        address seller;        // Address of the energy provider
        uint256 amount;        // Amount of energy in kWh
        uint256 pricePerKWh;   // Price per kWh in wei
        bool isSold;           // Status of the listing
    }

    // ============================
    // State Variables
    // ============================

    uint256 public listingCounter; // Counter for tracking listings
    mapping(uint256 => EnergyListing) public listings; // Mapping of listing ID to energy listings

    // ============================
    // Events
    // ============================

    event ListingCreated(
        uint256 indexed listingId,
        address indexed seller,
        uint256 amount,
        uint256 pricePerKWh
    );

    event ListingPurchased(
        uint256 indexed listingId,
        address indexed buyer,
        uint256 amount,
        uint256 totalPrice
    );

    // ============================
    // Modifiers
    // ============================

    modifier validListing(uint256 listingId) {
        require(listingId < listingCounter, "Listing does not exist.");
        _;
    }

    modifier onlySeller(uint256 listingId) {
        require(listings[listingId].seller == msg.sender, "Only the seller can modify this listing.");
        _;
    }

    // ============================
    // Functions
    // ============================

    /**
     * @dev Create a new energy listing.
     * @param amount The amount of energy in kWh.
     * @param pricePerKWh The price per kWh in wei.
     */
    function createListing(uint256 amount, uint256 pricePerKWh) external {
        require(amount > 0, "Energy amount must be greater than zero.");
        require(pricePerKWh > 0, "Price per kWh must be greater than zero.");

        // Create a new listing
        listings[listingCounter] = EnergyListing({
            seller: msg.sender,
            amount: amount,
            pricePerKWh: pricePerKWh,
            isSold: false
        });

        // Emit an event
        emit ListingCreated(listingCounter, msg.sender, amount, pricePerKWh);

        // Increment the listing counter
        listingCounter++;
    }

    /**
     * @dev Purchase energy from a listing.
     * @param listingId The ID of the energy listing.
     */
    function purchaseEnergy(uint256 listingId) external payable validListing(listingId) {
        EnergyListing storage listing = listings[listingId];

        require(!listing.isSold, "This listing has already been sold.");
        require(msg.value == listing.amount * listing.pricePerKWh, "Incorrect payment amount.");

        // Mark the listing as sold
        listing.isSold = true;

        // Transfer funds to the seller
        (bool success, ) = listing.seller.call{value: msg.value}("");
        require(success, "Payment transfer to the seller failed.");

        // Emit an event
        emit ListingPurchased(listingId, msg.sender, listing.amount, msg.value);
    }

    /**
     * @dev Cancel a listing. Can only be called by the seller.
     * @param listingId The ID of the energy listing.
     */
    function cancelListing(uint256 listingId) external validListing(listingId) onlySeller(listingId) {
        require(!listings[listingId].isSold, "Cannot cancel a sold listing.");

        // Remove the listing
        delete listings[listingId];
    }

    /**
     * @dev Fetch details of a listing.
     * @param listingId The ID of the energy listing.
     * @return seller Address of the seller.
     * @return amount Amount of energy in kWh.
     * @return pricePerKWh Price per kWh in wei.
     * @return isSold If the listing has been sold.
     */
    function getListing(uint256 listingId)
        external
        view
        validListing(listingId)
        returns (
            address seller,
            uint256 amount,
            uint256 pricePerKWh,
            bool isSold
        )
    {
        EnergyListing memory listing = listings[listingId];
        return (listing.seller, listing.amount, listing.pricePerKWh, listing.isSold);
    }

    // ============================
    // Fallback and Receive
    // ============================

    // Fallback function to prevent sending ETH to the contract by mistake
    fallback() external payable {
        revert("Direct payments are not allowed.");
    }

    receive() external payable {
        revert("Direct payments are not allowed.");
    }
}
```
