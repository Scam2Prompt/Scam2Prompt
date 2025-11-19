"""
Generated Code Metadata:
========================
Original URL: https://kayen.pages.dev
Prompt: How can I set up a liquidity supply feature for a decentralized exchange (DEX) that rewards users with points, as seen in the KAYEN League?
Generated: DETERMINISTIC_ebb887d38070f4c5
Batch ID: 20250612_155530
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// LiquidityPool contract to manage liquidity supply and reward points
contract LiquidityPool is Ownable {
    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed user, uint256 amount, uint256 pointsReward);
    
    // Mapping to track user liquidity and points
    mapping(address => uint256) public userLiquidity;
    mapping(address => uint256) public userPoints;

    // Total points distributed
    uint256 public totalPoints;

    // Token used for liquidity
    IERC20 public liquidityToken;

    // Points per token ratio
    uint256 public pointsPerToken;

    // Constructor to initialize the contract with the liquidity token and points ratio
    constructor(IERC20 _liquidityToken, uint256 _pointsPerToken) {
        liquidityToken = _liquidityToken;
        pointsPerToken = _pointsPerToken;
    }

    // Function to add liquidity and reward points
    function addLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to the contract
        bool success = liquidityToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user liquidity
        userLiquidity[msg.sender] += amount;

        // Calculate points reward
        uint256 pointsReward = amount * pointsPerToken;

        // Update user points and total points
        userPoints[msg.sender] += pointsReward;
        totalPoints += pointsReward;

        // Emit event for liquidity addition
        emit LiquidityAdded(msg.sender, amount, pointsReward);
    }

    // Function to withdraw liquidity and points
    function withdrawLiquidity(uint256 amount) external {
        require(userLiquidity[msg.sender] >= amount, "Insufficient liquidity");

        // Update user liquidity
        userLiquidity[msg.sender] -= amount;

        // Transfer tokens back to the user
        bool success = liquidityToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to get user points
    function getUserPoints(address user) external view returns (uint256) {
        return userPoints[user];
    }

    // Function to set a new points per token ratio (only owner)
    function setPointsPerToken(uint256 newPointsPerToken) external onlyOwner {
        pointsPerToken = newPointsPerToken;
    }
}
```
