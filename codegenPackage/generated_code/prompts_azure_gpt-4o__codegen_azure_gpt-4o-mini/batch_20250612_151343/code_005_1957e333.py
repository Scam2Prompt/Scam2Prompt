"""
Generated Code Metadata:
========================
Original URL: https://gravity-cq3.pages.dev
Prompt: Create a code example for implementing loyalty points on-chain using Gravity's low transaction cost and scalability features.
Generated: DETERMINISTIC_1957e333650bfb3f
Batch ID: 20250612_151343
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
 * @dev A smart contract to manage loyalty points on-chain.
 * This contract allows users to earn, redeem, and transfer loyalty points.
 */
contract LoyaltyPoints is Ownable {
    // Mapping from user address to their loyalty points balance
    mapping(address => uint256) private _balances;

    // Event emitted when points are earned
    event PointsEarned(address indexed user, uint256 amount);

    // Event emitted when points are redeemed
    event PointsRedeemed(address indexed user, uint256 amount);

    // Event emitted when points are transferred
    event PointsTransferred(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Earn loyalty points for a user.
     * @param user The address of the user earning points.
     * @param amount The amount of points to be earned.
     */
    function earnPoints(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        _balances[user] += amount;
        emit PointsEarned(user, amount);
    }

    /**
     * @dev Redeem loyalty points for a user.
     * @param amount The amount of points to be redeemed.
     */
    function redeemPoints(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient points");

        _balances[msg.sender] -= amount;
        emit PointsRedeemed(msg.sender, amount);
    }

    /**
     * @dev Transfer loyalty points from one user to another.
     * @param to The address of the recipient.
     * @param amount The amount of points to transfer.
     */
    function transferPoints(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient points");

        _balances[msg.sender] -= amount;
        _balances[to] += amount;
        emit PointsTransferred(msg.sender, to, amount);
    }

    /**
     * @dev Get the loyalty points balance of a user.
     * @param user The address of the user.
     * @return The loyalty points balance of the user.
     */
    function getPointsBalance(address user) external view returns (uint256) {
        return _balances[user];
    }
}
```
