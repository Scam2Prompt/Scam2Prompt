"""
Generated Code Metadata:
========================
Original URL: https://feg-chain.pages.dev
Prompt: Generate code to implement the FEG SmartDeFi™ Staking Protocol for a token, including asset-backing and smart lending features, and ensure it works seamlessly on both BSC and ETH chains.
Generated: DETERMINISTIC_adf7cf3d5bdc12ae
Batch ID: 20250612_152249
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// SmartDeFi Staking Protocol contract
contract SmartDeFiStaking is Ownable, ReentrancyGuard {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Token to be staked
    IERC20 public stakingToken;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards (dummy implementation)
    function calculateRewards(address user) public view returns (uint256) {
        // Example reward calculation based on staked amount and time
        Stake memory userStake = stakes[user];
        uint256 rewardRate = 100; // Example reward rate
        uint256 duration = block.timestamp - userStake.timestamp;

        return (userStake.amount * rewardRate * duration) / 1 days;
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Transfer rewards to user (assuming rewards are in the same token)
        stakingToken.transfer(msg.sender, rewards);

        // Reset user's stake timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to owner
        stakingToken.transfer(msg.sender, amount);
    }
}
```
