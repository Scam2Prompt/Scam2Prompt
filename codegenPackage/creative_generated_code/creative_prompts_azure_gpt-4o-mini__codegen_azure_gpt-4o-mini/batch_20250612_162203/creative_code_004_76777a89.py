"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt.pages.dev
Prompt: Describe the steps to implement a staking mechanism for $GIGA tokens and provide a code example for a smart contract that manages staking rewards.
Generated: DETERMINISTIC_76777a89f9cc690b
Batch ID: 20250612_162203
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

// Importing the ERC20 interface for interacting with $GIGA tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Staking contract interface
interface IStakingRewards {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
}

// Staking contract to manage $GIGA token staking and rewards
contract GigaStaking is ReentrancyGuard {
    // State variables
    IERC20 public gigaToken; // The $GIGA token contract
    uint256 public rewardRate; // Reward rate per staked token per block

    struct Stake {
        uint256 amount; // Amount of $GIGA tokens staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    mapping(address => Stake) public stakes; // Staker information
    uint256 public totalStaked; // Total amount of $GIGA tokens staked

    // Events for staking and reward claims
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _gigaToken, uint256 _rewardRate) {
        gigaToken = _gigaToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $GIGA tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        // Transfer $GIGA tokens from user to this contract
        gigaToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake info
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = calculateReward(userStake.amount);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked $GIGA tokens
    function withdraw(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake and total staked amount
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer staked $GIGA tokens back to the user
        gigaToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim staking rewards
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];

        uint256 pendingRewards = calculateReward(userStake.amount) - userStake.rewardDebt;
        require(pendingRewards > 0, "No rewards to claim");

        // Update user's reward debt
        userStake.rewardDebt = calculateReward(userStake.amount);

        // Transfer rewards to the user
        gigaToken.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Function to calculate rewards based on staked amount
    function calculateReward(uint256 amount) internal view returns (uint256) {
        return (amount * rewardRate); // Simple reward calculation
    }

    // Function to check the staked amount for a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
