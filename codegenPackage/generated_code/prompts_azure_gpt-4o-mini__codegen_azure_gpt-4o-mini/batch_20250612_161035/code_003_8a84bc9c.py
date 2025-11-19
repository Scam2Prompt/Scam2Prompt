"""
Generated Code Metadata:
========================
Original URL: https://globalmiracle.online
Prompt: Develop a smart contract for secure property transactions using Global Miracle Coin, ensuring transparency and immutability.
Generated: DETERMINISTIC_8a84bc9ca25c81d2
Batch ID: 20250612_161035
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

contract PropertyTransaction {
    // Event to log property transactions
    event PropertyTransferred(
        uint256 indexed propertyId,
        address indexed from,
        address indexed to,
        uint256 value,
        uint256 timestamp
    );

    // Structure to hold property details
    struct Property {
        uint256 id;
        string description;
        address owner;
        uint256 value;
        bool isForSale;
    }

    // Mapping to store properties by their ID
    mapping(uint256 => Property) public properties;

    // Counter for property IDs
    uint256 public propertyCounter;

    // Modifier to check if the caller is the owner of the property
    modifier onlyOwner(uint256 propertyId) {
        require(msg.sender == properties[propertyId].owner, "Not the property owner");
        _;
    }

    // Modifier to check if the property is for sale
    modifier isForSale(uint256 propertyId) {
        require(properties[propertyId].isForSale, "Property is not for sale");
        _;
    }

    // Function to create a new property
    function createProperty(string memory description, uint256 value) public {
        require(value > 0, "Property value must be greater than zero");

        propertyCounter++;
        properties[propertyCounter] = Property({
            id: propertyCounter,
            description: description,
            owner: msg.sender,
            value: value,
            isForSale: false
        });
    }

    // Function to put a property up for sale
    function putPropertyForSale(uint256 propertyId, uint256 salePrice) public onlyOwner(propertyId) {
        require(salePrice > 0, "Sale price must be greater than zero");
        properties[propertyId].isForSale = true;
        properties[propertyId].value = salePrice;
    }

    // Function to transfer property ownership
    function transferProperty(uint256 propertyId) public payable isForSale(propertyId) {
        Property storage property = properties[propertyId];

        require(msg.value >= property.value, "Insufficient funds sent");
        require(msg.sender != property.owner, "Owner cannot buy their own property");

        // Transfer ownership
        address previousOwner = property.owner;
        property.owner = msg.sender;
        property.isForSale = false;

        // Emit the property transfer event
        emit PropertyTransferred(propertyId, previousOwner, msg.sender, property.value, block.timestamp);

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);
    }

    // Function to get property details
    function getPropertyDetails(uint256 propertyId) public view returns (Property memory) {
        return properties[propertyId];
    }
}
```
