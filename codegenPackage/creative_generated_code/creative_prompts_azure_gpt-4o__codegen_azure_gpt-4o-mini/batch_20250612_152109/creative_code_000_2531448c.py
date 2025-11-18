"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Write an Ethereum smart contract for staking BTCETF tokens, allowing users to lock their tokens and earn rewards at a dynamic rate based on the total staked amount.
Generated: DETERMINISTIC_2531448ce5558235
Batch ID: 20250612_152109
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

// Interface for interacting with the BTCETF token contract
interface IBTCETF {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

// Staking contract for BTCETF tokens
contract StakingContract {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 reward;      // Accumulated rewards
        uint256 timestamp;   // Timestamp of the last update
    }

    // State variables
    IBTCETF public btcEtfToken; // The BTCETF token contract
    mapping(address => Stake) public stakes; // User stakes
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate;  // Reward rate per second per token

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the BTCETF token contract address and reward rate
    constructor(address _btcEtfToken, uint256 _rewardRate) {
        btcEtfToken = IBTCETF(_btcEtfToken);
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Update the user's rewards before staking
        updateRewards(msg.sender);

        // Transfer BTCETF tokens from the user to the contract
        require(btcEtfToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update stake information
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens and rewards
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's rewards before unstaking
        updateRewards(msg.sender);
        
        // Update the stake amount and total staked
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer the staked tokens back to the user
        require(btcEtfToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim accumulated rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = stakes[msg.sender].reward;
        require(reward > 0, "No rewards to claim");

        // Reset the user's reward and transfer it to them
        stakes[msg.sender].reward = 0;
        require(btcEtfToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to update user's rewards
    function updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 timeStaked = block.timestamp - userStake.timestamp;
            userStake.reward += userStake.amount * rewardRate * timeStaked;
        }
        userStake.timestamp = block.timestamp; // Update timestamp to current block time
    }

    // Function to get user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get user's accumulated rewards
    function getAccumulatedRewards(address user) external view returns (uint256) {
        return stakes[user].reward + (stakes[user].amount * rewardRate * (block.timestamp - stakes[user].timestamp));
    }
}
```
