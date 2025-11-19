"""
Generated Code Metadata:
========================
Original URL: https://rabbittherious.pages.dev
Prompt: Write a smart contract in Solidity for staking tokens, inspired by the functionality described on the "Rious The Rabbit" website.
Generated: DETERMINISTIC_d53ecf2b25d13f65
Batch ID: 20250612_152906
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
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title RiousTheRabbitStakingContract
 * @author [Your Name]
 * @notice A staking contract inspired by Rious The Rabbit website
 */
contract RiousTheRabbitStakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of token staking information
    mapping(address => TokenStakingInfo) public tokenStakingInfos;

    // Staking token address
    address public stakingTokenAddress;

    // Reward token address
    address public rewardTokenAddress;

    // Staking start timestamp
    uint256 public stakingStartTimestamp;

    // Staking end timestamp
    uint256 public stakingEndTimestamp;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Total reward amount
    uint256 public totalRewardAmount;

    // Reward per second
    uint256 public rewardPerSecond;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardClaimed(address indexed user, uint256 amount);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastRewardClaimTimestamp;
    }

    // Struct to store token staking information
    struct TokenStakingInfo {
        uint256 totalStakedAmount;
        uint256 totalRewardAmount;
    }

    /**
     * @notice Constructor
     * @param _stakingTokenAddress Staking token address
     * @param _rewardTokenAddress Reward token address
     * @param _stakingStartTimestamp Staking start timestamp
     * @param _stakingEndTimestamp Staking end timestamp
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        address _stakingTokenAddress,
        address _rewardTokenAddress,
        uint256 _stakingStartTimestamp,
        uint256 _stakingEndTimestamp,
        uint256 _rewardPerSecond
    ) public {
        require(_stakingTokenAddress != address(0), "Staking token address cannot be zero");
        require(_rewardTokenAddress != address(0), "Reward token address cannot be zero");
        require(_stakingStartTimestamp < _stakingEndTimestamp, "Invalid staking timestamps");
        require(_rewardPerSecond > 0, "Reward per second must be greater than zero");

        stakingTokenAddress = _stakingTokenAddress;
        rewardTokenAddress = _rewardTokenAddress;
        stakingStartTimestamp = _stakingStartTimestamp;
        stakingEndTimestamp = _stakingEndTimestamp;
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(block.timestamp >= stakingStartTimestamp, "Staking has not started yet");
        require(block.timestamp < stakingEndTimestamp, "Staking has ended");

        IERC20(stakingTokenAddress).safeTransferFrom(msg.sender, address(this), _amount);

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        TokenStakingInfo storage tokenStakingInfo = tokenStakingInfos[stakingTokenAddress];

        if (userStakingInfo.stakedAmount > 0) {
            _updateReward(msg.sender);
        }

        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        tokenStakingInfo.totalStakedAmount = tokenStakingInfo.totalStakedAmount.add(_amount);
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        TokenStakingInfo storage tokenStakingInfo = tokenStakingInfos[stakingTokenAddress];

        _updateReward(msg.sender);

        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);
        tokenStakingInfo.totalStakedAmount = tokenStakingInfo.totalStakedAmount.sub(_amount);
        totalStakedAmount = totalStakedAmount.sub(_amount);

        IERC20(stakingTokenAddress).safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimReward() external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");

        _updateReward(msg.sender);

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        uint256 rewardAmount = userStakingInfo.rewardDebt;
        userStakingInfo.rewardDebt = 0;
        userStakingInfo.lastRewardClaimTimestamp = block.timestamp;

        IERC20(rewardTokenAddress).safeTransfer(msg.sender, rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Update reward
     * @param _user User address
     */
    function _updateReward(address _user) internal {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        if (userStakingInfo.stakedAmount > 0) {
            uint256 reward = _calculateReward(_user);
            userStakingInfo.rewardDebt = userStakingInfo.rewardDebt.add(reward);
        }
    }

    /**
     * @notice Calculate reward
     * @param _user User address
     * @return Reward amount
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        uint256 stakingDuration = block.timestamp.sub(userStakingInfo.lastRewardClaimTimestamp);
        uint256 reward = userStakingInfo.stakedAmount.mul(rewardPerSecond).mul(stakingDuration).div(1e18);

        return reward;
    }

    /**
     * @notice Update reward per second
     * @param _newRewardPerSecond New reward per second
     */
    function updateRewardPerSecond(uint256 _newRewardPerSecond) external onlyOwner {
        require(_newRewardPerSecond > 0, "Reward per second must be greater than zero");

        rewardPerSecond = _newRewardPerSecond;
    }

    /**
     * @notice Withdraw tokens
     * @param _tokenAddress Token address
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_amount > 0, "Withdrawal amount must be greater than zero");

        IERC20(_tokenAddress).safeTransfer(msg.sender, _amount);
    }
}
```
