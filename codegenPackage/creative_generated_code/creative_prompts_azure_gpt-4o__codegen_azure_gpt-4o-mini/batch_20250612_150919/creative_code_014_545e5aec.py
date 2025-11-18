"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Generate a Solidity smart contract for a real estate ledger system on Mazze, leveraging its transparent and secure ledger for property transfers.
Generated: DETERMINISTIC_545e5aecb161b6df
Batch ID: 20250612_150919
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

// Importing libraries for safe math operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for managing a real estate ledger system
contract RealEstateLedger {
    using SafeMath for uint256;

    // Structure to represent a property
    struct Property {
        uint256 id;              // Unique identifier for the property
        string name;             // Name of the property
        address owner;           // Current owner's address
        uint256 price;           // Market price of the property
        bool isListed;           // Status indicating if the property is for sale
    }

    // Mapping to store properties by their unique ID
    mapping(uint256 => Property) private properties;
    uint256 private propertyCount;  // Counter for property IDs

    // Event emissions for property transactions
    event PropertyAdded(uint256 indexed propertyId, string name, address indexed owner, uint256 price);
    event PropertyListed(uint256 indexed propertyId, uint256 price);
    event PropertyTransferred(uint256 indexed propertyId, address indexed from, address indexed to, uint256 price);

    // Modifier to check if the caller is the property owner
    modifier onlyOwner(uint256 _propertyId) {
        require(properties[_propertyId].owner == msg.sender, "Caller is not the owner");
        _;
    }

    // Function to add a new property to the ledger
    function addProperty(string memory _name, uint256 _price) public {
        propertyCount = propertyCount.add(1); // Increase property count
        properties[propertyCount] = Property(propertyCount, _name, msg.sender, _price, false);
        emit PropertyAdded(propertyCount, _name, msg.sender, _price); // Emit event
    }

    // Function to list a property for sale
    function listProperty(uint256 _propertyId, uint256 _price) public onlyOwner(_propertyId) {
        require(!properties[_propertyId].isListed, "Property is already listed for sale");
        properties[_propertyId].isListed = true;
        properties[_propertyId].price = _price; // Update price
        emit PropertyListed(_propertyId, _price); // Emit event
    }

    // Function to transfer ownership of a property
    function transferProperty(uint256 _propertyId, address _newOwner) public payable onlyOwner(_propertyId) {
        require(properties[_propertyId].isListed, "Property is not listed for sale");
        require(msg.value >= properties[_propertyId].price, "Insufficient payment");

        // Transfer the ownership
        properties[_propertyId].owner = _newOwner;
        properties[_propertyId].isListed = false; // Remove listing status
        emit PropertyTransferred(_propertyId, msg.sender, _newOwner, msg.value); // Emit event

        // Transfer payment (could be improved with a withdrawal pattern)
        payable(msg.sender).transfer(msg.value);
    }

    // Function to get property details
    function getProperty(uint256 _propertyId) public view returns (string memory, address, uint256, bool) {
        Property memory property = properties[_propertyId];
        return (property.name, property.owner, property.price, property.isListed);
    }

    // Function to get the total number of properties
    function getTotalProperties() public view returns (uint256) {
        return propertyCount;
    }
}
```
