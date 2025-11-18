"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-in.web.app
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum that distributes rewards proportionally to the percentage of the staking pool over a two-year period.
Generated: DETERMINISTIC_afe81618637d4d31
Batch ID: 20250612_153401
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

// Import IERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Doge20Staking {
    // Define state variables
    IERC20 public doge20Token; // DOGE20 token contract
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    uint256 public rewardRate; // Reward rate per second (in wei)
    uint256 public stakingEnd; // Timestamp when staking period ends
    mapping(address => uint256) public stakedAmount; // Mapping of staked amount per user
    mapping(address => uint256) public rewards; // Mapping of pending rewards per user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the token and reward settings
    constructor(IERC20 _doge20Token, uint256 _rewardRate, uint256 _duration) {
        require(address(_doge20Token) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
        stakingEnd = block.timestamp + _duration;
    }

    // Modifier to check if staking is active
    modifier stakingActive() {
        require(block.timestamp < stakingEnd, "Staking period has ended");
        _;
    }

    // Modifier to check if staking is closed
    modifier stakingEnded() {
        require(block.timestamp >= stakingEnd, "Staking period is still active");
        _;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external stakingActive {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer DOGE20 tokens from user to contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update state variables
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens and claim rewards
    function unstake() external stakingEnded {
        uint256 amount = stakedAmount[msg.sender];
        require(amount > 0, "No tokens to unstake");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] += reward;

        // Reset user's staked amount
        stakedAmount[msg.sender] = 0;
        totalStaked -= amount;

        // Transfer original DOGE20 tokens back to user
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to claim rewards
    function claimRewards() external stakingEnded {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Reset user's rewards
        rewards[msg.sender] = 0;

        // Transfer rewards to user
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        uint256 userStake = stakedAmount[user];
        if (totalStaked == 0 || userStake == 0) {
            return 0; // No rewards if user has no stake
        }

        // Calculate total duration for rewards
        uint256 stakingDuration = stakingEnd - (stakingEnd - 1 days);
        return (userStake * rewardRate * stakingDuration) / totalStaked;
    }
}
```
