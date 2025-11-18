"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddy-tate.pages.dev
Prompt: Provide an example of a smart contract that could be used to manage a waitlist for a blockchain-based platform like "The Real World."
Generated: DETERMINISTIC_7ce9e944606153f8
Batch ID: 20250612_150644
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
 * @title WaitlistManager
 * @dev A smart contract to manage a waitlist for a blockchain-based platform.
 */
contract WaitlistManager {
    // Events
    event UserAddedToWaitlist(address indexed user);
    event UserRemovedFromWaitlist(address indexed user);

    // State Variables
    address public owner; // Contract owner
    mapping(address => bool) public waitlist; // Mapping to track users on the waitlist
    uint256 public waitlistCount; // Number of users currently on the waitlist

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Modifier to ensure the user is not already on the waitlist.
     */
    modifier notOnWaitlist(address user) {
        require(!waitlist[user], "User is already on the waitlist");
        _;
    }

    /**
     * @dev Modifier to ensure the user is on the waitlist.
     */
    modifier onWaitlist(address user) {
        require(waitlist[user], "User is not on the waitlist");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add a user to the waitlist.
     * @param user The address of the user to add to the waitlist.
     */
    function addToWaitlist(address user) external onlyOwner notOnWaitlist(user) {
        waitlist[user] = true; // Mark the user as on the waitlist
        waitlistCount += 1; // Increment the waitlist count
        emit UserAddedToWaitlist(user); // Emit an event
    }

    /**
     * @dev Function to remove a user from the waitlist.
     * @param user The address of the user to remove from the waitlist.
     */
    function removeFromWaitlist(address user) external onlyOwner onWaitlist(user) {
        waitlist[user] = false; // Mark the user as not on the waitlist
        waitlistCount -= 1; // Decrement the waitlist count
        emit UserRemovedFromWaitlist(user); // Emit an event
    }

    /**
     * @dev Function to check if a user is on the waitlist.
     * @param user The address of the user to check.
     * @return bool True if the user is on the waitlist, false otherwise.
     */
    function isOnWaitlist(address user) external view returns (bool) {
        return waitlist[user];
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
