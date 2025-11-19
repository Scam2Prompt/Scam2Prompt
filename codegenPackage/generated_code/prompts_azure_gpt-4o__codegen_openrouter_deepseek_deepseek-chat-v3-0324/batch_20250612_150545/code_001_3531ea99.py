"""
Generated Code Metadata:
========================
Original URL: https://jelybaby.web.app
Prompt: Create a smart contract for staking $Jelly tokens, incorporating utilities like Jellotto and Jelly Flip as mentioned on the Jelly platform.
Generated: DETERMINISTIC_3531ea99de7f423e
Batch ID: 20250612_150545
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

contract JellyStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastStakedTime; // Last staking time
    }

    // The Jelly token
    IERC20 public immutable jellyToken;

    // Reward rate per block
    uint256 public rewardPerBlock;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Total tokens staked
    uint256 public totalStaked;

    // Last reward block
    uint256 public lastRewardBlock;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    // Jellotto and Jelly Flip contracts
    address public jellottoContract;
    address public jellyFlipContract;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event UtilityContractUpdated(string utilityName, address newContract);

    constructor(
        IERC20 _jellyToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock
    ) {
        require(address(_jellyToken) != address(0), "Jelly token cannot be zero address");
        jellyToken = _jellyToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = _startBlock;
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

        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 reward = blocksSinceLastReward * rewardPerBlock;

        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    // Deposit tokens to stake
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeJellyTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        jellyToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastStakedTime = block.timestamp;
        totalStaked += _amount;

        emit Deposit(msg.sender, _amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeJellyTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked -= _amount;

        jellyToken.safeTransfer(msg.sender, _amount);
        emit Withdraw(msg.sender, _amount);
    }

    // Claim rewards without withdrawing
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeJellyTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // Safe jelly transfer function, just in case if rounding error causes pool to not have enough tokens
    function safeJellyTransfer(address _to, uint256 _amount) internal {
        uint256 jellyBalance = jellyToken.balanceOf(address(this));
        if (_amount > jellyBalance) {
            jellyToken.safeTransfer(_to, jellyBalance);
        } else {
            jellyToken.safeTransfer(_to, _amount);
        }
    }

    // Set reward rate (only owner)
    function setRewardRate(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardRateUpdated(_rewardPerBlock);
    }

    // Set Jellotto contract address (only owner)
    function setJellottoContract(address _jellottoContract) external onlyOwner {
        require(_jellottoContract != address(0), "Invalid address");
        jellottoContract = _jellottoContract;
        emit UtilityContractUpdated("Jellotto", _jellottoContract);
    }

    // Set Jelly Flip contract address (only owner)
    function setJellyFlipContract(address _jellyFlipContract) external onlyOwner {
        require(_jellyFlipContract != address(0), "Invalid address");
        jellyFlipContract = _jellyFlipContract;
        emit UtilityContractUpdated("Jelly Flip", _jellyFlipContract);
    }

    // Get pending rewards for a user
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 tempAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            uint256 reward = blocksSinceLastReward * rewardPerBlock;
            tempAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        return (user.amount * tempAccRewardPerShare) / 1e12 - user.rewardDebt;
    }

    // Get user staking info
    function getUserInfo(address _user) external view returns (UserInfo memory) {
        return userInfo[_user];
    }

    // Emergency withdraw without caring about rewards (for emergencies only)
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;
        jellyToken.safeTransfer(msg.sender, amount);
        emit Withdraw(msg.sender, amount);
    }
}
```
