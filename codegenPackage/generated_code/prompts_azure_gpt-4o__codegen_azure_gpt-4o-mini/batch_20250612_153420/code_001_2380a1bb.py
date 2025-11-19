"""
Generated Code Metadata:
========================
Original URL: https://magesdsdf.pages.dev
Prompt: Create a smart contract in Solidity for staking $Mners tokens in the Merlin ecosystem and earning dual incentives.
Generated: DETERMINISTIC_2380a1bb44e97291
Batch ID: 20250612_153420
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $Mners tokens in the Merlin ecosystem
contract MnersStaking is Ownable {
    // State variables
    IERC20 public mnersToken; // The $Mners token contract
    uint256 public rewardRate; // Rate of reward per block
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    mapping(address => uint256) public lastUpdate; // Last update time for rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the $Mners token address and reward rate
    constructor(IERC20 _mnersToken, uint256 _rewardRate) {
        mnersToken = _mnersToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any action
    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] += earned(account);
            lastUpdate[account] = block.number;
        }
        _;
    }

    // Function to stake $Mners tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        mnersToken.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake $Mners tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        mnersToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        // Transfer the reward tokens (assumed to be a separate token contract)
        // Replace with actual reward token contract address
        // rewardToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate earned rewards
    function earned(address account) public view returns (uint256) {
        return (stakedAmount[account] * (block.number - lastUpdate[account]) * rewardRate) / 1e18;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= mnersToken.balanceOf(address(this)), "Insufficient balance");
        mnersToken.transfer(msg.sender, amount);
    }
}
```
