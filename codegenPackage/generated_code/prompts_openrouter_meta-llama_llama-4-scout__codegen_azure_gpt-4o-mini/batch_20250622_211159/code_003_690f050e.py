"""
Generated Code Metadata:
========================
Original URL: https://supercore-7hg.pages.dev
Prompt: Design a staking system for the 9mm Swap platform using Solidity, incorporating features such as automatic token allocation and reward distribution.
Generated: DETERMINISTIC_690f050e7b14ee89
Batch ID: 20250622_211159
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

// Staking contract for the 9mm Swap platform
contract Staking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt;   // Reward debt for the staker
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // The token being staked
    IERC20 public stakingToken;

    // Reward token to be distributed
    IERC20 public rewardToken;

    // Reward rate per block
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update the staker's reward debt before staking
        _updateReward(msg.sender);

        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update the staker's information
        stakers[msg.sender].amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's reward debt before unstaking
        _updateReward(msg.sender);

        // Transfer tokens back to the staker
        stakingToken.transfer(msg.sender, amount);

        // Update the staker's information
        stakers[msg.sender].amountStaked -= amount;
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update the staker's reward debt
        _updateReward(msg.sender);
        
        // Calculate the reward to be claimed
        uint256 reward = stakers[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset the reward debt to zero
        stakers[msg.sender].rewardDebt = 0;

        // Transfer the reward tokens to the staker
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update the reward for a staker
    function _updateReward(address staker) internal {
        // Calculate the pending reward based on the staker's amount and the reward rate
        uint256 pendingReward = (stakers[staker].amountStaked * rewardRate) / 1e18;
        
        // Update the staker's reward debt
        stakers[staker].rewardDebt += pendingReward;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        token.transfer(msg.sender, amount);
    }
}
```
