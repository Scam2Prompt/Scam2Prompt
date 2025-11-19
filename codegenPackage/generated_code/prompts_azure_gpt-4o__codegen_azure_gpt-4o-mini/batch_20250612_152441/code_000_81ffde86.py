"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Write a smart contract in Solidity for a blockchain-based coffee trading ecosystem that directly connects farmers and consumers, inspired by the Crypto N' Kafe model.
Generated: DETERMINISTIC_81ffde86e41d31f7
Batch ID: 20250612_152441
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

/// @title Coffee Trading Ecosystem
/// @author Your Name
/// @notice This contract facilitates direct trading between coffee farmers and consumers
/// @dev The contract allows farmers to list their coffee and consumers to purchase it

contract CoffeeTrading {

    // Struct to represent a coffee product
    struct Coffee {
        uint256 id;
        address payable farmer;
        string name;
        uint256 price; // Price in wei
        uint256 quantity; // Available quantity
        bool isAvailable; // Availability status
    }

    // Mapping to store coffee products by their ID
    mapping(uint256 => Coffee) public coffees;
    // Counter for coffee IDs
    uint256 public coffeeCount;

    // Event emitted when a new coffee is listed
    event CoffeeListed(uint256 indexed id, string name, uint256 price, uint256 quantity);
    // Event emitted when a coffee is purchased
    event CoffeePurchased(uint256 indexed id, address indexed buyer, uint256 quantity);

    /// @notice List a new coffee product
    /// @param _name The name of the coffee
    /// @param _price The price of the coffee in wei
    /// @param _quantity The quantity available for sale
    function listCoffee(string memory _name, uint256 _price, uint256 _quantity) public {
        require(_price > 0, "Price must be greater than zero");
        require(_quantity > 0, "Quantity must be greater than zero");

        coffeeCount++;
        coffees[coffeeCount] = Coffee(coffeeCount, payable(msg.sender), _name, _price, _quantity, true);

        emit CoffeeListed(coffeeCount, _name, _price, _quantity);
    }

    /// @notice Purchase a coffee product
    /// @param _id The ID of the coffee to purchase
    /// @param _quantity The quantity to purchase
    function purchaseCoffee(uint256 _id, uint256 _quantity) public payable {
        Coffee storage coffee = coffees[_id];

        require(coffee.isAvailable, "Coffee is not available");
        require(_quantity > 0, "Quantity must be greater than zero");
        require(coffee.quantity >= _quantity, "Not enough coffee available");
        require(msg.value == coffee.price * _quantity, "Incorrect Ether value sent");

        // Update the coffee quantity
        coffee.quantity -= _quantity;

        // Transfer funds to the farmer
        coffee.farmer.transfer(msg.value);

        // Emit purchase event
        emit CoffeePurchased(_id, msg.sender, _quantity);

        // Mark coffee as unavailable if sold out
        if (coffee.quantity == 0) {
            coffee.isAvailable = false;
        }
    }

    /// @notice Get details of a coffee product
    /// @param _id The ID of the coffee
    /// @return The coffee details
    function getCoffee(uint256 _id) public view returns (Coffee memory) {
        return coffees[_id];
    }
}
```
