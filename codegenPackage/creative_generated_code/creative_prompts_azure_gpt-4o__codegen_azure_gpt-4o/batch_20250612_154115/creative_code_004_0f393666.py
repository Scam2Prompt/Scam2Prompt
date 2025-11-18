"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starksport.finance
Prompt: Write a smart contract in Solidity that interacts with a connected wallet to enable access to app features, inspired by starksport.finance's functionality.
Generated: DETERMINISTIC_0f393666f8df5c83
Batch ID: 20250612_154115
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
 * @title AccessControl
 * @dev A smart contract to interact with a connected wallet and grant access to app features.
 * Inspired by starksport.finance functionality.
 */

contract AccessControl {
    // Owner of the contract
    address public owner;

    // Mapping to track wallet access permissions
    mapping(address => bool) public hasAccess;

    // Event emitted when access is granted
    event AccessGranted(address indexed wallet);

    // Event emitted when access is revoked
    event AccessRevoked(address indexed wallet);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "AccessControl: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to grant access to a wallet.
     * @param wallet Address of the wallet to grant access to.
     */
    function grantAccess(address wallet) external onlyOwner {
        require(wallet != address(0), "AccessControl: Invalid wallet address");
        require(!hasAccess[wallet], "AccessControl: Wallet already has access");

        hasAccess[wallet] = true;
        emit AccessGranted(wallet);
    }

    /**
     * @dev Function to revoke access from a wallet.
     * @param wallet Address of the wallet to revoke access from.
     */
    function revokeAccess(address wallet) external onlyOwner {
        require(wallet != address(0), "AccessControl: Invalid wallet address");
        require(hasAccess[wallet], "AccessControl: Wallet does not have access");

        hasAccess[wallet] = false;
        emit AccessRevoked(wallet);
    }

    /**
     * @dev Function to check if a wallet has access.
     * @param wallet Address of the wallet to check.
     * @return True if the wallet has access, false otherwise.
     */
    function checkAccess(address wallet) external view returns (bool) {
        require(wallet != address(0), "AccessControl: Invalid wallet address");
        return hasAccess[wallet];
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "AccessControl: Invalid owner address");
        owner = newOwner;
    }
}
```
