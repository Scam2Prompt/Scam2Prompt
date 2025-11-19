"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy-io.github.io
Prompt: Develop a smart contract that allows users to provide liquidity to Zealy's liquidity pools and earn rewards in ORB tokens.
Generated: DETERMINISTIC_1b128499a9287848
Batch ID: 20250612_163135
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// ZealyLiquidityPool contract that allows users to provide liquidity and earn rewards
contract ZealyLiquidityPool is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Token used for liquidity provision
    IERC20 public liquidityToken;
    // Token used for rewards
    IERC20 public rewardToken;

    // Struct to store user information
    struct UserInfo {
        uint256 amount; // Amount of liquidity tokens provided by the user
        uint256 rewardDebt; // Amount of reward tokens owed to the user
    }

    // Mapping from user address to UserInfo
    mapping(address => UserInfo) public userInfo;

    // Total amount of liquidity tokens in the pool
    uint256 public totalLiquidity;
    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when liquidity is provided
    event LiquidityProvided(address indexed user, uint256 amount);
    // Event emitted when liquidity is withdrawn
    event LiquidityWithdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with tokens
    constructor(IERC20 _liquidityToken, IERC20 _rewardToken) {
        liquidityToken = _liquidityToken;
        rewardToken = _rewardToken;
    }

    // Function to provide liquidity to the pool
    function provideLiquidity(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to the contract
        liquidityToken.transferFrom(msg.sender, address(this), _amount);

        // Update user information
        UserInfo storage user = userInfo[msg.sender];
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.rewardDebt.add(_amount); // Simplified reward tracking for this example

        // Update total liquidity
        totalLiquidity = totalLiquidity.add(_amount);

        emit LiquidityProvided(msg.sender, _amount);
    }

    // Function to withdraw liquidity from the pool
    function withdrawLiquidity(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient balance");

        // Update user information
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.rewardDebt.sub(_amount); // Simplified reward tracking for this example
        
        // Transfer tokens back to the user
        liquidityToken.transfer(msg.sender, _amount);

        // Update total liquidity
        totalLiquidity = totalLiquidity.sub(_amount);

        emit LiquidityWithdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 rewardAmount = user.rewardDebt; // Simplified reward calculation for this example
        require(rewardAmount > 0, "No rewards to claim");

        // Reset user's reward debt
        user.rewardDebt = 0;

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, rewardAmount);
        totalRewards = totalRewards.add(rewardAmount); // Keep track of total rewards distributed

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to withdraw tokens in case of emergency (onlyOwner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= liquidityToken.balanceOf(address(this)), "Insufficient balance in pool");
        liquidityToken.transfer(msg.sender, _amount);
    }
}
```
