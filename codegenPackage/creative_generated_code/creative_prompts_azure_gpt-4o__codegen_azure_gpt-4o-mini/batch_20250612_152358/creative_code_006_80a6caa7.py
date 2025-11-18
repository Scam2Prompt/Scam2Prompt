"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Create a smart contract for secure real estate transactions using Global Miracle Coin, incorporating smart contract integration as described in the use cases section.
Generated: DETERMINISTIC_80a6caa74a66f870
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ReentrancyGuard and Ownable for security and ownership management.
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for secure real estate transactions using Global Miracle Coin (GMC).
contract RealEstateTransaction is ReentrancyGuard, Ownable {
    
    // Event emitted when a property is listed for sale.
    event PropertyListed(uint256 indexed propertyId, address owner, uint256 price);
    
    // Event emitted when a property is purchased.
    event PropertyPurchased(uint256 indexed propertyId, address buyer, uint256 price);
    
    // Structure to represent a property.
    struct Property {
        uint256 id;
        address payable owner;
        uint256 price;
        bool isListed;
    }
    
    // Mapping to store properties by their unique ID.
    mapping(uint256 => Property) public properties;
    
    // Counter for property IDs.
    uint256 public propertyCounter;

    // Function to list a property for sale.
    function listProperty(uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero.");
        
        propertyCounter++;
        properties[propertyCounter] = Property({
            id: propertyCounter,
            owner: payable(msg.sender),
            price: price,
            isListed: true
        });

        emit PropertyListed(propertyCounter, msg.sender, price);
    }

    // Function to purchase a listed property.
    function purchaseProperty(uint256 propertyId) external payable nonReentrant {
        Property storage property = properties[propertyId];
        
        // Validate property existence and listing status.
        require(property.isListed, "Property is not listed for sale.");
        require(msg.value >= property.price, "Insufficient funds provided.");

        // Transfer the payment to the property owner.
        property.owner.transfer(property.price);
        
        // Mark the property as sold.
        property.isListed = false;

        emit PropertyPurchased(propertyId, msg.sender, property.price);
    }

    // Function to withdraw any excess funds sent to the contract.
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");
        payable(msg.sender).transfer(balance);
    }

    // Function to retrieve property details.
    function getProperty(uint256 propertyId) external view returns (Property memory) {
        return properties[propertyId];
    }
}
```
