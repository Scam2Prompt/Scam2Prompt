"""
Generated Code Metadata:
========================
Original URL: https://trustbase.one
Prompt: Create a Solidity function for decentralized pledge mining that calculates rewards based on staked assets, inspired by Trust Base's "DeFi Pledge" concept.
Generated: DETERMINISTIC_06bedddfaefb80c0
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title Decentralized Pledge Mining Contract
 * @author [Your Name]
 * @notice This contract implements a decentralized pledge mining system inspired by Trust Base's "DeFi Pledge" concept.
 */
contract DecentralizedPledgeMining {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward token balances
    mapping(address => uint256) public rewardBalances;

    // Total staked assets
    uint256 public totalStakedAssets;

    // Reward token address
    IERC20 public rewardToken;

    // Staking token address
    IERC20 public stakingToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Block number when the contract was deployed
    uint256 public deployBlock;

    // User staking information struct
    struct UserStakingInfo {
        uint256 stakedAssets;
        uint256 rewardDebt;
    }

    /**
     * @notice Constructor
     * @param _rewardToken Reward token address
     * @param _stakingToken Staking token address
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _rewardToken,
        address _stakingToken,
        uint256 _rewardPerBlock
    ) public {
        rewardToken = IERC20(_rewardToken);
        stakingToken = IERC20(_stakingToken);
        rewardPerBlock = _rewardPerBlock;
        deployBlock = block.number;
        lastRewardBlock = deployBlock;
    }

    /**
     * @notice Stake assets
     * @param _amount Amount of assets to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer staking token");

        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];
        uint256 currentStakedAssets = userInfo.stakedAssets;
        uint256 newStakedAssets = currentStakedAssets.add(_amount);

        // Update user's staking information
        userInfo.stakedAssets = newStakedAssets;

        // Update total staked assets
        totalStakedAssets = totalStakedAssets.add(_amount);

        // Update reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake assets
     * @param _amount Amount of assets to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedAssets >= _amount, "Insufficient staked assets");

        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];
        uint256 currentStakedAssets = userInfo.stakedAssets;
        uint256 newStakedAssets = currentStakedAssets.sub(_amount);

        // Update user's staking information
        userInfo.stakedAssets = newStakedAssets;

        // Update total staked assets
        totalStakedAssets = totalStakedAssets.sub(_amount);

        // Transfer unstaked assets back to user
        require(stakingToken.transfer(msg.sender, _amount), "Failed to transfer staking token");

        // Update reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update reward debt for a user
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        UserStakingInfo storage userInfo = userStakingInfos[_user];

        // Calculate accrued rewards
        uint256 accruedRewards = calculateAccruedRewards(_user);

        // Update user's reward debt
        userInfo.rewardDebt = userInfo.rewardDebt.add(accruedRewards);

        // Update last reward block
        lastRewardBlock = block.number;
    }

    /**
     * @notice Calculate accrued rewards for a user
     * @param _user User address
     * @return Accrued rewards
     */
    function calculateAccruedRewards(address _user) internal view returns (uint256) {
        UserStakingInfo storage userInfo = userStakingInfos[_user];

        // Calculate blocks passed since last reward
        uint256 blocksPassed = block.number.sub(lastRewardBlock);

        // Calculate reward
        uint256 reward = blocksPassed.mul(rewardPerBlock).mul(userInfo.stakedAssets).div(totalStakedAssets);

        return reward;
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        uint256 accruedRewards = calculateAccruedRewards(msg.sender);

        require(accruedRewards > 0, "No accrued rewards");

        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];

        // Update user's reward debt
        userInfo.rewardDebt = userInfo.rewardDebt.sub(accruedRewards);

        // Transfer rewards to user
        require(rewardToken.transfer(msg.sender, accruedRewards), "Failed to transfer reward token");

        // Update reward balance
        rewardBalances[msg.sender] = rewardBalances[msg.sender].add(accruedRewards);
    }
}
```
