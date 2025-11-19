"""
Generated Code Metadata:
========================
Original URL: https://tgcasino-app.pages.dev
Prompt: Create a Solidity contract to implement TG.Casino's staking system, including immediate reward distribution and revenue-based rewards.
Generated: DETERMINISTIC_8996762e54db1adb
Batch ID: 20250612_153517
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

contract TGCasinoStaking is Ownable, ReentrancyGuard {
    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardToken;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public rewardDuration = 7 days;
    uint256 public periodFinish;

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardAdded(uint256 reward);
    event RevenueShared(uint256 amount);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < periodFinish ? block.timestamp : periodFinish;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    function earned(address account) public view returns (uint256) {
        return
            ((stakes[account].amount * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            _claimReward();
        }

        totalStaked += amount;
        userStake.amount += amount;
        userStake.rewardDebt = (userStake.amount * rewardPerTokenStored) / 1e18;
        userStake.lastStakeTime = block.timestamp;

        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient balance");

        _claimReward();

        totalStaked -= amount;
        userStake.amount -= amount;
        userStake.rewardDebt = (userStake.amount * rewardPerTokenStored) / 1e18;

        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function exit() external {
        withdraw(stakes[msg.sender].amount);
    }

    function claimReward() public nonReentrant updateReward(msg.sender) {
        _claimReward();
    }

    function _claimReward() internal {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function notifyRewardAmount(uint256 reward) external onlyOwner updateReward(address(0)) {
        require(reward > 0, "No reward");

        if (block.timestamp >= periodFinish) {
            rewardRate = reward / rewardDuration;
        } else {
            uint256 remaining = periodFinish - block.timestamp;
            uint256 leftover = remaining * rewardRate;
            rewardRate = (reward + leftover) / rewardDuration;
        }

        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardRate <= balance / rewardDuration, "Reward too high");

        lastUpdateTime = block.timestamp;
        periodFinish = block.timestamp + rewardDuration;
        emit RewardAdded(reward);
    }

    function shareRevenue(uint256 amount) external onlyOwner {
        require(amount > 0, "No revenue");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit RevenueShared(amount);
    }

    function setRewardDuration(uint256 _duration) external onlyOwner {
        require(_duration > 0, "Invalid duration");
        rewardDuration = _duration;
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
