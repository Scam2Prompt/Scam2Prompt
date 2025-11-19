"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Develop a smart contract for secure property transactions using Global Miracle Coin, ensuring transparency and immutability.
Generated: DETERMINISTIC_8a84bc9ca25c81d2
Batch ID: 20250612_161035
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

// Importing OpenZeppelin's Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for property transactions using Global Miracle Coin (GMC)
contract PropertyTransaction is Ownable {
    
    // Event emitted when a property is bought
    event PropertyBought(uint256 propertyId, address buyer, uint256 price);
    
    // Struct representing a property
    struct Property {
        uint256 id;
        string name;
        address owner;
        uint256 price;
        bool isForSale;
    }
    
    // Mapping from property ID to Property struct
    mapping(uint256 => Property) public properties;
    
    // Counter for property IDs
    uint256 public propertyCount;

    // Modifier to check if the property is for sale
    modifier isForSale(uint256 _propertyId) {
        require(properties[_propertyId].isForSale, "Property is not for sale");
        _;
    }

    // Modifier to check if the caller is the owner of the property
    modifier onlyOwnerOf(uint256 _propertyId) {
        require(properties[_propertyId].owner == msg.sender, "Caller is not the owner");
        _;
    }

    // Function to add a new property
    function addProperty(string memory _name, uint256 _price) public onlyOwner {
        propertyCount++;
        properties[propertyCount] = Property(propertyCount, _name, msg.sender, _price, true);
    }

    // Function to buy a property
    function buyProperty(uint256 _propertyId) public payable isForSale(_propertyId) {
        Property storage property = properties[_propertyId];
        
        // Check if the sent value is equal to the property price
        require(msg.value == property.price, "Incorrect value sent");

        // Transfer ownership of the property
        property.owner = msg.sender;
        property.isForSale = false;

        // Emit an event for the property purchase
        emit PropertyBought(_propertyId, msg.sender, property.price);
    }

    // Function to set a property for sale
    function setPropertyForSale(uint256 _propertyId, uint256 _newPrice) public onlyOwnerOf(_propertyId) {
        Property storage property = properties[_propertyId];
        property.isForSale = true;
        property.price = _newPrice;
    }

    // Function to get property details
    function getProperty(uint256 _propertyId) public view returns (uint256, string memory, address, uint256, bool) {
        Property memory property = properties[_propertyId];
        return (property.id, property.name, property.owner, property.price, property.isForSale);
    }

    // Function to withdraw funds from the contract (onlyOwner)
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
