"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nbnm.pages.dev
Prompt: Write a smart contract that incorporates Safe AA technology to enhance security and earn additional points in the Sonic Boom program.
Generated: DETERMINISTIC_c4ed71efe7b8a851
Batch ID: 20250612_155032
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
 * @title SonicBoomSafeAA
 * @dev This smart contract incorporates Safe Account Abstraction (AA) technology to enhance security
 *      and manage points in the Sonic Boom program.
 */
contract SonicBoomSafeAA {
    // Mapping to track user points balances
    mapping(address => uint256) private pointsBalances;

    // Event emitted when points are earned
    event PointsEarned(address indexed user, uint256 points);

    // Event emitted when points are redeemed
    event PointsRedeemed(address indexed user, uint256 points);

    // Modifier to ensure the caller is a valid EOA or contract
    modifier onlyValidAccount(address account) {
        require(account != address(0), "Invalid account address");
        _;
    }

    /**
     * @dev Function to earn points in the Sonic Boom program.
     * @param user The address of the user earning points.
     * @param points The number of points to award.
     */
    function earnPoints(address user, uint256 points) external onlyValidAccount(user) {
        require(points > 0, "Points must be greater than zero");

        // Update user's points balance
        pointsBalances[user] += points;

        // Emit event
        emit PointsEarned(user, points);
    }

    /**
     * @dev Function to redeem points in the Sonic Boom program.
     * @param user The address of the user redeeming points.
     * @param points The number of points to redeem.
     */
    function redeemPoints(address user, uint256 points) external onlyValidAccount(user) {
        require(points > 0, "Points must be greater than zero");
        require(pointsBalances[user] >= points, "Insufficient points balance");

        // Update user's points balance
        pointsBalances[user] -= points;

        // Emit event
        emit PointsRedeemed(user, points);
    }

    /**
     * @dev Function to check a user's points balance.
     * @param user The address of the user.
     * @return The user's points balance.
     */
    function getPointsBalance(address user) external view onlyValidAccount(user) returns (uint256) {
        return pointsBalances[user];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Ether transfers not allowed");
    }
}
```
