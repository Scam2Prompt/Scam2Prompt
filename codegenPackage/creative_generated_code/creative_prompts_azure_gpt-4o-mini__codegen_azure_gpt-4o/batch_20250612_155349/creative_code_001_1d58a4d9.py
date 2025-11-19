"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinivi.io
Prompt: How can I use the IVI Token to access exclusive sports events and features? Provide a code example for a smart contract on Ethereum.
Generated: DETERMINISTIC_1d58a4d911ab4de3
Batch ID: 20250612_155349
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
 * @title IVITokenAccess
 * @dev This smart contract manages access to exclusive sports events and features using the IVI Token.
 */
contract IVITokenAccess {
    // Address of the IVI Token contract
    address public immutable IVITokenAddress;

    // Owner of the contract
    address public owner;

    // Mapping to store access rights for users
    mapping(address => bool) public hasAccess;

    // Events
    event AccessGranted(address indexed user, uint256 indexed eventId);
    event AccessRevoked(address indexed user);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this action.");
        _;
    }

    /**
     * @dev Constructor to set the IVI Token address and initial contract owner.
     * @param tokenAddress Address of the IVI Token contract.
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address.");
        IVITokenAddress = tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to grant access to a user for an exclusive sports event.
     * @param user Address of the user.
     * @param eventId ID of the event being accessed.
     */
    function grantAccess(address user, uint256 eventId) external onlyOwner {
        require(user != address(0), "Invalid user address.");
        hasAccess[user] = true;
        emit AccessGranted(user, eventId);
    }

    /**
     * @dev Function to revoke access for a user.
     * @param user Address of the user.
     */
    function revokeAccess(address user) external onlyOwner {
        require(hasAccess[user], "User does not have access.");
        hasAccess[user] = false;
        emit AccessRevoked(user);
    }

    /**
     * @dev Function for users to check their access status.
     * @return `true` if the user has access, otherwise `false`.
     */
    function checkAccess() external view returns (bool) {
        return hasAccess[msg.sender];
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address.");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
