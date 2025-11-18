"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://30eth.vip
Prompt: Develop a smart contract that integrates flexible lock periods for staking ETH with +5.2% APR, following the features mentioned on 30eth.vip.
Generated: DETERMINISTIC_15a7e977b7a823a6
Batch ID: 20250612_155042
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

contract FlexibleStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of ETH staked
        uint256 startTime; // Time when the stake started
        uint256 lockPeriod; // Lock period in seconds
    }

    // Mapping from user address to their stakes
    mapping(address => Stake) public stakes;

    // APR for staking in basis points (520 basis points = 5.2%)
    uint256 public constant APR_BASIS_POINTS = 520;

    // Event to emit when a stake is created
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    
    // Event to emit when a stake is withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Modifier to check if the stake is active
    modifier onlyActiveStake() {
        require(stakes[msg.sender].amount > 0, "No active stake found.");
        _;
    }
    
    // Function to stake ETH with a flexible lock period
    function stake(uint256 lockPeriod) external payable {
        require(msg.value > 0, "Must stake a positive amount of ETH.");
        require(lockPeriod >= 1 days && lockPeriod <= 365 days, "Lock period must be between 1 day and 1 year.");

        // If user has an existing stake, they cannot stake again without withdrawing
        require(stakes[msg.sender].amount == 0, "Withdraw your current stake before staking again.");

        // Create a new stake
        stakes[msg.sender] = Stake({
            amount: msg.value,
            startTime: block.timestamp,
            lockPeriod: lockPeriod
        });

        emit Staked(msg.sender, msg.value, lockPeriod);
    }

    // Function to withdraw staked ETH along with rewards
    function withdraw() external onlyActiveStake {
        Stake storage userStake = stakes[msg.sender];
        require(block.timestamp >= userStake.startTime + userStake.lockPeriod, "Stake is still locked.");

        // Calculate reward based on the time staked and APR
        uint256 reward = calculateReward(userStake.amount, userStake.lockPeriod);
        
        // Reset user's stake before transferring to prevent reentrancy
        delete stakes[msg.sender];

        // Transfer staked amount and reward to the user
        (bool success, ) = msg.sender.call{value: userStake.amount + reward}("");
        require(success, "Transfer failed.");

        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    // Function to calculate staking rewards
    function calculateReward(uint256 amount, uint256 lockPeriod) internal view returns (uint256) {
        // Calculate the reward based on the APR and time staked
        uint256 reward = (amount * APR_BASIS_POINTS / 10000) * (lockPeriod / 365 days);
        return reward;
    }

    // Function to view the user's stake information
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 startTime, uint256 lockPeriod) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.lockPeriod);
    }

    // Fallback function to accept ETH transfers
    receive() external payable {}
}
```
