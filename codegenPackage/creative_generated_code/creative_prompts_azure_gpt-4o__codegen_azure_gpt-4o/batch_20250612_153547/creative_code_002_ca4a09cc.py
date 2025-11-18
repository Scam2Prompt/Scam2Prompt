"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkombatgame.pages.dev
Prompt: Create a smart contract in Solidity that supports a referral system with level ratings, inspired by the roadmap of "Hamster Kombat."
Generated: DETERMINISTIC_ca4a09ccd3302508
Batch ID: 20250612_153547
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
 * @title ReferralSystem
 * @dev A smart contract that implements a multi-level referral system with level ratings.
 */
contract ReferralSystem {
    // Struct to store user details including referrals and rating
    struct User {
        address referrer;
        uint256 level;
        uint256 rating;
        uint256 referralsCount;
    }

    // Mapping to store user data
    mapping(address => User) public users;

    // Event emitted when a new user registers with a referrer
    event UserRegistered(address indexed user, address indexed referrer, uint256 level);

    // Event emitted when a user's rating is updated
    event RatingUpdated(address indexed user, uint256 newRating);

    /**
     * @dev Register a new user with a referrer.
     * @param referrer The address of the referrer.
     */
    function registerUser(address referrer) external {
        // Ensure user is not already registered
        require(users[msg.sender].referrer == address(0), "User already registered");

        // Ensure referrer is registered or is address(0) (indicates no referrer)
        require(referrer == address(0) || users[referrer].referrer != address(0), "Invalid referrer");

        // Set the referrer and initialize user properties
        users[msg.sender].referrer = referrer;
        users[msg.sender].level = referrer == address(0) ? 1 : users[referrer].level + 1;
        users[msg.sender].rating = 0;
        users[msg.sender].referralsCount = 0;

        // Update referrer's referrals count
        if (referrer != address(0)) {
            users[referrer].referralsCount++;
        }

        // Emit event for registration
        emit UserRegistered(msg.sender, referrer, users[msg.sender].level);
    }

    /**
     * @dev Update a user's rating. Only callable by the user themselves.
     * @param newRating The new rating value.
     */
    function updateRating(uint256 newRating) external {
        // Ensure user is registered
        require(users[msg.sender].referrer != address(0), "User not registered");

        // Update the user's rating
        users[msg.sender].rating = newRating;

        // Emit event for rating update
        emit RatingUpdated(msg.sender, newRating);
    }

    /**
     * @dev Get details of a user.
     * @param user The address of the user.
     * @return referrer The address of the referrer.
     * @return level The user's referral level.
     * @return rating The user's rating.
     * @return referralsCount The user's referrals count.
     */
    function getUserDetails(address user) external view returns (address referrer, uint256 level, uint256 rating, uint256 referralsCount) {
        User memory u = users[user];
        return (u.referrer, u.level, u.rating, u.referralsCount);
    }
}
```
