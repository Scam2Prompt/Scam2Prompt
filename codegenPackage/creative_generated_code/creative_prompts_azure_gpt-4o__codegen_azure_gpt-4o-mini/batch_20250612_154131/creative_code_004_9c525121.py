"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fastyield.app
Prompt: Write a smart contract in Solidity that supports wallet-based access control for a dApp like FastYield.
Generated: DETERMINISTIC_9c52512189da43a1
Batch ID: 20250612_154131
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

/// @title FastYield Access Control Smart Contract
/// @notice This contract manages wallet-based access control for the FastYield dApp
/// @dev Only whitelisted addresses can interact with certain functions
contract FastYieldAccessControl {
    // State variable to store the owner of the contract
    address public owner;

    // Mapping to keep track of whitelisted addresses
    mapping(address => bool) private whitelistedAddresses;

    // Event emitted when an address is added to the whitelist
    event AddressAdded(address indexed addr);
    
    // Event emitted when an address is removed from the whitelist
    event AddressRemoved(address indexed addr);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this action");
        _;
    }

    // Modifier to check if the caller is whitelisted
    modifier onlyWhitelisted() {
        require(isWhitelisted(msg.sender), "Caller is not whitelisted");
        _;
    }

    /// @dev Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Add an address to the whitelist
    /// @param addr The address to be added
    function addAddressToWhitelist(address addr) external onlyOwner {
        require(addr != address(0), "Cannot whitelist the zero address");
        require(!isWhitelisted(addr), "Address is already whitelisted");

        whitelistedAddresses[addr] = true;
        emit AddressAdded(addr);
    }

    /// @notice Remove an address from the whitelist
    /// @param addr The address to be removed
    function removeAddressFromWhitelist(address addr) external onlyOwner {
        require(isWhitelisted(addr), "Address is not whitelisted");

        delete whitelistedAddresses[addr];
        emit AddressRemoved(addr);
    }

    /// @notice Check if an address is whitelisted
    /// @param addr The address to check
    /// @return bool True if the address is whitelisted, false otherwise
    function isWhitelisted(address addr) public view returns (bool) {
        return whitelistedAddresses[addr];
    }

    /// @notice Example function that can only be called by whitelisted addresses
    function accessRestrictedFunction() external onlyWhitelisted {
        // Function logic here
    }
}
```
