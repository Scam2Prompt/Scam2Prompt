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

/// @title Coffee Trading Smart Contract
/// @author Your Name
/// @notice This contract facilitates coffee trading between farmers and consumers
/// @dev The contract uses ERC20 standard for coffee tokens
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract CoffeeTrading {
    struct Coffee {
        uint256 id;
        string name;
        uint256 price; // Price in wei
        address farmer;
        bool isAvailable;
    }

    // State variables
    uint256 public coffeeCount; // Counter for coffee items
    mapping(uint256 => Coffee) public coffees; // Mapping of coffee ID to Coffee struct
    mapping(address => uint256[]) public farmerCoffees; // Tracking coffees per farmer

    // Events
    event CoffeeAdded(uint256 indexed coffeeId, string name, uint256 price, address indexed farmer);
    event CoffeePurchased(uint256 indexed coffeeId, address indexed buyer);

    // Modifier to check if the caller is the farmer
    modifier onlyFarmer(uint256 _coffeeId) {
        require(msg.sender == coffees[_coffeeId].farmer, "Caller is not the farmer");
        _;
    }

    /// @notice Adds a new coffee to the marketplace
    /// @param _name The name of the coffee
    /// @param _price The price of the coffee in wei
    function addCoffee(string memory _name, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");

        coffeeCount++;
        coffees[coffeeCount] = Coffee(coffeeCount, _name, _price, msg.sender, true);
        
        // Keeping track of coffees per farmer
        farmerCoffees[msg.sender].push(coffeeCount);
        
        emit CoffeeAdded(coffeeCount, _name, _price, msg.sender);
    }

    /// @notice Purchases a coffee from the farmer
    /// @param _coffeeId The ID of the coffee to purchase
    function purchaseCoffee(uint256 _coffeeId) public payable {
        Coffee storage coffee = coffees[_coffeeId];
        
        require(coffee.isAvailable, "Coffee not available");
        require(msg.value == coffee.price, "Incorrect value sent");

        // Transfer funds to the farmer
        payable(coffee.farmer).transfer(msg.value);
        
        // Mark coffee as not available
        coffee.isAvailable = false;
        
        emit CoffeePurchased(_coffeeId, msg.sender);
    }

    /// @notice Allows the farmer to update the price of their coffee
    /// @param _coffeeId The ID of the coffee to update
    /// @param _newPrice The new price in wei
    function updateCoffeePrice(uint256 _coffeeId, uint256 _newPrice) public onlyFarmer(_coffeeId) {
        require(_newPrice > 0, "Price must be greater than zero");
        coffees[_coffeeId].price = _newPrice;
    }

    /// @notice Allows the farmer to mark coffee as unavailable
    /// @param _coffeeId The ID of the coffee to mark as unavailable
    function markCoffeeUnavailable(uint256 _coffeeId) public onlyFarmer(_coffeeId) {
        coffees[_coffeeId].isAvailable = false;
    }

    /// @notice Allows consumers to retrieve coffee details
    /// @param _coffeeId The ID of the coffee to retrieve
    /// @return Coffee details
    function getCoffee(uint256 _coffeeId) public view returns (Coffee memory) {
        return coffees[_coffeeId];
    }
}
```
