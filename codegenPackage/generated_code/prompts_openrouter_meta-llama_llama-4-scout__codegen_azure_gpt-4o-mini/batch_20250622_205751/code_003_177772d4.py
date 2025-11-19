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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title WhitelistManager
 * @dev This contract manages the whitelisting of validators and services.
 */
contract WhitelistManager is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Set to store whitelisted addresses
    EnumerableSet.AddressSet private whitelistedAddresses;

    // Event emitted when an address is whitelisted
    event AddressWhitelisted(address indexed addr);

    // Event emitted when an address is removed from the whitelist
    event AddressRemoved(address indexed addr);

    /**
     * @dev Modifier to check if an address is whitelisted.
     * @param addr The address to check.
     */
    modifier onlyWhitelisted(address addr) {
        require(isWhitelisted(addr), "Address is not whitelisted");
        _;
    }

    /**
     * @dev Adds an address to the whitelist.
     * @param addr The address to whitelist.
     */
    function whitelistAddress(address addr) external onlyOwner {
        require(addr != address(0), "Cannot whitelist the zero address");
        require(!whitelistedAddresses.contains(addr), "Address is already whitelisted");

        whitelistedAddresses.add(addr);
        emit AddressWhitelisted(addr);
    }

    /**
     * @dev Removes an address from the whitelist.
     * @param addr The address to remove from the whitelist.
     */
    function removeWhitelistedAddress(address addr) external onlyOwner {
        require(whitelistedAddresses.contains(addr), "Address is not whitelisted");

        whitelistedAddresses.remove(addr);
        emit AddressRemoved(addr);
    }

    /**
     * @dev Checks if an address is whitelisted.
     * @param addr The address to check.
     * @return bool True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address addr) public view returns (bool) {
        return whitelistedAddresses.contains(addr);
    }

    /**
     * @dev Returns the number of whitelisted addresses.
     * @return uint256 The count of whitelisted addresses.
     */
    function getWhitelistedCount() external view returns (uint256) {
        return whitelistedAddresses.length();
    }

    /**
     * @dev Returns the address at a specific index in the whitelist.
     * @param index The index of the address to retrieve.
     * @return address The address at the specified index.
     */
    function getWhitelistedAddress(uint256 index) external view returns (address) {
        require(index < whitelistedAddresses.length(), "Index out of bounds");
        return whitelistedAddresses.at(index);
    }
}
```
