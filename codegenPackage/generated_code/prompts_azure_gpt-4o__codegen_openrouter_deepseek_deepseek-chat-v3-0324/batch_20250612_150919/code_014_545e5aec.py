"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Generate a Solidity smart contract for a real estate ledger system on Mazze, leveraging its transparent and secure ledger for property transfers.
Generated: DETERMINISTIC_545e5aecb161b6df
Batch ID: 20250612_150919
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
 * @title RealEstateLedger
 * @dev A smart contract for managing property ownership transfers on Mazze
 */
contract RealEstateLedger {
    // Struct to represent a property
    struct Property {
        uint256 id;
        address owner;
        string location;
        uint256 area;
        uint256 price;
        bool isForSale;
    }

    // Mapping from property ID to Property
    mapping(uint256 => Property) public properties;

    // Mapping to track authorized transfers (from owner to new owner)
    mapping(address => mapping(address => uint256)) public transferApprovals;

    // Event emitted when a property is registered
    event PropertyRegistered(
        uint256 indexed id,
        address indexed owner,
        string location,
        uint256 area,
        uint256 price
    );

    // Event emitted when a property is listed for sale
    event PropertyListedForSale(uint256 indexed id, uint256 price);

    // Event emitted when a property is delisted from sale
    event PropertyDelistedFromSale(uint256 indexed id);

    // Event emitted when a property transfer is initiated
    event TransferInitiated(
        uint256 indexed id,
        address indexed from,
        address indexed to
    );

    // Event emitted when a property is transferred
    event PropertyTransferred(
        uint256 indexed id,
        address indexed from,
        address indexed to,
        uint256 price
    );

    // Modifier to check if the caller is the property owner
    modifier onlyOwner(uint256 _propertyId) {
        require(
            properties[_propertyId].owner == msg.sender,
            "Only property owner can perform this action"
        );
        _;
    }

    // Modifier to check if the property exists
    modifier propertyExists(uint256 _propertyId) {
        require(
            properties[_propertyId].id != 0,
            "Property does not exist"
        );
        _;
    }

    /**
     * @dev Register a new property
     * @param _propertyId The unique ID of the property
     * @param _location The location/address of the property
     * @param _area The area of the property in square meters
     * @param _price The price of the property in wei
     */
    function registerProperty(
        uint256 _propertyId,
        string memory _location,
        uint256 _area,
        uint256 _price
    ) external {
        require(
            properties[_propertyId].id == 0,
            "Property already registered"
        );
        require(_area > 0, "Area must be greater than zero");
        require(_price > 0, "Price must be greater than zero");

        properties[_propertyId] = Property({
            id: _propertyId,
            owner: msg.sender,
            location: _location,
            area: _area,
            price: _price,
            isForSale: false
        });

        emit PropertyRegistered(_propertyId, msg.sender, _location, _area, _price);
    }

    /**
     * @dev List a property for sale
     * @param _propertyId The ID of the property to list
     * @param _price The asking price in wei
     */
    function listForSale(uint256 _propertyId, uint256 _price)
        external
        propertyExists(_propertyId)
        onlyOwner(_propertyId)
    {
        require(_price > 0, "Price must be greater than zero");
        
        Property storage property = properties[_propertyId];
        property.isForSale = true;
        property.price = _price;

        emit PropertyListedForSale(_propertyId, _price);
    }

    /**
     * @dev Delist a property from sale
     * @param _propertyId The ID of the property to delist
     */
    function delistFromSale(uint256 _propertyId)
        external
        propertyExists(_propertyId)
        onlyOwner(_propertyId)
    {
        Property storage property = properties[_propertyId];
        property.isForSale = false;

        emit PropertyDelistedFromSale(_propertyId);
    }

    /**
     * @dev Initiate a property transfer
     * @param _propertyId The ID of the property to transfer
     * @param _newOwner The address of the new owner
     */
    function initiateTransfer(uint256 _propertyId, address _newOwner)
        external
        propertyExists(_propertyId)
        onlyOwner(_propertyId)
    {
        require(_newOwner != address(0), "Invalid new owner address");
        require(_newOwner != msg.sender, "Cannot transfer to yourself");

        transferApprovals[msg.sender][_newOwner] = _propertyId;

        emit TransferInitiated(_propertyId, msg.sender, _newOwner);
    }

    /**
     * @dev Complete a property transfer
     * @param _propertyId The ID of the property to transfer
     * @param _currentOwner The address of the current owner
     */
    function completeTransfer(uint256 _propertyId, address _currentOwner)
        external
        payable
        propertyExists(_propertyId)
    {
        require(
            transferApprovals[_currentOwner][msg.sender] == _propertyId,
            "Transfer not approved"
        );
        
        Property storage property = properties[_propertyId];
        require(property.isForSale, "Property is not for sale");
        require(msg.value >= property.price, "Insufficient payment");

        // Transfer ownership
        address previousOwner = property.owner;
        property.owner = msg.sender;
        property.isForSale = false;

        // Clear the approval
        delete transferApprovals[_currentOwner][msg.sender];

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit PropertyTransferred(_propertyId, previousOwner, msg.sender, msg.value);
    }

    /**
     * @dev Get property details
     * @param _propertyId The ID of the property
     * @return Property details
     */
    function getProperty(uint256 _propertyId)
        external
        view
        propertyExists(_propertyId)
        returns (
            uint256,
            address,
            string memory,
            uint256,
            uint256,
            bool
        )
    {
        Property memory property = properties[_propertyId];
        return (
            property.id,
            property.owner,
            property.location,
            property.area,
            property.price,
            property.isForSale
        );
    }
}
```
