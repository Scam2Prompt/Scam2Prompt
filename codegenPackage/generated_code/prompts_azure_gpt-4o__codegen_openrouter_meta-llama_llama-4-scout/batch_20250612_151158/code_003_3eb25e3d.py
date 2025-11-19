"""
Generated Code Metadata:
========================
Original URL: https://openchainx.com
Prompt: Develop a smart contract for staking cryptocurrency that addresses common staking-related issues as outlined on OpenChainX.
Generated: DETERMINISTIC_3eb25e3de56fcaea
Batch ID: 20250612_151158
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A smart contract for staking cryptocurrency.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfo;

    // Mapping of staking pool information
    mapping(address => StakingPoolInfo) public stakingPoolInfo;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when staking rewards are claimed
    event RewardsClaimed(address indexed user, address indexed token, uint256 amount);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakedTimestamp;
    }

    // Struct to store staking pool information
    struct StakingPoolInfo {
        address token;
        uint256 totalStakedAmount;
        uint256 rewardsPerSecond;
        uint256 startTimestamp;
        uint256 endTimestamp;
    }

    // List of supported staking tokens
    address[] public supportedTokens;

    /**
     * @notice Constructor function.
     * @param _supportedTokens List of supported staking tokens.
     */
    constructor(address[] memory _supportedTokens) {
        for (uint256 i = 0; i < _supportedTokens.length; i++) {
            supportedTokens.push(_supportedTokens[i]);
            stakingPoolInfo[_supportedTokens[i]] = StakingPoolInfo(
                _supportedTokens[i],
                0,
                0,
                block.timestamp,
                block.timestamp.add(30 days)
            );
        }
    }

    /**
     * @notice Stake tokens.
     * @param _token Address of the token to stake.
     * @param _amount Amount of tokens to stake.
     */
    function stake(address _token, uint256 _amount) external nonReentrant {
        require(supportedTokens.contains(_token), "Unsupported token");
        require(_amount > 0, "Invalid amount");

        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        StakingPoolInfo storage poolInfo = stakingPoolInfo[_token];

        userInfo.stakedAmount = userInfo.stakedAmount.add(_amount);
        poolInfo.totalStakedAmount = poolInfo.totalStakedAmount.add(_amount);

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        userInfo.lastStakedTimestamp = block.timestamp;

        emit Staked(msg.sender, _token, _amount);
    }

    /**
     * @notice Unstake tokens.
     * @param _token Address of the token to unstake.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(address _token, uint256 _amount) external nonReentrant {
        require(supportedTokens.contains(_token), "Unsupported token");
        require(_amount > 0, "Invalid amount");

        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        StakingPoolInfo storage poolInfo = stakingPoolInfo[_token];

        require(userInfo.stakedAmount >= _amount, "Insufficient staked amount");

        userInfo.stakedAmount = userInfo.stakedAmount.sub(_amount);
        poolInfo.totalStakedAmount = poolInfo.totalStakedAmount.sub(_amount);

        IERC20(_token).safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _token, _amount);
    }

    /**
     * @notice Claim staking rewards.
     * @param _token Address of the token to claim rewards for.
     */
    function claimRewards(address _token) external nonReentrant {
        require(supportedTokens.contains(_token), "Unsupported token");

        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        StakingPoolInfo storage poolInfo = stakingPoolInfo[_token];

        uint256 rewards = calculateRewards(msg.sender, _token);

        require(rewards > 0, "No rewards to claim");

        userInfo.lastStakedTimestamp = block.timestamp;

        IERC20(_token).safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, _token, rewards);
    }

    /**
     * @notice Calculate staking rewards for a user.
     * @param _user Address of the user.
     * @param _token Address of the token.
     * @return Rewards amount.
     */
    function calculateRewards(address _user, address _token) internal view returns (uint256) {
        UserStakingInfo storage userInfo = userStakingInfo[_user];
        StakingPoolInfo storage poolInfo = stakingPoolInfo[_token];

        uint256 stakedDuration = block.timestamp.sub(userInfo.lastStakedTimestamp);
        uint256 rewards = stakedDuration.mul(poolInfo.rewardsPerSecond).mul(userInfo.stakedAmount);

        return rewards;
    }

    /**
     * @notice Update rewards per second for a staking pool.
     * @param _token Address of the token.
     * @param _rewardsPerSecond New rewards per second.
     */
    function updateRewardsPerSecond(address _token, uint256 _rewardsPerSecond) external {
        require(msg.sender == owner(), "Only owner can update rewards");

        StakingPoolInfo storage poolInfo = stakingPoolInfo[_token];
        poolInfo.rewardsPerSecond = _rewardsPerSecond;
    }

    /**
     * @notice Get supported staking tokens.
     * @return List of supported staking tokens.
     */
    function getSupportedTokens() external view returns (address[] memory) {
        return supportedTokens;
    }
}
```
