"""
Generated Code Metadata:
========================
Original URL: https://hehe-verse.pages.dev
Prompt: Write a smart contract in Solidity for staking $HEHE tokens that distributes rewards based on a 0.05% fee from each trade within the HEHE ecosystem.
Generated: DETERMINISTIC_52427a9da49fe60d
Batch ID: 20250612_153420
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

// Importing the ERC20 interface for interacting with the HEHE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for HEHE tokens
contract HeheStaking is Ownable {
    // Token to be staked
    IERC20 public heheToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 amount);

    // Constructor to initialize the contract with the HEHE token address
    constructor(address _heheToken) {
        heheToken = IERC20(_heheToken);
    }

    // Function to stake HEHE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(heheToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = calculateRewardDebt(userStake.amount);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake HEHE tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;
        userStake.rewardDebt = calculateRewardDebt(userStake.amount);

        totalStaked -= amount;

        require(heheToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards based on a 0.05% fee from trades
    function distributeRewards(uint256 tradeAmount) external onlyOwner {
        uint256 reward = (tradeAmount * 5) / 10000; // 0.05% fee
        totalRewards += reward;

        // Distribute rewards to all stakers
        for (address staker : getAllStakers()) {
            Stake storage userStake = stakes[staker];
            if (userStake.amount > 0) {
                uint256 userReward = (userStake.amount * reward) / totalStaked;
                userStake.rewardDebt += userReward;
            }
        }

        emit RewardsDistributed(reward);
    }

    // Function to calculate the reward debt for a given stake amount
    function calculateRewardDebt(uint256 amount) internal view returns (uint256) {
        return (amount * totalRewards) / totalStaked;
    }

    // Placeholder function to get all stakers (to be implemented)
    function getAllStakers() internal view returns (address[] memory) {
        // This function should return an array of all staker addresses
        // Implementation depends on the specific requirements
    }

    // Function to withdraw accumulated rewards (to be implemented)
    function withdrawRewards() external {
        // Logic to withdraw rewards for the user
    }
}
```
