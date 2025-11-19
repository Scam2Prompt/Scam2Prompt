"""
Generated Code Metadata:
========================
Original URL: https://zeek.social
Prompt: Generate a smart contract in Solidity for managing referral codes and rewards distribution, inspired by Zeek Network's SocialFi model.
Generated: DETERMINISTIC_7f09e77a92dfcac4
Batch ID: 20250612_152358
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

contract ReferralRewards {
    // Struct to hold user information
    struct User {
        address referrer; // Address of the referrer
        uint256 rewards;  // Total rewards earned by the user
        bool isRegistered; // Flag to check if user is registered
    }

    // Mapping to store user information by address
    mapping(address => User) public users;

    // Event to emit when a user registers
    event UserRegistered(address indexed user, address indexed referrer);

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Modifier to check if the user is registered
    modifier onlyRegistered() {
        require(users[msg.sender].isRegistered, "User not registered");
        _;
    }

    // Function to register a user with an optional referrer
    function register(address _referrer) external {
        require(!users[msg.sender].isRegistered, "User already registered");
        
        // Register the user
        users[msg.sender] = User({
            referrer: _referrer,
            rewards: 0,
            isRegistered: true
        });

        // Emit the registration event
        emit UserRegistered(msg.sender, _referrer);
    }

    // Function to distribute rewards to a user
    function distributeRewards(address _user, uint256 _amount) external onlyRegistered {
        require(_amount > 0, "Reward amount must be greater than zero");
        
        // Update the user's rewards
        users[_user].rewards += _amount;

        // Emit the rewards distribution event
        emit RewardsDistributed(_user, _amount);
    }

    // Function to get the rewards of a user
    function getRewards() external view onlyRegistered returns (uint256) {
        return users[msg.sender].rewards;
    }

    // Function to get the referrer of a user
    function getReferrer() external view onlyRegistered returns (address) {
        return users[msg.sender].referrer;
    }
}
```
