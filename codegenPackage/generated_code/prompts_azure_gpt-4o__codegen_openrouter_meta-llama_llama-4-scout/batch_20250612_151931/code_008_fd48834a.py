"""
Generated Code Metadata:
========================
Original URL: https://wenwen.pages.dev
Prompt: Write a Solidity contract to enable staking of WEN tokens with rewards distributed based on tokenomics principles.
Generated: DETERMINISTIC_fd48834a196172b4
Batch ID: 20250612_151931
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title WenStakingContract
 * @author [Your Name]
 * @notice This contract enables staking of WEN tokens with rewards distributed based on tokenomics principles.
 */
contract WenStakingContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // WEN token contract
    IERC20 public wenToken;

    // Reward token contract (same as WEN for simplicity)
    IERC20 public rewardToken;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Reward per share
    uint256 public rewardPerShare;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward distribution interval (in seconds)
    uint256 public rewardInterval;

    // Last reward distribution timestamp
    uint256 public lastRewardTimestamp;

    // Reward per interval
    uint256 public rewardPerInterval;

    /**
     * @notice Constructor
     * @param _wenToken WEN token contract address
     * @param _rewardToken Reward token contract address (same as WEN for simplicity)
     * @param _rewardInterval Reward distribution interval (in seconds)
     * @param _rewardPerInterval Reward per interval
     */
    constructor(
        address _wenToken,
        address _rewardToken,
        uint256 _rewardInterval,
        uint256 _rewardPerInterval
    ) public {
        wenToken = IERC20(_wenToken);
        rewardToken = IERC20(_rewardToken);
        rewardInterval = _rewardInterval;
        rewardPerInterval = _rewardPerInterval;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @notice Stake WEN tokens
     * @param _amount Amount of WEN tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        // Transfer WEN tokens from user to contract
        wenToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake WEN tokens
     * @param _amount Amount of WEN tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer WEN tokens from contract to user
        wenToken.safeTransfer(msg.sender, _amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update user's reward debt
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        // Calculate accumulated reward per share
        accRewardPerShare = getAccRewardPerShare();

        // Update user's reward debt
        rewardDebt[_user] = stakingBalances[_user].mul(accRewardPerShare).div(1e18);
    }

    /**
     * @notice Get accumulated reward per share
     * @return Accumulated reward per share
     */
    function getAccRewardPerShare() public view returns (uint256) {
        // Calculate elapsed time since last reward distribution
        uint256 elapsedTime = block.timestamp.sub(lastRewardTimestamp);

        // Calculate reward per share
        if (totalStakingBalance > 0) {
            uint256 reward = elapsedTime.div(rewardInterval).mul(rewardPerInterval);
            rewardPerShare = rewardPerShare.add(reward.mul(1e18).div(totalStakingBalance));
        }

        // Update last reward distribution timestamp
        return rewardPerShare;
    }

    /**
     * @notice Get user's reward
     * @param _user User address
     * @return User's reward
     */
    function getReward(address _user) public view returns (uint256) {
        // Calculate user's reward
        uint256 userReward = stakingBalances[_user].mul(getAccRewardPerShare().sub(rewardDebt[_user])).div(1e18);

        return userReward;
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external {
        // Calculate user's reward
        uint256 userReward = getReward(msg.sender);

        // Update user's reward debt
        rewardDebt[msg.sender] = getAccRewardPerShare();

        // Transfer reward to user
        if (userReward > 0) {
            rewardToken.safeTransfer(msg.sender, userReward);
        }
    }
}
```
