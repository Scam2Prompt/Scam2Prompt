"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-eng.pages.dev
Prompt: Write a smart contract for staking $PEPU tokens on Pepe Unchained's Layer 2 blockchain, ensuring compatibility with Ethereum and Pepe Chain bridging.
Generated: DETERMINISTIC_aee8eb6986753c82
Batch ID: 20250612_151141
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

// Importing the ERC20 interface for interacting with the $PEPU token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $PEPU tokens
contract PepuStaking is Ownable {
    // State variables
    IERC20 public pepuToken; // Reference to the $PEPU token contract
    uint256 public totalStaked; // Total amount of $PEPU tokens staked
    uint256 public rewardRate; // Reward rate for staking
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    mapping(address => uint256) public lastUpdate; // Last update timestamp for rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the $PEPU token address and reward rate
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        pepuToken = _pepuToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any staking or unstaking action
    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] = earned(account);
            lastUpdate[account] = block.timestamp;
        }
        _;
    }

    // Function to stake $PEPU tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        pepuToken.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake $PEPU tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        pepuToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        pepuToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (stakedAmount[account] * rewardRate * (block.timestamp - lastUpdate[account])) / 1e18;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        pepuToken.transfer(msg.sender, amount);
    }
}
```
