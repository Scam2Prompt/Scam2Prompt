"""
Generated Code Metadata:
========================
Original URL: https://globalmiracle.online
Prompt: Create a smart contract for secure real estate transactions using Global Miracle Coin, incorporating smart contract integration as described in the use cases section.
Generated: DETERMINISTIC_80a6caa74a66f870
Batch ID: 20250612_152358
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

// Importing the ERC20 interface for Global Miracle Coin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for secure real estate transactions
contract RealEstateTransaction {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public globalMiracleCoin; // Instance of the Global Miracle Coin contract

    // Struct to represent a property
    struct Property {
        uint256 id;
        string name;
        address payable seller;
        address buyer;
        uint256 price;
        bool isSold;
    }

    // Mapping to store properties by their ID
    mapping(uint256 => Property) public properties;
    uint256 public propertyCount; // Counter for property IDs

    // Events for logging
    event PropertyListed(uint256 id, string name, address seller, uint256 price);
    event PropertySold(uint256 id, address buyer, uint256 price);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _globalMiracleCoin) {
        owner = msg.sender; // Set the contract deployer as the owner
        globalMiracleCoin = IERC20(_globalMiracleCoin); // Set the Global Miracle Coin contract address
    }

    // Function to list a property for sale
    function listProperty(string memory _name, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");

        propertyCount++; // Increment property count
        properties[propertyCount] = Property(propertyCount, _name, payable(msg.sender), address(0), _price, false);

        emit PropertyListed(propertyCount, _name, msg.sender, _price); // Emit event
    }

    // Function to buy a property
    function buyProperty(uint256 _id) public {
        Property storage property = properties[_id]; // Reference to the property

        require(_id > 0 && _id <= propertyCount, "Property does not exist");
        require(!property.isSold, "Property is already sold");
        require(msg.sender != property.seller, "Seller cannot buy their own property");
        require(globalMiracleCoin.balanceOf(msg.sender) >= property.price, "Insufficient funds");

        // Transfer the payment
        globalMiracleCoin.transferFrom(msg.sender, property.seller, property.price);

        // Update property status
        property.buyer = msg.sender;
        property.isSold = true;

        emit PropertySold(_id, msg.sender, property.price); // Emit event
    }

    // Function to retrieve property details
    function getProperty(uint256 _id) public view returns (Property memory) {
        require(_id > 0 && _id <= propertyCount, "Property does not exist");
        return properties[_id]; // Return the property details
    }

    // Function to withdraw funds (only for the owner)
    function withdrawFunds() public onlyOwner {
        payable(owner).transfer(address(this).balance); // Transfer contract balance to owner
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
