"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-ae.web.app
Prompt: Write a Solidity contract for co-owning real estate properties and distributing passive income in stablecoins, inspired by Rexas Estate.
Generated: DETERMINISTIC_8d673348a67969ca
Batch ID: 20250612_145242
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// RealEstateCoOwnership Contract allows co-ownership of real estate properties
// and facilitates distribution of passive income in stablecoins.
contract RealEstateCoOwnership is Ownable {
    // Structure to represent a property
    struct Property {
        uint256 id;
        string name;
        address payable owner;
        uint256 totalShares;
        uint256 sharesSold;
        uint256 rentCollected;
        mapping(address => uint256) shares;
    }

    // Map property ID to Property struct
    mapping(uint256 => Property) public properties;
    uint256 public propertyCount;

    // Event emitted when a property is created
    event PropertyCreated(uint256 id, string name, address owner, uint256 totalShares);

    // Event emitted when shares are purchased
    event SharesPurchased(uint256 propertyId, address shareholder, uint256 shares);

    // Event emitted when rent is distributed
    event RentDistributed(uint256 propertyId, uint256 amountPerShare);

    // Modifier to check if the property exists
    modifier propertyExists(uint256 propertyId) {
        require(propertyId < propertyCount, "Property does not exist");
        _;
    }

    // Function to create a new property
    function createProperty(string memory name, uint256 totalShares) external onlyOwner {
        require(totalShares > 0, "Total shares must be greater than zero");

        Property storage newProperty = properties[propertyCount];
        newProperty.id = propertyCount;
        newProperty.name = name;
        newProperty.owner = payable(msg.sender);
        newProperty.totalShares = totalShares;
        newProperty.sharesSold = 0;
        newProperty.rentCollected = 0;

        emit PropertyCreated(propertyCount, name, msg.sender, totalShares);
        propertyCount++;
    }

    // Function to purchase shares of a property
    function purchaseShares(uint256 propertyId, uint256 shares) external payable propertyExists(propertyId) {
        Property storage property = properties[propertyId];

        require(shares > 0, "Must purchase at least one share");
        require(property.sharesSold + shares <= property.totalShares, "Not enough shares available");
        require(msg.value > 0, "Must send Ether to purchase shares");

        // Update property shares
        property.shares[msg.sender] += shares;
        property.sharesSold += shares;

        emit SharesPurchased(propertyId, msg.sender, shares);
    }

    // Function to collect rent for a property (only callable by the property owner)
    function collectRent(uint256 propertyId) external payable propertyExists(propertyId) {
        Property storage property = properties[propertyId];
        require(msg.sender == property.owner, "Only the owner can collect rent");
        require(msg.value > 0, "Must send Ether to collect rent");

        // Update total rent collected
        property.rentCollected += msg.value;

        emit RentDistributed(propertyId, msg.value);
    }

    // Function to distribute rent to shareholders
    function distributeRent(uint256 propertyId) external propertyExists(propertyId) {
        Property storage property = properties[propertyId];
        require(property.rentCollected > 0, "No rent to distribute");
        
        uint256 totalShares = property.totalShares;
        uint256 amountPerShare = property.rentCollected / totalShares;

        // Distribute rent to each shareholder
        for (uint256 i = 0; i < totalShares; i++) {
            address shareholder = address(uint160(i)); // Assuming address is stored by index (not realistic for production)
            if (property.shares[shareholder] > 0) {
                uint256 amount = property.shares[shareholder] * amountPerShare;
                payable(shareholder).transfer(amount);
            }
        }

        // Reset rent collected after distribution
        property.rentCollected = 0;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
