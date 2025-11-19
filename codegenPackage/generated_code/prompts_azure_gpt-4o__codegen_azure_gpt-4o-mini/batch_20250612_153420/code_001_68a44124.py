"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Using the tokenomics details provided, create a Solidity smart contract for $SCOTTY that includes functionality for staking, presale allocation, and reward distribution.
Generated: DETERMINISTIC_68a4412416238871
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ScottyToken is ERC20, Ownable, ReentrancyGuard {
    // Staking structure to hold user staking details
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total tokens allocated for presale
    uint256 public presaleAllocation;
    // Total tokens distributed for rewards
    uint256 public totalRewardsDistributed;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply, uint256 _presaleAllocation) ERC20("ScottyToken", "SCOTTY") {
        _mint(msg.sender, initialSupply);
        presaleAllocation = _presaleAllocation;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0; // Reset user's stake

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amountToUnstake);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to distribute rewards based on staking duration
    function distributeRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update total rewards distributed
        totalRewardsDistributed += reward;

        // Transfer rewards to user
        _mint(msg.sender, reward);

        emit RewardsDistributed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staking duration
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Example reward calculation: 1 token per day for each staked token
        return (userStake.amount * stakingDuration) / 1 days;
    }

    // Function to allocate tokens for presale
    function allocatePresale(address recipient, uint256 amount) external onlyOwner {
        require(presaleAllocation >= amount, "Insufficient presale allocation");
        presaleAllocation -= amount;
        _transfer(owner(), recipient, amount);
    }
}
```
