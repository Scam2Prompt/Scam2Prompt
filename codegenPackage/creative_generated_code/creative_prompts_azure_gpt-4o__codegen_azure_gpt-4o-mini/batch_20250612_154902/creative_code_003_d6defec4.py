"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudo-protocol.xyz
Prompt: Write a Solidity contract that implements a staking mechanism for CRUDO tokens, allowing users to lock their tokens and earn passive income based on a predefined reward rate.
Generated: DETERMINISTIC_d6defec47971cd40
Batch ID: 20250612_154902
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

// Importing OpenZeppelin's ERC20 interface to interact with the CRUDO token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Staking Contract for CRUDO tokens
contract StakingContract is ReentrancyGuard {
    // Token interface
    IERC20 public crudoToken;

    // Struct to hold information about each user's stake
    struct Stake {
        uint256 amount;     // Amount of tokens staked
        uint256 rewardDebt; // Amount of rewards that have been distributed
        uint256 lastStakedAt; // Timestamp of the last stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward rate in tokens per second
    uint256 public rewardRate;
    
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the CRUDO token address and reward rate
    constructor(IERC20 _crudoToken, uint256 _rewardRate) {
        require(address(_crudoToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        crudoToken = _crudoToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        
        // Transfer tokens from user to this contract
        crudoToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the total staked amount
        totalStaked += amount;

        // Update user's stake information
        userStake.amount += amount;
        userStake.rewardDebt += calculateReward(userStake.amount, userStake.lastStakedAt);
        userStake.lastStakedAt = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update reward and user stake
        userStake.rewardDebt += calculateReward(userStake.amount, userStake.lastStakedAt);
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        crudoToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];

        uint256 reward = calculateReward(userStake.amount, userStake.lastStakedAt);
        require(reward > 0, "No rewards to claim");

        // Reset last stake time
        userStake.lastStakedAt = block.timestamp;
        userStake.rewardDebt += reward;

        // Transfer rewards to user
        crudoToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate the reward based on stake and time
    function calculateReward(uint256 amount, uint256 lastStakedAt) internal view returns (uint256) {
        if (lastStakedAt == 0) return 0; // No previous stake time
        uint256 duration = block.timestamp - lastStakedAt; // Calculate duration since last stake
        return (amount * rewardRate * duration) / 1e18; // Return calculated reward
    }

    // Function to get the user's current stake and rewards
    function getUserInfo(address user) external view returns (uint256 stakedAmount, uint256 pendingReward) {
        Stake storage userStake = stakes[user];
        stakedAmount = userStake.amount;
        pendingReward = calculateReward(userStake.amount, userStake.lastStakedAt);
    }
}
```
