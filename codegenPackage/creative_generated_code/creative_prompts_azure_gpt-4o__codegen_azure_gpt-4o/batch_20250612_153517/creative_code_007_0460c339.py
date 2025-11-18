"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adidasverse.pages.dev
Prompt: Create a Solidity contract for whitelisting addresses for future NFT mints, similar to the whitelist system described for Adidas Originals collaborations.
Generated: DETERMINISTIC_0460c3392d171c0b
Batch ID: 20250612_153517
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
 * @title Whitelist Contract for NFT Mints
 * @dev This contract manages a whitelist system for NFT mints.
 */
contract NFTWhitelist {
    // Mapping to store whitelisted addresses
    mapping(address => bool) private whitelist;

    // Address of the contract owner
    address private owner;

    // Event emitted when an address is added to the whitelist
    event AddressWhitelisted(address indexed account);

    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed account);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Adds an address to the whitelist.
     * @param _account Address to be added to the whitelist.
     */
    function addToWhitelist(address _account) external onlyOwner {
        require(_account != address(0), "Cannot whitelist zero address");
        require(!whitelist[_account], "Address is already whitelisted");

        whitelist[_account] = true;
        emit AddressWhitelisted(_account);
    }

    /**
     * @dev Removes an address from the whitelist.
     * @param _account Address to be removed from the whitelist.
     */
    function removeFromWhitelist(address _account) external onlyOwner {
        require(_account != address(0), "Cannot remove zero address");
        require(whitelist[_account], "Address is not whitelisted");

        whitelist[_account] = false;
        emit AddressRemovedFromWhitelist(_account);
    }

    /**
     * @dev Checks if an address is whitelisted.
     * @param _account Address to check.
     * @return bool True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address _account) external view returns (bool) {
        return whitelist[_account];
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be zero address");
        owner = _newOwner;
    }

    /**
     * @dev Returns the current owner of the contract.
     * @return address The address of the contract owner.
     */
    function getOwner() external view returns (address) {
        return owner;
    }
}
```
