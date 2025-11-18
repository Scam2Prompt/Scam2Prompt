"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Provide a Solidity example for a decentralized staking mechanism that supports variable lock-in periods for BTCMTX tokens, as described in the Bitcoin Minetrix roadmap.
Generated: DETERMINISTIC_5294173f7ef53555
Batch ID: 20250612_152620
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

/**
 * @title BTCMTX Staking Contract
 * @dev This contract allows users to stake BTCMTX tokens with variable lock-in periods.
 * The contract supports staking, withdrawing, and rewards management.
 */

interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}

contract BTCMTXStaking {
    // Token contract instance
    IERC20 public btcmtxToken;

    // Struct to represent a staking position
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 unlockTime;   // Timestamp when tokens can be withdrawn
        uint256 rewards;      // Accumulated rewards for this stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake[]) public stakes;

    // Reward rate per second (set by contract owner)
    uint256 public rewardRatePerSecond;

    // Contract owner address
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);
    event RewardRateUpdated(uint256 oldRate, uint256 newRate);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize token address and reward rate.
     * @param _btcmtxToken Address of the BTCMTX token contract.
     * @param _rewardRatePerSecond Reward rate per second for staking.
     */
    constructor(IERC20 _btcmtxToken, uint256 _rewardRatePerSecond) {
        btcmtxToken = _btcmtxToken;
        rewardRatePerSecond = _rewardRatePerSecond;
        owner = msg.sender;
    }

    /**
     * @dev Function to stake BTCMTX tokens.
     * @param amount Amount of tokens to stake.
     * @param lockInPeriod Lock-in period in seconds.
     */
    function stake(uint256 amount, uint256 lockInPeriod) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockInPeriod > 0, "Lock-in period must be greater than zero");

        // Transfer tokens from user to contract
        require(
            btcmtxToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Calculate unlock time for this stake
        uint256 unlockTime = block.timestamp + lockInPeriod;

        // Create a new stake and add it to the user's list
        stakes[msg.sender].push(Stake({
            amount: amount,
            unlockTime: unlockTime,
            rewards: 0
        }));

        emit Staked(msg.sender, amount, unlockTime);
    }

    /**
     * @dev Function to withdraw staked tokens and accumulated rewards.
     * @param stakeIndex Index of the stake to withdraw.
     */
    function withdraw(uint256 stakeIndex) external {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = stakes[msg.sender][stakeIndex];

        // Ensure the stake is unlocked
        require(block.timestamp >= userStake.unlockTime, "Stake is still locked");

        // Calculate rewards for the stake
        uint256 rewardDuration = userStake.unlockTime - (block.timestamp - (userStake.unlockTime - userStake.amount));
        uint256 rewards = rewardDuration * rewardRatePerSecond;

        // Transfer tokens and rewards back to the user
        require(btcmtxToken.transfer(msg.sender, userStake.amount), "Token transfer failed");
        require(btcmtxToken.transfer(msg.sender, rewards), "Reward transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, userStake.amount, rewards);

        // Remove the stake from the user's list
        delete stakes[msg.sender][stakeIndex];
    }

    /**
     * @dev Function to update the reward rate per second (owner only).
     * @param newRate New reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        uint256 oldRate = rewardRatePerSecond;
        rewardRatePerSecond = newRate;

        emit RewardRateUpdated(oldRate, newRate);
    }

    /**
     * @dev Function to check the number of stakes for a user.
     * @param user Address of the user.
     * @return Number of stakes for the user.
     */
    function getStakeCount(address user) external view returns (uint256) {
        return stakes[user].length;
    }
}
```
