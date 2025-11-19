"""
Generated Code Metadata:
========================
Original URL: https://wisemonky-allocation.pages.dev
Prompt: "Design a simple staking contract for $monky using Solidity on the Ethereum blockchain."
Generated: DETERMINISTIC_91b38ca3982b025d
Batch ID: 20250622_210958
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

contract MonkyStaking is Ownable, ReentrancyGuard {
    IERC20 public monkyToken;

    struct Stake {
        uint256 amount;
        uint256 startTime;
    }

    uint256 public rewardRate = 10; // 10% APY
    uint256 public constant SECONDS_IN_YEAR = 31536000;

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(address _monkyToken) {
        require(_monkyToken != address(0), "Invalid token address");
        monkyToken = IERC20(_monkyToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            monkyToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        if (stakes[msg.sender].amount > 0) {
            _claimReward();
        }

        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            startTime: block.timestamp
        });

        emit Staked(msg.sender, amount);
    }

    function unstake() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake found");

        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 reward = calculateReward(msg.sender);

        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;

        require(
            monkyToken.transfer(msg.sender, stakedAmount + reward),
            "Transfer failed"
        );

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    function claimReward() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake found");
        uint256 reward = _claimReward();
        emit RewardClaimed(msg.sender, reward);
    }

    function _claimReward() private returns (uint256) {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            require(
                monkyToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            stakes[msg.sender].startTime = block.timestamp;
        }
        return reward;
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        return (userStake.amount * rewardRate * stakingDuration) / (SECONDS_IN_YEAR * 100);
    }

    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        rewardRate = newRate;
    }

    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(monkyToken), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
