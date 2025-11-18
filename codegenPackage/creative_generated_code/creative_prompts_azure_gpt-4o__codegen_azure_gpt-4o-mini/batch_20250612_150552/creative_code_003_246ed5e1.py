"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogtokens-com.pages.dev
Prompt: Write a smart contract in Solidity that locks $SMOG tokens for 90 days upon staking and calculates rewards based on APY, as described in the website's staking mechanism.
Generated: DETERMINISTIC_246ed5e1c4fc3a13
Batch ID: 20250612_150552
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

// Importing required OpenZeppelin contracts for ERC20 interface and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingRewards contract allows users to stake $SMOG tokens and earn rewards
contract StakingRewards is Ownable {
    // State variables
    IERC20 public smogToken; // The $SMOG token contract
    uint256 public constant LOCK_PERIOD = 90 days; // Lock period for staking
    uint256 public apy; // Annual Percentage Yield
    uint256 public totalStaked; // Total amount of tokens staked
    
    struct Stake {
        uint256 amount; // Amount staked
        uint256 stakedAt; // Timestamp when the stake was made
        uint256 rewards; // Accumulated rewards
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Constructor to set the $SMOG token address and APY
    constructor(IERC20 _smogToken, uint256 _apy) {
        smogToken = _smogToken;
        setAPY(_apy);
    }

    // Function to set the APY (only callable by the contract owner)
    function setAPY(uint256 _apy) public onlyOwner {
        apy = _apy;
    }

    // Function to stake $SMOG tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(smogToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.stakedAt = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards based on the staked amount and time
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.stakedAt;
        uint256 yearsStaked = stakingDuration / 365 days;

        // Calculate rewards based on the amount staked and APY
        return (userStake.amount * apy * yearsStaked) / 100; // Rewards calculation
    }

    // Function to unstake $SMOG tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(block.timestamp >= userStake.stakedAt + LOCK_PERIOD, "Tokens are still locked");
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate rewards before resetting the stake
        uint256 rewards = calculateRewards(msg.sender);
        uint256 amountToTransfer = userStake.amount + rewards;

        // Update total staked and user's stake information
        totalStaked -= userStake.amount;
        delete stakes[msg.sender]; // Reset user's stake

        // Transfer the staked tokens and rewards back to the user
        require(smogToken.transfer(msg.sender, amountToTransfer), "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, rewards);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to view user's stake details
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 stakedAt, uint256 rewards) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.stakedAt, calculateRewards(user));
    }
}
```
