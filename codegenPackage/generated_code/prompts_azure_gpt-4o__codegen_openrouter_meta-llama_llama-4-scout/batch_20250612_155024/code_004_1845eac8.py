"""
Generated Code Metadata:
========================
Original URL: https://dinamikaplus.ru
Prompt: Write a smart contract in Solidity to enable staking of BELT tokens and distribute rewards based on the mechanisms described in Belt Finance.
Generated: DETERMINISTIC_1845eac8f9ec3e5e
Batch ID: 20250612_155024
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Belt Staking Contract
 * @author [Your Name]
 * @notice This contract enables staking of BELT tokens and distributes rewards.
 */
contract BeltStaking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // BELT token contract
    IERC20 public beltToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Staking pool structure
    struct StakingPool {
        uint256 totalStaked;
        uint256 totalRewards;
        uint256 lastUpdateTime;
        uint256 rewardPerShare;
    }

    // Mapping of user staking information
    mapping(address => mapping(uint256 => uint256)) public userStaking;

    // Mapping of staking pools
    mapping(uint256 => StakingPool) public stakingPools;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _beltToken BELT token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _beltToken, address _rewardToken) public {
        beltToken = IERC20(_beltToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Stake BELT tokens
     * @param _amount Amount of BELT tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        // Transfer BELT tokens to contract
        beltToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        userStaking[msg.sender][0] = userStaking[msg.sender][0].add(_amount);

        // Update staking pool
        stakingPools[0].totalStaked = stakingPools[0].totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake BELT tokens
     * @param _amount Amount of BELT tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(userStaking[msg.sender][0] >= _amount, "Insufficient staked tokens");

        // Update user's staking information
        userStaking[msg.sender][0] = userStaking[msg.sender][0].sub(_amount);

        // Update staking pool
        stakingPools[0].totalStaked = stakingPools[0].totalStaked.sub(_amount);

        // Transfer BELT tokens to user
        beltToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distribute rewards to stakers
     */
    function distributeRewards() external onlyOwner {
        // Calculate reward per share
        uint256 reward = rewardToken.balanceOf(address(this));
        uint256 totalStaked = stakingPools[0].totalStaked;

        if (totalStaked > 0) {
            stakingPools[0].rewardPerShare = stakingPools[0].rewardPerShare.add(reward.mul(1e18).div(totalStaked));
            stakingPools[0].totalRewards = stakingPools[0].totalRewards.add(reward);
        }

        // Transfer rewards to stakers
        for (address user in userStaking) {
            uint256 stakedAmount = userStaking[user][0];
            if (stakedAmount > 0) {
                uint256 userReward = stakedAmount.mul(stakingPools[0].rewardPerShare).div(1e18);
                rewardToken.safeTransfer(user, userReward);
                emit RewardsDistributed(user, userReward);
            }
        }
    }

    /**
     * @dev Update reward per share
     */
    function updateRewardPerShare() internal {
        StakingPool storage pool = stakingPools[0];
        uint256 timeElapsed = block.timestamp.sub(pool.lastUpdateTime);

        if (timeElapsed > 0 && pool.totalStaked > 0) {
            // Calculate new reward per share
            pool.rewardPerShare = pool.rewardPerShare.add(timeElapsed.mul(1e18).div(pool.totalStaked));
            pool.lastUpdateTime = block.timestamp;
        }
    }

    /**
     * @dev Get user's staking information
     * @param _user User address
     * @return Staked amount and reward
     */
    function getStakingInfo(address _user) external view returns (uint256, uint256) {
        uint256 stakedAmount = userStaking[_user][0];
        uint256 reward = stakedAmount.mul(stakingPools[0].rewardPerShare).div(1e18);

        return (stakedAmount, reward);
    }
}
```
