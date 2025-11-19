"""
Generated Code Metadata:
========================
Original URL: https://cowswap-finance.medium.com
Prompt: Explain how to implement a presale farming pool using the concepts from CowSwap's recent announcements.
Generated: DETERMINISTIC_9c91e57e325c8a99
Batch ID: 20250612_163135
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

// PresaleFarmingPool contract allows users to stake tokens and earn rewards
contract PresaleFarmingPool is Ownable {
    // State variables
    IERC20 public stakingToken; // Token to be staked
    IERC20 public rewardToken;  // Token to be rewarded
    uint256 public rewardRate;  // Rate of reward per block
    uint256 public lastUpdateBlock; // Last block when rewards were updated
    uint256 public totalStaked; // Total amount of tokens staked

    // Mapping to track user stakes and rewards
    mapping(address => uint256) public stakes;
    mapping(address => uint256) public rewards;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    // Modifier to update rewards before any action
    modifier updateReward(address account) {
        rewards[account] += earned(account);
        lastUpdateBlock = block.number;
        _;
    }

    // Function to calculate earned rewards
    function earned(address account) public view returns (uint256) {
        return (stakes[account] * rewardRate * (block.number - lastUpdateBlock)) / 1e18;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        stakes[msg.sender] += amount;
        totalStaked += amount;
        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");
        stakes[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to withdraw remaining tokens in case of emergency
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.transfer(msg.sender, balance);
    }
}
```
