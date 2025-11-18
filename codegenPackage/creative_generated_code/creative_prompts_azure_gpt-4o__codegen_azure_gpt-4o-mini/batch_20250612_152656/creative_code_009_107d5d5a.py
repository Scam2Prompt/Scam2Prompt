"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testai-qhn.pages.dev
Prompt: Design a staking pool system in Solidity that supports multiple lock terms, compounding rewards, and tier boosts, similar to the staking pools described on the Solidus AI Tech webpage.
Generated: DETERMINISTIC_107d5d5a6c31d5d7
Batch ID: 20250612_152656
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The StakingPool contract allows users to stake tokens with multiple lock terms
// and compounding rewards, integrated with tier boosts for enhanced staking benefits.
contract StakingPool is ReentrancyGuard, Ownable {
    // Structure to hold information about each staker
    struct StakerInfo {
        uint256 amountStaked; // Amount of tokens staked
        uint256 startTime; // Start time of the stake
        uint256 lockTerm; // Duration for which tokens are locked
        uint256 tier; // Tier level of the staker
        bool isActive; // Indicates if the stake is active
    }

    // Variables
    IERC20 public stakingToken; // ERC20 token being staked
    uint256 public totalStaked; // Total tokens staked in the pool
    uint256 public rewardRate; // Reward rate per second
    mapping(address => StakerInfo) public stakers; // Mapping of staker information

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockTerm, uint256 tier);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking pool
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens with a specified lock term and tier
    function stake(uint256 amount, uint256 lockTerm, uint256 tier) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(lockTerm > 0, "Lock term must be greater than zero");
        require(tier > 0, "Tier must be greater than zero");

        StakerInfo storage staker = stakers[msg.sender];

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        staker.amountStaked += amount;
        staker.startTime = block.timestamp;
        staker.lockTerm = lockTerm;
        staker.tier = tier;
        staker.isActive = true;

        totalStaked += amount;

        emit Staked(msg.sender, amount, lockTerm, tier);
    }

    // Function to calculate accrued rewards based on stake duration and tier
    function calculateRewards(address user) public view returns (uint256) {
        StakerInfo storage staker = stakers[user];
        if (!staker.isActive) {
            return 0;
        }

        uint256 stakedDuration = block.timestamp - staker.startTime;
        uint256 rewards = (staker.amountStaked * rewardRate * stakedDuration) / 1e18;

        return rewards * staker.tier; // Apply tier boost
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset start time to prevent double claiming
        stakers[msg.sender].startTime = block.timestamp;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to unstake tokens after the lock term has expired
    function unstake() external nonReentrant {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.isActive, "No active stake");
        require(block.timestamp >= staker.startTime + staker.lockTerm, "Lock term not expired");

        uint256 amountToUnstake = staker.amountStaked;

        // Reset staker's information
        staker.amountStaked = 0;
        staker.isActive = false;

        totalStaked -= amountToUnstake;

        // Transfer staked tokens back to the user
        stakingToken.transfer(msg.sender, amountToUnstake);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to update the reward rate (only callable by the owner)
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakingToken, "Cannot withdraw staked tokens");
        token.transfer(msg.sender, amount);
    }
}
```
