"""
Generated Code Metadata:
========================
Original URL: https://cloudsignsonchain.pages.dev
Prompt: Create code to whitelist a wallet for NFT minting as described in the KYC/Whitelist section of the CloudSignsOnChain documentation.
Generated: DETERMINISTIC_de039d2e66407c37
Batch ID: 20250612_151003
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

/**
 * @title Whitelist
 * @dev Manages a whitelist of addresses for NFT minting
 */
contract Whitelist is Ownable {
    mapping(address => bool) private _whitelistedAddresses;

    event AddressWhitelisted(address indexed account);
    event AddressRemovedFromWhitelist(address indexed account);

    /**
     * @dev Add an address to the whitelist
     * @param account The address to whitelist
     */
    function addToWhitelist(address account) external onlyOwner {
        require(account != address(0), "Whitelist: zero address");
        require(!_whitelistedAddresses[account], "Whitelist: already whitelisted");

        _whitelistedAddresses[account] = true;
        emit AddressWhitelisted(account);
    }

    /**
     * @dev Remove an address from the whitelist
     * @param account The address to remove
     */
    function removeFromWhitelist(address account) external onlyOwner {
        require(account != address(0), "Whitelist: zero address");
        require(_whitelistedAddresses[account], "Whitelist: not whitelisted");

        _whitelistedAddresses[account] = false;
        emit AddressRemovedFromWhitelist(account);
    }

    /**
     * @dev Check if an address is whitelisted
     * @param account The address to check
     * @return bool Whether the address is whitelisted
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelistedAddresses[account];
    }

    /**
     * @dev Batch add addresses to the whitelist
     * @param accounts Array of addresses to whitelist
     */
    function batchAddToWhitelist(address[] calldata accounts) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            address account = accounts[i];
            if (account != address(0) && !_whitelistedAddresses[account]) {
                _whitelistedAddresses[account] = true;
                emit AddressWhitelisted(account);
            }
        }
    }
}
```
