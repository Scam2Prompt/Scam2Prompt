"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secure-greenbitcoin.pages.dev
Prompt: Provide an example of a Solidity contract that allows users to stake their $GBTC tokens and earn rewards, while ensuring energy efficiency in line with Green Bitcoin's eco-friendly approach.
Generated: DETERMINISTIC_367835084990b56e
Batch ID: 20250612_160853
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

// Importing OpenZeppelin's ERC20 interface for handling token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingContract allows users to stake $GBTC tokens and earn rewards
contract StakingContract is Ownable {
    // Token being staked
    IERC20 public gbtcToken;

    // Struct to represent a user's staking data
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastUpdatedTime;
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Total staked amount in the contract
    uint256 public totalStaked;
    
    // Reward rate per token staked (in wei)
    uint256 public rewardRate = 1e18; // Example: 1 token per second per token staked

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _gbtcToken) {
        gbtcToken = _gbtcToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = calculatePendingRewards(msg.sender);
        userStake.lastUpdatedTime = block.timestamp;
        
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake
        userStake.rewardDebt = calculatePendingRewards(msg.sender);
        userStake.amount -= amount;
        totalStaked -= amount;

        require(gbtcToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculatePendingRewards(msg.sender);

        require(reward > 0, "No rewards to claim");
        
        // Update user's reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer the reward
        require(gbtcToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate pending rewards for a user
    function calculatePendingRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp - userStake.lastUpdatedTime;
        return (userStake.amount * rewardRate * timeStaked) / 1e18 + userStake.rewardDebt;
    }

    // Function to update reward rate, can only be called by the owner
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
