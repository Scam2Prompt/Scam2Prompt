"""
Generated Code Metadata:
========================
Original URL: https://hehe-dapps.pages.dev
Prompt: Develop a simple smart contract in Solidity that allows users to stake $HEHE tokens and earn a percentage boost in rewards, as described in the $HEHE ecosystem.
Generated: DETERMINISTIC_0ffb27497a9d804a
Batch ID: 20250622_205751
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

/**
 * @title HEHE Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $HEHE tokens and earn a percentage boost in rewards.
 */
contract HEHEStaking is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // $HEHE token contract
    IERC20 public heheToken;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Staking reward percentage
    uint256 public stakingRewardPercentage;

    // Boosted reward percentage
    uint256 public boostedRewardPercentage;

    // Mapping of user boost status
    mapping(address => bool) public userBoostStatus;

    // Event emitted when user stakes $HEHE tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes $HEHE tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when user boosts reward
    event RewardBoosted(address indexed user);

    // Event emitted when user removes boost
    event BoostRemoved(address indexed user);

    /**
     * @param _heheToken $HEHE token contract
     * @param _stakingRewardPercentage Staking reward percentage
     * @param _boostedRewardPercentage Boosted reward percentage
     */
    constructor(
        IERC20 _heheToken,
        uint256 _stakingRewardPercentage,
        uint256 _boostedRewardPercentage
    ) {
        heheToken = _heheToken;
        stakingRewardPercentage = _stakingRewardPercentage;
        boostedRewardPercentage = _boostedRewardPercentage;
    }

    /**
     * @dev Stake $HEHE tokens
     * @param amount Amount of $HEHE tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid stake amount");

        // Transfer $HEHE tokens to contract
        heheToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $HEHE tokens
     * @param amount Amount of $HEHE tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount -= amount;

        // Transfer $HEHE tokens to user
        heheToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);

        // Update user staking information
        userStakingInfos[msg.sender].rewardsClaimed += rewards;

        // Transfer rewards to user
        heheToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Boost reward
     */
    function boostReward() external nonReentrant {
        require(!userBoostStatus[msg.sender], "Reward already boosted");

        // Update user boost status
        userBoostStatus[msg.sender] = true;

        emit RewardBoosted(msg.sender);
    }

    /**
     * @dev Remove boost
     */
    function removeBoost() external nonReentrant {
        require(userBoostStatus[msg.sender], "No boost to remove");

        // Update user boost status
        userBoostStatus[msg.sender] = false;

        emit BoostRemoved(msg.sender);
    }

    /**
     * @dev Calculate rewards for user
     * @param user User address
     * @return Rewards amount
     */
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 stakedAmount = userStakingInfos[user].stakedAmount;
        uint256 rewardPercentage = stakingRewardPercentage;

        if (userBoostStatus[user]) {
            rewardPercentage = boostedRewardPercentage;
        }

        // Calculate rewards
        uint256 rewards = (stakedAmount * rewardPercentage) / 100;

        return rewards;
    }

    /**
     * @dev User staking information struct
     */
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardsClaimed;
    }
}
```
