"""
Generated Code Metadata:
========================
Original URL: https://swiftchain-node.pages.dev
Prompt: Implement a staking-related functionality using a decentralized protocol, including activation, exchange, and whitelist management.
Generated: DETERMINISTIC_7702cf9dd07aec57
Batch ID: 20250622_210914
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingContract is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        bool isActive;
    }

    mapping(address => Stake) public stakes;
    mapping(address => bool) public whitelist;

    uint256 public stakingDuration = 30 days;
    uint256 public rewardRate = 10; // 10% reward
    uint256 public totalStaked;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event Whitelisted(address indexed user, bool status);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "Not whitelisted");
        _;
    }

    function stake(uint256 amount) external nonReentrant onlyWhitelisted {
        require(amount > 0, "Amount must be greater than 0");
        require(!stakes[msg.sender].isActive, "Already staked");

        stakes[msg.sender] = Stake({
            amount: amount,
            stakedAt: block.timestamp,
            isActive: true
        });

        totalStaked += amount;

        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        emit Staked(msg.sender, amount);
    }

    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake");
        require(
            block.timestamp >= userStake.stakedAt + stakingDuration,
            "Staking period not ended"
        );

        uint256 stakedAmount = userStake.amount;
        uint256 reward = (stakedAmount * rewardRate) / 100;

        totalStaked -= stakedAmount;
        userStake.isActive = false;

        require(
            stakingToken.transfer(msg.sender, stakedAmount),
            "Transfer failed"
        );
        require(
            rewardToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    function addToWhitelist(address user) external onlyOwner {
        whitelist[user] = true;
        emit Whitelisted(user, true);
    }

    function removeFromWhitelist(address user) external onlyOwner {
        whitelist[user] = false;
        emit Whitelisted(user, false);
    }

    function updateStakingDuration(uint256 newDuration) external onlyOwner {
        stakingDuration = newDuration;
    }

    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        stakingToken.transfer(owner(), balance);
    }
}
```
