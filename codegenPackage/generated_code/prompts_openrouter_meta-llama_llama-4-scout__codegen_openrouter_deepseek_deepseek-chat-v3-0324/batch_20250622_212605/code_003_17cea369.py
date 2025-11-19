"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Generate a smart contract code snippet in Solidity for a custom staking pool on Story Staking, incorporating dynamic interest rates and automated reward distribution.
Generated: DETERMINISTIC_17cea369ad8f97c4
Batch ID: 20250622_212605
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

contract StoryStakingPool is ReentrancyGuard, Ownable {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 lastClaimTime;
    }

    uint256 public totalStaked;
    uint256 public rewardRate = 10; // Base reward rate (percentage)
    uint256 public rewardInterval = 1 days;
    uint256 public minStakeDuration = 7 days;
    uint256 public maxStakeDuration = 365 days;
    uint256 public dynamicRateFactor = 2; // Factor for dynamic rate calculation

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public pendingRewards;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }

        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + _amount,
            timestamp: block.timestamp,
            lastClaimTime: block.timestamp
        });

        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp >= userStake.timestamp + minStakeDuration, "Minimum stake duration not met");

        _claimRewards();

        uint256 amount = userStake.amount;
        totalStaked -= amount;
        delete stakes[msg.sender];

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount == 0) return;

        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            pendingRewards[msg.sender] = 0;
            userStake.lastClaimTime = block.timestamp;
            
            require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.lastClaimTime;
        if (stakingDuration == 0) return 0;

        uint256 effectiveRate = getDynamicRate(userStake.timestamp);
        uint256 reward = (userStake.amount * effectiveRate * stakingDuration) / 
                        (100 * rewardInterval * 365 days);

        return reward + pendingRewards[_user];
    }

    function getDynamicRate(uint256 _stakeTimestamp) public view returns (uint256) {
        uint256 stakeDuration = block.timestamp - _stakeTimestamp;
        uint256 durationFactor = stakeDuration / (30 days); // Monthly factor
        
        // Cap the duration factor to prevent excessive rewards
        if (durationFactor > 12) durationFactor = 12;
        
        return rewardRate + (durationFactor * dynamicRateFactor);
    }

    function setRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Rate must be greater than 0");
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    function setDynamicRateFactor(uint256 _factor) external onlyOwner {
        dynamicRateFactor = _factor;
    }

    function withdrawRewardTokens(uint256 _amount) external onlyOwner {
        require(rewardToken.transfer(owner(), _amount), "Transfer failed");
    }

    function emergencyWithdraw() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");

        uint256 amount = userStake.amount;
        totalStaked -= amount;
        delete stakes[msg.sender];

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }
}
```
