"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://belegends.pages.dev
Prompt: Create a Solidity contract that integrates `$LEGEND` token staking with additional features for sports-related rewards or fan engagement.
Generated: DETERMINISTIC_995b28ff7361c6c1
Batch ID: 20250612_151301
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

// Importing the ERC20 interface to interact with the LEGEND token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for staking LEGEND tokens and rewarding users with sports-related benefits
contract LegendStaking is Ownable {
    // Struct to hold staking information for each user
    struct Staker {
        uint256 amount;  // Amount of LEGEND tokens staked
        uint256 lastClaimed;  // Timestamp of the last reward claim
        bool isStaking;  // Status of staking
    }

    // Mapping to keep track of each user's staking information
    mapping(address => Staker) public stakers;

    // The ERC20 token used for staking
    IERC20 public legendToken;

    // Reward rate per second (in wei) for staking LEGEND tokens
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the LEGEND token address and reward rate
    constructor(address _legendToken, uint256 _rewardRate) {
        legendToken = IERC20(_legendToken);
        rewardRate = _rewardRate;
    }

    // Function to stake LEGEND tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(legendToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        Staker storage staker = stakers[msg.sender];
        if (staker.isStaking) {
            // Recalculate rewards before updating the staker's amount
            uint256 reward = calculateReward(msg.sender);
            totalRewards += reward;
        } else {
            staker.isStaking = true; // Mark the user as staking
        }

        staker.amount += amount; // Update the staked amount
        staker.lastClaimed = block.timestamp; // Update last claimed timestamp

        emit Staked(msg.sender, amount);
    }

    // Function to unstake LEGEND tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.isStaking, "No stakes found for user");
        require(staker.amount >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        totalRewards += reward;

        // Update staker's details
        staker.amount -= amount;
        if (staker.amount == 0) {
            staker.isStaking = false; // No longer staking if amount is zero
        }

        // Transfer unstaked tokens back to the user
        require(legendToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        Staker storage staker = stakers[msg.sender];
        staker.lastClaimed = block.timestamp; // Update last claimed timestamp
        totalRewards += reward; // Update total rewards

        // Transfer rewards to the user
        // Assuming rewards are paid in LEGEND tokens
        require(legendToken.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        Staker storage staker = stakers[user];
        if (!staker.isStaking) return 0; // No rewards for non-stakers

        uint256 timeStaked = block.timestamp - staker.lastClaimed; // Time since last claim
        return (timeStaked * staker.amount * rewardRate) / 1e18; // Calculate reward
    }

    // Function to set a new reward rate, restricted to the owner
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
