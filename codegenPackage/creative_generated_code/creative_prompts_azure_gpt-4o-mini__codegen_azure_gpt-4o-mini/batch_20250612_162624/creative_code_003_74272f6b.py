"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana10x.com
Prompt: Generate a sample code snippet for a smart contract that manages staking rewards with a cap strategy like SOL10X's.
Generated: DETERMINISTIC_74272f6b19c2043e
Batch ID: 20250612_162624
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

// Importing the Ownable contract from OpenZeppelin for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingRewards contract to manage staking and rewards with a cap strategy
contract StakingRewards is Ownable {
    // Struct to store user staking data
    struct Stake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakeTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking data
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Total rewards distributed
    uint256 public totalRewards;

    // The maximum amount of rewards that can be distributed
    uint256 public rewardCap;

    // Reward per second for staking
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize reward cap and reward rate
    constructor(uint256 _rewardCap, uint256 _rewardRate) {
        rewardCap = _rewardCap;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Update total staked and user's stake data
        totalStaked += _amount;
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastStakeTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(_amount > 0, "Amount must be greater than 0");
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update total staked and user's stake data
        totalStaked -= _amount;
        userStake.amount -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate pending rewards for a user
    function calculatePendingRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 timeStaked = block.timestamp - userStake.lastStakeTime;
        uint256 pendingRewards = (userStake.amount * rewardRate * timeStaked) / 1e18; // Adjust for decimals
        return pendingRewards + userStake.rewardDebt;
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        require(totalRewards + pendingRewards <= rewardCap, "Reward cap reached");

        // Update total rewards and user's reward debt
        totalRewards += pendingRewards;
        userStake.rewardDebt = 0; // Reset user's reward debt

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Function to set a new reward cap (only owner)
    function setRewardCap(uint256 _newCap) external onlyOwner {
        require(_newCap > totalRewards, "New cap must be greater than current total rewards");
        rewardCap = _newCap;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
