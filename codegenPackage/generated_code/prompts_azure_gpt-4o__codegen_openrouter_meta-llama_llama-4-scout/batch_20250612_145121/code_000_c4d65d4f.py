"""
Generated Code Metadata:
========================
Original URL: https://looksrare.tech
Prompt: Write a Solidity smart contract to implement a staking mechanism similar to LooksRare, where users can stake tokens and earn rewards in both the staked token and a share of platform fees.
Generated: DETERMINISTIC_c4d65d4f7eacbc2c
Batch ID: 20250612_145121
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
 * @title StakingContract
 * @author [Your Name]
 * @notice A staking contract similar to LooksRare, allowing users to stake tokens and earn rewards.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward token information
    mapping(address => RewardTokenInfo) public rewardTokenInfos;

    // Platform fee rate (in bps)
    uint16 public platformFeeRate;

    // Address of the staked token
    address public stakedToken;

    // Address of the reward token
    address public rewardToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 stakedTokenReward, uint256 rewardTokenReward);

    // Event emitted when the platform fee rate is updated
    event PlatformFeeRateUpdated(uint16 newRate);

    // Event emitted when a reward token is added or removed
    event RewardTokenUpdated(address indexed token, bool added);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakedTokenRewardDebt;
        mapping(address => uint256) rewardTokenDebt;
    }

    // Struct to store reward token information
    struct RewardTokenInfo {
        uint256 accumulatedRewardPerShare;
        uint256 lastRewardTime;
        uint256 rewardPerSecond;
    }

    /**
     * @notice Constructor
     * @param _stakedToken Address of the staked token
     * @param _rewardToken Address of the reward token
     * @param _platformFeeRate Platform fee rate (in bps)
     */
    constructor(address _stakedToken, address _rewardToken, uint16 _platformFeeRate) {
        require(_stakedToken != address(0), "Staked token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_platformFeeRate >= 0 && _platformFeeRate <= 10000, "Invalid platform fee rate");

        stakedToken = _stakedToken;
        rewardToken = _rewardToken;
        platformFeeRate = _platformFeeRate;

        rewardTokenInfos[_rewardToken].lastRewardTime = block.timestamp;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        IERC20(stakedToken).safeTransferFrom(msg.sender, address(this), _amount);

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);

        IERC20(stakedToken).safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward token debt for a user
     * @param _user Address of the user
     * @param _token Address of the reward token
     */
    function updateRewardTokenDebt(address _user, address _token) internal {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];
        RewardTokenInfo storage rewardTokenInfo = rewardTokenInfos[_token];

        uint256 accumulatedRewardPerShare = rewardTokenInfo.accumulatedRewardPerShare;
        uint256 stakedAmount = userStakingInfo.stakedAmount;

        if (stakedAmount > 0) {
            uint256 reward = stakedAmount.mul(accumulatedRewardPerShare).div(1e18);
            userStakingInfo.rewardTokenDebt[_token] = reward;
        }
    }

    /**
     * @notice Distribute rewards to users
     */
    function distributeRewards() external {
        RewardTokenInfo storage rewardTokenInfo = rewardTokenInfos[rewardToken];

        uint256 currentTime = block.timestamp;
        uint256 lastRewardTime = rewardTokenInfo.lastRewardTime;
        uint256 rewardPerSecond = rewardTokenInfo.rewardPerSecond;

        if (currentTime > lastRewardTime) {
            uint256 totalStaked = IERC20(stakedToken).balanceOf(address(this));
            uint256 reward = rewardPerSecond.mul(currentTime.sub(lastRewardTime));

            if (totalStaked > 0) {
                rewardTokenInfo.accumulatedRewardPerShare = rewardTokenInfo.accumulatedRewardPerShare.add(reward.mul(1e18).div(totalStaked));
            }

            rewardTokenInfo.lastRewardTime = currentTime;
        }

        for (address user in userStakingInfos) {
            UserStakingInfo storage userStakingInfo = userStakingInfos[user];

            updateRewardTokenDebt(user, rewardToken);

            uint256 stakedTokenReward = userStakingInfo.stakedAmount.mul(rewardTokenInfo.accumulatedRewardPerShare).div(1e18);
            uint256 rewardTokenReward = userStakingInfo.rewardTokenDebt[rewardToken];

            if (stakedTokenReward > 0) {
                IERC20(stakedToken).safeTransfer(user, stakedTokenReward);
                userStakingInfo.stakedTokenRewardDebt = userStakingInfo.stakedTokenRewardDebt.add(stakedTokenReward);
            }

            if (rewardTokenReward > 0) {
                IERC20(rewardToken).safeTransfer(user, rewardTokenReward);
                userStakingInfo.rewardTokenDebt[rewardToken] = 0;
            }

            emit RewardsDistributed(user, stakedTokenReward, rewardTokenReward);
        }
    }

    /**
     * @notice Update platform fee rate
     * @param _newRate New platform fee rate (in bps)
     */
    function updatePlatformFeeRate(uint16 _newRate) external onlyOwner {
        require(_newRate >= 0 && _newRate <= 10000, "Invalid platform fee rate");

        platformFeeRate = _newRate;

        emit PlatformFeeRateUpdated(_newRate);
    }

    /**
     * @notice Add or remove a reward token
     * @param _token Address of the reward token
     * @param _added Whether to add or remove the reward token
     */
    function updateRewardToken(address _token, bool _added) external onlyOwner {
        if (_added) {
            rewardTokenInfos[_token].lastRewardTime = block.timestamp;
        } else {
            delete rewardTokenInfos[_token];
        }

        emit RewardTokenUpdated(_token, _added);
    }

    /**
     * @notice Update reward per second for a reward token
     * @param _token Address of the reward token
     * @param _newRewardPerSecond New reward per second
     */
    function updateRewardPerSecond(address _token, uint256 _newRewardPerSecond) external onlyOwner {
        rewardTokenInfos[_token].rewardPerSecond = _newRewardPerSecond;
    }
}
```
