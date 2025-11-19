"""
Generated Code Metadata:
========================
Original URL: https://scottytheaidapp.pages.dev
Prompt: Create a smart contract in Solidity for staking $SCOTTY tokens, ensuring the contract includes functionality for calculating rewards based on the user's share of the staking pool and dynamic rewards rate.
Generated: DETERMINISTIC_84a2496734fb0045
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking $SCOTTY tokens with dynamic rewards calculation.
 */
contract StakingContract is Ownable {
    IERC20 public scottyToken; // The $SCOTTY token contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Dynamic reward rate per block
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastUpdate; // Last block number when user staked/unstaked
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor to initialize the contract with the $SCOTTY token address.
     * @param _scottyToken Address of the $SCOTTY token contract.
     */
    constructor(IERC20 _scottyToken) {
        scottyToken = _scottyToken;
        rewardRate = 1e18; // Initial reward rate (1 token per block)
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of $SCOTTY tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update rewards before staking
        _updateRewards(msg.sender);

        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastUpdate[msg.sender] = block.number;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens.
     * @param amount Amount of $SCOTTY tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to update the reward rate.
     * @param newRate New reward rate to be set.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user to update rewards for.
     */
    function _updateRewards(address user) internal {
        uint256 staked = stakedAmount[user];
        if (staked > 0) {
            uint256 blocksStaked = block.number - lastUpdate[user];
            rewards[user] += (blocksStaked * rewardRate * staked) / totalStaked;
        }
        lastUpdate[user] = block.number;
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        require(scottyToken.transfer(msg.sender, reward), "Transfer failed");
    }

    /**
     * @dev Function to view the total rewards of a user.
     * @param user Address of the user.
     * @return Total rewards of the user.
     */
    function viewRewards(address user) external view returns (uint256) {
        uint256 staked = stakedAmount[user];
        uint256 blocksStaked = block.number - lastUpdate[user];
        uint256 totalRewards = rewards[user] + (blocksStaked * rewardRate * staked) / totalStaked;
        return totalRewards;
    }
}
```
