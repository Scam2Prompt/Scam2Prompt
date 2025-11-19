"""
Generated Code Metadata:
========================
Original URL: https://web3tokenswap.com
Prompt: "Design a basic decentralized finance (DeFi) farming application using the DApp Mainnet platform, focusing on security and user adoption."
Generated: DETERMINISTIC_4543ed8d4f4100dc
Batch ID: 20250622_212235
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DeFiFarm is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent user stake
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Token contracts
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Farm parameters
    uint256 public rewardPerBlock;
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;
    uint256 public totalStaked;

    // User stakes mapping
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdrawn(address indexed user, uint256 amount);

    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    // Update reward variables
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksPassed = block.number.sub(lastRewardBlock);
        uint256 reward = blocksPassed.mul(rewardPerBlock);
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e12).div(totalStaked));
        lastRewardBlock = block.number;
    }

    // Stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        updatePool();

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        stakingToken.transferFrom(msg.sender, address(this), _amount);
        userStake.amount = userStake.amount.add(_amount);
        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 _amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Withdraw amount exceeds stake");
        updatePool();

        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        userStake.amount = userStake.amount.sub(_amount);
        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);
        totalStaked = totalStaked.sub(_amount);

        stakingToken.transfer(msg.sender, _amount);
        emit Withdrawn(msg.sender, _amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        updatePool();

        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
        require(pending > 0, "No rewards to claim");

        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);
        safeRewardTransfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    // Emergency withdraw without rewards
    function emergencyWithdraw() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        uint256 amount = userStake.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked = totalStaked.sub(amount);
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        stakingToken.transfer(msg.sender, amount);
        emit EmergencyWithdrawn(msg.sender, amount);
    }

    // Safe reward transfer function
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (_amount > rewardBalance) {
            rewardToken.transfer(_to, rewardBalance);
        } else {
            rewardToken.transfer(_to, _amount);
        }
    }

    // Owner functions
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
    }

    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
