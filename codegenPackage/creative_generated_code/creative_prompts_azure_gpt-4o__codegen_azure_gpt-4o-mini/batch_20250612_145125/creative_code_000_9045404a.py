"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yifistake.finance
Prompt: Write a smart contract in Solidity to enable staking and farming of YI12 tokens, including functionality for claiming rewards and unfarming as described on the YI12 Stake Finance platform.
Generated: DETERMINISTIC_9045404a100d1b5d
Batch ID: 20250612_145125
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

// Importing the ERC20 interface for YI12 token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking and farming YI12 tokens
contract YI12StakeFarm is ReentrancyGuard, Ownable {
    // Token to be staked
    IERC20 public yi12Token;

    // Struct to hold user staking information
    struct UserStake {
        uint256 amount; // Amount of YI12 staked
        uint256 rewardDebt; // Reward debt
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserStake) public userStakes;

    // Total staked amount
    uint256 public totalStaked;
    
    // Reward parameters
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalRewards; // Total rewards distributed

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    // Constructor to initialize contract with the token address and reward rate
    constructor(IERC20 _yi12Token, uint256 _rewardRate) {
        yi12Token = _yi12Token;
        rewardRate = _rewardRate;
    }

    // Modifier to check if amount is greater than zero
    modifier amountGreaterThanZero(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    // Function to stake YI12 tokens
    function stake(uint256 amount) external nonReentrant amountGreaterThanZero(amount) {
        UserStake storage user = userStakes[msg.sender];

        // Transfer the tokens to the contract
        yi12Token.transferFrom(msg.sender, address(this), amount);

        // Update stakes
        user.amount += amount;
        user.rewardDebt += calculatePendingRewards(msg.sender);
        user.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake YI12 tokens
    function unstake(uint256 amount) external nonReentrant amountGreaterThanZero(amount) {
        UserStake storage user = userStakes[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");

        // Update stakes and rewards
        user.rewardDebt += calculatePendingRewards(msg.sender);
        user.amount -= amount;

        // Transfer tokens back to the user
        yi12Token.transfer(msg.sender, amount);

        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        UserStake storage user = userStakes[msg.sender];
        uint256 reward = calculatePendingRewards(msg.sender);

        require(reward > 0, "No rewards to claim");

        // Update the user's reward debt
        user.rewardDebt = 0;
        totalRewards += reward;

        // Transfer rewards to the user
        yi12Token.transfer(msg.sender, reward);

        emit Claimed(msg.sender, reward);
    }

    // Function to calculate pending rewards for a user
    function calculatePendingRewards(address userAddress) internal view returns (uint256) {
        UserStake storage user = userStakes[userAddress];
        uint256 timeDiff = block.timestamp - user.lastStakedTime;

        // Calculate pending rewards based on staked amount and time
        return (user.amount * rewardRate * timeDiff) / 1e18; // Assuming reward rate is per 1e18 seconds
    }

    // Function to withdraw remaining contract balance (only owner)
    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = yi12Token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        yi12Token.transfer(owner(), balance);
    }
}
```
