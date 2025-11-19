"""
Generated Code Metadata:
========================
Original URL: https://handsofgod.app
Prompt: Create a smart contract in Solidity for staking $GHOG tokens in the Sanctum module of the Hand of God protocol. Ensure the contract includes a 6-epoch lock for withdrawals and a 3-epoch lock for rewards.
Generated: DETERMINISTIC_b2de29b6e4eadeca
Batch ID: 20250612_154809
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $GHOG tokens
contract SanctumStaking is Ownable {
    // Token to be staked
    IERC20 public ghogToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Constants for epoch durations
    uint256 public constant EPOCH_DURATION = 1 days; // Duration of an epoch
    uint256 public constant LOCK_EPOCHS_FOR_WITHDRAWAL = 6; // Lock period for withdrawals
    uint256 public constant LOCK_EPOCHS_FOR_REWARDS = 3; // Lock period for rewards

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _ghogToken) {
        ghogToken = _ghogToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(ghogToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens after the lock period
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        require(block.timestamp >= userStake.timestamp + (LOCK_EPOCHS_FOR_WITHDRAWAL * EPOCH_DURATION), "Withdrawal locked");

        userStake.amount -= amount;
        require(ghogToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards after the lock period
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");
        require(block.timestamp >= userStake.timestamp + (LOCK_EPOCHS_FOR_REWARDS * EPOCH_DURATION), "Rewards locked");

        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        userStake.rewards = 0; // Reset rewards after claiming
        require(ghogToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate rewards (placeholder logic)
    function calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        // Example reward calculation: 10% of staked amount per epoch
        uint256 epochsStaked = (block.timestamp - userStake.timestamp) / EPOCH_DURATION;
        return (userStake.amount * 10 / 100) * epochsStaked;
    }

    // Function to get the user's stake information
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 rewards, uint256 timestamp) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.rewards, userStake.timestamp);
    }
}
```
