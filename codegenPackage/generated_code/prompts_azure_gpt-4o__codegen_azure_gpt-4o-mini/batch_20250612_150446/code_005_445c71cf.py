"""
Generated Code Metadata:
========================
Original URL: https://apphubs.pages.dev
Prompt: Develop a decentralized staking mechanism for tokens, allowing users to earn from their assets, as outlined in the "Stake tokens" section of the Synchronizer Panel.
Generated: DETERMINISTIC_445c71cfb23a063d
Batch ID: 20250612_150446
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Decentralized Staking Mechanism
 * @dev This contract allows users to stake ERC20 tokens and earn rewards.
 */
contract StakingContract is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The ERC20 token being staked
    IERC20 public stakingToken;

    // Reward rate in tokens per second
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract
     * @param _stakingToken Address of the ERC20 token to be staked
     * @param _rewardRate Reward rate in tokens per second
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens along with rewards
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        totalRewards += reward;

        // Reset user's stake
        uint256 amount = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens and rewards back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Withdrawn(msg.sender, amount, reward);
    }

    /**
     * @dev Calculates the reward for a user based on their stake
     * @param user Address of the user
     * @return The calculated reward
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        return (stakedDuration * rewardRate * userStake.amount) / 1e18; // Adjust for precision
    }

    /**
     * @dev Allows the owner to withdraw any tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transfer(owner(), amount), "Transfer failed");
    }
}
```
