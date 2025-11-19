"""
Generated Code Metadata:
========================
Original URL: https://trustbase.one
Prompt: Create a DeFi staking contract that incorporates features for pledge mining and referral rewards, similar to the use cases mentioned on Trust Base.
Generated: DETERMINISTIC_5575bee0a7a8f3b0
Batch ID: 20250612_153814
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
 * @title DeFi Staking Contract
 * @author [Your Name]
 * @notice This contract provides staking functionality with pledge mining and referral rewards.
 */
contract DeFiStakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of referral rewards
    mapping(address => uint256) public referralRewards;

    // Mapping of token balances
    mapping(address => uint256) public tokenBalances;

    // Staking token address
    address public stakingToken;

    // Reward token address
    address public rewardToken;

    // Total staked tokens
    uint256 public totalStakedTokens;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Block reward
    uint256 public blockReward;

    // Referral commission rate
    uint256 public referralCommissionRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ReferralRewardClaimed(address indexed user, uint256 amount);

    // Struct for user staking information
    struct UserStakingInfo {
        uint256 stakedTokens;
        uint256 rewardDebt;
        address referral;
        uint256 referralReward;
    }

    /**
     * @notice Constructor
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     * @param _blockReward Block reward
     * @param _referralCommissionRate Referral commission rate
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock,
        uint256 _blockReward,
        uint256 _referralCommissionRate
    ) public {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        blockReward = _blockReward;
        referralCommissionRate = _referralCommissionRate;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     * @param _referral Referral address
     */
    function stake(uint256 _amount, address _referral) public nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(stakingStartBlock <= block.number && block.number <= stakingEndBlock, "Staking period has not started or has ended");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // Transfer staking tokens from user
        IERC20(stakingToken).safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakingInfo.stakedTokens = userStakingInfo.stakedTokens.add(_amount);
        userStakingInfo.rewardDebt = userStakingInfo.stakedTokens.mul(blockReward).div(10**18);
        userStakingInfo.referral = _referral;

        // Update total staked tokens
        totalStakedTokens = totalStakedTokens.add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount);

        // Update referral rewards
        if (_referral != address(0)) {
            referralRewards[_referral] = referralRewards[_referral].add(_amount.mul(referralCommissionRate).div(100));
        }
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedTokens >= _amount, "Insufficient staked tokens");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // Update user staking information
        userStakingInfo.stakedTokens = userStakingInfo.stakedTokens.sub(_amount);
        userStakingInfo.rewardDebt = userStakingInfo.stakedTokens.mul(blockReward).div(10**18);

        // Transfer staking tokens to user
        IERC20(stakingToken).safeTransfer(msg.sender, _amount);

        // Update total staked tokens
        totalStakedTokens = totalStakedTokens.sub(_amount);

        // Emit event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimReward() public nonReentrant {
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // Calculate reward
        uint256 reward = userStakingInfo.stakedTokens.mul(blockReward).div(10**18).sub(userStakingInfo.rewardDebt);

        // Update user staking information
        userStakingInfo.rewardDebt = userStakingInfo.stakedTokens.mul(blockReward).div(10**18);

        // Transfer reward tokens to user
        IERC20(rewardToken).safeTransfer(msg.sender, reward);

        // Emit event
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Claim referral rewards
     */
    function claimReferralReward() public nonReentrant {
        uint256 reward = referralRewards[msg.sender];

        // Reset referral rewards
        referralRewards[msg.sender] = 0;

        // Transfer reward tokens to user
        IERC20(rewardToken).safeTransfer(msg.sender, reward);

        // Emit event
        emit ReferralRewardClaimed(msg.sender, reward);
    }
}
```
