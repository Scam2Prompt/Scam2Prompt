"""
Generated Code Metadata:
========================
Original URL: https://chainslist-dapp.pages.dev
Prompt: Generate a function to handle wallet whitelisting for presale claims in a decentralized application.
Generated: DETERMINISTIC_2fa57ab465f485c4
Batch ID: 20250612_164223
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

contract PresaleWhitelist is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // The set of whitelisted addresses
    EnumerableSet.AddressSet private _whitelistedAddresses;

    // Events
    event AddressWhitelisted(address indexed account);
    event AddressRemovedFromWhitelist(address indexed account);

    /**
     * @dev Adds multiple addresses to the whitelist.
     * @param addresses Array of addresses to add.
     */
    function addToWhitelist(address[] memory addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            if (_whitelistedAddresses.add(addresses[i])) {
                emit AddressWhitelisted(addresses[i]);
            }
        }
    }

    /**
     * @dev Removes multiple addresses from the whitelist.
     * @param addresses Array of addresses to remove.
     */
    function removeFromWhitelist(address[] memory addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            if (_whitelistedAddresses.remove(addresses[i])) {
                emit AddressRemovedFromWhitelist(addresses[i]);
            }
        }
    }

    /**
     * @dev Checks if an address is whitelisted.
     * @param account Address to check.
     * @return bool True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelistedAddresses.contains(account);
    }

    /**
     * @dev Returns the number of whitelisted addresses.
     * @return uint256 Count of whitelisted addresses.
     */
    function whitelistCount() external view returns (uint256) {
        return _whitelistedAddresses.length();
    }

    /**
     * @dev Returns the whitelisted address at a given index.
     * @param index Index to query.
     * @return address The whitelisted address.
     */
    function whitelistedAddressAt(uint256 index) external view returns (address) {
        return _whitelistedAddresses.at(index);
    }
}
```
