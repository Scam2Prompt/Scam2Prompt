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

/**
 * @title RealEstateLedger
 * @dev A smart contract that facilitates the transparent and secure transfer of property ownership.
 */
contract RealEstateLedger {
    // Struct to represent a property
    struct Property {
        uint256 propertyId; // Unique identifier for the property
        string location;    // Geographical location of the property
        uint256 size;       // Size of the property in square meters
        address owner;      // Current owner of the property
    }

    // Mapping of property ID to Property details
    mapping(uint256 => Property) private properties;

    // Event emitted when a new property is registered
    event PropertyRegistered(
        uint256 indexed propertyId,
        string location,
        uint256 size,
        address indexed owner
    );

    // Event emitted when property ownership is transferred
    event OwnershipTransferred(
        uint256 indexed propertyId,
        address indexed previousOwner,
        address indexed newOwner
    );

    // Modifier to check if the caller is the owner of the property
    modifier onlyOwner(uint256 propertyId) {
        require(
            properties[propertyId].owner == msg.sender,
            "Caller is not the owner of the property"
        );
        _;
    }

    /**
     * @dev Registers a new property in the ledger.
     * @param propertyId Unique ID for the property.
     * @param location Geographical location of the property.
     * @param size Size of the property in square meters.
     */
    function registerProperty(
        uint256 propertyId,
        string memory location,
        uint256 size
    ) external {
        // Ensure that the property ID is unique
        require(
            properties[propertyId].owner == address(0),
            "Property ID already exists"
        );

        // Create and store the new property
        properties[propertyId] = Property({
            propertyId: propertyId,
            location: location,
            size: size,
            owner: msg.sender
        });

        // Emit event for property registration
        emit PropertyRegistered(propertyId, location, size, msg.sender);
    }

    /**
     * @dev Transfers ownership of a property to a new owner.
     * @param propertyId ID of the property to transfer.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(uint256 propertyId, address newOwner)
        external
        onlyOwner(propertyId)
    {
        // Ensure the new owner address is valid
        require(newOwner != address(0), "Invalid new owner address");

        // Get the current owner of the property
        address previousOwner = properties[propertyId].owner;

        // Update the property owner
        properties[propertyId].owner = newOwner;

        // Emit event for ownership transfer
        emit OwnershipTransferred(propertyId, previousOwner, newOwner);
    }

    /**
     * @dev Retrieves details of a property.
     * @param propertyId ID of the property to fetch.
     * @return location Geographical location of the property.
     * @return size Size of the property in square meters.
     * @return owner Address of the current owner.
     */
    function getPropertyDetails(uint256 propertyId)
        external
        view
        returns (
            string memory location,
            uint256 size,
            address owner
        )
    {
        // Ensure the property exists
        require(
            properties[propertyId].owner != address(0),
            "Property does not exist"
        );

        Property memory property = properties[propertyId];
        return (property.location, property.size, property.owner);
    }
}
```
