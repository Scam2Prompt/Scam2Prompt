"""
Generated Code Metadata:
========================
Original URL: https://trustbase.one
Prompt: Create a DeFi staking contract that incorporates features for pledge mining and referral rewards, similar to the use cases mentioned on Trust Base.
Generated: DETERMINISTIC_5575bee0a7a8f3b0
Batch ID: 20250612_153814
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

contract DeFiStaking is Ownable, ReentrancyGuard {
    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;         // Amount of tokens staked by user
        uint256 rewardDebt;     // Reward debt for calculating pending rewards
        uint256 referralBonus;  // Referral bonus accumulated
        address referrer;       // Address of referrer
    }

    // The staking token
    IERC20 public stakingToken;
    // The reward token
    IERC20 public rewardToken;

    // Reward rate per block
    uint256 public rewardPerBlock;
    // Last block number that rewards were calculated
    uint256 public lastRewardBlock;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    // Total tokens staked
    uint256 public totalStaked;

    // Referral commission rate (percentage)
    uint256 public referralCommissionRate = 10; // 10%
    // Minimum stake amount
    uint256 public minStakeAmount;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ReferralBonusPaid(address indexed referrer, address indexed user, uint256 bonusAmount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _minStakeAmount
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        minStakeAmount = _minStakeAmount;
        lastRewardBlock = block.number;
    }

    // Update reward variables to be up-to-date
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocks = block.number - lastRewardBlock;
        uint256 reward = blocks * rewardPerBlock;
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    // Deposit tokens to contract for staking
    function deposit(uint256 _amount, address _referrer) external nonReentrant {
        require(_amount >= minStakeAmount, "Amount below minimum stake");
        UserInfo storage user = userInfo[msg.sender];

        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        if (_amount > 0) {
            uint256 beforeBalance = stakingToken.balanceOf(address(this));
            stakingToken.transferFrom(msg.sender, address(this), _amount);
            _amount = stakingToken.balanceOf(address(this)) - beforeBalance;

            user.amount += _amount;
            totalStaked += _amount;

            // Handle referral
            if (user.referrer == address(0) && _referrer != address(0) && _referrer != msg.sender) {
                user.referrer = _referrer;
            }
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        emit Deposit(msg.sender, _amount);
    }

    // Withdraw staked tokens and collect rewards
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        if (_amount > 0) {
            user.amount -= _amount;
            totalStaked -= _amount;
            stakingToken.transfer(msg.sender, _amount);
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        emit Withdraw(msg.sender, _amount);
    }

    // Claim pending rewards
    function claimReward() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
            emit RewardClaimed(msg.sender, pending);
        }

        // Claim referral bonus if any
        if (user.referralBonus > 0) {
            uint256 bonus = user.referralBonus;
            user.referralBonus = 0;
            safeRewardTransfer(msg.sender, bonus);
            emit RewardClaimed(msg.sender, bonus);
        }
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;
        user.referralBonus = 0;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (_amount > rewardBalance) {
            rewardToken.transfer(_to, rewardBalance);
        } else {
            rewardToken.transfer(_to, _amount);
        }
    }

    // Pay referral commission to the referrer
    function payReferralCommission(address _user, uint256 _pending) internal {
        UserInfo storage user = userInfo[_user];
        if (user.referrer != address(0) && referralCommissionRate > 0) {
            uint256 commissionAmount = (_pending * referralCommissionRate) / 100;
            userInfo[user.referrer].referralBonus += commissionAmount;
            emit ReferralBonusPaid(user.referrer, _user, commissionAmount);
        }
    }

    // View function to see pending rewards on frontend
    function pendingReward(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocks = block.number - lastRewardBlock;
            uint256 reward = blocks * rewardPerBlock;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        return (user.amount * currentAccRewardPerShare) / 1e12 - user.rewardDebt;
    }

    // View function to see referral bonus
    function pendingReferralBonus(address _user) external view returns (uint256) {
        return userInfo[_user].referralBonus;
    }

    // Owner functions
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
    }

    function setReferralCommissionRate(uint256 _rate) external onlyOwner {
        require(_rate <= 20, "Commission rate too high");
        referralCommissionRate = _rate;
    }

    function setMinStakeAmount(uint256 _minStakeAmount) external onlyOwner {
        minStakeAmount = _minStakeAmount;
    }

    // Recover any ERC20 tokens sent to the contract by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
