"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkweb.web.app
Prompt: What are the best practices for creating a whitelist in a decentralized application?
Generated: DETERMINISTIC_6346667386068f1b
Batch ID: 20250612_160940
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

contract Whitelist {
    // Mapping to keep track of whitelisted addresses
    mapping(address => bool) private whitelistedAddresses;
    
    // Address of the contract owner
    address private owner;

    // Event to signal the addition of an address to the whitelist
    event AddressAdded(address indexed _address);

    // Event to signal the removal of an address from the whitelist
    event AddressRemoved(address indexed _address);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Constructor to set the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    // Function to add an address to the whitelist
    function addAddressToWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Cannot whitelist the zero address");
        require(!whitelistedAddresses[_address], "Address is already whitelisted");
        
        // Add the address to the whitelist
        whitelistedAddresses[_address] = true;

        // Emit an event for the addition
        emit AddressAdded(_address);
    }

    // Function to remove an address from the whitelist
    function removeAddressFromWhitelist(address _address) external onlyOwner {
        require(whitelistedAddresses[_address], "Address is not whitelisted");

        // Remove the address from the whitelist
        delete whitelistedAddresses[_address];

        // Emit an event for the removal
        emit AddressRemoved(_address);
    }

    // Function to check if an address is whitelisted
    function isWhitelisted(address _address) external view returns (bool) {
        return whitelistedAddresses[_address];
    }
}
```
