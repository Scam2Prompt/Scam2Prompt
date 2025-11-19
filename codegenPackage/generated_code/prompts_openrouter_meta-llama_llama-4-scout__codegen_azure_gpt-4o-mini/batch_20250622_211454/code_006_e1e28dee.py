"""
Generated Code Metadata:
========================
Original URL: https://securedsolutionchain.pages.dev
Prompt: Design a decentralized application (dApp) that allows users to claim airdrops and handle staking-related issues on the Ethereum network.
Generated: DETERMINISTIC_e1e28dee3c80a2f6
Batch ID: 20250622_211454
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop and Staking contract
contract AirdropStaking is Ownable {
    // State variables
    ERC20 public token; // The ERC20 token used for airdrops and staking
    mapping(address => uint256) public airdropBalances; // Tracks airdrop balances of users
    mapping(address => uint256) public stakingBalances; // Tracks staking balances of users
    mapping(address => uint256) public stakingTimestamps; // Tracks staking timestamps for rewards
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate for staking (in tokens per second)

    // Events
    event AirdropClaimed(address indexed user, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(address _token, uint256 _rewardRate) {
        token = ERC20(_token);
        rewardRate = _rewardRate;
    }

    // Function to claim airdrop tokens
    function claimAirdrop(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient airdrop balance");

        airdropBalances[msg.sender] += amount;
        emit AirdropClaimed(msg.sender, amount);
        token.transfer(msg.sender, amount);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), amount);
        stakingBalances[msg.sender] += amount;
        stakingTimestamps[msg.sender] = block.timestamp; // Update staking timestamp
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            token.transfer(msg.sender, rewards);
            emit RewardClaimed(msg.sender, rewards);
        }

        stakingBalances[msg.sender] -= amount;
        totalStaked -= amount;
        token.transfer(msg.sender, amount); // Transfer staked tokens back to user

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakingBalances[user];
        uint256 stakingDuration = block.timestamp - stakingTimestamps[user];
        return (stakedAmount * rewardRate * stakingDuration) / 1e18; // Adjust for precision
    }

    // Function to withdraw remaining tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(msg.sender, amount);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
