"""
Generated Code Metadata:
========================
Original URL: https://agix-reward.com
Prompt: Generate a smart contract in Solidity to enable AGIX token staking and reward distribution based on on-chain activity, as described in the SingularityNET rewards event.
Generated: DETERMINISTIC_e7ab16435fad68a1
Batch ID: 20250612_152018
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

// Importing the ERC20 interface for AGIX token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for AGIX token
contract AGIXStaking is Ownable {
    // AGIX token interface
    IERC20 public agixToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of AGIX staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the AGIX token address
    constructor(address _agixToken) {
        agixToken = IERC20(_agixToken);
    }

    // Function to stake AGIX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(agixToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake AGIX tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;
        totalStaked -= amount;

        require(agixToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards based on staking duration
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Example reward calculation: 1% of staked amount per day
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 rewardRate = 1; // 1% per day
        uint256 rewards = (userStake.amount * rewardRate * stakingDuration) / (1 days * 100);

        return rewards;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset the staking timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer rewards to the user (assuming rewards are paid in AGIX)
        require(agixToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the user's stake information
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }
}
```
