"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.mantranetwork.world
Prompt: Write a smart contract that integrates with MANTRA's ecosystem to facilitate token staking and rewards distribution using $OM tokens.
Generated: DETERMINISTIC_fd8d2e69a0d4bc53
Batch ID: 20250612_153256
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract to facilitate token staking and rewards distribution
contract MantraStaking {
    // Address of the $OM token
    IERC20 public immutable omToken;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardsEarned;
        uint256 lastUpdate;
    }

    // Mapping to track staker information
    mapping(address => Staker) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate (in tokens per second) for staking
    uint256 public rewardRate;

    // Event to log staking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the $OM token address and reward rate
    constructor(IERC20 _omToken, uint256 _rewardRate) {
        require(address(_omToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        omToken = _omToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $OM tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the tokens from the user to the contract
        omToken.transferFrom(msg.sender, address(this), amount);

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        updateRewards(msg.sender);

        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $OM tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than zero");
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateRewards(msg.sender);

        // Reduce the staked amount and total staked amount
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the user
        omToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = staker.rewardsEarned;

        require(rewards > 0, "No rewards to claim");
        staker.rewardsEarned = 0;

        // Transfer the rewards to the user
        omToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to update rewards based on the time since last update
    function updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeElapsed = block.timestamp - staker.lastUpdate;

        if (staker.amountStaked > 0) {
            staker.rewardsEarned += staker.amountStaked * rewardRate * timeElapsed;
        }

        // Update the last update time
        staker.lastUpdate = block.timestamp;
    }

    // Function to view the staked amount of a user
    function viewStake(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to view the earned rewards of a user
    function viewRewards(address user) external view returns (uint256) {
        Staker memory staker = stakers[user];
        uint256 timeElapsed = block.timestamp - staker.lastUpdate;
        uint256 earnedRewards = staker.rewardsEarned + (staker.amountStaked * rewardRate * timeElapsed);
        return earnedRewards;
    }
}
```
