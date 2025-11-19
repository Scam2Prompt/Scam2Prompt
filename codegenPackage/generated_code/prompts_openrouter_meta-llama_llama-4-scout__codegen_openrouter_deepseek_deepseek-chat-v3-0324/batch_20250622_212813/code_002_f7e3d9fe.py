"""
Generated Code Metadata:
========================
Original URL: https://presale-alainetwork.pages.dev
Prompt: Generate a smart contract code in Solidity that handles token staking and dividend distribution for a cryptocurrency platform like ALAI Network.
Generated: DETERMINISTIC_f7e3d9fe44ee761e
Batch ID: 20250622_212813
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

contract StakingDividend is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Stake {
        uint256 amount;
        uint256 stakeTime;
        uint256 lastClaimTime;
    }

    uint256 public totalStaked;
    uint256 public rewardPerToken;
    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public constant MIN_STAKE_DURATION = 7 days;

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        if (stakes[msg.sender].amount > 0) {
            claimReward();
        }

        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            stakeTime: block.timestamp,
            lastClaimTime: block.timestamp
        });

        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        require(
            block.timestamp >= userStake.stakeTime + MIN_STAKE_DURATION,
            "Minimum stake duration not met"
        );

        claimReward();

        userStake.amount -= amount;
        totalStaked -= amount;

        require(
            stakingToken.transfer(msg.sender, amount),
            "Transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    function claimReward() public nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            require(
                rewardToken.balanceOf(address(this)) >= reward,
                "Insufficient reward tokens"
            );
            userStake.lastClaimTime = block.timestamp;
            require(
                rewardToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.lastClaimTime;
        uint256 annualReward = (userStake.amount * REWARD_RATE) / 100;
        uint256 reward = (annualReward * stakingDuration) / REWARD_INTERVAL;

        return reward;
    }

    function updateRewardToken(address _rewardToken) external onlyOwner {
        rewardToken = IERC20(_rewardToken);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.transfer(owner(), balance);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
