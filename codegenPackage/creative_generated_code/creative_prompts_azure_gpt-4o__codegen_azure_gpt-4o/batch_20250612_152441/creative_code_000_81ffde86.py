"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Write a smart contract in Solidity for a blockchain-based coffee trading ecosystem that directly connects farmers and consumers, inspired by the Crypto N' Kafe model.
Generated: DETERMINISTIC_81ffde86e41d31f7
Batch ID: 20250612_152441
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
 * @title CoffeeTrading
 * @dev Smart contract for a blockchain-based coffee trading ecosystem
 * that connects farmers and consumers directly.
 */
contract CoffeeTrading {
    // Struct to represent a coffee product
    struct Coffee {
        uint256 id;
        string name;
        string origin;
        string description;
        uint256 price; // in wei
        address payable farmer;
        bool sold;
    }

    // State variables
    uint256 private nextCoffeeId;
    mapping(uint256 => Coffee) private coffees;

    // Events
    event CoffeeListed(
        uint256 indexed coffeeId,
        string name,
        string origin,
        uint256 price,
        address indexed farmer
    );
    event CoffeePurchased(
        uint256 indexed coffeeId,
        string name,
        address indexed buyer
    );

    /**
     * @dev Modifier to check if the caller is the farmer of a coffee product.
     * @param coffeeId The ID of the coffee product.
     */
    modifier onlyFarmer(uint256 coffeeId) {
        require(
            coffees[coffeeId].farmer == msg.sender,
            "Only the farmer can perform this action."
        );
        _;
    }

    /**
     * @dev Function for farmers to list their coffee products.
     * @param name The name of the coffee product.
     * @param origin The origin of the coffee product (e.g., country, region).
     * @param description A description of the coffee product.
     * @param price The price of the coffee product in wei.
     */
    function listCoffee(
        string memory name,
        string memory origin,
        string memory description,
        uint256 price
    ) external {
        require(price > 0, "Price must be greater than zero.");

        // Create a new coffee product
        Coffee memory newCoffee = Coffee({
            id: nextCoffeeId,
            name: name,
            origin: origin,
            description: description,
            price: price,
            farmer: payable(msg.sender),
            sold: false
        });

        // Save the coffee product in the mapping
        coffees[nextCoffeeId] = newCoffee;
        nextCoffeeId++;

        // Emit CoffeeListed event
        emit CoffeeListed(newCoffee.id, name, origin, price, msg.sender);
    }

    /**
     * @dev Function for consumers to purchase a coffee product.
     * @param coffeeId The ID of the coffee product to purchase.
     */
    function purchaseCoffee(uint256 coffeeId) external payable {
        Coffee storage coffee = coffees[coffeeId];

        // Validate the coffee product
        require(coffee.id == coffeeId, "Coffee product does not exist.");
        require(!coffee.sold, "Coffee product has already been sold.");
        require(msg.value == coffee.price, "Incorrect payment amount.");

        // Mark the coffee as sold
        coffee.sold = true;

        // Transfer payment to the farmer
        coffee.farmer.transfer(msg.value);

        // Emit CoffeePurchased event
        emit CoffeePurchased(coffeeId, coffee.name, msg.sender);
    }

    /**
     * @dev Function for consumers to view the details of a coffee product.
     * @param coffeeId The ID of the coffee product.
     * @return Coffee details.
     */
    function viewCoffee(uint256 coffeeId)
        external
        view
        returns (
            string memory name,
            string memory origin,
            string memory description,
            uint256 price,
            address farmer,
            bool sold
        )
    {
        Coffee memory coffee = coffees[coffeeId];
        require(coffee.id == coffeeId, "Coffee product does not exist.");

        return (
            coffee.name,
            coffee.origin,
            coffee.description,
            coffee.price,
            coffee.farmer,
            coffee.sold
        );
    }

    /**
     * @dev Function to get the total number of coffee products listed.
     * @return Total number of coffee products.
     */
    function getTotalCoffeeProducts() external view returns (uint256) {
        return nextCoffeeId;
    }
}
```
