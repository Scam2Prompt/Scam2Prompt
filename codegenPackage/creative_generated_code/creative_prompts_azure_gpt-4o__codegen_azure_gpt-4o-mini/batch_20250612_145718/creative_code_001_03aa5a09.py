"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: Develop a smart contract in Solidity for managing the referral system and LVL ratings planned for April 2024, as outlined on the Hamster Kombat roadmap.
Generated: DETERMINISTIC_03aa5a092ad3019f
Batch ID: 20250612_145718
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

contract HamsterKombatReferral {

    // Event emitted when a new referral is created
    event NewReferral(address indexed referrer, address indexed referee);

    // Structure to track user data
    struct User {
        address referrer;
        uint256 referralCount;
        uint256 level;
    }

    // Mapping from user address to User data
    mapping(address => User) public users;

    // Level thresholds defined for the referral system
    uint256[] public levelThresholds = [0, 5, 15, 30]; // Example thresholds

    // Modifier to ensure a user is registered
    modifier onlyRegistered() {
        require(users[msg.sender].referrer != address(0) || msg.sender == address(0), "User not registered");
        _;
    }

    // Function to register a new user with a referrer
    function register(address referrer) external {
        require(users[msg.sender].referrer == address(0), "User already registered");
        
        if (referrer != address(0)) {
            require(users[referrer].referrer != address(0) || referrer == address(0), "Invalid referrer");
            users[referrer].referralCount += 1;
            users[msg.sender].referrer = referrer;
            emit NewReferral(referrer, msg.sender);
        }
    }

    // Function to update user levels based on their referral count
    function updateLevel(address user) external onlyRegistered {
        User storage currentUser = users[user];
        
        for (uint256 i = 0; i < levelThresholds.length; i++) {
            if (currentUser.referralCount >= levelThresholds[i]) {
                currentUser.level = i + 1; // Level starts from 1
            }
        }
    }

    // Function to get user details
    function getUserDetails(address user) external view returns (address referrer, uint256 referralCount, uint256 level) {
        User storage currentUser = users[user];
        return (currentUser.referrer, currentUser.referralCount, currentUser.level);
    }

    // Function to get the level of a user
    function getUserLevel(address user) external view onlyRegistered returns (uint256) {
        return users[user].level;
    }
}
```
