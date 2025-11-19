"""
Generated Code Metadata:
========================
Original URL: https://memekombatio.pages.dev
Prompt: Create a step-by-step guide for integrating $MK token staking functionality into a decentralized application using the Meme Kombat platform.
Generated: DETERMINISTIC_b2166605ef0586f4
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeKombatStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Staking token (MK)
    IERC20 public immutable stakingToken;

    // Struct to store user staking details
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (tokens per second per token staked)
    uint256 public rewardRate;

    // Last update timestamp for rewards
    uint256 public lastUpdateTime;

    // Reward per token stored
    uint256 public rewardPerTokenStored;

    // Mapping from user address to their reward per token paid
    mapping(address => uint256) public userRewardPerTokenPaid;

    // Mapping from user address to their rewards
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
    }

    // Update reward for a given account
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            ((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked;
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return ((stakes[account].amount * 
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) + 
                rewards[account];
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakedAt = block.timestamp;
        totalStaked += amount;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            stakingToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(stakes[msg.sender].amount);
        getReward();
    }

    // Update reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```

```javascript
// Frontend integration example (React + ethers.js)
import { ethers } from 'ethers';
import stakingABI from './stakingABI.json';

const stakingContractAddress = "0x..."; // Replace with actual contract address

// Initialize provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Initialize contract
const stakingContract = new ethers.Contract(
  stakingContractAddress,
  stakingABI,
  signer
);

// Stake tokens
async function stakeTokens(amount) {
  try {
    const tx = await stakingContract.stake(amount);
    await tx.wait();
    console.log('Staking successful');
  } catch (error) {
    console.error('Staking failed:', error);
  }
}

// Withdraw tokens
async function withdrawTokens(amount) {
  try {
    const tx = await stakingContract.withdraw(amount);
    await tx.wait();
    console.log('Withdrawal successful');
  } catch (error) {
    console.error('Withdrawal failed:', error);
  }
}

// Claim rewards
async function claimRewards() {
  try {
    const tx = await stakingContract.getReward();
    await tx.wait();
    console.log('Rewards claimed successfully');
  } catch (error) {
    console.error('Claim failed:', error);
  }
}

// Get user stake info
async function getUserStake(address) {
  try {
    const stake = await stakingContract.stakes(address);
    return {
      amount: stake.amount.toString(),
      stakedAt: stake.stakedAt.toString()
    };
  } catch (error) {
    console.error('Error fetching stake:', error);
    return null;
  }
}

// Get earned rewards
async function getEarnedRewards(address) {
  try {
    const rewards = await stakingContract.earned(address);
    return rewards.toString();
  } catch (error) {
    console.error('Error fetching rewards:', error);
    return '0';
  }
}
```
