"""
Generated Code Metadata:
========================
Original URL: https://bafybeifxemhmcoxzasei3ihjmhn4lqipe5agpyl4q7uezcvyeecdfm7oj4.ipfs.dweb.link
Prompt: Generate a smart contract for a community-driven project inspired by Keyboard Cat, including features for user registration and eligibility criteria.
Generated: DETERMINISTIC_6fcbb18f6c89e7da
Batch ID: 20250612_161035
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

contract KeyboardCatCommunity {
    // Struct to hold user information
    struct User {
        address userAddress;
        string username;
        bool isRegistered;
        uint256 registrationTime;
    }

    // Mapping to store registered users
    mapping(address => User) private users;

    // Event to emit when a user registers
    event UserRegistered(address indexed userAddress, string username, uint256 registrationTime);

    // Modifier to check if the user is already registered
    modifier onlyRegistered() {
        require(users[msg.sender].isRegistered, "User is not registered.");
        _;
    }

    // Modifier to check if the user is not registered
    modifier onlyUnregistered() {
        require(!users[msg.sender].isRegistered, "User is already registered.");
        _;
    }

    // Function to register a new user
    function registerUser(string memory _username) public onlyUnregistered {
        // Ensure the username is not empty
        require(bytes(_username).length > 0, "Username cannot be empty.");

        // Create a new user and store it in the mapping
        users[msg.sender] = User({
            userAddress: msg.sender,
            username: _username,
            isRegistered: true,
            registrationTime: block.timestamp
        });

        // Emit the registration event
        emit UserRegistered(msg.sender, _username, block.timestamp);
    }

    // Function to check if a user is registered
    function isUserRegistered(address _userAddress) public view returns (bool) {
        return users[_userAddress].isRegistered;
    }

    // Function to get user details
    function getUserDetails(address _userAddress) public view returns (string memory username, uint256 registrationTime) {
        require(users[_userAddress].isRegistered, "User is not registered.");
        User memory user = users[_userAddress];
        return (user.username, user.registrationTime);
    }

    // Function to unregister a user (if needed)
    function unregisterUser() public onlyRegistered {
        delete users[msg.sender];
    }
}
```
