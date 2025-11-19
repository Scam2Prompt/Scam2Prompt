"""
Generated Code Metadata:
========================
Original URL: https://bafybeibawo7r32uj46hju347auzbhmfq4h6f35azlyhnfqjz4d5whkaq5q.ipfs.dweb.link
Prompt: "Generate a smart contract code snippet in Solidity for whitelisting validators and services on a platform similar to Kelp DAO."
Generated: DETERMINISTIC_177772d49aa27023
Batch ID: 20250622_205751
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
 * @title WhitelistManager
 * @dev A smart contract for managing whitelisted validators and services on a platform.
 */
contract WhitelistManager {
    // Owner of the contract
    address public owner;

    // Mapping to store whitelisted validators
    mapping(address => bool) public validators;

    // Mapping to store whitelisted services
    mapping(address => bool) public services;

    // Events for logging actions
    event ValidatorAdded(address indexed validator);
    event ValidatorRemoved(address indexed validator);
    event ServiceAdded(address indexed service);
    event ServiceRemoved(address indexed service);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a validator to the whitelist.
     * @param _validator Address of the validator to be added.
     */
    function addValidator(address _validator) external onlyOwner {
        require(_validator != address(0), "Invalid validator address");
        require(!validators[_validator], "Validator already whitelisted");
        validators[_validator] = true;
        emit ValidatorAdded(_validator);
    }

    /**
     * @dev Remove a validator from the whitelist.
     * @param _validator Address of the validator to be removed.
     */
    function removeValidator(address _validator) external onlyOwner {
        require(validators[_validator], "Validator not whitelisted");
        validators[_validator] = false;
        emit ValidatorRemoved(_validator);
    }

    /**
     * @dev Add a service to the whitelist.
     * @param _service Address of the service to be added.
     */
    function addService(address _service) external onlyOwner {
        require(_service != address(0), "Invalid service address");
        require(!services[_service], "Service already whitelisted");
        services[_service] = true;
        emit ServiceAdded(_service);
    }

    /**
     * @dev Remove a service from the whitelist.
     * @param _service Address of the service to be removed.
     */
    function removeService(address _service) external onlyOwner {
        require(services[_service], "Service not whitelisted");
        services[_service] = false;
        emit ServiceRemoved(_service);
    }

    /**
     * @dev Check if an address is a whitelisted validator.
     * @param _validator Address to check.
     * @return bool True if the address is a whitelisted validator, false otherwise.
     */
    function isValidator(address _validator) external view returns (bool) {
        return validators[_validator];
    }

    /**
     * @dev Check if an address is a whitelisted service.
     * @param _service Address to check.
     * @return bool True if the address is a whitelisted service, false otherwise.
     */
    function isService(address _service) external view returns (bool) {
        return services[_service];
    }
}
```
