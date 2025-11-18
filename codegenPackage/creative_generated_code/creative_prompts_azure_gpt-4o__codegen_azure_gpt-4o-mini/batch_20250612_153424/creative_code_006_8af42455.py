"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freedumfighert.pages.dev
Prompt: Develop a smart contract to manage staking pools for FreeDum Fighters, ensuring rewards are distributed according to the project's tokenomics.
Generated: DETERMINISTIC_8af4245502ebf0f5
Batch ID: 20250612_153424
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

// Import OpenZeppelin's ERC20 contract for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingPool contract to manage staking and reward distribution
contract StakingPool is Ownable {
    // Token being staked
    IERC20 public immutable stakingToken;
    
    // Reward token to distribute
    IERC20 public immutable rewardToken;

    // Struct to keep track of user's staked amount and rewards
    struct Staker {
        uint256 amountStaked;
        uint256 rewards;
        uint256 lastStakedTime;
    }

    // Mapping of user addresses to their staking data
    mapping(address => Staker) public stakers;

    // Total staked amount in the pool
    uint256 public totalStaked;
    
    // Reward rate in reward tokens per second per staked token
    uint256 public rewardRate;

    // Event emitted when rewards are updated
    event RewardsUpdated(uint256 newRewardRate);

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the staking and reward tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _initialRewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _initialRewardRate;
    }

    // Function to update the reward rate
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
        emit RewardsUpdated(newRewardRate);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount should be greater than 0");

        // Update rewards for the user before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update the staker's data
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].lastStakedTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update rewards before withdrawing
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Update staker's data
        staker.amountStaked -= amount;
        totalStaked -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        
        // Calculate the rewards to be claimed
        uint256 rewardsToClaim = stakers[msg.sender].rewards;
        require(rewardsToClaim > 0, "No rewards available to claim");
        
        // Reset user's rewards to zero
        stakers[msg.sender].rewards = 0;

        // Transfer reward tokens to the user
        rewardToken.transfer(msg.sender, rewardsToClaim);

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        
        // Calculate elapsed time since last stake and update rewards
        uint256 elapsedTime = block.timestamp - staker.lastStakedTime;
        staker.rewards += (staker.amountStaked * rewardRate * elapsedTime);

        // Update the last staked time to the current block timestamp
        staker.lastStakedTime = block.timestamp;
    }
}
```
