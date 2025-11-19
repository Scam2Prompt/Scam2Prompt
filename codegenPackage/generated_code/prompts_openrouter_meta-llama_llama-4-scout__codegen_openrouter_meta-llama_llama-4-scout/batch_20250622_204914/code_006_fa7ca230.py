"""
Generated Code Metadata:
========================
Original URL: https://claimcatfloki.pages.dev
Prompt: Write a smart contract in Solidity to manage the staking and reward distribution for FLOKI tokens on a blockchain platform.
Generated: DETERMINISTIC_fa7ca2301e7b3585
Batch ID: 20250622_204914
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Floki Staking Contract
 * @author [Your Name]
 * @notice This contract manages the staking and reward distribution for FLOKI tokens.
 */
contract FlokiStakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // FLOKI token contract
    IERC20 public flokiToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Staking start timestamp
    uint256 public stakingStart;

    // Staking end timestamp
    uint256 public stakingEnd;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Event emitted when user stakes FLOKI tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes FLOKI tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakeTimestamp;
    }

    /**
     * @notice Constructor
     * @param _flokiToken FLOKI token contract address
     * @param _rewardToken Reward token contract address
     * @param _stakingStart Staking start timestamp
     * @param _stakingEnd Staking end timestamp
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _flokiToken,
        address _rewardToken,
        uint256 _stakingStart,
        uint256 _stakingEnd,
        uint256 _rewardPerBlock
    ) public {
        require(_flokiToken != address(0), "FLOKI token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_stakingStart < _stakingEnd, "Staking start timestamp must be less than staking end timestamp");

        flokiToken = IERC20(_flokiToken);
        rewardToken = IERC20(_rewardToken);
        stakingStart = _stakingStart;
        stakingEnd = _stakingEnd;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @notice Stake FLOKI tokens
     * @param _amount Amount of FLOKI tokens to stake
     */
    function stake(uint256 _amount) external {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Stake amount must be greater than zero");
        require(block.timestamp >= stakingStart && block.timestamp <= stakingEnd, "Staking period has not started or has ended");

        // Update user's staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        uint256 newStakedAmount = userStakingInfo.stakedAmount.add(_amount);

        // Transfer FLOKI tokens from user to contract
        require(flokiToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer FLOKI tokens");

        userStakingInfo.stakedAmount = newStakedAmount;
        userStakingInfo.lastStakeTimestamp = block.timestamp;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake FLOKI tokens
     * @param _amount Amount of FLOKI tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "User does not have enough staked FLOKI tokens");

        // Update user's staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        uint256 newStakedAmount = userStakingInfo.stakedAmount.sub(_amount);

        // Transfer FLOKI tokens from contract to user
        require(flokiToken.transfer(msg.sender, _amount), "Failed to transfer FLOKI tokens");

        userStakingInfo.stakedAmount = newStakedAmount;
        userStakingInfo.rewardDebt = getRewardDebt(msg.sender);

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Get reward debt for a user
     * @param _user User address
     * @return Reward debt
     */
    function getRewardDebt(address _user) internal view returns (uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];
        uint256 reward = userStakingInfo.stakedAmount.mul(rewardPerBlock).mul(block.timestamp.sub(userStakingInfo.lastStakeTimestamp));
        return userStakingInfo.rewardDebt.add(reward);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        require(msg.sender != address(0), "User address cannot be zero");

        // Calculate reward
        uint256 reward = getRewardDebt(msg.sender).sub(userStakingInfos[msg.sender].rewardDebt);

        // Update user's reward debt
        userStakingInfos[msg.sender].rewardDebt = getRewardDebt(msg.sender);

        // Transfer reward tokens to user
        require(rewardToken.transfer(msg.sender, reward), "Failed to transfer reward tokens");

        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Withdraw stuck tokens
     * @param _token Token contract address
     */
    function withdrawStuckTokens(address _token) external onlyOwner {
        require(_token != address(0), "Token address cannot be zero");

        IERC20 token = IERC20(_token);

        // Transfer tokens to owner
        require(token.transfer(msg.sender, token.balanceOf(address(this))), "Failed to transfer tokens");
    }
}
```
