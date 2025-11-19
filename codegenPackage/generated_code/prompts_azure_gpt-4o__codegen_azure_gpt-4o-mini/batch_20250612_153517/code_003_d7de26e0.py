"""
Generated Code Metadata:
========================
Original URL: https://tgcasino-app.pages.dev
Prompt: Create a smart contract in Solidity for staking $TGC tokens, incorporating TG.Casino's tokenomics (e.g., 20% liquidity pool, 40% presale allocation).
Generated: DETERMINISTIC_d7de26e01f7d464c
Batch ID: 20250612_153517
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $TGC tokens
contract TGCStaking is Ownable {
    // Token interface for $TGC
    IERC20 public tgcToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $TGC token address
    constructor(address _tgcToken) {
        require(_tgcToken != address(0), "Invalid token address");
        tgcToken = IERC20(_tgcToken);
    }

    // Function to stake $TGC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tgcToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        tgcToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $TGC tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        tgcToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards (for demonstration purposes, rewards logic can be added)
    function claimRewards() external {
        // Placeholder for reward calculation logic
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Transfer rewards to the user (assuming rewards are also in $TGC)
        tgcToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards based on the stake duration (placeholder logic)
    function calculateRewards(address user) internal view returns (uint256) {
        // Example reward calculation based on staked amount and duration
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Simple reward logic: 1% of staked amount per day
        uint256 daysStaked = (block.timestamp - userStake.timestamp) / 1 days;
        return (userStake.amount * daysStaked) / 100; // 1% reward
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(tgcToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        tgcToken.transfer(msg.sender, amount);
    }
}
```
