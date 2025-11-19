"""
Generated Code Metadata:
========================
Original URL: https://sanctumio.pages.dev
Prompt: Generate a sample code snippet in Solidity to create a smart contract that interacts with the Infinity Pool, allowing users to stake their INF tokens and earn rewards.
Generated: DETERMINISTIC_7bc62698eb6c49f9
Batch ID: 20250622_211454
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

/**
 * @title Infinity Pool Staking Contract
 * @dev Allows users to stake INF tokens and earn rewards
 */
contract InfinityPoolStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
    }

    // The INF token contract
    IERC20 public immutable infToken;

    // Reward token (could be same as INF or different)
    IERC20 public immutable rewardToken;

    // Reward tokens per block
    uint256 public rewardPerBlock;

    // Last block number where rewards were calculated
    uint256 public lastRewardBlock;

    // Accumulated rewards per share, times 1e12
    uint256 public accRewardPerShare;

    // Total staked tokens
    uint256 public totalStaked;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPerBlockUpdated(uint256 oldAmount, uint256 newAmount);

    /**
     * @dev Constructor
     * @param _infToken Address of the INF token contract
     * @param _rewardToken Address of the reward token contract
     * @param _rewardPerBlock Reward tokens per block
     */
    constructor(
        address _infToken,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) {
        require(_infToken != address(0), "INF token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        infToken = IERC20(_infToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update pool rewards
     */
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

    /**
     * @dev Deposit INF tokens to stake
     * @param _amount Amount of tokens to stake
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        infToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        totalStaked += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        require(_amount > 0, "Amount must be greater than zero");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        totalStaked -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        infToken.safeTransfer(msg.sender, _amount);
        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards without withdrawing staked tokens
     */
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Safe reward transfer function
     * @param _to Address to transfer rewards to
     * @param _amount Amount of rewards to transfer
     */
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (_amount > rewardBalance) {
            rewardToken.safeTransfer(_to, rewardBalance);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    /**
     * @dev Update reward per block (only owner)
     * @param _rewardPerBlock New reward per block amount
     */
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        updatePool();
        emit RewardPerBlockUpdated(rewardPerBlock, _rewardPerBlock);
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Emergency withdraw all tokens (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        rewardToken.safeTransfer(owner(), balance);
    }
}
```
