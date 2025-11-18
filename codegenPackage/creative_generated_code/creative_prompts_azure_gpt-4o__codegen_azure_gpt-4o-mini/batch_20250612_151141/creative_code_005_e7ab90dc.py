"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Provide code to implement a staking mechanism for CRUDO tokens, allowing token holders to earn passive income, as described in the Crudo Protocol roadmap.
Generated: DETERMINISTIC_e7ab90dcffd6a0b4
Batch ID: 20250612_151141
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

// Interface for the CRUDO token
interface ICRUDOToken {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for CRUDO tokens
contract CRUDOStaking {
    // Token details
    ICRUDOToken public crudoToken;
    uint256 public rewardRate; // Reward rate per staked token per block

    // Staker details
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt;   // Reward debt for the staker
        uint256 lastStakedBlock; // Last block number when the user staked
    }

    // Mapping of staker addresses to their details
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(ICRUDOToken _crudoToken, uint256 _rewardRate) {
        crudoToken = _crudoToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(crudoToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update staker's reward debt
        if (staker.amountStaked > 0) {
            uint256 pendingReward = calculateReward(msg.sender);
            staker.rewardDebt += pendingReward;
        }

        staker.amountStaked += amount;
        staker.lastStakedBlock = block.number;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];

        require(amount > 0, "Cannot withdraw 0 tokens");
        require(staker.amountStaked >= amount, "Insufficient staked balance");

        // Update staker's reward debt
        uint256 pendingReward = calculateReward(msg.sender);
        staker.rewardDebt += pendingReward;

        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(crudoToken.transferFrom(address(this), msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim accumulated rewards
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt += reward;

        // Transfer reward to the user (assume CRUDO token can send rewards)
        require(crudoToken.transferFrom(address(this), msg.sender, reward), "Reward transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staked amount and time
    function calculateReward(address user) internal view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 blocksStaked = block.number - staker.lastStakedBlock;
        return (staker.amountStaked * rewardRate * blocksStaked) / 1e18; // Adjust reward calculation as needed
    }

    // Function to check total staked tokens
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to check staker's details
    function getStakerInfo(address user) external view returns (uint256, uint256) {
        Staker storage staker = stakers[user];
        return (staker.amountStaked, staker.rewardDebt);
    }
}
```
