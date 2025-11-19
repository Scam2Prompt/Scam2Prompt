"""
Generated Code Metadata:
========================
Original URL: https://polygon6d.com
Prompt: Create a Solidity contract that implements the six degrees of separation theory for staking rewards distribution, as described in Polygon6D.
Generated: DETERMINISTIC_397566b3117bf1df
Batch ID: 20250612_150644
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

contract Polygon6D is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    uint256 public totalStaked;
    uint256 public rewardPerLevel;
    uint256 public maxLevels = 6;
    uint256 public stakingDuration = 30 days;
    uint256 public lastRewardDistribution;

    struct Staker {
        address upline;
        uint256 amount;
        uint256 stakeTime;
        uint256 claimedRewards;
        address[] referrals;
    }

    mapping(address => Staker) public stakers;
    mapping(address => bool) public isStaker;

    event Staked(address indexed user, address indexed upline, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, address indexed referral, uint256 level, uint256 amount);

    constructor(address _rewardToken, uint256 _rewardPerLevel) {
        rewardToken = IERC20(_rewardToken);
        rewardPerLevel = _rewardPerLevel;
        lastRewardDistribution = block.timestamp;
    }

    function stake(uint256 _amount, address _upline) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(!isStaker[msg.sender], "Already staked");
        require(_upline != msg.sender, "Cannot refer yourself");
        require(_upline == address(0) || isStaker[_upline], "Upline must be staker or zero");

        rewardToken.transferFrom(msg.sender, address(this), _amount);

        Staker storage newStaker = stakers[msg.sender];
        newStaker.upline = _upline;
        newStaker.amount = _amount;
        newStaker.stakeTime = block.timestamp;
        newStaker.claimedRewards = 0;

        if (_upline != address(0)) {
            stakers[_upline].referrals.push(msg.sender);
        }

        totalStaked += _amount;
        isStaker[msg.sender] = true;

        emit Staked(msg.sender, _upline, _amount);
    }

    function unstake() external nonReentrant {
        require(isStaker[msg.sender], "Not staked");
        Staker storage staker = stakers[msg.sender];

        require(block.timestamp >= staker.stakeTime + stakingDuration, "Staking period not ended");

        uint256 amount = staker.amount;
        rewardToken.transfer(msg.sender, amount);

        totalStaked -= amount;
        isStaker[msg.sender] = false;

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        require(isStaker[msg.sender], "Not staked");
        distributeRewards();
        
        Staker storage staker = stakers[msg.sender];
        uint256 claimable = calculateRewards(msg.sender) - staker.claimedRewards;
        require(claimable > 0, "No rewards to claim");

        staker.claimedRewards += claimable;
        rewardToken.transfer(msg.sender, claimable);

        emit RewardClaimed(msg.sender, claimable);
    }

    function distributeRewards() public {
        if (block.timestamp <= lastRewardDistribution + 1 days) {
            return;
        }

        uint256 daysPassed = (block.timestamp - lastRewardDistribution) / 1 days;
        lastRewardDistribution += daysPassed * 1 days;

        for (uint256 i = 0; i < daysPassed; i++) {
            _distributeDailyRewards();
        }
    }

    function _distributeDailyRewards() private {
        uint256 totalRewards = rewardPerLevel * maxLevels;
        require(rewardToken.balanceOf(address(this)) >= totalStaked + totalRewards, "Insufficient contract balance");

        address[] memory activeStakers = _getActiveStakers();
        for (uint256 i = 0; i < activeStakers.length; i++) {
            address staker = activeStakers[i];
            _distributeReferralRewards(staker);
        }
    }

    function _distributeReferralRewards(address _staker) private {
        address current = _staker;
        for (uint256 level = 1; level <= maxLevels; level++) {
            current = stakers[current].upline;
            if (current == address(0)) break;

            rewardToken.transfer(current, rewardPerLevel);
            emit RewardDistributed(_staker, current, level, rewardPerLevel);
        }
    }

    function calculateRewards(address _staker) public view returns (uint256) {
        if (!isStaker[_staker]) return 0;

        Staker storage staker = stakers[_staker];
        uint256 daysStaked = (block.timestamp - staker.stakeTime) / 1 days;
        uint256 maxDays = stakingDuration / 1 days;
        daysStaked = daysStaked > maxDays ? maxDays : daysStaked;

        return (staker.amount * daysStaked * rewardPerLevel) / (totalStaked > 0 ? totalStaked : 1);
    }

    function _getActiveStakers() private view returns (address[] memory) {
        uint256 count = 0;
        for (uint256 i = 0; i < _getStakerCount(); i++) {
            address staker = _getStakerAtIndex(i);
            if (isStaker[staker] && block.timestamp < stakers[staker].stakeTime + stakingDuration) {
                count++;
            }
        }

        address[] memory activeStakers = new address[](count);
        count = 0;
        for (uint256 i = 0; i < _getStakerCount(); i++) {
            address staker = _getStakerAtIndex(i);
            if (isStaker[staker] && block.timestamp < stakers[staker].stakeTime + stakingDuration) {
                activeStakers[count] = staker;
                count++;
            }
        }

        return activeStakers;
    }

    function _getStakerCount() private view returns (uint256) {
        // In a real implementation, you would track staker count
        // This is a simplified version
        return 1000; // Placeholder
    }

    function _getStakerAtIndex(uint256 index) private view returns (address) {
        // In a real implementation, you would have a way to iterate stakers
        // This is a simplified version
        return address(0); // Placeholder
    }

    function setRewardPerLevel(uint256 _rewardPerLevel) external onlyOwner {
        rewardPerLevel = _rewardPerLevel;
    }

    function setMaxLevels(uint256 _maxLevels) external onlyOwner {
        require(_maxLevels > 0, "Max levels must be greater than 0");
        maxLevels = _maxLevels;
    }

    function setStakingDuration(uint256 _stakingDuration) external onlyOwner {
        stakingDuration = _stakingDuration;
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        rewardToken.transfer(owner(), balance);
    }
}
```
