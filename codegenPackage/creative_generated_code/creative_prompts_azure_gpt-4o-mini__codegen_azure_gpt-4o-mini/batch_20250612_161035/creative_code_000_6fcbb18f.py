"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifxemhmcoxzasei3ihjmhn4lqipe5agpyl4q7uezcvyeecdfm7oj4.ipfs.dweb.link
Prompt: Generate a smart contract for a community-driven project inspired by Keyboard Cat, including features for user registration and eligibility criteria.
Generated: DETERMINISTIC_6fcbb18f6c89e7da
Batch ID: 20250612_161035
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

contract KeyboardCatCommunity {
    // Event to notify when a new user registers
    event UserRegistered(address indexed user, string username);

    // Struct to hold user information
    struct User {
        string username;
        uint256 registrationTime;
        bool isActive;
    }

    // Mapping from user address to User struct
    mapping(address => User) private users;

    // Variable to track the number of registered users
    uint256 public userCount;

    // Eligibility criteria constants
    uint256 public constant MIN_REGISTRATION_TIME = 1 days; // Minimum time a user should be active
    uint256 public constant MAX_USER_COUNT = 100; // Maximum number of users

    // Modifier to check whether the user is already registered
    modifier onlyRegistered() {
        require(users[msg.sender].isActive, "User is not registered");
        _;
    }

    // Modifier to check if registration is possible
    modifier canRegister(string memory _username) {
        require(userCount < MAX_USER_COUNT, "User limit reached");
        require(bytes(_username).length > 0, "Username cannot be empty");
        require(!users[msg.sender].isActive, "User already registered");
        _;
    }

    // Function to register a new user
    function register(string memory _username) public canRegister(_username) {
        users[msg.sender] = User({
            username: _username,
            registrationTime: block.timestamp,
            isActive: true
        });

        userCount++;
        emit UserRegistered(msg.sender, _username);
    }

    // Function to check if a user is eligible based on their registration time
    function isEligible() public view onlyRegistered returns (bool) {
        return (block.timestamp - users[msg.sender].registrationTime >= MIN_REGISTRATION_TIME);
    }

    // Function to get user information
    function getUserInfo() public view onlyRegistered returns (string memory username, uint256 registrationTime) {
        User memory user = users[msg.sender];
        return (user.username, user.registrationTime);
    }

    // Function for users to deactivate their account
    function deactivateAccount() public onlyRegistered {
        users[msg.sender].isActive = false;
        userCount--;
    }
}
```
