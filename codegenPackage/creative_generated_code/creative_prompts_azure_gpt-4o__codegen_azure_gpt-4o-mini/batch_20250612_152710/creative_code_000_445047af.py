"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a smart contract in Solidity for staking AITECH tokens with compounding rewards, similar to the staking pools described on the Solidus AI Tech platform. Include parameters for reward composition, lock term, and investor tier boosts.
Generated: DETERMINISTIC_445047af36da93a6
Batch ID: 20250612_152710
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

// Import OpenZeppelin contracts for security and functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/// @title AITECH Staking Contract
/// @dev This contract allows users to stake AITECH tokens and earn compounded rewards.
contract AITECHStaking is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public aitechToken; // The AITECH token contract
    uint256 public totalStaked; // Total amount of AITECH tokens staked
    uint256 public rewardRate; // Reward rate per second
    uint256 public lockDuration; // Duration for which funds are locked

    struct UserStake {
        uint256 amount; // Amount staked by the user
        uint256 rewardDebt; // Amount of rewards already claimed
        uint256 lastClaimedTime; // Last time rewards were claimed
        uint256 tierBoost; // Tier boost for rewards
    }

    mapping(address => UserStake) public userStakes; // User stakes mapping

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier hasStaked() {
        require(userStakes[msg.sender].amount > 0, "No stakes found.");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _aitechToken, uint256 _rewardRate, uint256 _lockDuration) {
        aitechToken = _aitechToken;
        rewardRate = _rewardRate; // Set reward rate
        lockDuration = _lockDuration; // Set lock duration
    }

    /// @notice Stake AITECH tokens
    /// @param _amount Amount of tokens to stake
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero.");
        
        // Update user's stake
        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount = userStake.amount.add(_amount);
        userStake.tierBoost = calculateTierBoost(msg.sender); // Calculate tier boost
        userStake.lastClaimedTime = block.timestamp;

        totalStaked = totalStaked.add(_amount);
        aitechToken.transferFrom(msg.sender, address(this), _amount); // Transfer tokens to contract
        
        emit Staked(msg.sender, _amount);
    }

    /// @notice Unstake AITECH tokens
    /// @param _amount Amount of tokens to unstake
    function unstake(uint256 _amount) external hasStaked {
        UserStake storage userStake = userStakes[msg.sender];
        require(block.timestamp >= userStake.lastClaimedTime.add(lockDuration), "Funds are locked.");
        require(userStake.amount >= _amount, "Insufficient staked amount.");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        userStake.rewardDebt = userStake.rewardDebt.add(rewards); // Update reward debt

        userStake.amount = userStake.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        aitechToken.transfer(msg.sender, _amount); // Transfer tokens back to user

        emit Unstaked(msg.sender, _amount);
    }

    /// @notice Claim rewards earned
    function claimRewards() external hasStaked {
        UserStake storage userStake = userStakes[msg.sender];

        // Calculate total rewards
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim.");

        userStake.rewardDebt = userStake.rewardDebt.add(rewards); // Update reward debt
        userStake.lastClaimedTime = block.timestamp; // Update last claimed time
        aitechToken.transfer(msg.sender, rewards); // Send rewards to user

        emit RewardClaimed(msg.sender, rewards);
    }

    /// @notice Calculate rewards based on the user's stake and reward rate
    /// @param _user Address of the user
    /// @return Total calculated rewards
    function calculateRewards(address _user) public view returns (uint256) {
        UserStake memory userStake = userStakes[_user];
        uint256 timeStaked = block.timestamp.sub(userStake.lastClaimedTime);
        uint256 baseReward = timeStaked.mul(rewardRate).mul(userStake.amount).div(1e18); // Base reward calculation
        uint256 boostedReward = baseReward.mul(userStake.tierBoost).div(100); // Apply tier boost

        return boostedReward.sub(userStake.rewardDebt); // Total rewards minus already claimed rewards
    }

    /// @notice Calculate the tier boost for rewards (stub implementation)
    /// @param _user Address of the user
    /// @return Tier boost percentage
    function calculateTierBoost(address _user) internal view returns (uint256) {
        // Placeholder for tier calculation logic (should be updated based on actual tiers)
        return 100; // 100% boost for demonstration (1x)
    }
}
```
