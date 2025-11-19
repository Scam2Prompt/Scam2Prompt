"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-dogeverse-claim.pages.dev
Prompt: Create a Solidity contract that mimics the Dogeverse token staking mechanism, detailing how rewards are distributed per Ethereum block.
Generated: DETERMINISTIC_3a2bdb28cc11ca94
Batch ID: 20250612_160940
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

// A contract that implements a staking mechanism for a token
contract DogeverseStaking is Ownable {
    // Token to be staked
    IERC20 public stakingToken;

    // Reward token that will be distributed
    IERC20 public rewardToken;

    // Struct to hold user staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for user
        uint256 lastStakedBlock; // Block number of last stake
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set initial token addresses and reward rate
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update user reward debt before transferring tokens
        updateReward(msg.sender);

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakedBlock = block.number;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user reward debt before transferring tokens
        updateReward(msg.sender);

        // Transfer tokens back to user
        userStake.amount -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateReward(msg.sender);
        uint256 reward = stakes[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer reward tokens to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateReward(address user) internal {
        Stake storage userStake = stakes[user];

        // Calculate rewards based on blocks staked
        uint256 blocksStaked = block.number - userStake.lastStakedBlock;
        uint256 newReward = blocksStaked * rewardPerBlock;

        // Update user's reward debt
        userStake.rewardDebt += newReward;
        userStake.lastStakedBlock = block.number;
    }

    // Function to withdraw contract's tokens (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(msg.sender, amount);
    }
}
```
