"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbridge-site.github.io
Prompt: Create a smart contract that enables staking of LP tokens on cBridge for yield farming rewards, ensuring compatibility with Layer 2 solutions like Arbitrum and Optimism.
Generated: DETERMINISTIC_b3650d2d59c81057
Batch ID: 20250612_155048
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for the cBridge contract (simplified for demonstration)
interface IcBridge {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getRewards(address user) external view returns (uint256);
}

contract StakingLP is Ownable, ReentrancyGuard {
    // LP Token interface
    IERC20 public lpToken;
    IcBridge public cBridge;

    // User stakes mapping
    mapping(address => uint256) public stakes;
    mapping(address => uint256) public rewards;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _lpToken, IcBridge _cBridge) {
        lpToken = _lpToken;
        cBridge = _cBridge;
    }

    // Function to stake LP tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Staking amount must be greater than zero");

        // Transfer LP tokens from user to contract
        lpToken.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender] += amount;

        // Stake the amount in cBridge
        cBridge.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked LP tokens
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update stakes
        stakes[msg.sender] -= amount;

        // Withdraw from cBridge
        cBridge.withdraw(amount);

        // Transfer LP tokens back to user
        lpToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = cBridge.getRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] += rewardAmount; // Update internal rewards mapping

        // Transfer rewards to the user (assuming rewards are also in LP tokens)
        lpToken.transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to get user's staked amount
    function getUserStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to get total rewards of the user
    function getUserRewards(address user) external view returns (uint256) {
        return rewards[user] + cBridge.getRewards(user);
    }
}
```
