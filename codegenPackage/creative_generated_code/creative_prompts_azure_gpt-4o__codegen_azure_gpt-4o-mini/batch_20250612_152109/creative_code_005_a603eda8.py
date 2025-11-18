"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-com.pages.dev
Prompt: Provide a step-by-step tutorial for deploying a token presale smart contract on Ethereum, including features for staking and reward claiming as described in the $SCOTTY presale.
Generated: DETERMINISTIC_a603eda889082660
Batch ID: 20250612_152109
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

// Importing required libraries
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the SCOTTY token contract which extends ERC20 and Ownable
contract SCOTTYToken is ERC20, Ownable {
    // Mapping to track stakers and their stakes
    mapping(address => uint256) public stakes;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // The reward rate for staking
    uint256 public rewardRate = 100; // Example reward rate

    // Constructor to initialize the token
    constructor() ERC20("SCOTTY Token", "SCOTTY") {
        // Mint initial supply to the owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        _transfer(msg.sender, address(this), amount);
        
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update stakes and total staked
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Transfer rewards to the user
        _mint(msg.sender, rewards);

        // Emit an event for claiming rewards
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate rewards for the user
    function calculateRewards(address user) internal view returns (uint256) {
        // Calculate rewards based on the staked amount and the reward rate
        return (stakes[user] * rewardRate) / 1000; // Example calculation
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
