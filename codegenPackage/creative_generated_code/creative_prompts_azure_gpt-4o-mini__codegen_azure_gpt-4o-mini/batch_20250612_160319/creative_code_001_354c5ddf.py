"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsemex.com
Prompt: Generate a Solidity contract that allows staking of $PLSX tokens on the PulseX DEX.
Generated: DETERMINISTIC_354c5ddf1a7626ff
Batch ID: 20250612_160319
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

// Importing the IERC20 interface for ERC20 token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for staking $PLSX tokens on the PulseX DEX
contract PLSXStaking {
    // State variables
    IERC20 public plsxToken; // The PLSX token contract
    mapping(address => uint256) public stakes; // Tracks the stakes of each user
    mapping(address => uint256) public rewards; // Tracks the rewards for each user
    uint256 public totalStaked; // Total amount of PLSX staked
    uint256 public rewardRate; // Reward rate per staked token (in wei)
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the PLSX token address and reward rate
    constructor(address _plsxToken, uint256 _rewardRate) {
        require(_plsxToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        plsxToken = IERC20(_plsxToken);
        rewardRate = _rewardRate;
    }

    // Function to stake PLSX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer PLSX tokens from the user to this contract
        plsxToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake PLSX tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer PLSX tokens back to the user
        plsxToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate the reward for a user
    function calculateReward(address user) public view returns (uint256) {
        return (stakes[user] * rewardRate) / 1e18; // Adjust reward calculation based on decimals
    }

    // Function to claim rewards
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update rewards
        rewards[msg.sender] += reward;

        // Transfer rewards to the user
        plsxToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Function to withdraw all staked PLSX and rewards
    function withdraw() external {
        uint256 stakedAmount = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        require(stakedAmount > 0 || reward > 0, "Nothing to withdraw");

        // Unstake tokens if applicable
        if (stakedAmount > 0) {
            stakes[msg.sender] = 0;
            totalStaked -= stakedAmount;
            plsxToken.transfer(msg.sender, stakedAmount);
            emit Unstaked(msg.sender, stakedAmount);
        }

        // Pay out rewards if any
        if (reward > 0) {
            rewards[msg.sender] += reward;
            plsxToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }
}
```
