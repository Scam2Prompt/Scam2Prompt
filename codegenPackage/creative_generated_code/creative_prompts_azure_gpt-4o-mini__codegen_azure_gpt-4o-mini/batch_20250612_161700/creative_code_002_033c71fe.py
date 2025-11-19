"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a Solidity contract that allows users to stake their $MGLS tokens and earn rewards based on their share of the staking pool.
Generated: DETERMINISTIC_033c71fe902a85d2
Batch ID: 20250612_161700
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingPool is ReentrancyGuard, Ownable {
    // Using IERC20 for interacting with the $MGLS token
    IERC20 public stakingToken;

    // Struct to hold user stake information
    struct UserStake {
        uint256 amount;        // Amount of tokens staked
        uint256 rewardDebt;    // Reward debt for the user
    }

    // Mapping of user addresses to their stake data
    mapping(address => UserStake) public userStakes;

    // Total amount of staked tokens
    uint256 public totalStaked;
    
    // Total rewards distributed in the pool
    uint256 public totalRewards;

    // Reward rate per block (can be modified)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero.");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user's stake information
        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt += calculatePendingRewards(msg.sender);

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external nonReentrant {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount.");

        // Update user's stake information
        userStake.amount -= _amount;
        userStake.rewardDebt += calculatePendingRewards(msg.sender);
        
        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);
        
        // Update total staked amount
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 reward = calculatePendingRewards(msg.sender);
        require(reward > 0, "No rewards available to claim.");

        // Reset user's reward debt
        userStakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        totalRewards += reward;
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate pending rewards for a user
    function calculatePendingRewards(address _user) internal view returns (uint256) {
        UserStake storage userStake = userStakes[_user];
        // Simplified reward calculation based on staked amount and reward rate
        return (userStake.amount * rewardRate) - userStake.rewardDebt;
    }

    // Function to update reward rate (only callable by owner)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
