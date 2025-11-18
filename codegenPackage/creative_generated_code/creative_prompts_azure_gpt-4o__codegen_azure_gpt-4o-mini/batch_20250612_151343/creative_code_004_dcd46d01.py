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

contract PepeToken {
    // Address of the Based $PEPE token contract
    address public constant PEPE_TOKEN_ADDRESS = 0x52b492a33E447Cdb854c7FC19F1e57E8BfA1777D;

    // Mapping to keep track of blacklisted addresses
    mapping(address => bool) private blacklist;

    // Event emitted when an address is added to or removed from the blacklist
    event BlacklistUpdated(address indexed account, bool isBlacklisted);

    // Modifier to check if the caller is the contract owner
    modifier onlyOwner() {
        // Assuming the owner is the deployer of the contract
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract and set the owner
    address private owner;

    constructor() {
        owner = msg.sender; // Set the deployer as the contract owner
    }

    /**
     * @dev Checks if a wallet address is blacklisted from interacting with the Based $PEPE token contract.
     * @param account The address to check.
     * @return bool True if the address is blacklisted, false otherwise.
     */
    function isBlacklisted(address account) external view returns (bool) {
        require(account != address(0), "Invalid address: zero address");
        return blacklist[account];
    }

    /**
     * @dev Adds an address to the blacklist.
     * Only callable by the contract owner.
     * @param account The address to blacklist.
     */
    function addToBlacklist(address account) external onlyOwner {
        require(account != address(0), "Invalid address: zero address");
        require(!blacklist[account], "Address is already blacklisted");

        blacklist[account] = true;
        emit BlacklistUpdated(account, true);
    }

    /**
     * @dev Removes an address from the blacklist.
     * Only callable by the contract owner.
     * @param account The address to remove from the blacklist.
     */
    function removeFromBlacklist(address account) external onlyOwner {
        require(account != address(0), "Invalid address: zero address");
        require(blacklist[account], "Address is not blacklisted");

        blacklist[account] = false;
        emit BlacklistUpdated(account, false);
    }
}
```
