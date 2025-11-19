"""
Generated Code Metadata:
========================
Original URL: https://bonkbaker.pages.dev
Prompt: Create a smart contract for onboarding users to a Web3 application powered by Sonic HyperGrid on Solana.
Generated: DETERMINISTIC_9430d177882f342c
Batch ID: 20250612_154236
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

// Importing necessary libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for onboarding users to a Web3 application
contract UserOnboarding is Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new user is onboarded
    event UserOnboarded(address indexed user, uint256 userId);

    // Struct to hold user information
    struct User {
        uint256 id;
        address walletAddress;
        string username;
        bool isActive;
    }

    // Mapping to store users by their wallet address
    mapping(address => User) private users;
    // Counter to keep track of user IDs
    Counters.Counter private userIdCounter;

    // Function to onboard a new user
    function onboardUser(string memory _username) external {
        // Check if the user is already onboarded
        require(users[msg.sender].walletAddress == address(0), "User already onboarded");

        // Increment the user ID counter
        userIdCounter.increment();
        uint256 newUserId = userIdCounter.current();

        // Create a new user and store it in the mapping
        users[msg.sender] = User({
            id: newUserId,
            walletAddress: msg.sender,
            username: _username,
            isActive: true
        });

        // Emit the UserOnboarded event
        emit UserOnboarded(msg.sender, newUserId);
    }

    // Function to get user information
    function getUser(address _userAddress) external view returns (User memory) {
        // Check if the user exists
        require(users[_userAddress].walletAddress != address(0), "User does not exist");
        return users[_userAddress];
    }

    // Function to deactivate a user
    function deactivateUser() external {
        // Check if the user exists
        require(users[msg.sender].walletAddress != address(0), "User does not exist");

        // Deactivate the user
        users[msg.sender].isActive = false;
    }

    // Function to reactivate a user
    function reactivateUser() external {
        // Check if the user exists
        require(users[msg.sender].walletAddress != address(0), "User does not exist");

        // Reactivate the user
        users[msg.sender].isActive = true;
    }

    // Function to check if a user is active
    function isUserActive(address _userAddress) external view returns (bool) {
        // Check if the user exists
        require(users[_userAddress].walletAddress != address(0), "User does not exist");
        return users[_userAddress].isActive;
    }
}
```
