"""
Generated Code Metadata:
========================
Original URL: https://arbitriumltd.com
Prompt: Generate a Solidity smart contract template for a business-focused blockchain solution, ensuring it adheres to the quality standards described by Arbitrium Ltd.
Generated: DETERMINISTIC_698d4cad70eb685a
Batch ID: 20250612_150342
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
 * @title BusinessContractTemplate
 * @dev A template for business-focused smart contracts adhering to Arbitrium Ltd quality standards
 * @notice This contract includes common business functionalities with proper access control,
 *         event logging, and error handling mechanisms.
 */
contract BusinessContractTemplate {
    // Contract owner
    address private _owner;

    // Mapping to track authorized administrators
    mapping(address => bool) private _administrators;

    // Business data structure
    struct BusinessData {
        uint256 id;
        string name;
        uint256 value;
        bool isActive;
    }

    // Business data storage
    mapping(uint256 => BusinessData) private _businessData;

    // Events for logging contract activities
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event AdministratorAdded(address indexed admin);
    event AdministratorRemoved(address indexed admin);
    event BusinessDataAdded(uint256 indexed id, string name, uint256 value);
    event BusinessDataUpdated(uint256 indexed id, string name, uint256 value);
    event BusinessDataStatusChanged(uint256 indexed id, bool isActive);

    // Custom errors for better error handling
    error Unauthorized();
    error InvalidAddress();
    error InvalidValue();
    error BusinessDataNotFound(uint256 id);
    error BusinessDataAlreadyExists(uint256 id);

    /**
     * @dev Modifier to check if the caller is the owner
     */
    modifier onlyOwner() {
        if (msg.sender != _owner) revert Unauthorized();
        _;
    }

    /**
     * @dev Modifier to check if the caller is an administrator
     */
    modifier onlyAdmin() {
        if (!_administrators[msg.sender] && msg.sender != _owner) revert Unauthorized();
        _;
    }

    /**
     * @dev Contract constructor sets the initial owner
     */
    constructor() {
        _owner = msg.sender;
        emit OwnershipTransferred(address(0), _owner);
    }

    /**
     * @dev Returns the address of the current owner
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @dev Transfers ownership of the contract to a new account
     * @param newOwner The address to transfer ownership to
     */
    function transferOwnership(address newOwner) public onlyOwner {
        if (newOwner == address(0)) revert InvalidAddress();
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }

    /**
     * @dev Adds an administrator
     * @param admin The address to add as administrator
     */
    function addAdministrator(address admin) public onlyOwner {
        if (admin == address(0)) revert InvalidAddress();
        _administrators[admin] = true;
        emit AdministratorAdded(admin);
    }

    /**
     * @dev Removes an administrator
     * @param admin The address to remove from administrators
     */
    function removeAdministrator(address admin) public onlyOwner {
        if (admin == address(0)) revert InvalidAddress();
        _administrators[admin] = false;
        emit AdministratorRemoved(admin);
    }

    /**
     * @dev Checks if an address is an administrator
     * @param account The address to check
     */
    function isAdministrator(address account) public view returns (bool) {
        return _administrators[account] || account == _owner;
    }

    /**
     * @dev Adds new business data
     * @param id The unique identifier for the business data
     * @param name The name of the business data
     * @param value The value associated with the business data
     */
    function addBusinessData(uint256 id, string memory name, uint256 value) public onlyAdmin {
        if (_businessData[id].id != 0) revert BusinessDataAlreadyExists(id);
        if (value == 0) revert InvalidValue();
        
        _businessData[id] = BusinessData(id, name, value, true);
        emit BusinessDataAdded(id, name, value);
    }

    /**
     * @dev Updates existing business data
     * @param id The unique identifier for the business data
     * @param name The new name of the business data
     * @param value The new value associated with the business data
     */
    function updateBusinessData(uint256 id, string memory name, uint256 value) public onlyAdmin {
        if (_businessData[id].id == 0) revert BusinessDataNotFound(id);
        if (value == 0) revert InvalidValue();
        
        _businessData[id].name = name;
        _businessData[id].value = value;
        emit BusinessDataUpdated(id, name, value);
    }

    /**
     * @dev Changes the active status of business data
     * @param id The unique identifier for the business data
     * @param isActive The new active status
     */
    function setBusinessDataStatus(uint256 id, bool isActive) public onlyAdmin {
        if (_businessData[id].id == 0) revert BusinessDataNotFound(id);
        
        _businessData[id].isActive = isActive;
        emit BusinessDataStatusChanged(id, isActive);
    }

    /**
     * @dev Retrieves business data by ID
     * @param id The unique identifier for the business data
     */
    function getBusinessData(uint256 id) public view returns (BusinessData memory) {
        if (_businessData[id].id == 0) revert BusinessDataNotFound(id);
        return _businessData[id];
    }

    /**
     * @dev Emergency function to withdraw any accidentally sent Ether
     */
    function withdraw() external onlyOwner {
        payable(_owner).transfer(address(this).balance);
    }

    /**
     * @dev Prevents direct sending of Ether to the contract
     */
    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```
