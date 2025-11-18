"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Write a Solidity contract for EarthMeta's NFT marketplace that supports trading virtual properties with gamified UX/UI features.
Generated: DETERMINISTIC_19c03e48573ec6ce
Batch ID: 20250612_145526
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

// Import required OpenZeppelin contracts for ERC721 and Ownable functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the NFT Marketplace
contract EarthMetaMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Data structure to hold property details
    struct Property {
        uint256 id;
        string name;
        string location;
        uint256 price;
        address owner;
        bool isListed;
    }

    // Mapping from property ID to property details
    mapping(uint256 => Property) private properties;
    
    // Tracking the next property ID
    Counters.Counter private propertyIdCounter;

    // Event emitted when a property is listed
    event PropertyListed(uint256 indexed propertyId, string name, uint256 price, address indexed owner);
    
    // Event emitted when a property is sold
    event PropertySold(uint256 indexed propertyId, address indexed newOwner, uint256 price);

    // Constructor to initialize the contract with a name and symbol for the NFT
    constructor() ERC721("EarthMetaProperty", "EMP") {}

    // Function to list a property for sale
    function listProperty(string memory name, string memory location, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        // Increment the property ID and create a new property
        propertyIdCounter.increment();
        uint256 newPropertyId = propertyIdCounter.current();
        properties[newPropertyId] = Property(newPropertyId, name, location, price, msg.sender, true);

        emit PropertyListed(newPropertyId, name, price, msg.sender);
    }

    // Function to buy a property
    function buyProperty(uint256 propertyId) external payable {
        Property storage property = properties[propertyId];

        // Ensure the property is listed and the price matches the value sent
        require(property.isListed, "Property is not listed");
        require(msg.value == property.price, "Incorrect price");

        // Transfer ownership of the property
        property.owner = msg.sender;
        property.isListed = false;

        // Transfer the funds to the previous owner
        payable(owner()).transfer(msg.value);

        emit PropertySold(propertyId, msg.sender, property.price);
    }

    // Function to get property details by ID
    function getProperty(uint256 propertyId) external view returns (Property memory) {
        return properties[propertyId];
    }

    // Function to withdraw contract balance (for owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to check if a property is listed for sale
    function isPropertyListed(uint256 propertyId) external view returns (bool) {
        return properties[propertyId].isListed;
    }
}
```
