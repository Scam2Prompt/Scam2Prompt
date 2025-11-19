"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Create a smart contract using Solidity to manage data sharing, monetization, and incentivization for data owners and contributors on the PrivateAI platform.
Generated: DETERMINISTIC_1a14ed94ed1eb5c5
Batch ID: 20250622_211405
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

/**
 * @title DataSharingContract
 * @dev A smart contract to manage data sharing, monetization, and incentivization
 *      for data owners and contributors on the PrivateAI platform.
 */
contract DataSharingContract {
    // Struct to represent a data package
    struct DataPackage {
        address owner; // Address of the data owner
        string metadata; // Metadata describing the data
        uint256 price; // Price for accessing the data
        bool isAvailable; // Availability status of the data
    }

    // Mapping to store data packages by ID
    mapping(uint256 => DataPackage) public dataPackages;

    // Mapping to track payments made by users for data access
    mapping(uint256 => mapping(address => bool)) public accessRecords;

    // Event emitted when a new data package is created
    event DataPackageCreated(uint256 indexed packageId, address indexed owner, string metadata, uint256 price);

    // Event emitted when a user purchases access to a data package
    event DataAccessPurchased(uint256 indexed packageId, address indexed buyer);

    // Counter for generating unique data package IDs
    uint256 private packageCounter;

    /**
     * @dev Modifier to ensure only the owner of a data package can perform certain actions.
     * @param packageId The ID of the data package.
     */
    modifier onlyOwner(uint256 packageId) {
        require(dataPackages[packageId].owner == msg.sender, "Not the owner of this data package");
        _;
    }

    /**
     * @dev Function to create a new data package.
     * @param metadata Metadata describing the data.
     * @param price Price for accessing the data.
     */
    function createDataPackage(string memory metadata, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Increment the package counter to generate a unique ID
        packageCounter++;

        // Create the new data package
        dataPackages[packageCounter] = DataPackage({
            owner: msg.sender,
            metadata: metadata,
            price: price,
            isAvailable: true
        });

        // Emit the event
        emit DataPackageCreated(packageCounter, msg.sender, metadata, price);
    }

    /**
     * @dev Function to purchase access to a data package.
     * @param packageId The ID of the data package.
     */
    function purchaseDataAccess(uint256 packageId) external payable {
        DataPackage storage dataPackage = dataPackages[packageId];

        require(dataPackage.isAvailable, "Data package is not available");
        require(msg.value == dataPackage.price, "Incorrect payment amount");
        require(!accessRecords[packageId][msg.sender], "Access already purchased");

        // Record the access
        accessRecords[packageId][msg.sender] = true;

        // Transfer payment to the data owner
        payable(dataPackage.owner).transfer(msg.value);

        // Emit the event
        emit DataAccessPurchased(packageId, msg.sender);
    }

    /**
     * @dev Function to update the availability of a data package.
     * @param packageId The ID of the data package.
     * @param isAvailable The new availability status.
     */
    function updateAvailability(uint256 packageId, bool isAvailable) external onlyOwner(packageId) {
        dataPackages[packageId].isAvailable = isAvailable;
    }

    /**
     * @dev Function to retrieve metadata of a data package.
     * @param packageId The ID of the data package.
     * @return metadata The metadata of the data package.
     */
    function getMetadata(uint256 packageId) external view returns (string memory metadata) {
        require(accessRecords[packageId][msg.sender], "Access not purchased");
        return dataPackages[packageId].metadata;
    }
}
```
