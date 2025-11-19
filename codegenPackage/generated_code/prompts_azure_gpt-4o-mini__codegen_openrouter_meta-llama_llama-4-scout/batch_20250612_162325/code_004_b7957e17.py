"""
Generated Code Metadata:
========================
Original URL: https://decubate-platform.pages.dev
Prompt: Create a Solidity contract that allows users to stake DCB and earn rewards with compounding interest over 30 days.
Generated: DETERMINISTIC_b7957e173ff1cddb
Batch ID: 20250612_162325
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DCB Staking Contract
 * @author [Your Name]
 * @notice Allows users to stake DCB and earn rewards with compounding interest over 30 days.
 */
contract DCBStaking {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // DCB token contract
    IERC20 public dcbToken;

    // Reward token contract (assuming same as DCB for simplicity)
    IERC20 public rewardToken;

    // Staking duration in seconds (30 days)
    uint256 public constant STAKING_DURATION = 30 days;

    // Reward rate per second (assuming 10% APY for simplicity)
    uint256 public constant REWARD_RATE = 0.00000367;

    // Mapping of user staking information
    mapping(address => UserStaking) public userStakings;

    // Event emitted when user stakes DCB
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes DCB
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _dcbToken DCB token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _dcbToken, address _rewardToken) {
        require(_dcbToken != address(0), "DCB token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        dcbToken = IERC20(_dcbToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @notice Stake DCB tokens
     * @param _amount Amount of DCB tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer DCB tokens from user to contract
        dcbToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Initialize or update user staking information
        UserStaking storage userStaking = userStakings[msg.sender];
        if (userStaking.stakeTime == 0) {
            userStaking.stakeTime = block.timestamp;
        }
        userStaking.stakedAmount = userStaking.stakedAmount.add(_amount);
        userStaking.lastClaimTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake DCB tokens
     */
    function unstake() external {
        UserStaking storage userStaking = userStakings[msg.sender];
        require(userStaking.stakedAmount > 0, "User has no staked DCB");
        require(block.timestamp.sub(userStaking.stakeTime) >= STAKING_DURATION, "Staking duration not completed");

        uint256 unstakeAmount = userStaking.stakedAmount;
        userStaking.stakedAmount = 0;
        userStaking.stakeTime = 0;
        userStaking.lastClaimTime = 0;

        // Transfer DCB tokens from contract to user
        dcbToken.safeTransfer(msg.sender, unstakeAmount);

        emit Unstaked(msg.sender, unstakeAmount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        UserStaking storage userStaking = userStakings[msg.sender];
        require(userStaking.stakedAmount > 0, "User has no staked DCB");

        uint256 rewards = calculateRewards(userStaking);
        userStaking.lastClaimTime = block.timestamp;

        // Transfer rewards to user
        rewardToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for user
     * @param _userStaking User staking information
     * @return Rewards amount
     */
    function calculateRewards(UserStaking storage _userStaking) internal view returns (uint256) {
        uint256 stakingTime = block.timestamp.sub(_userStaking.lastClaimTime);
        uint256 rewards = _userStaking.stakedAmount.mul(REWARD_RATE).mul(stakingTime);
        return rewards;
    }

    /**
     * @dev User staking information struct
     */
    struct UserStaking {
        uint256 stakeTime;
        uint256 stakedAmount;
        uint256 lastClaimTime;
    }
}
```
