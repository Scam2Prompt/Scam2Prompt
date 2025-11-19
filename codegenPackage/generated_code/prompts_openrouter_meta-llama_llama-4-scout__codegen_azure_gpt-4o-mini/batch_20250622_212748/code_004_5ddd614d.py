"""
Generated Code Metadata:
========================
Original URL: https://jamecomfi.pages.dev
Prompt: Create a blockchain-based staking system with features like token claiming, airdrop distribution, and staking rewards tracking.
Generated: DETERMINISTIC_5ddd614d854738f5
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract interface
interface IStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function claimRewards() external;
}

// Main Staking Contract
contract StakingSystem is Ownable {
    // Token used for staking
    IERC20 public stakingToken;
    
    // Struct to hold user staking data
    struct UserStake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastClaimed; // Last time rewards were claimed
    }

    // Mapping of user addresses to their staking data
    mapping(address => UserStake) public userStakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    
    // Constructor to initialize the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user stake data
        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt += calculatePendingRewards(msg.sender);
        userStake.lastClaimed = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user stake data
        userStake.rewardDebt += calculatePendingRewards(msg.sender);
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim staking rewards
    function claimRewards() external {
        UserStake storage userStake = userStakes[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        
        require(pendingRewards > 0, "No rewards to claim");

        // Update user reward debt
        userStake.rewardDebt += pendingRewards;
        userStake.lastClaimed = block.timestamp;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Internal function to calculate pending rewards for a user
    function calculatePendingRewards(address user) internal view returns (uint256) {
        UserStake storage userStake = userStakes[user];
        uint256 timeStaked = block.timestamp - userStake.lastClaimed;
        return (userStake.amount * rewardRate * timeStaked) / 1e18; // Adjust for reward rate precision
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
