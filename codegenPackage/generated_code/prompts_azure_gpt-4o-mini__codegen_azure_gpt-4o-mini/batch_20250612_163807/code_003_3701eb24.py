"""
Generated Code Metadata:
========================
Original URL: https://gravity-cq3.pages.dev
Prompt: Provide an example of how to create loyalty points on-chain using Gravity's low transaction cost features.
Generated: DETERMINISTIC_3701eb24424a4749
Batch ID: 20250612_163807
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LoyaltyPoints
 * @dev A contract to manage loyalty points on-chain using Gravity's low transaction cost features.
 */
contract LoyaltyPoints is Ownable {
    // Mapping from user address to their loyalty points balance
    mapping(address => uint256) private _pointsBalance;

    // Event emitted when points are awarded
    event PointsAwarded(address indexed user, uint256 points);

    // Event emitted when points are redeemed
    event PointsRedeemed(address indexed user, uint256 points);

    /**
     * @dev Award loyalty points to a user.
     * @param user The address of the user to award points to.
     * @param points The number of points to award.
     */
    function awardPoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(points > 0, "Points must be greater than zero");

        _pointsBalance[user] += points;

        emit PointsAwarded(user, points);
    }

    /**
     * @dev Redeem loyalty points for a user.
     * @param points The number of points to redeem.
     */
    function redeemPoints(uint256 points) external {
        require(points > 0, "Points must be greater than zero");
        require(_pointsBalance[msg.sender] >= points, "Insufficient points");

        _pointsBalance[msg.sender] -= points;

        emit PointsRedeemed(msg.sender, points);
    }

    /**
     * @dev Get the loyalty points balance of a user.
     * @param user The address of the user.
     * @return The number of loyalty points the user has.
     */
    function getPointsBalance(address user) external view returns (uint256) {
        return _pointsBalance[user];
    }
}
```
