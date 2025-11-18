"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olivedao.finance
Prompt: Generate a smart contract that checks access requirements for a DeFi app, inspired by the OliveDAO Finance platform.
Generated: DETERMINISTIC_3f0684f591d94a16
Batch ID: 20250612_145117
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
 * @title AccessControl for DeFi Application
 * @dev Smart contract to manage access requirements for a decentralized finance (DeFi) platform.
 */
contract AccessControl {
    // Owner of the contract
    address public owner;

    // Mapping to store addresses with access permission
    mapping(address => bool) private accessList;

    // Event emitted when access is granted
    event AccessGranted(address indexed account);

    // Event emitted when access is revoked
    event AccessRevoked(address indexed account);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "AccessControl: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to grant access to an address.
     * @param account Address to be granted access.
     */
    function grantAccess(address account) external onlyOwner {
        require(account != address(0), "AccessControl: Invalid address");
        require(!accessList[account], "AccessControl: Address already has access");

        accessList[account] = true;
        emit AccessGranted(account);
    }

    /**
     * @dev Function to revoke access from an address.
     * @param account Address to have access revoked.
     */
    function revokeAccess(address account) external onlyOwner {
        require(account != address(0), "AccessControl: Invalid address");
        require(accessList[account], "AccessControl: Address does not have access");

        accessList[account] = false;
        emit AccessRevoked(account);
    }

    /**
     * @dev Function to check if an address has access.
     * @param account Address to be checked.
     * @return bool Returns true if the address has access, false otherwise.
     */
    function hasAccess(address account) external view returns (bool) {
        require(account != address(0), "AccessControl: Invalid address");
        return accessList[account];
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "AccessControl: New owner cannot be zero address");
        owner = newOwner;
    }
}
```
