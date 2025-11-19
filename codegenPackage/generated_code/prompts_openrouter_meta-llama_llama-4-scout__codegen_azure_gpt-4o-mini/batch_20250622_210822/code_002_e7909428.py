"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Design a simple smart contract on the Pepe Unchained blockchain to automate the buying and staking of $PEPU tokens, using Solidity programming language.
Generated: DETERMINISTIC_e79094285de29e23
Batch ID: 20250622_210822
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

// Smart contract for automating the buying and staking of $PEPU tokens
contract PepeStaking is Ownable {
    // State variables
    IERC20 public pepuToken; // The $PEPU token contract
    uint256 public stakingRewardRate; // Reward rate for staking
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastStakedTime; // Last time the user staked tokens
    mapping(address => uint256) public rewards; // Rewards earned by each user

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $PEPU token address and reward rate
    constructor(address _pepuToken, uint256 _stakingRewardRate) {
        require(_pepuToken != address(0), "Invalid token address");
        require(_stakingRewardRate > 0, "Reward rate must be greater than zero");
        
        pepuToken = IERC20(_pepuToken);
        stakingRewardRate = _stakingRewardRate;
    }

    // Function to stake $PEPU tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        pepuToken.transferFrom(msg.sender, address(this), amount);

        // Update staked amount and last staked time
        stakedAmount[msg.sender] += amount;
        lastStakedTime[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake $PEPU tokens
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        _calculateRewards(msg.sender);

        // Update staked amount
        stakedAmount[msg.sender] -= amount;

        // Transfer tokens back to the user
        pepuToken.transfer(msg.sender, amount);

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _calculateRewards(msg.sender);
        
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards after claiming
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        pepuToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function _calculateRewards(address user) internal {
        uint256 stakedDuration = block.timestamp - lastStakedTime[user];
        uint256 reward = (stakedAmount[user] * stakingRewardRate * stakedDuration) / 1e18; // Assuming reward rate is in wei

        // Update rewards and last staked time
        rewards[user] += reward;
        lastStakedTime[user] = block.timestamp;
    }

    // Function to set a new staking reward rate (only owner)
    function setStakingRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        stakingRewardRate = newRate;
    }
}
```
