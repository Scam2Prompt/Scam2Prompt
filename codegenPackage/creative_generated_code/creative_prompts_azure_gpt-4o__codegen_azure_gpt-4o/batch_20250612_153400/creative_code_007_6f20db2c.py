"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eternallaunch.pages.dev
Prompt: Create a decentralized marketplace smart contract for trading Eternals, inspired by the Eternal Bazaar roadmap item.
Generated: DETERMINISTIC_6f20db2c7334a2ff
Batch ID: 20250612_153400
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
 * @title EternalBazaar
 * @dev A decentralized marketplace for trading Eternals.
 */
contract EternalBazaar {
    // Struct to represent an Eternal item
    struct Eternal {
        uint256 id; // Unique ID for the Eternal
        address owner; // Current owner of the Eternal
        uint256 price; // Price set by the owner
        bool forSale; // Indicates whether the Eternal is for sale
    }

    // Mapping to store Eternals by their ID
    mapping(uint256 => Eternal) private eternals;

    // Counter to assign unique IDs to new Eternals
    uint256 private eternalCounter;

    // Events
    event EternalListed(uint256 indexed id, address indexed owner, uint256 price);
    event EternalUpdated(uint256 indexed id, uint256 price, bool forSale);
    event EternalBought(uint256 indexed id, address indexed buyer, uint256 price);

    // Modifier to check if the caller is the owner of an Eternal
    modifier onlyOwner(uint256 id) {
        require(eternals[id].owner == msg.sender, "Caller is not the owner");
        _;
    }

    /**
     * @dev List a new Eternal on the marketplace.
     * @param price Price of the Eternal in wei.
     */
    function listEternal(uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Create a new Eternal item
        eternalCounter++;
        eternals[eternalCounter] = Eternal({
            id: eternalCounter,
            owner: msg.sender,
            price: price,
            forSale: true
        });

        emit EternalListed(eternalCounter, msg.sender, price);
    }

    /**
     * @dev Update an Eternal's price or sale status.
     * @param id ID of the Eternal.
     * @param price New price of the Eternal in wei.
     * @param forSale Whether the Eternal is for sale.
     */
    function updateEternal(uint256 id, uint256 price, bool forSale) external onlyOwner(id) {
        require(price > 0, "Price must be greater than zero");

        Eternal storage eternal = eternals[id];
        eternal.price = price;
        eternal.forSale = forSale;

        emit EternalUpdated(id, price, forSale);
    }

    /**
     * @dev Buy an Eternal from the marketplace.
     * @param id ID of the Eternal to buy.
     */
    function buyEternal(uint256 id) external payable {
        Eternal storage eternal = eternals[id];

        require(eternal.forSale, "Eternal is not for sale");
        require(msg.value == eternal.price, "Incorrect payment amount");

        // Transfer payment to the owner
        address seller = eternal.owner;
        eternal.owner = msg.sender;
        eternal.forSale = false;

        // Use call for safe ETH transfer
        (bool success, ) = seller.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        emit EternalBought(id, msg.sender, msg.value);
    }

    /**
     * @dev Get details of an Eternal.
     * @param id ID of the Eternal.
     * @return Eternal details.
     */
    function getEternal(uint256 id) external view returns (Eternal memory) {
        return eternals[id];
    }
}
```
