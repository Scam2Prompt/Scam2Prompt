"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Generate a smart contract in Solidity for a coffee trading platform that connects farmers directly to consumers, as described on the Crypto N' Kafe website.
Generated: DETERMINISTIC_11737b737f025698
Batch ID: 20250612_161201
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
 * @title CoffeeTradingPlatform
 * @dev A smart contract to connect farmers directly to consumers for coffee trading.
 */
contract CoffeeTradingPlatform {
    // Struct to represent a Coffee Batch
    struct CoffeeBatch {
        uint256 id;             // Unique ID of the coffee batch
        string origin;          // Origin of the coffee (e.g., country/region)
        string type;            // Type of coffee (e.g., Arabica, Robusta)
        uint256 weight;         // Weight in kilograms
        uint256 pricePerKg;     // Price per kilogram in wei
        address payable farmer; // Address of the farmer
        bool sold;              // Indicates if the batch is sold
    }

    // Mapping to store coffee batches by ID
    mapping(uint256 => CoffeeBatch) public coffeeBatches;

    // Counter for generating unique IDs for coffee batches
    uint256 public nextBatchId;

    // Event emitted when a new coffee batch is listed
    event CoffeeBatchListed(
        uint256 indexed id,
        string origin,
        string type,
        uint256 weight,
        uint256 pricePerKg,
        address indexed farmer
    );

    // Event emitted when a coffee batch is sold
    event CoffeeBatchSold(
        uint256 indexed id,
        address indexed buyer,
        uint256 totalPrice
    );

    /**
     * @dev List a new coffee batch for sale.
     * @param origin The origin of the coffee.
     * @param type The type of coffee.
     * @param weight The weight of the coffee batch in kilograms.
     * @param pricePerKg The price per kilogram in wei.
     */
    function listCoffeeBatch(
        string memory origin,
        string memory type,
        uint256 weight,
        uint256 pricePerKg
    ) external {
        require(weight > 0, "Weight must be greater than zero.");
        require(pricePerKg > 0, "Price per kilogram must be greater than zero.");

        // Create a new coffee batch struct and store it in the mapping
        coffeeBatches[nextBatchId] = CoffeeBatch({
            id: nextBatchId,
            origin: origin,
            type: type,
            weight: weight,
            pricePerKg: pricePerKg,
            farmer: payable(msg.sender),
            sold: false
        });

        // Emit the CoffeeBatchListed event
        emit CoffeeBatchListed(nextBatchId, origin, type, weight, pricePerKg, msg.sender);

        // Increment the batch ID counter for the next batch
        nextBatchId++;
    }

    /**
     * @dev Purchase a coffee batch.
     * @param batchId The ID of the coffee batch to purchase.
     */
    function purchaseCoffeeBatch(uint256 batchId) external payable {
        CoffeeBatch storage batch = coffeeBatches[batchId];

        require(batch.id == batchId, "Batch does not exist.");
        require(!batch.sold, "Batch has already been sold.");
        uint256 totalPrice = batch.weight * batch.pricePerKg;
        require(msg.value >= totalPrice, "Insufficient funds sent.");

        // Transfer funds to the farmer
        batch.farmer.transfer(totalPrice);

        // Mark the batch as sold
        batch.sold = true;

        // Emit the CoffeeBatchSold event
        emit CoffeeBatchSold(batchId, msg.sender, totalPrice);

        // Refund excess payment if applicable
        if (msg.value > totalPrice) {
            payable(msg.sender).transfer(msg.value - totalPrice);
        }
    }

    /**
     * @dev Get details of a coffee batch.
     * @param batchId The ID of the coffee batch.
     * @return CoffeeBatch struct with all details.
     */
    function getCoffeeBatch(uint256 batchId) external view returns (CoffeeBatch memory) {
        require(coffeeBatches[batchId].id == batchId, "Batch does not exist.");
        return coffeeBatches[batchId];
    }
}
```
