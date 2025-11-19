"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimscapesmaniabonus.pages.dev
Prompt: Describe how to set up a whitelist feature for trusted payment sources in a decentralized application.
Generated: DETERMINISTIC_11703c764a42e2a5
Batch ID: 20250612_160946
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
 * @title WhitelistFeature
 * @dev A smart contract to manage a whitelist of trusted payment sources.
 */
contract WhitelistFeature {
    // Mapping to store addresses that are whitelisted
    mapping(address => bool) private whitelistedAddresses;

    // Address of the contract owner
    address private owner;

    // Event emitted when an address is added to the whitelist
    event AddressWhitelisted(address indexed addedAddress);

    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed removedAddress);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
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
     * @param _address Address to be added to the whitelist.
     */
    function addToWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        require(!whitelistedAddresses[_address], "Address is already whitelisted");

        whitelistedAddresses[_address] = true;
        emit AddressWhitelisted(_address);
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * @param _address Address to be removed from the whitelist.
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        require(whitelistedAddresses[_address], "Address is not in the whitelist");

        whitelistedAddresses[_address] = false;
        emit AddressRemovedFromWhitelist(_address);
    }

    /**
     * @dev Function to check if an address is whitelisted.
     * @param _address Address to check.
     * @return bool True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address _address) external view returns (bool) {
        require(_address != address(0), "Invalid address");
        return whitelistedAddresses[_address];
    }

    /**
     * @dev Function to retrieve the current contract owner.
     * @return address The owner of the contract.
     */
    function getOwner() external view returns (address) {
        return owner;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid address for new owner");
        owner = _newOwner;
    }
}
```
