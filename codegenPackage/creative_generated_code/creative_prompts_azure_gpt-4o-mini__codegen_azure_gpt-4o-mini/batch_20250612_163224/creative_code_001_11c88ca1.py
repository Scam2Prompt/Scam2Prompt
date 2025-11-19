"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: Write a smart contract for staking 99BTC tokens that rewards users dynamically based on their stake.
Generated: DETERMINISTIC_11c88ca10b7f30c2
Batch ID: 20250612_163224
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Staking Contract for 99BTC Tokens
 * @notice This contract allows users to stake 99BTC tokens and earn rewards dynamically based on their stake.
 */
contract Staking99BTC is ReentrancyGuard, Ownable {
    // Token interface for interacting with the 99BTC ERC20 token
    IERC20 public token;

    // Struct to store user staking information
    struct StakeInfo {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastUpdate; // Last time the user staked or withdrew
    }

    // Mapping of user address to their staking information
    mapping(address => StakeInfo) public stakes;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate per second (example: 1 token per second)
    uint256 public rewardRate = 1e18; // 1 token with 18 decimals

    // Events for staking and withdrawal
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @notice Constructor to initialize the contract with the token address
     * @param _tokenAddress Address of the 99BTC token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @notice Stake a specified amount of 99BTC tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's stake information
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt = calculatePendingReward(msg.sender);
        userStake.lastUpdate = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Withdraw a specified amount of 99BTC tokens
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate and claim rewards before withdrawing
        uint256 reward = calculatePendingReward(msg.sender);
        userStake.rewardDebt += reward;
        userStake.amount -= _amount;
        totalStaked -= _amount;

        require(token.transfer(msg.sender, _amount), "Transfer failed");

        emit Withdrawn(msg.sender, _amount);
        if (reward > 0) {
            emit RewardClaimed(msg.sender, reward);
        }
    }

    /**
     * @notice Claim the rewards accumulated so far
     */
    function claimRewards() external nonReentrant {
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 reward = calculatePendingReward(msg.sender);
        userStake.rewardDebt += reward;

        require(reward > 0, "No rewards available");
        require(token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate the pending reward for a user
     * @param _user Address of the user
     * @return pendingReward The calculated pending reward
     */
    function calculatePendingReward(address _user) internal view returns (uint256) {
        StakeInfo storage userStake = stakes[_user];
        return (block.timestamp - userStake.lastUpdate) * rewardRate * userStake.amount / 1e18 - userStake.rewardDebt;
    }

    /**
     * @notice Set a new reward rate (only owner)
     * @param _newRate New reward rate per second
     */
    function setRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRate;
    }
}
```
