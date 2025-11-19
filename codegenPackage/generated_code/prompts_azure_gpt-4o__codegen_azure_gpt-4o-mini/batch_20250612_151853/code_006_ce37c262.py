"""
Generated Code Metadata:
========================
Original URL: https://doggodao.web.app
Prompt: Create a staking mechanism for Solana NFT projects that rewards users with $DOGGO tokens, including wallet integration and reward calculation.
Generated: DETERMINISTIC_ce37c262032c5609
Batch ID: 20250612_151853
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Solana NFT projects rewarding users with $DOGGO tokens
contract StakingContract is Ownable {
    // Token to be rewarded
    IERC20 public doggoToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of NFTs staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastUpdate; // Last time rewards were updated
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total staked NFTs
    uint256 public totalStaked;

    // Reward per NFT staked per second
    uint256 public rewardRate;

    // Event emitted when a user stakes NFTs
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes NFTs
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the DOGGO token address and reward rate
    constructor(IERC20 _doggoToken, uint256 _rewardRate) {
        doggoToken = _doggoToken;
        rewardRate = _rewardRate;
    }

    // Function to stake NFTs
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake NFTs
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update user's stake information
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = stakes[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer DOGGO tokens to the user
        require(doggoToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        Stake storage stakeInfo = stakes[user];
        uint256 timeElapsed = block.timestamp - stakeInfo.lastUpdate;

        // Calculate rewards based on the time elapsed and reward rate
        uint256 pendingReward = (stakeInfo.amount * rewardRate * timeElapsed) / 1e18;

        // Update user's reward debt
        stakeInfo.rewardDebt += pendingReward;
        stakeInfo.lastUpdate = block.timestamp;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        _updateRewards(msg.sender);
        rewardRate = newRate;
    }
}
```
