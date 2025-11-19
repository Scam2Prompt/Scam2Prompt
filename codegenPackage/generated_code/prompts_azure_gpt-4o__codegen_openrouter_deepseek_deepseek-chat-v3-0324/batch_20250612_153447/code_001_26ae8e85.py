"""
Generated Code Metadata:
========================
Original URL: https://pepeu.pages.dev
Prompt: Generate Solidity code for a smart contract that facilitates double staking rewards for $PEPU tokens on Pepe Unchained.
Generated: DETERMINISTIC_26ae8e8553ed9edb
Batch ID: 20250612_153447
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PEPUDoubleStaking is Ownable, ReentrancyGuard {
    IERC20 public pepuToken;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    uint256 public constant REWARD_RATE = 2; // 2x rewards
    uint256 public constant LOCK_PERIOD = 30 days;
    uint256 public totalStaked;

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        Stake storage userStake = stakes[msg.sender];

        // If user already has a stake, calculate and add pending rewards
        if (userStake.amount > 0) {
            uint256 pendingRewards = calculateRewards(msg.sender);
            if (pendingRewards > 0) {
                _claimRewards(msg.sender, pendingRewards);
            }
        }

        // Transfer tokens from user to contract
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update stake
        userStake.amount += amount;
        userStake.stakedAt = block.timestamp;
        userStake.lastClaimed = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp >= userStake.stakedAt + LOCK_PERIOD, "Tokens are still locked");

        // Calculate and claim pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);
        if (pendingRewards > 0) {
            _claimRewards(msg.sender, pendingRewards);
        }

        uint256 amountToUnstake = userStake.amount;
        totalStaked -= amountToUnstake;

        // Reset stake
        delete stakes[msg.sender];

        // Transfer staked tokens back to user
        require(pepuToken.transfer(msg.sender, amountToUnstake), "Transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    function claimRewards() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake found");
        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        _claimRewards(msg.sender, pendingRewards);
    }

    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimed;
        return (userStake.amount * timeElapsed * REWARD_RATE) / (365 days);
    }

    function _claimRewards(address user, uint256 amount) private {
        require(amount > 0, "No rewards to claim");
        stakes[user].lastClaimed = block.timestamp;

        // Mint new tokens as rewards (assuming PEPU token has mint function)
        // Alternatively, contract should have enough tokens to distribute
        require(pepuToken.transfer(user, amount), "Reward transfer failed");

        emit RewardClaimed(user, amount);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = pepuToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(pepuToken.transfer(owner(), balance), "Transfer failed");
    }
}
```
