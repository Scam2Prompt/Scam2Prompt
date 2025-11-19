"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-d.pages.dev
Prompt: How can I implement a staking mechanism for the DOGE20 token using Ethereum smart contracts to earn passive rewards?
Generated: DETERMINISTIC_49428dd268c592c6
Batch ID: 20250612_161500
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

// Import the ERC20 interface for DOGE20 token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20Staking is ReentrancyGuard, Ownable {
    // Structure to hold user staking data
    struct Stake {
        uint256 amount;         // Amount of DOGE20 staked
        uint256 rewardDebt;     // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping for user stakes
    mapping(address => Stake) public stakes;

    // Total amount of DOGE20 staked
    uint256 public totalStaked;

    // The DOGE20 token contract
    IERC20 public doge20Token;

    // Reward rate per second (in tokens)
    uint256 public rewardRate;

    // Event for staking
    event Staked(address indexed user, uint256 amount);

    // Event for unstaking
    event Unstaked(address indexed user, uint256 amount);

    // Event for claiming rewards
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set up the staking contract
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    // Modifier to check if the user has staked
    modifier hasStaked() {
        require(stakes[msg.sender].amount > 0, "No stake found");
        _;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer DOGE20 tokens from the sender to the contract
        doge20Token.transferFrom(msg.sender, address(this), amount);

        // Update user's stake data
        Stake storage stakeData = stakes[msg.sender];
        stakeData.amount += amount;
        stakeData.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external nonReentrant hasStaked {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        uint256 pendingReward = calculateReward(msg.sender);
        if (pendingReward > 0) {
            claimReward(); // Automatically claim the reward
        }

        // Update user's stake data
        stakeData.amount -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens back to the user
        doge20Token.transfer(msg.sender, amount);

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() public nonReentrant hasStaked {
        uint256 pendingReward = calculateReward(msg.sender);
        require(pendingReward > 0, "No rewards available");

        // Update user's reward debt
        stakes[msg.sender].rewardDebt += pendingReward;

        // Transfer rewards to user
        doge20Token.transfer(msg.sender, pendingReward);

        // Emit reward claimed event
        emit RewardClaimed(msg.sender, pendingReward);
    }

    // Internal function to calculate rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage stakeData = stakes[user];
        uint256 stakedDuration = block.timestamp - stakeData.lastStakedTime;
        uint256 reward = (stakeData.amount * rewardRate * stakedDuration) / 1e18; // Adjust for decimals
        return reward - stakeData.rewardDebt; // Adjust for already claimed rewards
    }

    // Function to view total staked amount
    function viewTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
