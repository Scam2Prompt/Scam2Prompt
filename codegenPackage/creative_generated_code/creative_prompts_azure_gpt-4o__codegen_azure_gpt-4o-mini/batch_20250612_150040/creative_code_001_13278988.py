"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://high-sugar-sparse.on-fleek.app
Prompt: Create a smart contract for staking GamerCoin ($GHX) on the BNB Chain. Ensure the contract includes features for calculating rewards based on the staking duration and amount.
Generated: DETERMINISTIC_1327898881c07877
Batch ID: 20250612_150040
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

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for staking GamerCoin ($GHX)
contract GamerCoinStaking {
    // State variables
    IERC20 public ghxToken; // The ERC20 token being staked
    uint256 public rewardRate; // Reward rate per second per token
    uint256 public totalStaked; // Total tokens staked in the contract

    // Staker information structure
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the staking started
        uint256 rewards; // Rewards accumulated by the staker
    }

    // Mapping of staker addresses to their information
    mapping(address => Staker) public stakers;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _ghxToken, uint256 _rewardRate) {
        ghxToken = _ghxToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(ghxToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.startTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.amount == 0) {
            return 0; // No staked tokens, no rewards
        }
        uint256 stakingDuration = block.timestamp - staker.startTime;
        return (staker.amount * stakingDuration * rewardRate) / 1e18; // Adjust for precision
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");
        
        // Update staker's rewards before transferring
        Staker storage staker = stakers[msg.sender];
        staker.rewards += rewards;
        staker.startTime = block.timestamp; // Reset start time
        
        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked tokens to unstake");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        staker.rewards += rewards;

        // Transfer staked tokens back to the user
        require(ghxToken.transfer(msg.sender, staker.amount), "Transfer failed");

        // Reset staker data
        totalStaked -= staker.amount;
        delete stakers[msg.sender];

        emit Unstaked(msg.sender, staker.amount);
        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to withdraw accumulated rewards (if rewards are paid out in a separate token)
    function withdrawRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.rewards > 0, "No rewards to withdraw");

        uint256 rewardsToWithdraw = staker.rewards;
        staker.rewards = 0;

        require(ghxToken.transfer(msg.sender, rewardsToWithdraw), "Transfer failed");
    }

    // Function to set a new reward rate (onlyOwner modifier should be implemented in production)
    function setRewardRate(uint256 _newRate) external {
        rewardRate = _newRate;
    }
}
```
