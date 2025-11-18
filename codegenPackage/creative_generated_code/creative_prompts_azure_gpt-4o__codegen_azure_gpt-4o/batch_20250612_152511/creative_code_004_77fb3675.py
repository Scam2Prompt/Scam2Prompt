"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-app.pages.dev
Prompt: Create a smart contract in Solidity that mimics Everyworld's dual incentivization model, allowing users to earn points and pledge them to environmental charities.
Generated: DETERMINISTIC_77fb36756e53193b
Batch ID: 20250612_152511
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
 * @title DualIncentivizationContract
 * @dev A smart contract that mimics Everyworld's dual incentivization model.
 * Users can earn points and pledge them to environmental charities.
 */
contract DualIncentivizationContract {
    // Struct to represent a user's account
    struct User {
        uint256 points; // Points earned by the user
        uint256 pledgedPoints; // Points pledged by the user to charities
    }

    // Mapping to store user data
    mapping(address => User) private users;

    // Event emitted when points are earned
    event PointsEarned(address indexed user, uint256 amount);

    // Event emitted when points are pledged to a charity
    event PointsPledged(address indexed user, address indexed charity, uint256 amount);

    /**
     * @dev Modifier to ensure users have enough points to pledge.
     * @param user Address of the user.
     * @param amount The amount of points to check.
     */
    modifier hasSufficientPoints(address user, uint256 amount) {
        require(users[user].points >= amount, "Insufficient points");
        _;
    }

    /**
     * @dev Earn points by interacting with the system.
     * @param amount The amount of points to earn.
     */
    function earnPoints(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Add points to user's account
        users[msg.sender].points += amount;

        // Emit an event
        emit PointsEarned(msg.sender, amount);
    }

    /**
     * @dev Pledge points to an environmental charity.
     * @param charity Address of the charity to pledge points to.
     * @param amount The amount of points to pledge.
     */
    function pledgePoints(address charity, uint256 amount)
        external
        hasSufficientPoints(msg.sender, amount)
    {
        require(charity != address(0), "Invalid charity address");
        require(amount > 0, "Amount must be greater than zero");

        // Deduct points from user's account
        users[msg.sender].points -= amount;

        // Add pledged points to user's account
        users[msg.sender].pledgedPoints += amount;

        // Emit an event
        emit PointsPledged(msg.sender, charity, amount);
    }

    /**
     * @dev Get the balance of points for a user.
     * @param user Address of the user to query.
     * @return points The balance of points for the user.
     */
    function getPointsBalance(address user) external view returns (uint256 points) {
        return users[user].points;
    }

    /**
     * @dev Get the pledged points for a user.
     * @param user Address of the user to query.
     * @return pledgedPoints The total pledged points for the user.
     */
    function getPledgedPoints(address user) external view returns (uint256 pledgedPoints) {
        return users[user].pledgedPoints;
    }
}
```
