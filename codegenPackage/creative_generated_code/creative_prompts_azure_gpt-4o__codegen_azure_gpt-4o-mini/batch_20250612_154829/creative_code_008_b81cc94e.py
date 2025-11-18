"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9eth.eu
Prompt: Provide an example of a staking mechanism in Solidity that offers flexible lock periods and a fixed annual yield, inspired by the staking features on the site.
Generated: DETERMINISTIC_b81cc94e3d3bc19e
Batch ID: 20250612_154829
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

// Staking contract to manage flexible lock periods and fixed annual yield
contract FlexibleStaking is Ownable {
    // Struct to hold staking details
    struct Stake {
        uint256 amount;       // Amount staked
        uint256 startTime;    // Start time of the stake
        uint256 lockPeriod;   // Lock period in seconds
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token for staking
    IERC20 public stakingToken;

    // Fixed annual yield rate (e.g., 10% = 1000, 5% = 500)
    uint256 public annualYieldRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize staking token and yield rate
    constructor(IERC20 _stakingToken, uint256 _annualYieldRate) {
        require(_annualYieldRate > 0, "Annual yield rate must be greater than zero.");
        stakingToken = _stakingToken;
        annualYieldRate = _annualYieldRate;
    }

    // Function to stake tokens with a flexible lock period
    function stake(uint256 amount, uint256 lockPeriod) external {
        require(amount > 0, "Amount to stake must be greater than zero.");
        require(lockPeriod > 0, "Lock period must be greater than zero.");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update stakes mapping
        stakes[msg.sender] = Stake(amount, block.timestamp, lockPeriod);

        emit Staked(msg.sender, amount, lockPeriod);
    }

    // Function to withdraw tokens and earned rewards
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];

        // Ensure there is an active stake
        require(userStake.amount > 0, "No active stake found.");
        require(block.timestamp >= userStake.startTime + userStake.lockPeriod, "Lock period has not expired.");

        // Calculate rewards based on the staked amount and the elapsed time
        uint256 rewards = calculateRewards(userStake.amount, userStake.lockPeriod);
        
        // Reset user's stake to zero before transferring to prevent re-entrancy
        delete stakes[msg.sender];

        // Transfer the staked amount and rewards back to the user
        stakingToken.transfer(msg.sender, userStake.amount + rewards);

        emit Withdrawn(msg.sender, userStake.amount, rewards);
    }

    // Function to calculate rewards based on the stake amount and lock period
    function calculateRewards(uint256 amount, uint256 lockPeriod) internal view returns (uint256) {
        // Calculate the number of years the funds were staked (in seconds)
        uint256 yearsStaked = lockPeriod / 365 days;
        uint256 rewards = (amount * annualYieldRate * yearsStaked) / 10000; // Adjust for percentage
        return rewards;
    }

    // Function to update the annual yield rate (only callable by the owner)
    function updateAnnualYieldRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Annual yield rate must be greater than zero.");
        annualYieldRate = newRate;
    }
}
```
