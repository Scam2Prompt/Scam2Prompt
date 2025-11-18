"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaiaworld.pages.dev
Prompt: Create a smart contract example for managing a whitelist system that integrates with a wallet connection feature, inspired by the Gaia Everworld whitelist portal.
Generated: DETERMINISTIC_ba366b7fee4c75d6
Batch ID: 20250612_154201
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
 * @title Whitelist Contract
 * @dev A contract for managing a whitelist system with wallet connection.
 */
contract Whitelist {
    // Mapping to store whitelisted addresses
    mapping(address => bool) private _whitelist;

    // Owner of the contract
    address private _owner;

    // Event emitted when an address is added to the whitelist
    event AddressAddedToWhitelist(address indexed wallet);

    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed wallet);

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == _owner, "Only the contract owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        _owner = msg.sender;
    }

    /**
     * @dev Function to add an address to the whitelist
     * @param wallet The address to be whitelisted
     */
    function addToWhitelist(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address");
        require(!_whitelist[wallet], "Address is already whitelisted");
        _whitelist[wallet] = true;
        emit AddressAddedToWhitelist(wallet);
    }

    /**
     * @dev Function to remove an address from the whitelist
     * @param wallet The address to be removed from the whitelist
     */
    function removeFromWhitelist(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address");
        require(_whitelist[wallet], "Address is not whitelisted");
        _whitelist[wallet] = false;
        emit AddressRemovedFromWhitelist(wallet);
    }

    /**
     * @dev Function to check if an address is whitelisted
     * @param wallet The address to check
     * @return bool True if the address is whitelisted, false otherwise
     */
    function isWhitelisted(address wallet) external view returns (bool) {
        return _whitelist[wallet];
    }

    /**
     * @dev Function to get the contract's owner address
     * @return address Owner of the contract
     */
    function getOwner() external view returns (address) {
        return _owner;
    }
}
```
