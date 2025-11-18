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

contract WaitlistManager {
    // Struct to hold user information
    struct User {
        address addr;   // User's wallet address
        uint256 addedAt; // Timestamp when user was added to the waitlist
    }

    // Mapping to store the waitlist of users
    mapping(address => User) public waitlist;
    // Array to keep track of the order of users in the waitlist
    address[] public waitlistOrder;
    // Count of users in the waitlist
    uint256 public waitlistCount;

    // Event emitted when a user is added to the waitlist
    event UserAdded(address indexed user);
    // Event emitted when a user is removed from the waitlist
    event UserRemoved(address indexed user);

    // Function to add a user to the waitlist
    function addToWaitlist() external {
        require(waitlist[msg.sender].addr == address(0), "User already waitlisted");

        // Create a new User and add to the waitlist
        waitlist[msg.sender] = User({
            addr: msg.sender,
            addedAt: block.timestamp
        });
        waitlistOrder.push(msg.sender);
        waitlistCount++;

        emit UserAdded(msg.sender);
    }

    // Function to remove a user from the waitlist
    function removeFromWaitlist() external {
        require(waitlist[msg.sender].addr != address(0), "User not in waitlist");

        // Remove user from the waitlist
        delete waitlist[msg.sender];
        waitlistCount--;

        // Find and remove the user from the waitlistOrder array
        for (uint256 i = 0; i < waitlistOrder.length; i++) {
            if (waitlistOrder[i] == msg.sender) {
                // Move the last element into the place to delete
                waitlistOrder[i] = waitlistOrder[waitlistOrder.length - 1];
                waitlistOrder.pop(); // Remove the last element
                break;
            }
        }

        emit UserRemoved(msg.sender);
    }

    // Function to get the waitlist count
    function getWaitlistCount() external view returns (uint256) {
        return waitlistCount;
    }

    // Function to get the waitlist of addresses
    function getWaitlist() external view returns (address[] memory) {
        return waitlistOrder;
    }

    // Function to check if an address is on the waitlist
    function isUserOnWaitlist(address user) external view returns (bool) {
        return waitlist[user].addr != address(0);
    }
}
```
