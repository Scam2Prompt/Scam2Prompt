"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswapf.imweb.me
Prompt: Generate a Solidity contract that allows users to stake tokens in SushiSwap liquidity pools and earn SUSHI tokens as rewards.
Generated: DETERMINISTIC_11374609968dbb83
Batch ID: 20250612_155155
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

// Import interfaces for ERC20 and SushiSwap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// This contract allows users to stake tokens in SushiSwap liquidity pools
// and earn SUSHI tokens as rewards.
contract SushiStake {
    using SafeMath for uint256;

    // State variables
    IERC20 public stakeToken; // The token being staked
    IERC20 public rewardToken; // The SUSHI token rewarded
    uint256 public rewardRate; // Reward rate per staked token per second

    struct StakeInfo {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastUpdate; // Last timestamp when rewards were updated
    }

    mapping(address => StakeInfo) public stakes; // User stakes information
    uint256 public totalStaked; // Total amount staked in the contract

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with stake and reward tokens
    constructor(IERC20 _stakeToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakeToken = _stakeToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update user's reward debt and last update
        updateReward(msg.sender);

        // Transfer tokens from user to this contract
        stakeToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");

        // Update user's reward debt and last update
        updateReward(msg.sender);

        // Update the user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to user
        stakeToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateReward(msg.sender);
        uint256 reward = stakes[msg.sender].rewardDebt;

        require(reward > 0, "No rewards available");

        // Reset user's reward debt to zero
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update the user's rewards and last update timestamp
    function updateReward(address user) internal {
        StakeInfo storage stakeInfo = stakes[user];

        if (stakeInfo.amount > 0) {
            uint256 timeDiff = block.timestamp.sub(stakeInfo.lastUpdate);
            uint256 earnedReward = timeDiff.mul(rewardRate).mul(stakeInfo.amount).div(1e18);
            stakeInfo.rewardDebt = stakeInfo.rewardDebt.add(earnedReward);
        }

        stakeInfo.lastUpdate = block.timestamp;
    }

    // View function to see the staked amount for a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // View function to see the rewards for a user
    function earnedRewards(address user) external view returns (uint256) {
        StakeInfo memory stakeInfo = stakes[user];
        uint256 timeDiff = block.timestamp.sub(stakeInfo.lastUpdate);
        uint256 earnedReward = timeDiff.mul(rewardRate).mul(stakeInfo.amount).div(1e18);
        return stakeInfo.rewardDebt.add(earnedReward);
    }
}
```
