"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy-io.github.io
Prompt: Generate Solidity code for a smart contract that enables staking of ORB tokens on the Zealy platform, allowing users to earn rewards in stablecoins.
Generated: DETERMINISTIC_a58fc2cb57eacbad
Batch ID: 20250612_150858
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

// Interface for the ORB token contract
interface IOrbToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for the stablecoin contract
interface IStablecoin {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Staking contract for ORB tokens
contract OrbStaking {
    // State variables
    IOrbToken public orbToken; // ORB token contract instance
    IStablecoin public stablecoin; // Stablecoin contract instance
    uint256 public rewardRate; // Reward rate in stablecoins per token staked per block

    // Struct for user staking data
    struct Stake {
        uint256 amount; // Amount of ORB tokens staked
        uint256 rewards; // Accumulated rewards
        uint256 lastUpdateBlock; // Last block when rewards were updated
    }

    // Mapping of user addresses to their staking data
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with ORB and stablecoin addresses
    constructor(address _orbToken, address _stablecoin, uint256 _rewardRate) {
        orbToken = IOrbToken(_orbToken);
        stablecoin = IStablecoin(_stablecoin);
        rewardRate = _rewardRate;
    }

    // Modifier to ensure that the user has staked ORB tokens
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No stake found.");
        _;
    }

    // Function to stake ORB tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(orbToken.balanceOf(msg.sender) >= amount, "Insufficient ORB balance.");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer ORB tokens from the user to the contract
        require(orbToken.transfer(msg.sender, amount), "Transfer failed.");

        // Update user's stake data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastUpdateBlock = block.number;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked ORB tokens and claim rewards
    function withdraw(uint256 amount) external hasStake {
        require(amount > 0, "Amount must be greater than zero.");
        require(stakes[msg.sender].amount >= amount, "Withdrawal exceeds stake.");

        // Update rewards before withdrawing
        _updateRewards(msg.sender);

        // Update user's stake data
        stakes[msg.sender].amount -= amount;

        // Transfer ORB tokens back to the user
        require(orbToken.transfer(msg.sender, amount), "Transfer failed.");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim accumulated rewards
    function claimRewards() external hasStake {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].rewards;
        require(reward > 0, "No rewards to claim.");

        // Reset rewards to zero
        stakes[msg.sender].rewards = 0;

        // Transfer stablecoins as rewards
        require(stablecoin.transfer(msg.sender, reward), "Transfer failed.");

        emit RewardPaid(msg.sender, reward);
    }

    // Private function to update user's rewards
    function _updateRewards(address user) private {
        Stake storage stakeData = stakes[user];
        uint256 blocksStaked = block.number - stakeData.lastUpdateBlock;

        // Calculate earned rewards
        if (blocksStaked > 0) {
            uint256 earnedRewards = stakeData.amount * blocksStaked * rewardRate;
            stakeData.rewards += earnedRewards;
            stakeData.lastUpdateBlock = block.number;
        }
    }

    // Function to get the total rewards of a user
    function getRewards(address user) external view returns (uint256) {
        Stake storage stakeData = stakes[user];
        uint256 blocksStaked = block.number - stakeData.lastUpdateBlock;
        uint256 earnedRewards = stakeData.amount * blocksStaked * rewardRate;
        return stakeData.rewards + earnedRewards;
    }
}
```
