"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20claim-now.pages.dev
Prompt: Generate Solidity code for a staking smart contract that mimics the DOGE20 reward distribution mechanism, providing rewards to stakers over a two-year period based on their share of the staking pool.
Generated: DETERMINISTIC_0397cc25d96a50c1
Batch ID: 20250612_150552
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

contract StakingContract is Ownable {
    // Information about a staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimedTime;
        uint256 rewardsEarned;
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward token
    IERC20 public rewardToken;

    // Duration for reward distribution (2 years)
    uint256 public constant DURATION = 2 * 365 days;

    // Total rewards allocated for staking
    uint256 public totalRewards;

    // Reward rate per block
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the reward token
    constructor(IERC20 _rewardToken, uint256 _totalRewards) {
        rewardToken = _rewardToken;
        totalRewards = _totalRewards;
        rewardRate = totalRewards / DURATION; // Calculate reward rate per second
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer tokens from staker to contract
        rewardToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastClaimedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        // Claim rewards before unstaking
        claimRewards();

        // Transfer tokens back to staker
        staker.amountStaked -= amount;
        totalStaked -= amount;
        
        rewardToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() public {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        
        require(rewards > 0, "No rewards available");

        staker.rewardsEarned += rewards;
        staker.lastClaimedTime = block.timestamp;

        // Transfer rewards to staker
        rewardToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];

        // Calculate the time since last claimed
        uint256 timeStaked = block.timestamp - staker.lastClaimedTime;
        
        // Calculate rewards based on the staker's share of the total staked
        uint256 earnedRewards = (staker.amountStaked * rewardRate * timeStaked) / (totalStaked);
        
        return earnedRewards;
    }

    // Function to withdraw remaining rewards (for owner)
    function withdrawRemainingRewards() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No remaining rewards to withdraw");
        
        rewardToken.transfer(owner(), balance);
    }
}
```
