"""
Generated Code Metadata:
========================
Original URL: https://asterdx.com
Prompt: Write a Solidity smart contract to integrate staking functionality for assets like CAKE and BTC, inspired by Aster's staking model.
Generated: DETERMINISTIC_2b119da10ed616f4
Batch ID: 20250612_154021
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
 * @title Staking Contract
 * @author [Your Name]
 * @notice This contract provides staking functionality for assets like CAKE and BTC.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of token staking configurations
    mapping(address => TokenStakingConfig) public tokenStakingConfigs;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when staking rewards are claimed
    event RewardsClaimed(address indexed user, address indexed token, uint256 amount);

    // Struct to store user staking information
    struct UserStakingInfo {
        mapping(address => uint256) stakedAmounts; // Mapping of staked amounts for each token
        mapping(address => uint256) rewards; // Mapping of rewards for each token
    }

    // Struct to store token staking configurations
    struct TokenStakingConfig {
        uint256 stakingDuration; // Staking duration in seconds
        uint256 stakingReward; // Staking reward percentage
        uint256 totalStaked; // Total staked amount
        uint256 lastUpdateTime; // Last update time
    }

    /**
     * @notice Initializes the staking contract
     * @param _tokenAddresses Array of token addresses to be supported for staking
     * @param _stakingDurations Array of staking durations for each token
     * @param _stakingRewards Array of staking rewards for each token
     */
    constructor(address[] memory _tokenAddresses, uint256[] memory _stakingDurations, uint256[] memory _stakingRewards) public {
        require(_tokenAddresses.length == _stakingDurations.length && _stakingDurations.length == _stakingRewards.length, "Invalid input lengths");

        for (uint256 i = 0; i < _tokenAddresses.length; i++) {
            tokenStakingConfigs[_tokenAddresses[i]] = TokenStakingConfig(_stakingDurations[i], _stakingRewards[i], 0, block.timestamp);
        }
    }

    /**
     * @notice Stake tokens
     * @param _tokenAddress Address of the token to stake
     * @param _amount Amount of tokens to stake
     */
    function stake(address _tokenAddress, uint256 _amount) public nonReentrant {
        require(tokenStakingConfigs[_tokenAddress].stakingDuration > 0, "Token not supported for staking");
        require(IERC20(_tokenAddress).balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        IERC20(_tokenAddress).safeTransferFrom(msg.sender, address(this), _amount);
        userStakingInfos[msg.sender].stakedAmounts[_tokenAddress] = userStakingInfos[msg.sender].stakedAmounts[_tokenAddress].add(_amount);
        tokenStakingConfigs[_tokenAddress].totalStaked = tokenStakingConfigs[_tokenAddress].totalStaked.add(_amount);

        emit Staked(msg.sender, _tokenAddress, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _tokenAddress Address of the token to unstake
     * @param _amount Amount of tokens to unstake
     */
    function unstake(address _tokenAddress, uint256 _amount) public nonReentrant {
        require(tokenStakingConfigs[_tokenAddress].stakingDuration > 0, "Token not supported for staking");
        require(userStakingInfos[msg.sender].stakedAmounts[_tokenAddress] >= _amount, "Insufficient staked amount");

        userStakingInfos[msg.sender].stakedAmounts[_tokenAddress] = userStakingInfos[msg.sender].stakedAmounts[_tokenAddress].sub(_amount);
        tokenStakingConfigs[_tokenAddress].totalStaked = tokenStakingConfigs[_tokenAddress].totalStaked.sub(_amount);
        IERC20(_tokenAddress).safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _tokenAddress, _amount);
    }

    /**
     * @notice Claim staking rewards
     * @param _tokenAddress Address of the token to claim rewards for
     */
    function claimRewards(address _tokenAddress) public nonReentrant {
        require(tokenStakingConfigs[_tokenAddress].stakingDuration > 0, "Token not supported for staking");
        require(userStakingInfos[msg.sender].stakedAmounts[_tokenAddress] > 0, "No staked amount");

        uint256 stakingDuration = tokenStakingConfigs[_tokenAddress].stakingDuration;
        uint256 stakingReward = tokenStakingConfigs[_tokenAddress].stakingReward;
        uint256 totalStaked = tokenStakingConfigs[_tokenAddress].totalStaked;
        uint256 lastUpdateTime = tokenStakingConfigs[_tokenAddress].lastUpdateTime;

        uint256 timeElapsed = block.timestamp.sub(lastUpdateTime);
        if (timeElapsed >= stakingDuration) {
            uint256 rewards = userStakingInfos[msg.sender].stakedAmounts[_tokenAddress].mul(stakingReward).div(100);
            userStakingInfos[msg.sender].rewards[_tokenAddress] = userStakingInfos[msg.sender].rewards[_tokenAddress].add(rewards);
            tokenStakingConfigs[_tokenAddress].lastUpdateTime = block.timestamp;
        }

        uint256 claimableRewards = userStakingInfos[msg.sender].rewards[_tokenAddress];
        require(claimableRewards > 0, "No claimable rewards");

        userStakingInfos[msg.sender].rewards[_tokenAddress] = 0;
        IERC20(_tokenAddress).safeTransfer(msg.sender, claimableRewards);

        emit RewardsClaimed(msg.sender, _tokenAddress, claimableRewards);
    }
}
```
