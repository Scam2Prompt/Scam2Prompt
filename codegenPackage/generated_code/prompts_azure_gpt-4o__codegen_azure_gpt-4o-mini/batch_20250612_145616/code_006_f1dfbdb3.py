"""
Generated Code Metadata:
========================
Original URL: https://moonhop.pages.dev
Prompt: Create a Solidity smart contract that implements a referral program similar to MOONHOP's, allowing users to generate referral codes and track rewards.
Generated: DETERMINISTIC_f1dfbdb3fc332712
Batch ID: 20250612_145616
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

contract ReferralProgram {
    // Struct to hold user information
    struct User {
        address referrer; // Address of the referrer
        uint256 rewards;  // Total rewards earned by the user
        uint256 referralsCount; // Number of referrals made by the user
    }

    // Mapping to store user information by address
    mapping(address => User) public users;

    // Event emitted when a new referral is created
    event ReferralCreated(address indexed user, address indexed referrer);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Function to register a user with a referrer
    function register(address _referrer) external {
        require(users[msg.sender].referrer == address(0), "User already registered");
        require(_referrer != msg.sender, "Cannot refer yourself");

        // Register the user with the referrer
        users[msg.sender].referrer = _referrer;
        users[_referrer].referralsCount += 1;

        emit ReferralCreated(msg.sender, _referrer);
    }

    // Function to calculate rewards based on referrals
    function calculateRewards(address _user) internal view returns (uint256) {
        // Example reward calculation: 10 tokens per referral
        return users[_user].referralsCount * 10;
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update user's rewards
        users[msg.sender].rewards += rewards;

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get user information
    function getUserInfo(address _user) external view returns (address referrer, uint256 rewards, uint256 referralsCount) {
        User memory user = users[_user];
        return (user.referrer, user.rewards, user.referralsCount);
    }
}
```
