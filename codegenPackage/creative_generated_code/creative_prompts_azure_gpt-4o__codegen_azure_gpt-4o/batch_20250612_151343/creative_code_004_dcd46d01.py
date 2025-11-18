"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedonpepe.pages.dev
Prompt: Create a Solidity function that checks if a wallet address is blacklisted from interacting with the Based $PEPE token contract (`0x52b492a33E447Cdb854c7FC19F1e57E8BfA1777D`).
Generated: DETERMINISTIC_dcd46d0180de923c
Batch ID: 20250612_151343
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
 * @title BlacklistChecker
 * @notice A contract to check if a wallet address is blacklisted from interacting with the Based $PEPE token.
 */
contract BlacklistChecker {
    // Address of the Based $PEPE token contract
    address public constant BASED_PEPE_TOKEN = 0x52b492a33E447Cdb854c7FC19F1e57E8BfA1777D;

    // Mapping to track blacklisted addresses
    mapping(address => bool) private blacklist;

    /**
     * @notice Adds an address to the blacklist.
     * @param _address The wallet address to blacklist.
     */
    function addToBlacklist(address _address) external {
        require(_address != address(0), "Invalid address");
        blacklist[_address] = true;
    }

    /**
     * @notice Removes an address from the blacklist.
     * @param _address The wallet address to remove from the blacklist.
     */
    function removeFromBlacklist(address _address) external {
        require(_address != address(0), "Invalid address");
        blacklist[_address] = false;
    }

    /**
     * @notice Checks if a wallet address is blacklisted.
     * @param _wallet The wallet address to check.
     * @return True if the wallet address is blacklisted, otherwise false.
     */
    function isBlacklisted(address _wallet) external view returns (bool) {
        require(_wallet != address(0), "Invalid wallet address");
        return blacklist[_wallet];
    }
}
```
