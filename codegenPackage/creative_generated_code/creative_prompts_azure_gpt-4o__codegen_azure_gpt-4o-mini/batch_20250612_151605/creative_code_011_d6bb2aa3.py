"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmpeppe.web.app
Prompt: Write a Solidity smart contract for a tiered staking system that rewards users based on the amount of $MPEPE tokens staked and the duration of staking.
Generated: DETERMINISTIC_d6bb2aa366fc94d9
Batch ID: 20250612_151605
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

// Importing OpenZeppelin's SafeERC20 library and IERC20 interface for token handling
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TieredStaking is Ownable {
    using SafeERC20 for IERC20;

    // Structure to hold staking details
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 startTime;     // Timestamp when the stake was made
        uint256 tier;          // Tier level of the staker
    }

    // Mapping from user address to their stake details
    mapping(address => Stake) public stakes;

    // Staking token
    IERC20 public stakingToken;

    // Reward multipliers based on tiers
    uint256[] public tierMultipliers = [1, 2, 3]; // Example multipliers for 3 tiers

    // Events
    event Staked(address indexed user, uint256 amount, uint256 tier);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount, uint256 tier) external {
        require(amount > 0, "Amount must be greater than zero");
        require(tier < tierMultipliers.length, "Invalid tier");

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update user's stake details
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            tier: tier
        });

        emit Staked(msg.sender, amount, tier);
    }

    // Function to calculate rewards based on staking duration and tier
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];

        require(userStake.amount > 0, "No active stake");
        
        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Simple reward calculation: amount * tier multiplier * duration in seconds
        // Assuming rewards are calculated per second
        return userStake.amount * tierMultipliers[userStake.tier] * stakingDuration;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No active stake");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        // Reset stake details
        delete stakes[msg.sender];

        // Transfer original staked tokens back to the user
        stakingToken.safeTransfer(msg.sender, userStake.amount);
        
        // Transfer rewards to the user (implementing a mechanism to handle rewards distribution)
        // For simplicity, we're assuming rewards are paid out in a stable manner
        // In production, consider using a separate reward token contract or pool
        if (reward > 0) {
            // Transfer the reward (could be in a different token)
            stakingToken.safeTransfer(msg.sender, reward); // For example, reward could be the same token
        }

        emit Unstaked(msg.sender, userStake.amount, reward);
    }
}
```
