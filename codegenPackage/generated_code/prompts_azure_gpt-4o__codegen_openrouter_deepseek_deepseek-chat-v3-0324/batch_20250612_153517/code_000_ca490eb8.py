"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Write a smart contract in Solidity for staking $HEHE tokens that includes a reward distribution mechanism based on the user's share of the staking pool fees, as described in the HEHE ecosystem.
Generated: DETERMINISTIC_ca490eb83e70f900
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract HEHEStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;         // Amount of tokens staked by user
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastClaimTime;  // Last time user claimed rewards
    }

    // The HEHE token contract
    IERC20 public immutable heheToken;

    // Total amount of HEHE tokens staked
    uint256 public totalStaked;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Last time rewards were calculated
    uint256 public lastRewardTime;

    // Reward distribution rate (rewards per second)
    uint256 public rewardRate;

    // Precision factor for reward calculations
    uint256 private constant PRECISION_FACTOR = 1e12;

    // Minimum staking duration (in seconds)
    uint256 public constant MIN_STAKING_DURATION = 7 days;

    // Mapping of user addresses to their staking info
    mapping(address => UserInfo) public userInfo;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(IERC20 _heheToken, uint256 _rewardRate) {
        require(address(_heheToken) != address(0), "Invalid token address");
        heheToken = _heheToken;
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
    }

    // Update reward variables to be up-to-date
    function updatePool() public {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 rewards = timeElapsed * rewardRate;

        accRewardPerShare += (rewards * PRECISION_FACTOR) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    // Stake HEHE tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
            if (pending > 0) {
                safeHeheTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        heheToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaimTime = block.timestamp;

        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    // Unstake HEHE tokens and claim rewards
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp >= user.lastClaimTime + MIN_STAKING_DURATION, "Minimum staking duration not met");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        if (pending > 0) {
            safeHeheTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        if (_amount > 0) {
            user.amount -= _amount;
            heheToken.safeTransfer(msg.sender, _amount);
            emit Unstaked(msg.sender, _amount);
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaimTime = block.timestamp;
        totalStaked -= _amount;
    }

    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No staked tokens");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        safeHeheTransfer(msg.sender, pending);
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaimTime = block.timestamp;

        emit RewardClaimed(msg.sender, pending);
    }

    // Safe HEHE transfer function, just in case if rounding error causes pool to not have enough HEHE
    function safeHeheTransfer(address _to, uint256 _amount) internal {
        uint256 heheBalance = heheToken.balanceOf(address(this));
        if (_amount > heheBalance) {
            heheToken.safeTransfer(_to, heheBalance);
        } else {
            heheToken.safeTransfer(_to, _amount);
        }
    }

    // Update reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updatePool();
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;

        heheToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // View function to see pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 rewards = timeElapsed * rewardRate;
            currentAccRewardPerShare += (rewards * PRECISION_FACTOR) / totalStaked;
        }

        return (user.amount * currentAccRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
    }

    // Recover any ERC20 tokens sent to the contract by mistake (except HEHE tokens)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(heheToken), "Cannot recover HEHE tokens");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
