"""
Generated Code Metadata:
========================
Original URL: https://doge20-claim.pages.dev
Prompt: "Generate a smart contract in Solidity for a staking platform similar to Dogecoin20's, with dynamic rewards rates and monthly, daily return calculations."
Generated: DETERMINISTIC_94196aac735bd0dc
Batch ID: 20250622_210914
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for dynamic rewards
contract StakingPlatform is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Time when the stake was created
        uint256 rewardRate; // Reward rate for the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            rewardRate: calculateRewardRate(amount)
        });

        emit Staked(msg.sender, amount);
    }

    // Function to calculate reward rate based on the amount staked
    function calculateRewardRate(uint256 amount) internal pure returns (uint256) {
        // Example reward rate calculation (can be modified)
        if (amount < 1000 * 10 ** 18) {
            return 5; // 5% reward rate
        } else if (amount < 5000 * 10 ** 18) {
            return 10; // 10% reward rate
        } else {
            return 15; // 15% reward rate
        }
    }

    // Function to calculate rewards based on time and rate
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 duration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * userStake.rewardRate * duration) / (365 days * 100); // Annualized reward
        return reward;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        // Calculate rewards
        uint256 reward = calculateRewards(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset user's stake
        delete stakes[msg.sender];

        // Transfer staked amount and rewards back to user
        stakingToken.transfer(msg.sender, totalAmount);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= stakingToken.balanceOf(address(this)), "Insufficient contract balance");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
