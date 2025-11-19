"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-in.web.app
Prompt: Develop a smart contract code snippet for staking $POODL tokens and earning rewards, based on the project's staking kennel mechanism.
Generated: DETERMINISTIC_faeb8d758775f024
Batch ID: 20250622_210650
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

contract PoodlStakingKennel is Ownable, ReentrancyGuard {
    IERC20 public poodlToken;
    IERC20 public rewardToken;

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }

    uint256 public constant REWARD_RATE = 10; // 10% APY
    uint256 public constant REWARD_INTERVAL = 1 days;
    uint256 public totalStaked;
    uint256 public lastRewardTime;
    uint256 public accRewardPerShare;

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _poodlToken, address _rewardToken) {
        require(_poodlToken != address(0), "Invalid POODL token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        poodlToken = IERC20(_poodlToken);
        rewardToken = IERC20(_rewardToken);
        lastRewardTime = block.timestamp;
    }

    function updateReward() internal {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            return;
        }

        uint256 timePassed = block.timestamp - lastRewardTime;
        uint256 rewardAmount = (totalStaked * REWARD_RATE * timePassed) / (365 days * 100);
        
        if (rewardAmount > 0) {
            accRewardPerShare += (rewardAmount * 1e12) / totalStaked;
        }
        
        lastRewardTime = block.timestamp;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        updateReward();
        
        if (stakes[msg.sender].amount > 0) {
            uint256 pending = (stakes[msg.sender].amount * accRewardPerShare) / 1e12 - stakes[msg.sender].rewardDebt;
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
            }
        }

        poodlToken.transferFrom(msg.sender, address(this), amount);
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].rewardDebt = (stakes[msg.sender].amount * accRewardPerShare) / 1e12;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        
        updateReward();
        
        uint256 pending = (stakes[msg.sender].amount * accRewardPerShare) / 1e12 - stakes[msg.sender].rewardDebt;
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
        }
        
        stakes[msg.sender].amount -= amount;
        stakes[msg.sender].rewardDebt = (stakes[msg.sender].amount * accRewardPerShare) / 1e12;
        totalStaked -= amount;
        
        poodlToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    function claimReward() external nonReentrant {
        updateReward();
        
        uint256 pending = (stakes[msg.sender].amount * accRewardPerShare) / 1e12 - stakes[msg.sender].rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        stakes[msg.sender].rewardDebt = (stakes[msg.sender].amount * accRewardPerShare) / 1e12;
        safeTransferReward(msg.sender, pending);
        
        emit RewardClaimed(msg.sender, pending);
    }

    function pendingReward(address user) external view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timePassed = block.timestamp - lastRewardTime;
            uint256 rewardAmount = (totalStaked * REWARD_RATE * timePassed) / (365 days * 100);
            currentAccRewardPerShare += (rewardAmount * 1e12) / totalStaked;
        }
        
        return (userStake.amount * currentAccRewardPerShare) / 1e12 - userStake.rewardDebt;
    }

    function safeTransferReward(address to, uint256 amount) internal {
        uint256 balance = rewardToken.balanceOf(address(this));
        if (amount > balance) {
            rewardToken.transfer(to, balance);
        } else {
            rewardToken.transfer(to, amount);
        }
    }

    function emergencyWithdraw() external nonReentrant {
        uint256 amount = stakes[msg.sender].amount;
        require(amount > 0, "No staked tokens");
        
        totalStaked -= amount;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        
        poodlToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    function setRewardToken(address _rewardToken) external onlyOwner {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(poodlToken), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
