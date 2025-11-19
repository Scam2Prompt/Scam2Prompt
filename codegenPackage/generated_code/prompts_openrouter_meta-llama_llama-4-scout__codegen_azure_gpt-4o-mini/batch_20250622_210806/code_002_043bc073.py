"""
Generated Code Metadata:
========================
Original URL: https://airdrop-inqubeta.pages.dev
Prompt: Generate a smart contract code (in Solidity) for creating a decentralized application (dApp) that allows users to stake $QUBE tokens and earn rewards from the 5% sell tax.
Generated: DETERMINISTIC_043bc07329ddd587
Batch ID: 20250622_210806
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

// Importing the ERC20 interface for interacting with the QUBE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for QUBE token
contract QubeStaking is Ownable {
    // State variables
    IERC20 public qubeToken; // The QUBE token contract
    uint256 public totalStaked; // Total amount of QUBE tokens staked
    uint256 public rewardRate; // Reward rate based on the sell tax
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    mapping(address => uint256) public lastUpdate; // Last update timestamp for rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the QUBE token address and reward rate
    constructor(IERC20 _qubeToken, uint256 _rewardRate) {
        qubeToken = _qubeToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any action
    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] += earned(account);
            lastUpdate[account] = block.timestamp;
        }
        _;
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (stakedAmount[account] * rewardRate * (block.timestamp - lastUpdate[account])) / 1e18;
    }

    // Function to stake QUBE tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        qubeToken.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake QUBE tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        qubeToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        qubeToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= qubeToken.balanceOf(address(this)), "Insufficient balance");
        qubeToken.transfer(msg.sender, amount);
    }
}
```
