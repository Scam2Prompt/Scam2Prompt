"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Write a smart contract that supports multiple lock terms (e.g., 90 days, 180 days, 365 days) with corresponding reward percentages and boosts, based on the AITECH staking structure.
Generated: DETERMINISTIC_45598edc403a2e02
Batch ID: 20250612_152620
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

// Import OpenZeppelin Contracts for Ownable functionality
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for ERC20 token to handle AITECH tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Contract declaration for AITECH Staking
contract AITECHStaking is Ownable {
    // Struct to hold each staking deposit
    struct Stake {
        uint256 amount;
        uint256 unlockTime;
        uint256 rewardPercentage;
        bool withdrawn;
    }

    // Mapping from staker address to their stakes
    mapping(address => Stake[]) public stakes;

    // Reward percentages and lock durations in days
    uint256[] public lockDurations = [90 days, 180 days, 365 days];
    uint256[] public rewardPercentages = [10, 20, 30]; // Corresponding percentages for the durations

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Event to emit when a new stake is created
    event Staked(address indexed user, uint256 amount, uint256 duration);
    // Event to emit when rewards are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens with a selected duration
    function stake(uint256 amount, uint256 durationIndex) external {
        require(durationIndex < lockDurations.length, "Invalid duration index");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Create a new stake
        Stake memory newStake = Stake({
            amount: amount,
            unlockTime: block.timestamp + lockDurations[durationIndex],
            rewardPercentage: rewardPercentages[durationIndex],
            withdrawn: false
        });

        stakes[msg.sender].push(newStake);

        emit Staked(msg.sender, amount, lockDurations[durationIndex]);
    }

    // Function to withdraw rewards after the lock period has ended
    function withdraw(uint256 stakeIndex) external {
        Stake storage userStake = stakes[msg.sender][stakeIndex];
        require(!userStake.withdrawn, "Stake already withdrawn");
        require(block.timestamp >= userStake.unlockTime, "Stake is still locked");

        // Calculate total reward
        uint256 reward = (userStake.amount * userStake.rewardPercentage) / 100;

        // Mark the stake as withdrawn
        userStake.withdrawn = true;

        // Transfer the original amount and reward to the user
        stakingToken.transfer(msg.sender, userStake.amount);
        stakingToken.transfer(msg.sender, reward);

        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    // Function to get the number of stakes for a user
    function getStakeCount(address user) external view returns (uint256) {
        return stakes[user].length;
    }

    // Function to get details of a specific stake
    function getStakeDetails(address user, uint256 stakeIndex) external view returns (Stake memory) {
        require(stakeIndex < stakes[user].length, "Invalid stake index");
        return stakes[user][stakeIndex];
    }
}
```
