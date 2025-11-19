"""
Generated Code Metadata:
========================
Original URL: https://smartwebssolution.web.app
Prompt: "Implement a staking and harvesting system for assets on a decentralized platform."
Generated: DETERMINISTIC_2c65b3b79b4b8672
Batch ID: 20250622_205006
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

// Staking and Harvesting contract for a decentralized platform
contract StakingHarvesting is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward token
    IERC20 public rewardToken;

    // Staking token
    IERC20 public stakingToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt = calculateReward(msg.sender);
        userStake.lastStakedTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update user stake information
        userStake.rewardDebt = calculateReward(msg.sender);
        userStake.amount -= _amount;
        totalStaked -= _amount;

        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to harvest rewards
    function harvest() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        userStake.rewardDebt = 0; // Reset reward debt
        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");

        emit Harvested(msg.sender, reward);
    }

    // Internal function to calculate rewards
    function calculateReward(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 blocksStaked = (block.timestamp - userStake.lastStakedTime) / 15; // Assuming 15 seconds per block
        return (userStake.amount * rewardPerBlock * blocksStaked) - userStake.rewardDebt;
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(stakingToken.transfer(msg.sender, balance), "Transfer failed");
    }
}
```
