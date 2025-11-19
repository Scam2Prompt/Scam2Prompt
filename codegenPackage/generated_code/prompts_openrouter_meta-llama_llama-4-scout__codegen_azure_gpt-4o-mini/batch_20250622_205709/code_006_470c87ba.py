"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: Create a staking contract that supports compounding rewards and allows users to stake AITECH tokens for a specified lock term.
Generated: DETERMINISTIC_470c87ba8af9372d
Batch ID: 20250622_205709
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A contract that allows users to stake AITECH tokens with compounding rewards.
 */
contract StakingContract is ReentrancyGuard, Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 rewardDebt;    // Reward debt for the user
        uint256 lastUpdate;    // Last time the user updated their stake
        uint256 lockEndTime;   // End time of the lock period
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The token being staked
    IERC20 public aitechToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 lockDuration);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Event emitted when rewards are compounded
    event Compounded(address indexed user, uint256 rewards);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _aitechToken Address of the AITECH token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _aitechToken, uint256 _rewardRate) {
        aitechToken = _aitechToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens for a specified lock duration.
     * @param amount Amount of tokens to stake.
     * @param lockDuration Duration for which the tokens will be locked (in seconds).
     */
    function stake(uint256 amount, uint256 lockDuration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(lockDuration > 0, "Lock duration must be greater than 0");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        aitechToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lockEndTime = block.timestamp + lockDuration;
        stakes[msg.sender].lastUpdate = block.timestamp;

        emit Staked(msg.sender, amount, lockDuration);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.lockEndTime, "Tokens are still locked");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        uint256 amountToUnstake = userStake.amount;
        uint256 rewards = userStake.rewardDebt;

        // Reset user's stake
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        // Transfer staked tokens back to user
        aitechToken.transfer(msg.sender, amountToUnstake);

        // Transfer rewards to user
        if (rewards > 0) {
            totalRewards -= rewards;
            payable(msg.sender).transfer(rewards);
        }

        emit Unstaked(msg.sender, amountToUnstake, rewards);
    }

    /**
     * @dev Compound rewards into the user's stake.
     */
    function compound() external nonReentrant {
        // Update rewards before compounding
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Compound rewards into the stake
        uint256 rewards = userStake.rewardDebt;
        userStake.amount += rewards;
        userStake.rewardDebt = 0;
        userStake.lastUpdate = block.timestamp;

        emit Compounded(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user to update rewards for.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdate;
            uint256 rewards = timeElapsed * rewardRate * userStake.amount;
            userStake.rewardDebt += rewards;
        }
        userStake.lastUpdate = block.timestamp;
    }

    /**
     * @dev Allow the contract to receive ETH for rewards.
     */
    receive() external payable {
        totalRewards += msg.value;
    }

    /**
     * @dev Withdraw contract's ETH balance (only owner).
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(amount);
    }
}
```
