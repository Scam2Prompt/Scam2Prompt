"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olliivveemmaaiinn12893891bndjdbiqw.pages.dev
Prompt: Write a smart contract in Solidity that implements a staking rewards system similar to the "Olive Boost" feature, allowing users to earn 3x rewards for restaking their deposits.
Generated: DETERMINISTIC_87392dab39591431
Batch ID: 20250612_151246
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
 * @title StakingRewards
 * @dev A smart contract for staking and earning boosted rewards.
 */
contract StakingRewards {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalDeposits; // Total deposits in the contract
    uint256 public rewardRate = 1; // Default reward rate
    uint256 public boostedRewardRate = 3; // Boosted reward rate for restaking

    struct Staker {
        uint256 deposit; // Amount deposited by the staker
        uint256 rewards; // Accumulated rewards
        uint256 lastUpdateTime; // Last time rewards were updated
    }

    mapping(address => Staker) public stakers; // Mapping of staker addresses to their data

    // Events
    event Deposited(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 amount);
    event Restaked(address indexed staker, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier updateRewards(address staker) {
        if (stakers[staker].deposit > 0) {
            uint256 timeElapsed = block.timestamp - stakers[staker].lastUpdateTime;
            uint256 newRewards = stakers[staker].deposit * rewardRate * timeElapsed / (1 days);
            stakers[staker].rewards += newRewards;
        }
        stakers[staker].lastUpdateTime = block.timestamp;
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the deployer as owner
    }

    /**
     * @dev Allows users to deposit funds for staking.
     * @param amount The amount to deposit.
     */
    function deposit(uint256 amount) external payable updateRewards(msg.sender) {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount, "Insufficient ETH sent");

        stakers[msg.sender].deposit += amount;
        totalDeposits += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their deposit without claiming rewards.
     */
    function withdraw(uint256 amount) external updateRewards(msg.sender) {
        require(stakers[msg.sender].deposit >= amount, "Insufficient deposit");

        stakers[msg.sender].deposit -= amount;
        totalDeposits -= amount;
        payable(msg.sender).transfer(amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = stakers[msg.sender].rewards;
        require(rewards > 0, "No rewards available");

        stakers[msg.sender].rewards = 0;
        payable(msg.sender).transfer(rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Allows users to restake their deposit for boosted rewards.
     */
    function restake() external updateRewards(msg.sender) {
        require(stakers[msg.sender].deposit > 0, "No deposit to restake");

        rewardRate = boostedRewardRate; // Apply boosted reward rate

        emit Restaked(msg.sender, stakers[msg.sender].deposit);
    }

    /**
     * @dev Fallback function to handle unintentional ETH transfers.
     */
    fallback() external payable {
        revert("Direct deposits not allowed");
    }

    /**
     * @dev Receive function to handle ETH transfers.
     */
    receive() external payable {
        revert("Direct deposits not allowed");
    }
}
```
