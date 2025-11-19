"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a Solidity contract for staking Bitcoin ETF Token (BTCETF) that rewards users based on the number of tokens staked.
Generated: DETERMINISTIC_ac6c523fcb89b150
Batch ID: 20250612_163848
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// The Staking contract for BTCETF token
contract BTCETFStaking {
    // Token to be staked
    IERC20 public btcEFTToken;

    // Reward rate per block for each token staked
    uint256 public rewardRate;

    // Information about each staker
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked
        uint256 rewardDebt;   // Reward debt to calculate rewards
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of stakers to their information
    mapping(address => Staker) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the token and reward rate
    constructor(IERC20 _btcEFTToken, uint256 _rewardRate) {
        btcEFTToken = _btcEFTToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");

        // Transfer tokens from the user to the contract
        require(btcEFTToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Withdraw amount exceeds staked amount");

        // Update the staker's information
        staker.stakedAmount -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the user
        require(btcEFTToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to calculate pending rewards
    function calculateRewards(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        return (staker.stakedAmount * rewardRate * (block.timestamp - staker.lastStakedTime)) / 1e18;
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update last staked time to the current block timestamp
        staker.lastStakedTime = block.timestamp;

        // Transfer reward tokens to the user (assumes rewards are in the same token)
        require(btcEFTToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner can call this)
    function setRewardRate(uint256 newRewardRate) external {
        // Functionality to restrict to the owner can be added
        rewardRate = newRewardRate;
    }
}
```
