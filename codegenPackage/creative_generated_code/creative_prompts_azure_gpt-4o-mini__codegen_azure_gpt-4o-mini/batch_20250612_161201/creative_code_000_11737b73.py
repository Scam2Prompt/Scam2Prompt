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

/// @title Coffee Trading Platform
/// @author Your Name
/// @notice A smart contract that allows farmers to sell coffee directly to consumers
/// @dev This contract includes features for adding farmers, listing coffees, and handling transactions

contract CoffeeTradingPlatform {
    // Struct to represent a Farmer
    struct Farmer {
        address farmerAddress;
        string name;
        bool isRegistered;
    }

    // Struct to represent a Coffee product
    struct Coffee {
        uint256 id;
        address farmer;
        string name;
        uint256 price; // in wei
        uint256 quantity; // in units
        bool isAvailable;
    }

    // Mapping of farmer address to Farmer data
    mapping(address => Farmer) public farmers;
    // Mapping to store coffees by unique ID
    mapping(uint256 => Coffee) public coffees;
    // Counter for coffee IDs
    uint256 public coffeeCount;

    // Events to log important contract actions
    event FarmerRegistered(address farmerAddress, string name);
    event CoffeeListed(uint256 id, string name, uint256 price, uint256 quantity);
    event CoffeePurchased(uint256 id, address buyer, uint256 quantity);

    /// @notice Registers a new farmer
    /// @param _name The name of the farmer
    function registerFarmer(string memory _name) external {
        require(!farmers[msg.sender].isRegistered, "Farmer is already registered.");

        farmers[msg.sender] = Farmer({
            farmerAddress: msg.sender,
            name: _name,
            isRegistered: true
        });

        emit FarmerRegistered(msg.sender, _name);
    }

    /// @notice Lists a new coffee for sale
    /// @param _name The name of the coffee
    /// @param _price The price of the coffee in wei
    /// @param _quantity The available quantity of the coffee
    function listCoffee(string memory _name, uint256 _price, uint256 _quantity) external {
        require(farmers[msg.sender].isRegistered, "Only registered farmers can list coffee.");
        require(_price > 0, "Price must be greater than zero.");
        require(_quantity > 0, "Quantity must be greater than zero.");

        coffeeCount++;
        coffees[coffeeCount] = Coffee({
            id: coffeeCount,
            farmer: msg.sender,
            name: _name,
            price: _price,
            quantity: _quantity,
            isAvailable: true
        });

        emit CoffeeListed(coffeeCount, _name, _price, _quantity);
    }

    /// @notice Purchases a specified quantity of coffee
    /// @param _coffeeId The ID of the coffee to purchase
    /// @param _quantity The quantity of coffee to purchase
    function purchaseCoffee(uint256 _coffeeId, uint256 _quantity) external payable {
        Coffee storage coffee = coffees[_coffeeId];
        
        require(coffee.isAvailable, "Coffee is not available.");
        require(_quantity > 0, "Quantity must be greater than zero.");
        require(coffee.quantity >= _quantity, "Not enough coffee available.");
        require(msg.value == coffee.price * _quantity, "Incorrect Ether sent.");

        // Update coffee quantity
        coffee.quantity -= _quantity;

        // Forward the payment to the farmer
        payable(coffee.farmer).transfer(msg.value);

        emit CoffeePurchased(_coffeeId, msg.sender, _quantity);
    }

    /// @notice Allows a farmer to withdraw their earnings
    function withdrawEarnings() external {
        // Note: Implement earnings tracking and withdrawal logic as needed
        // This is a placeholder for potential future development
    }

    /// @notice Allows the farmer to update the coffee listing
    /// @param _coffeeId The ID of the coffee to be updated
    /// @param _newPrice The new price for the coffee
    /// @param _newQuantity The new quantity for the coffee
    function updateCoffee(uint256 _coffeeId, uint256 _newPrice, uint256 _newQuantity) external {
        Coffee storage coffee = coffees[_coffeeId];
        require(msg.sender == coffee.farmer, "Only the farmer can update the coffee.");
        require(coffee.isAvailable, "Coffee is not available.");
        require(_newPrice > 0, "Price must be greater than zero.");
        require(_newQuantity >= 0, "Quantity must be non-negative.");

        coffee.price = _newPrice;
        coffee.quantity = _newQuantity;
    }
}
```
