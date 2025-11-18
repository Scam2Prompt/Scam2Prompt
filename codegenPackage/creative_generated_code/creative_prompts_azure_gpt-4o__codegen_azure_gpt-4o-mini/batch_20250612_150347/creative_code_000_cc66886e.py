"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchaineden.pages.dev
Prompt: Write a smart contract for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, incorporating double staking rewards as described in the tokenomics.
Generated: DETERMINISTIC_cc66886e27ed59e4
Batch ID: 20250612_150347
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the PEPU token
interface IPEPUToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for $PEPU tokens
contract PepuStaking is Ownable {
    // PEPU Token contract instance
    IPEPUToken public pepuToken;

    // Struct to hold user staking data
    struct Stake {
        uint256 amount; // Amount staked
        uint256 reward; // Rewards accumulated
        uint256 timestamp; // Timestamp of the last stake
    }

    // Mapping of user address to their stake
    mapping(address => Stake) public stakes;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the PEPU token address
    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid PEPU token address");
        pepuToken = IPEPUToken(_pepuToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake data
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards (double staking rewards)
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);
        userStake.reward += reward; // Accumulate rewards
        uint256 totalAmount = userStake.amount + userStake.reward;

        // Reset user's stake
        userStake.amount = 0;
        userStake.reward = 0;

        // Transfer back the staked amount and rewards
        require(pepuToken.transfer(msg.sender, totalAmount), "Transfer failed");

        emit Unstaked(msg.sender, totalAmount, reward);
    }

    // Function to claim rewards without unstaking
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);
        userStake.reward += reward; // Accumulate rewards
        userStake.timestamp = block.timestamp; // Update timestamp for rewards calculation

        // Transfer the rewards to the user
        require(pepuToken.mint(msg.sender, userStake.reward), "Minting failed");

        emit RewardsClaimed(msg.sender, userStake.reward);
        userStake.reward = 0; // Reset rewards after claiming
    }

    // Function to calculate rewards based on amount staked and staking duration
    function calculateReward(uint256 amount, uint256 lastTimestamp) internal view returns (uint256) {
        uint256 duration = block.timestamp - lastTimestamp; // Duration in seconds
        uint256 rewardRate = 1e18; // Example reward rate (1 PEPU per second per token staked)
        uint256 reward = (amount * duration * rewardRate) / 1e18; // Calculate reward based on duration
        return reward;
    }
}
```
