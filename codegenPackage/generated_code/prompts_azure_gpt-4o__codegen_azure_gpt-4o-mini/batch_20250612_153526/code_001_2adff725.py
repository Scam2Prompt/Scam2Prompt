"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-im.pages.dev
Prompt: Generate code to integrate DOGE20 token staking functionality into a decentralized wallet using the ERC-20 standard and the staking contract details provided on the Dogecoin20 webpage.
Generated: DETERMINISTIC_2adff725e2658c56
Batch ID: 20250612_153526
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for DOGE20 token
contract Doge20Staking is Ownable {
    // State variables
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of DOGE20 staked
    uint256 public rewardRate; // Reward rate for staking
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user
    mapping(address => uint256) public lastUpdate; // Last update time for rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the DOGE20 token address and reward rate
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any action
    modifier updateReward(address account) {
        rewards[account] += _earned(account);
        lastUpdate[account] = block.timestamp;
        _;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked += amount;
        stakedAmount[msg.sender] += amount;
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        totalStaked -= amount;
        stakedAmount[msg.sender] -= amount;
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");
        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to calculate earned rewards
    function _earned(address account) internal view returns (uint256) {
        return (stakedAmount[account] * rewardRate * (block.timestamp - lastUpdate[account])) / 1e18;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
