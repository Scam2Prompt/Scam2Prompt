"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lynexfl.org
Prompt: Develop a staking mechanism for Lynex FI that allows users to stake tokens and earn passive income without deposit or withdrawal fees. Include security measures to ensure funds remain under user control.
Generated: DETERMINISTIC_aa36f386e71fd83b
Batch ID: 20250612_150417
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

// Importing OpenZeppelin's ReentrancyGuard to prevent reentrancy attacks
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
// Importing OpenZeppelin's SafeERC20 for safe token operations
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
// Importing OpenZeppelin's Ownable contract to restrict access to contract functions
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Lynex FI
contract LynexFiStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token to be staked
    IERC20 public stakingToken;

    // Structure to hold user stake information
    struct UserStake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their stake information
    mapping(address => UserStake) public userStakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per token staked per block (can be adjusted)
    uint256 public rewardRate = 1e18; // Example reward rate (adjust as needed)

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Update user's stake information
        UserStake storage user = userStakes[msg.sender];
        user.amount += _amount;
        totalStaked += _amount;

        // Transfer the staking tokens from user to the contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    // Function to calculate the reward for a user
    function calculateReward(address _user) internal view returns (uint256) {
        UserStake storage user = userStakes[_user];
        return (user.amount * rewardRate) / 1e18 - user.rewardDebt;
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update user's reward debt
        userStakes[msg.sender].rewardDebt += reward;

        // Transfer the reward to the user
        stakingToken.safeTransfer(msg.sender, reward);

        // Emit event
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external nonReentrant {
        UserStake storage user = userStakes[msg.sender];
        require(user.amount >= _amount, "Not enough staked tokens");

        // Update total staked and user's stake amount
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer the staked tokens back to the user
        stakingToken.safeTransfer(msg.sender, _amount);

        // Emit event
        emit Withdrawn(msg.sender, _amount);
    }

    // Function to set reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to view total staked amount
    function totalStakedAmount() external view returns (uint256) {
        return totalStaked;
    }

    // Function to view user's staked amount
    function userStakedAmount(address _user) external view returns (uint256) {
        return userStakes[_user].amount;
    }
}
```
