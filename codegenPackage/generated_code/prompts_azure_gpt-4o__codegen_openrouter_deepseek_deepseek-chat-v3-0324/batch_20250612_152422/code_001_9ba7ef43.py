"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt-io.web.app
Prompt: Generate Solidity code for a staking contract compatible with the $GIGA token, ensuring LP tokens are locked and rewards are distributed based on staked amounts.
Generated: DETERMINISTIC_9ba7ef4362d5f6aa
Batch ID: 20250612_152422
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GigaStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many LP tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
    }

    // The GIGA token contract
    IERC20 public immutable gigaToken;
    // The LP token contract
    IERC20 public immutable lpToken;
    // Reward tokens per block
    uint256 public rewardPerBlock;
    // Last block number that rewards were calculated
    uint256 public lastRewardBlock;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    // Total LP tokens staked
    uint256 public totalStaked;

    // Info of each user that stakes LP tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPerBlockUpdated(uint256 oldReward, uint256 newReward);

    constructor(
        IERC20 _gigaToken,
        IERC20 _lpToken,
        uint256 _rewardPerBlock
    ) {
        require(address(_gigaToken) != address(0), "GIGA token address cannot be zero");
        require(address(_lpToken) != address(0), "LP token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        gigaToken = _gigaToken;
        lpToken = _lpToken;
        rewardPerBlock = _rewardPerBlock;
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

    // Deposit LP tokens to contract for GIGA allocation
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeGigaTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        if (_amount > 0) {
            lpToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            totalStaked += _amount;
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        emit Deposit(msg.sender, _amount);
    }

    // Withdraw LP tokens and claim rewards
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeGigaTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        if (_amount > 0) {
            user.amount -= _amount;
            totalStaked -= _amount;
            lpToken.safeTransfer(msg.sender, _amount);
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        emit Withdraw(msg.sender, _amount);
    }

    // Claim pending rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeGigaTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // Safe GIGA transfer function, just in case if rounding error causes pool to not have enough GIGA tokens
    function safeGigaTransfer(address _to, uint256 _amount) internal {
        uint256 gigaBalance = gigaToken.balanceOf(address(this));
        if (_amount > gigaBalance) {
            gigaToken.safeTransfer(_to, gigaBalance);
        } else {
            gigaToken.safeTransfer(_to, _amount);
        }
    }

    // Update reward per block (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        updatePool();
        emit RewardPerBlockUpdated(rewardPerBlock, _rewardPerBlock);
        rewardPerBlock = _rewardPerBlock;
    }

    // Emergency withdraw LP tokens without claiming rewards (only for emergencies)
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;

        lpToken.safeTransfer(msg.sender, amount);
        emit Withdraw(msg.sender, amount);
    }

    // Recover any ERC20 tokens sent to the contract by mistake (except LP and GIGA tokens)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(lpToken), "Cannot withdraw LP token");
        require(tokenAddress != address(gigaToken), "Cannot withdraw GIGA token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
