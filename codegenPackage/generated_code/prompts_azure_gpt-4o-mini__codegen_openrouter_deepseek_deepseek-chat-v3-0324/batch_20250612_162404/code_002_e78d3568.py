"""
Generated Code Metadata:
========================
Original URL: https://tokencatgirl.pages.dev
Prompt: Generate a code snippet for a decentralized application (DApp) that allows users to stake CATGIRL¢ tokens and earn rewards, based on the features outlined in the Catgirl ecosystem.
Generated: DETERMINISTIC_e78d356830c29c88
Batch ID: 20250612_162404
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

/**
 * @title Catgirl Staking Contract
 * @dev Allows users to stake CATGIRL¢ tokens and earn rewards
 */
contract CatgirlStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastStaked; // Timestamp of last stake
    }

    // The CATGIRL¢ token contract
    IERC20 public catgirlToken;

    // Reward token (could be same as staking token)
    IERC20 public rewardToken;

    // Reward rate per block
    uint256 public rewardPerBlock;

    // Last block number that rewards were calculated
    uint256 public lastRewardBlock;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Total tokens staked
    uint256 public totalStaked;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor
     * @param _catgirlToken Address of the CATGIRL¢ token
     * @param _rewardToken Address of the reward token
     * @param _rewardPerBlock Reward rate per block
     */
    constructor(
        IERC20 _catgirlToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock
    ) {
        require(address(_catgirlToken) != address(0), "Invalid token address");
        require(address(_rewardToken) != address(0), "Invalid reward token address");
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");

        catgirlToken = _catgirlToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update reward variables
     */
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

    /**
     * @dev Stake CATGIRL¢ tokens
     * @param _amount Amount to stake
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        catgirlToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastStaked = block.timestamp;
        totalStaked += _amount;

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     * @param _amount Amount to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked -= _amount;

        catgirlToken.safeTransfer(msg.sender, _amount);
        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards without withdrawing staked tokens
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
     * @dev Emergency withdraw without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;

        catgirlToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Safe reward transfer function
     * @param _to Address to transfer to
     * @param _amount Amount to transfer
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
     * @dev Update reward rate
     * @param _rewardPerBlock New reward rate per block
     */
    function updateRewardRate(uint256 _rewardPerBlock) external onlyOwner {
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardRateUpdated(_rewardPerBlock);
    }

    /**
     * @dev View function to see pending rewards
     * @param _user Address of user
     * @return Pending rewards for user
     */
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocks = block.number - lastRewardBlock;
            uint256 reward = blocks * rewardPerBlock;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        
        return (user.amount * currentAccRewardPerShare) / 1e12 - user.rewardDebt;
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(catgirlToken), "Cannot recover staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
