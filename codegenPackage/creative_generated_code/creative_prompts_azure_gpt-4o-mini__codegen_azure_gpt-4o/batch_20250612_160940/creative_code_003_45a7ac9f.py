"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkweb.web.app
Prompt: Provide code examples for integrating a whitelist system in a blockchain-based project.
Generated: DETERMINISTIC_45a7ac9f486ae5f2
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a code example in Solidity for a simple whitelist system in a blockchain-based project. This code adheres to your requirements:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Whitelist Contract
 * @dev A contract for managing a whitelist of addresses in a blockchain-based project.
 */
contract Whitelist {
    // Mapping to store whitelisted addresses. True if address is whitelisted, false otherwise.
    mapping(address => bool) private whitelistedAddresses;

    // Address of the contract owner
    address private owner;

    // Event emitted when an address is added to the whitelist
    event AddressAddedToWhitelist(address indexed addedAddress);

    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed removedAddress);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add an address to the whitelist.
     * @param _address The address to be added to the whitelist.
     */
    function addToWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address"); // Prevent adding the zero address
        require(!whitelistedAddresses[_address], "Address already whitelisted"); // Prevent duplicates

        // Add the address to the whitelist
        whitelistedAddresses[_address] = true;

        // Emit event
        emit AddressAddedToWhitelist(_address);
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * @param _address The address to be removed from the whitelist.
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address"); // Prevent removing the zero address
        require(whitelistedAddresses[_address], "Address not in whitelist"); // Prevent removing non-whitelisted addresses

        // Remove the address from the whitelist
        whitelistedAddresses[_address] = false;

        // Emit event
        emit AddressRemovedFromWhitelist(_address);
    }

    /**
     * @dev Function to check if an address is whitelisted.
     * @param _address The address to check.
     * @return bool True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address _address) external view returns (bool) {
        return whitelistedAddresses[_address];
    }

    /**
     * @dev Function to retrieve the contract owner.
     * @return address The address of the contract owner.
     */
    function getOwner() external view returns (address) {
        return owner;
    }
}
```

This code contains all requested features and adheres to best practices for Solidity development, including proper error handling, event emission, and restriction of access using modifiers.
