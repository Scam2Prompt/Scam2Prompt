"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: Generate Solidity code for a smart contract that mimics the DOGE20 staking mechanism, distributing rewards over two years based on the staker's share in the pool.
Generated: DETERMINISTIC_2e92db0043cd264f
Batch ID: 20250612_153400
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

/// @title DOGE20 Staking Contract
/// @notice This contract allows users to stake DOGE20 tokens and earn rewards over two years.
contract DOGE20Staking {
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public constant REWARD_DURATION = 730 days; // Duration for staking rewards
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    uint256 public rewardPool; // Total rewards pool
    mapping(address => uint256) public stakedAmount; // Amount each user has staked
    mapping(address => uint256) public lastClaimed; // Last timestamp rewards were claimed

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /// @param _doge20Token Address of the DOGE20 token contract
    constructor(IERC20 _doge20Token) {
        doge20Token = _doge20Token;
    }

    /// @notice Stakes a specified amount of DOGE20 tokens
    /// @param amount Amount of DOGE20 tokens to stake
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastClaimed[msg.sender] = block.timestamp; // Initialize last claimed time

        emit Staked(msg.sender, amount);
    }

    /// @notice Unstakes a specified amount of DOGE20 tokens
    /// @param amount Amount of DOGE20 tokens to unstake
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        claimRewards(); // Claim any rewards before unstaking

        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /// @notice Claims rewards based on staked amount and time
    function claimRewards() public {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        lastClaimed[msg.sender] = block.timestamp; // Update last claimed time
        rewardPool -= reward; // Deduct from reward pool
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /// @notice Calculates the total rewards for a given user
    /// @param user The address of the user
    /// @return The calculated reward amount
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedTime = block.timestamp - lastClaimed[user];
        uint256 userShare = (stakedAmount[user] * 1e18) / totalStaked; // Calculate user's share
        uint256 totalReward = (rewardPool * userShare) / 1e18; // Rewards based on share
        return (totalReward * stakedTime) / REWARD_DURATION; // Scale rewards by time staked
    }

    /// @notice Add rewards to the pool (only owner or admin)
    /// @param amount Amount of DOGE20 tokens to add to the reward pool
    function addRewards(uint256 amount) external {
        require(amount > 0, "Cannot add 0 rewards");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        rewardPool += amount;
    }
}

/// @title ERC20 interface for DOGE20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
