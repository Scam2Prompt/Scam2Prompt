"""
Generated Code Metadata:
========================
Original URL: https://dogegovapp.com
Prompt: Write a Solidity contract that supports staking and unstaking $DOGEGOV memecoin, incorporating the community-driven principles described on the DOGEGOV website.
Generated: DETERMINISTIC_cbdc489af7d742c5
Batch ID: 20250612_150237
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

contract DogeGovStaking is Ownable, ReentrancyGuard {
    IERC20 public dogeGovToken;

    struct Stake {
        uint256 amount;
        uint256 startTime;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public constant MAX_STAKE_DURATION = 365 days;
    uint256 public constant REWARD_RATE = 10; // 10% annual reward

    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 reward, uint256 timestamp);

    constructor(address _dogeGovToken) {
        require(_dogeGovToken != address(0), "Invalid token address");
        dogeGovToken = IERC20(_dogeGovToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(dogeGovToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        if (stakes[msg.sender].amount > 0) {
            _updateStake(msg.sender);
        } else {
            stakes[msg.sender] = Stake(amount, block.timestamp);
        }

        totalStaked += amount;
        require(dogeGovToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit Staked(msg.sender, amount, block.timestamp);
    }

    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        require(stakingDuration >= MIN_STAKE_DURATION, "Minimum stake duration not met");

        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        totalStaked -= userStake.amount;
        delete stakes[msg.sender];

        require(dogeGovToken.transfer(msg.sender, totalAmount), "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward, block.timestamp);
    }

    function calculateReward(address staker) public view returns (uint256) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 effectiveDuration = stakingDuration > MAX_STAKE_DURATION 
            ? MAX_STAKE_DURATION 
            : stakingDuration;

        return (userStake.amount * REWARD_RATE * effectiveDuration) / (100 * 365 days);
    }

    function emergencyWithdraw() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        totalStaked -= userStake.amount;
        delete stakes[msg.sender];

        require(dogeGovToken.transfer(msg.sender, userStake.amount), "Transfer failed");
    }

    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Reward rate too high");
        REWARD_RATE = newRate;
    }

    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(dogeGovToken), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
