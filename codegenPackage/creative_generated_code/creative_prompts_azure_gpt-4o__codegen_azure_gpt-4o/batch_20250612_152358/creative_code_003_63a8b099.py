"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonnect-2024.pages.dev
Prompt: Create a smart contract for staking TON tokens using the Tonstakers platform, ensuring compatibility with the TON ecosystem.
Generated: DETERMINISTIC_63a8b099f9e7b47b
Batch ID: 20250612_152358
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

/**
 * @title TON Token Staking Contract
 * @notice This contract allows users to stake TON tokens on the Tonstakers platform.
 * Users can deposit, withdraw, and earn rewards based on their staked TON tokens.
 * @dev Ensure compatibility with the TON ecosystem and adhere to best practices.
 */
contract TonStaking {
    // Address of TON token contract
    IERC20 public tonToken;

    // Structure to store staking details for a user
    struct Stake {
        uint256 amount;         // Amount of TON tokens staked
        uint256 rewardDebt;     // Reward debt from previous transactions
        uint256 stakeTimestamp; // Timestamp of when the stake was created
    }

    // Mapping of user address to their staking data
    mapping(address => Stake) public stakes;

    // Total amount of TON tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate in TON tokens per second
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _tonToken Address of the TON token contract.
     * @param _rewardRate Reward rate in TON tokens per second.
     */
    constructor(IERC20 _tonToken, uint256 _rewardRate) {
        require(address(_tonToken) != address(0), "Invalid TON token address");
        tonToken = _tonToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure the user has an active stake.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No active stake found");
        _;
    }

    /**
     * @dev Function to calculate the pending reward for a user.
     * @param user Address of the user.
     * @return Pending reward in TON tokens.
     */
    function pendingReward(address user) public view returns (uint256) {
        Stake memory stake = stakes[user];
        if (stake.amount == 0) {
            return 0;
        }
        uint256 stakedDuration = block.timestamp - stake.stakeTimestamp;
        return (stake.amount * stakedDuration * rewardRate) / 1e18;
    }

    /**
     * @dev Function to stake TON tokens.
     * @param amount Amount of TON tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer TON tokens from the user to the contract
        require(tonToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking details for the user
        uint256 reward = pendingReward(msg.sender);
        stakes[msg.sender].rewardDebt += reward;
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakeTimestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked TON tokens.
     */
    function withdraw() external hasStake {
        // Calculate reward and total amount to withdraw
        uint256 reward = pendingReward(msg.sender) + stakes[msg.sender].rewardDebt;
        uint256 withdrawAmount = stakes[msg.sender].amount;

        // Reset user stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        stakes[msg.sender].stakeTimestamp = 0;

        // Update total staked amount
        totalStaked -= withdrawAmount;

        // Transfer TON tokens and reward to the user
        require(tonToken.transfer(msg.sender, withdrawAmount), "Withdraw token transfer failed");
        if (reward > 0) {
            require(tonToken.transfer(msg.sender, reward), "Reward token transfer failed");
            emit RewardPaid(msg.sender, reward);
        }

        emit Withdrawn(msg.sender, withdrawAmount);
    }

    /**
     * @dev Function to update reward rate.
     * @param _rewardRate New reward rate in TON tokens per second.
     */
    function updateRewardRate(uint256 _rewardRate) external {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }
}

// IERC20 interface for TON token compatibility
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
