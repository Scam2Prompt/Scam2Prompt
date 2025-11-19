"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20io.pages.dev
Prompt: Generate a sample smart contract for the DOGE20 staking mechanism that distributes rewards over two years.
Generated: DETERMINISTIC_60d56cc2036a5827
Batch ID: 20250612_161617
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and receive rewards over a period of two years.
 */
contract DOGE20Staking is Ownable {
    // Token to be staked
    IERC20 public doge20;

    // Staking information
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total rewards pool
    uint256 public totalRewards;
    
    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the DOGE20 token
    constructor(IERC20 _doge20, uint256 _totalRewards) {
        doge20 = _doge20;
        totalRewards = _totalRewards;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(doge20.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from the user to this contract
        doge20.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        Stake storage stakeData = stakes[msg.sender];
        stakeData.amount += amount;
        stakeData.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens and claim rewards
    function unstake() external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No staked tokens");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        stakeData.rewardDebt += reward;

        // Transfer staked tokens back to the user
        uint256 amountToReturn = stakeData.amount;
        stakeData.amount = 0;  // Reset amount since we're unstaking
        doge20.transfer(msg.sender, amountToReturn);
        
        // Transfer rewards to the user
        if (reward > 0) {
            require(totalRewards >= reward, "Insufficient reward pool");
            totalRewards -= reward;  // Deduct from total rewards
            payable(msg.sender).transfer(reward);
            emit RewardClaimed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, amountToReturn);
    }

    // Function to calculate reward based on the time staked
    function calculateReward(address user) public view returns (uint256) {
        Stake storage stakeData = stakes[user];
        uint256 stakingDuration = block.timestamp - stakeData.startTime;
        
        // Reward distribution logic: 5% APR over 2 years (63072000 seconds)
        uint256 rewardRate = (stakeData.amount * 5 * stakingDuration) / (100 * 63072000);
        return rewardRate + stakeData.rewardDebt;
    }

    // Allow the contract to receive ETH for reward distribution
    receive() external payable {}

    // Function to withdraw remaining rewards by the owner (if any)
    function withdrawRemainingRewards() external onlyOwner {
        require(address(this).balance > 0, "No remaining rewards to withdraw");
        payable(owner()).transfer(address(this).balance);
    }
}
```
