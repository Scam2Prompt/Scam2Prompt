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

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary OpenZeppelin contracts for security and utility
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract Whitelist is Ownable {
    using Counters for Counters.Counter;

    // Counter for keeping track of the number of whitelisted addresses
    Counters.Counter private _whitelistedCount;

    // Mapping to store whitelisted addresses
    mapping(address => bool) private _whitelistedAddresses;

    // Event emitted when an address is whitelisted
    event AddressWhitelisted(address indexed account);

    // Event emitted when an address is removed from the whitelist
    event AddressRemoved(address indexed account);

    /**
     * @dev Function to whitelist an address.
     * Can only be called by the contract owner.
     * @param account The address to be whitelisted.
     */
    function addAddressToWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address"); // Ensure address is not zero
        require(!_whitelistedAddresses[account], "Address already whitelisted"); // Prevent duplicate whitelisting

        _whitelistedAddresses[account] = true; // Add address to whitelist
        _whitelistedCount.increment(); // Increment the whitelisted count
        emit AddressWhitelisted(account); // Emit the event
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * Can only be called by the contract owner.
     * @param account The address to be removed from the whitelist.
     */
    function removeAddressFromWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address"); // Ensure address is not zero
        require(_whitelistedAddresses[account], "Address not whitelisted"); // Ensure address is in the whitelist

        _whitelistedAddresses[account] = false; // Remove address from whitelist
        _whitelistedCount.decrement(); // Decrement the whitelisted count
        emit AddressRemoved(account); // Emit the event
    }

    /**
     * @dev Function to check if an address is whitelisted.
     * @param account The address to check.
     * @return bool indicating whether the address is whitelisted or not.
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelistedAddresses[account]; // Return the whitelist status of the address
    }

    /**
     * @dev Function to get the number of whitelisted addresses.
     * @return uint256 representing the count of whitelisted addresses.
     */
    function getWhitelistedCount() external view returns (uint256) {
        return _whitelistedCount.current(); // Return the current count of whitelisted addresses
    }
}
```
