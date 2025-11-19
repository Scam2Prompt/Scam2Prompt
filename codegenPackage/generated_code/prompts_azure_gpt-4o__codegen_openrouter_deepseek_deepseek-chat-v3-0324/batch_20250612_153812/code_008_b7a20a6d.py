"""
Generated Code Metadata:
========================
Original URL: https://kenduinu-an.web.app
Prompt: Write a Solidity contract to implement a reward distribution mechanism for Kendu Inu, ensuring fair allocation of staking rewards to token holders.
Generated: DETERMINISTIC_b7a20a6d4252a05c
Batch ID: 20250612_153812
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

contract KenduInuRewardDistributor is Ownable, ReentrancyGuard {
    IERC20 public kenduInuToken;
    IERC20 public rewardToken;

    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 pendingRewards;
    }

    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public rewardDuration = 7 days;

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(address _kenduInuToken, address _rewardToken) {
        require(_kenduInuToken != address(0), "Invalid Kendu Inu token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        kenduInuToken = IERC20(_kenduInuToken);
        rewardToken = IERC20(_rewardToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        
        if (account != address(0)) {
            stakers[account].pendingRewards = earned(account);
            stakers[account].rewardDebt = stakers[account].amountStaked * rewardPerTokenStored / 1e18;
        }
        _;
    }

    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < (lastUpdateTime + rewardDuration) ? block.timestamp : (lastUpdateTime + rewardDuration);
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18 / totalStaked
        );
    }

    function earned(address account) public view returns (uint256) {
        Staker memory staker = stakers[account];
        return staker.amountStaked * (rewardPerToken() - staker.rewardDebt) / 1e18 + staker.pendingRewards;
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        totalStaked += amount;
        staker.amountStaked += amount;
        staker.rewardDebt = staker.amountStaked * rewardPerTokenStored / 1e18;
        
        require(kenduInuToken.transferFrom(msg.sender, address(this, amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        totalStaked -= amount;
        staker.amountStaked -= amount;
        staker.rewardDebt = staker.amountStaked * rewardPerTokenStored / 1e18;
        
        require(kenduInuToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = stakers[msg.sender].pendingRewards;
        if (reward > 0) {
            stakers[msg.sender].pendingRewards = 0;
            require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(stakers[msg.sender].amountStaked);
        getReward();
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner updateReward(address(0)) {
        require(_rewardRate > 0, "Reward rate must be positive");
        
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
        emit RewardRateUpdated(_rewardRate);
    }

    function notifyRewardAmount(uint256 reward) external onlyOwner updateReward(address(0)) {
        require(reward > 0, "No reward provided");
        
        uint256 balance = rewardToken.balanceOf(address(this));
        require(reward <= balance, "Insufficient reward token balance");
        
        rewardRate = reward / rewardDuration;
        lastUpdateTime = block.timestamp;
        emit RewardRateUpdated(rewardRate);
    }

    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amountStaked;
        require(amount > 0, "No staked amount");
        
        totalStaked -= amount;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;
        staker.pendingRewards = 0;
        
        require(kenduInuToken.transfer(msg.sender, amount), "Transfer failed");
        emit EmergencyWithdraw(msg.sender, amount);
    }

    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(kenduInuToken), "Cannot withdraw staking token");
        require(tokenAddress != address(rewardToken), "Cannot withdraw reward token");
        
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
