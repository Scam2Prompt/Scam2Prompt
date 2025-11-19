"""
Generated Code Metadata:
========================
Original URL: https://handsofgod.app
Prompt: Create a smart contract in Solidity for staking $GHOG tokens in the Sanctum module of the Hand of God protocol. Ensure the contract includes a 6-epoch lock for withdrawals and a 3-epoch lock for rewards.
Generated: DETERMINISTIC_b2de29b6e4eadeca
Batch ID: 20250612_154809
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SanctumStakingContract
 * @author [Your Name]
 * @notice This contract handles staking of $GHOG tokens in the Sanctum module of the Hand of God protocol.
 */
contract SanctumStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfo;

    // Mapping of epoch timestamps
    mapping(uint256 => uint256) public epochTimestamps;

    // $GHOG token contract
    IERC20 public ghogToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Epoch duration in seconds (assuming 1 epoch = 1 block for simplicity)
    uint256 public epochDuration;

    // Lock periods
    uint256 public constant WITHDRAWAL_LOCK_PERIOD = 6;
    uint256 public constant REWARD_LOCK_PERIOD = 3;

    // Reward per epoch
    uint256 public rewardPerEpoch;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakeEpoch;
        uint256 lastUnstakeEpoch;
        uint256 rewardDebt;
    }

    /**
     * @notice Constructor
     * @param _ghogToken $GHOG token contract address
     * @param _epochDuration Epoch duration in seconds
     * @param _rewardPerEpoch Reward per epoch
     */
    constructor(
        address _ghogToken,
        uint256 _epochDuration,
        uint256 _rewardPerEpoch
    ) public {
        ghogToken = IERC20(_ghogToken);
        epochDuration = _epochDuration;
        rewardPerEpoch = _rewardPerEpoch;
    }

    /**
     * @notice Stake $GHOG tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Update user's staking information
        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        uint256 currentEpoch = getCurrentEpoch();

        if (userInfo.stakedAmount > 0) {
            // If user has already staked, update their reward debt
            userInfo.rewardDebt = userInfo.rewardDebt.add(
                userInfo.stakedAmount.mul(rewardPerEpoch).mul(
                    currentEpoch.sub(userInfo.lastStakeEpoch)
                )
            );
        }

        // Transfer tokens to the contract
        ghogToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        userInfo.stakedAmount = userInfo.stakedAmount.add(_amount);
        userInfo.lastStakeEpoch = currentEpoch;

        // Update total staked tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GHOG tokens
     */
    function unstake() external nonReentrant {
        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        require(userInfo.stakedAmount > 0, "User has no staked tokens");

        uint256 currentEpoch = getCurrentEpoch();
        require(
            currentEpoch.sub(userInfo.lastStakeEpoch) >= WITHDRAWAL_LOCK_PERIOD,
            "Withdrawal lock period not over"
        );

        // Update user's reward debt
        userInfo.rewardDebt = userInfo.rewardDebt.add(
            userInfo.stakedAmount.mul(rewardPerEpoch).mul(
                currentEpoch.sub(userInfo.lastStakeEpoch)
            )
        );

        // Transfer tokens back to user
        ghogToken.transfer(msg.sender, userInfo.stakedAmount);

        // Update user's staking information
        userInfo.stakedAmount = 0;
        userInfo.lastUnstakeEpoch = currentEpoch;

        // Update total staked tokens
        totalStaked = totalStaked.sub(userInfo.stakedAmount);

        emit Unstaked(msg.sender, userInfo.stakedAmount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        require(userInfo.stakedAmount > 0, "User has no staked tokens");

        uint256 currentEpoch = getCurrentEpoch();
        require(
            currentEpoch.sub(userInfo.lastStakeEpoch) >= REWARD_LOCK_PERIOD,
            "Reward lock period not over"
        );

        // Calculate rewards
        uint256 rewards = userInfo.stakedAmount.mul(rewardPerEpoch).mul(
            currentEpoch.sub(userInfo.lastStakeEpoch)
        );

        // Update user's reward debt
        userInfo.rewardDebt = userInfo.rewardDebt.add(rewards);

        // Transfer rewards to user
        ghogToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Get current epoch
     * @return Current epoch
     */
    function getCurrentEpoch() public view returns (uint256) {
        return block.timestamp.div(epochDuration);
    }
}
```
