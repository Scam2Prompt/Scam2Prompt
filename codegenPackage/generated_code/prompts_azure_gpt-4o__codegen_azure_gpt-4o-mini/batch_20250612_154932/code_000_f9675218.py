"""
Generated Code Metadata:
========================
Original URL: https://aria.fyi
Prompt: Write a smart contract in Solidity to interact with the ARIA20 token on Ethereum, including functions for staking and transferring tokens as described in the Arianee Protocol documentation.
Generated: DETERMINISTIC_f96752186bfc4788
Batch ID: 20250612_154932
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

// Importing the ERC20 interface for the ARIA20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking and transferring ARIA20 tokens
contract ArianeeStaking is Ownable {
    // State variables
    IERC20 public ariaToken; // Instance of the ARIA20 token
    mapping(address => uint256) public stakes; // Mapping to track user stakes
    mapping(address => uint256) public rewards; // Mapping to track user rewards
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate for staking

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the ARIA20 token address and reward rate
    constructor(address _ariaToken, uint256 _rewardRate) {
        require(_ariaToken != address(0), "Invalid token address");
        ariaToken = IERC20(_ariaToken);
        rewardRate = _rewardRate;
    }

    // Function to stake ARIA20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(ariaToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        ariaToken.transferFrom(msg.sender, address(this), amount);

        // Update stakes and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake ARIA20 tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update stakes and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        ariaToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and distribute rewards
    function calculateReward(address user) public view returns (uint256) {
        return (stakes[user] * rewardRate) / 1e18; // Assuming rewardRate is in wei
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update rewards mapping
        rewards[msg.sender] += reward;

        // Transfer rewards to the user
        ariaToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= ariaToken.balanceOf(address(this)), "Insufficient contract balance");
        ariaToken.transfer(msg.sender, amount);
    }
}
```
