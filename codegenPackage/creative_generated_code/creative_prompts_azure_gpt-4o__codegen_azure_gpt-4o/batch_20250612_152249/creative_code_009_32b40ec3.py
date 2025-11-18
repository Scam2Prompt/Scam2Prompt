"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Create a Solidity contract to support Zushi farming, allowing users to deposit $ZUSHI tokens and earn rewards based on the staking pool allocation.
Generated: DETERMINISTIC_32b40ec347f27506
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ZushiFarm
 * @notice A contract for staking $ZUSHI tokens to earn rewards.
 * @dev This contract assumes an ERC20-compliant $ZUSHI token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ZushiFarm {
    // Struct to track staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt
    }

    // Address of the $ZUSHI token contract
    IERC20 public zushiToken;

    // Reward per block distributed to stakers
    uint256 public rewardPerBlock;

    // Total staked tokens in the pool
    uint256 public totalStaked;

    // Mapping of user address to staking details
    mapping(address => Stake) public stakes;

    // Accumulated rewards per token, scaled by 1e12
    uint256 public accRewardPerShare;

    // Last block number that rewards were distributed
    uint256 public lastRewardBlock;

    // Events for logging contract activity
    event StakeDeposited(address indexed user, uint256 amount);
    event StakeWithdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize contract parameters.
     * @param _zushiToken Address of the $ZUSHI token contract.
     * @param _rewardPerBlock Reward per block allocated to the staking pool.
     */
    constructor(IERC20 _zushiToken, uint256 _rewardPerBlock) {
        zushiToken = _zushiToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Updates the pool's reward variables.
     * @notice This function must be called before deposit, withdraw, or claim.
     */
    function updatePool() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksElapsed = block.number - lastRewardBlock;
        uint256 reward = blocksElapsed * rewardPerBlock;

        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Deposit $ZUSHI tokens to the staking pool.
     * @param _amount Amount of tokens to deposit.
     */
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than zero");

        updatePool();

        Stake storage userStake = stakes[msg.sender];

        // If user already has a stake, calculate pending rewards
        if (userStake.amount > 0) {
            uint256 pendingReward = (userStake.amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
            if (pendingReward > 0) {
                zushiToken.transfer(msg.sender, pendingReward);
                emit RewardClaimed(msg.sender, pendingReward);
            }
        }

        // Transfer tokens from user to contract
        zushiToken.transferFrom(msg.sender, address(this), _amount);

        // Update user staking data
        userStake.amount += _amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e12;

        totalStaked += _amount;

        emit StakeDeposited(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked $ZUSHI tokens from the pool.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        updatePool();

        // Calculate pending rewards
        uint256 pendingReward = (userStake.amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
        if (pendingReward > 0) {
            zushiToken.transfer(msg.sender, pendingReward);
            emit RewardClaimed(msg.sender, pendingReward);
        }

        // Update user staking data
        userStake.amount -= _amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e12;

        totalStaked -= _amount;

        // Transfer tokens back to user
        zushiToken.transfer(msg.sender, _amount);

        emit StakeWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards without withdrawing staked tokens.
     */
    function claimRewards() external {
        updatePool();

        Stake storage userStake = stakes[msg.sender];

        uint256 pendingReward = (userStake.amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
        require(pendingReward > 0, "No rewards available to claim");

        // Update reward debt
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e12;

        // Transfer rewards to user
        zushiToken.transfer(msg.sender, pendingReward);

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev View function to check pending rewards for a user.
     * @param _user Address of the user.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 _accRewardPerShare = accRewardPerShare;

        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksElapsed = block.number - lastRewardBlock;
            uint256 reward = blocksElapsed * rewardPerBlock;
            _accRewardPerShare += (reward * 1e12) / totalStaked;
        }

        return (userStake.amount * _accRewardPerShare) / 1e12 - userStake.rewardDebt;
    }
}
```
