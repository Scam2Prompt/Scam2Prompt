"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaicats-claim.pages.dev
Prompt: Create a smart contract in Solidity for staking $KAI tokens in the "KAI Staking Pond" with reward calculations based on the current reward percentage.
Generated: DETERMINISTIC_ed33f1e7ffeaa735
Batch ID: 20250612_151310
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
 * @title KAI Staking Pond
 * @dev A smart contract for staking KAI tokens and earning rewards based on a dynamic reward percentage.
 */
contract KAIStakingPond {
    // Token interface for interacting with KAI token contract
    IERC20 public kaiToken;

    // Reward percentage (in basis points, e.g., 500 = 5%)
    uint256 public rewardPercentage;

    // Struct to track user staking information
    struct Stake {
        uint256 amount; // Staked amount
        uint256 timestamp; // Timestamp of staking
    }

    // Mapping to store stakes of users
    mapping(address => Stake) public stakes;

    // Events
    event StakeDeposited(address indexed user, uint256 amount);
    event StakeWithdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with token address and reward percentage.
     * @param _kaiToken Address of the KAI token contract.
     * @param _rewardPercentage Initial reward percentage (in basis points).
     */
    constructor(address _kaiToken, uint256 _rewardPercentage) {
        require(_kaiToken != address(0), "Invalid token address");
        require(_rewardPercentage > 0 && _rewardPercentage <= 10000, "Invalid reward percentage");

        kaiToken = IERC20(_kaiToken);
        rewardPercentage = _rewardPercentage;
    }

    /**
     * @dev Modifier to check if the caller has an active stake.
     */
    modifier hasActiveStake() {
        require(stakes[msg.sender].amount > 0, "No active stake found");
        _;
    }

    /**
     * @dev Stake KAI tokens into the staking pond.
     * @param _amount Amount of KAI tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Transfer KAI tokens to the contract
        require(kaiToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit StakeDeposited(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked KAI tokens along with calculated rewards.
     */
    function withdraw() external hasActiveStake {
        Stake storage userStake = stakes[msg.sender];

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate reward based on the staking duration and reward percentage
        uint256 reward = (userStake.amount * rewardPercentage * stakingDuration) / (365 days * 10000);

        // Amount to return (staked amount + reward)
        uint256 totalAmount = userStake.amount + reward;

        // Reset user stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked amount and reward to the user
        require(kaiToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit StakeWithdrawn(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Update the reward percentage by the contract owner.
     * @param _newRewardPercentage New reward percentage (in basis points).
     */
    function updateRewardPercentage(uint256 _newRewardPercentage) external {
        require(_newRewardPercentage > 0 && _newRewardPercentage <= 10000, "Invalid reward percentage");

        rewardPercentage = _newRewardPercentage;
    }
}

// Minimal IERC20 interface for token interaction
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
