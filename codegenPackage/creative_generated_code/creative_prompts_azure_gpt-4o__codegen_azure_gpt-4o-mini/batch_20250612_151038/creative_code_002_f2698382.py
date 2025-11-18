"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prerich.pages.dev
Prompt: Generate code for deploying a smart contract on Ethereum that handles user registration for a Web3-based service.
Generated: DETERMINISTIC_f269838246ae9bc3
Batch ID: 20250612_151038
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

import "@openzeppelin/contracts/access/Ownable.sol"; // Import OpenZeppelin's Ownable for access control
import "@openzeppelin/contracts/utils/Counters.sol"; // Import Counters for unique ID generation

/**
 * @title UserRegistration
 * @dev A smart contract for registering users on a Web3-based service
 */
contract UserRegistration is Ownable {
    using Counters for Counters.Counter; // Using Counters for managing user IDs

    // Struct to represent a user
    struct User {
        uint256 id; // Unique ID of the user
        string username; // Username of the user
        bool registered; // Registration status
    }

    // Mapping from user address to User details
    mapping(address => User) private users;

    // Counter for generating unique user IDs
    Counters.Counter private userIdCounter;

    // Event emitted when a user registers
    event UserRegistered(address indexed userAddress, uint256 userId, string username);

    /**
     * @dev Registers a new user with a unique username
     * @param _username The username for the new user
     */
    function register(string calldata _username) external {
        // Check if user is already registered
        require(!users[msg.sender].registered, "User already registered");

        // Increment the userIdCounter to get a new unique ID
        userIdCounter.increment();
        uint256 newUserId = userIdCounter.current();

        // Create a new user and store it in the mapping
        users[msg.sender] = User(newUserId, _username, true);

        // Emit the UserRegistered event
        emit UserRegistered(msg.sender, newUserId, _username);
    }

    /**
     * @dev Retrieves user details by address
     * @param _userAddress The address of the user
     * @return The user's ID, username, and registration status
     */
    function getUser(address _userAddress) external view returns (uint256, string memory, bool) {
        // Check if user is registered
        require(users[_userAddress].registered, "User not registered");

        User memory user = users[_userAddress];
        return (user.id, user.username, user.registered);
    }

    /**
     * @dev Checks if a user is registered
     * @param _userAddress The address of the user
     * @return True if registered, otherwise false
     */
    function isRegistered(address _userAddress) external view returns (bool) {
        return users[_userAddress].registered;
    }

    /**
     * @dev Allows the owner to remove a user registration (for administrative purposes)
     * @param _userAddress The address of the user to unregister
     */
    function unregister(address _userAddress) external onlyOwner {
        // Check if user is registered
        require(users[_userAddress].registered, "User not registered");

        // Delete the user from the mapping
        delete users[_userAddress];
    }
}
```
