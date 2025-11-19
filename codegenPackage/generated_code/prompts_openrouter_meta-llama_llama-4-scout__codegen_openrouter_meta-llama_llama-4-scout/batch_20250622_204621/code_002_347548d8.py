"""
Generated Code Metadata:
========================
Original URL: https://claim-etuktuk-io.pages.dev
Prompt: Develop a simple smart contract in Solidity for staking $TUK tokens and earning rewards, inspired by the eTukTuk staking mechanism.
Generated: DETERMINISTIC_347548d84db783bd
Batch ID: 20250622_204621
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title eTukTuk Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $TUK tokens and earn rewards.
 */
contract ETukTukStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward rates for different staking periods
    mapping (uint256 => RewardRate) public rewardRates;

    // $TUK token contract
    IERC20 public tukToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward token contract (e.g. $TUK or other reward token)
    IERC20 public rewardToken;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _tukToken $TUK token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _tukToken, address _rewardToken) public {
        tukToken = IERC20(_tukToken);
        rewardToken = IERC20(_rewardToken);

        // Initialize reward rates for different staking periods (in days)
        rewardRates[7] = RewardRate(100, 365); // 100% APY for 7-day staking
        rewardRates[30] = RewardRate(500, 365); // 500% APY for 30-day staking
        // Add more reward rates as needed
    }

    /**
     * @dev Stake $TUK tokens for a specified period
     * @param _amount Amount of tokens to stake
     * @param _period Staking period in days
     */
    function stake(uint256 _amount, uint256 _period) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(rewardRates[_period].rate > 0, "Invalid staking period");

        // Transfer $TUK tokens to the contract
        require(tukToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].stakingPeriod = _period;
        userStakingInfos[msg.sender].stakeTimestamp = block.timestamp;

        // Update total staked tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $TUK tokens
     */
    function unstake() external nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No tokens staked");

        // Calculate unstake amount
        uint256 unstakeAmount = userStakingInfos[msg.sender].stakedAmount;

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = 0;
        userStakingInfos[msg.sender].stakingPeriod = 0;
        userStakingInfos[msg.sender].stakeTimestamp = 0;

        // Update total staked tokens
        totalStaked = totalStaked.sub(unstakeAmount);

        // Transfer $TUK tokens back to user
        require(tukToken.transfer(msg.sender, unstakeAmount), "Token transfer failed");

        emit Unstaked(msg.sender, unstakeAmount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No tokens staked");

        // Calculate reward amount
        uint256 rewardAmount = calculateReward(msg.sender);

        // Update user staking information
        userStakingInfos[msg.sender].lastClaimTimestamp = block.timestamp;

        // Transfer reward tokens to user
        require(rewardToken.transfer(msg.sender, rewardAmount), "Reward token transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Calculate reward amount for a user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 stakingPeriod = userStakingInfos[_user].stakingPeriod;
        uint256 stakeTimestamp = userStakingInfos[_user].stakeTimestamp;
        uint256 stakedAmount = userStakingInfos[_user].stakedAmount;

        // Calculate elapsed time
        uint256 elapsedTime = block.timestamp.sub(stakeTimestamp);

        // Calculate reward rate
        RewardRate memory rewardRate = rewardRates[stakingPeriod];

        // Calculate reward amount
        uint256 rewardAmount = stakedAmount.mul(rewardRate.rate).mul(elapsedTime).div(365 * 86400);

        return rewardAmount;
    }

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakingPeriod;
        uint256 stakeTimestamp;
        uint256 lastClaimTimestamp;
    }

    // Struct to store reward rate information
    struct RewardRate {
        uint256 rate; // Rate in basis points (e.g. 100 = 100%)
        uint256 period; // Period in days
    }
}
```
