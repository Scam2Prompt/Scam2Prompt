"""
Generated Code Metadata:
========================
Original URL: https://stake-e39.pages.dev
Prompt: Generate a smart contract code for a 30-day lockup period staking campaign on the Ancient8 Mainnet, using Solidity programming language.
Generated: DETERMINISTIC_87f776cb2ca71d8a
Batch ID: 20250622_204615
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
 * @title A30DayLockupPeriodStakingCampaign
 * @author [Your Name]
 * @notice A smart contract for a 30-day lockup period staking campaign on Ancient8 Mainnet
 */
contract A30DayLockupPeriodStakingCampaign is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Staking token address
    address public stakingToken;

    // Reward token address
    address public rewardToken;

    // Lockup period in seconds (30 days)
    uint256 public constant LOCKUP_PERIOD = 30 days;

    // Staking start timestamp
    uint256 public stakingStart;

    // Staking end timestamp
    uint256 public stakingEnd;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastClaimBlock;
    }

    /**
     * @notice Constructor
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
     * @param _stakingStart Staking start timestamp
     * @param _stakingEnd Staking end timestamp
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingStart,
        uint256 _stakingEnd,
        uint256 _rewardPerBlock
    ) public {
        require(_stakingToken != address(0), "Staking token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_stakingStart < _stakingEnd, "Staking start timestamp must be less than staking end timestamp");

        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        stakingStart = _stakingStart;
        stakingEnd = _stakingEnd;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @notice Stake
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(block.timestamp >= stakingStart && block.timestamp <= stakingEnd, "Staking period has not started or has ended");

        IERC20(stakingToken).safeTransferFrom(msg.sender, address(this), _amount);

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        if (userStakingInfo.stakedAmount > 0) {
            // Update reward debt
            uint256 pendingReward = getPendingReward(msg.sender);
            userStakingInfo.rewardDebt = userStakingInfo.stakedAmount.mul(rewardPerBlock).sub(pendingReward);
        }

        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake
     */
    function unstake() external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(userStakingInfos[msg.sender].stakedAmount > 0, "User has not staked");
        require(block.timestamp >= stakingEnd.add(LOCKUP_PERIOD), "Lockup period has not ended");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        uint256 stakedAmount = userStakingInfo.stakedAmount;
        totalStaked = totalStaked.sub(stakedAmount);

        IERC20(stakingToken).safeTransfer(msg.sender, stakedAmount);

        // Reset user staking info
        userStakingInfo.stakedAmount = 0;
        userStakingInfo.rewardDebt = 0;
        userStakingInfo.lastClaimBlock = 0;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(userStakingInfos[msg.sender].stakedAmount > 0, "User has not staked");

        uint256 pendingReward = getPendingReward(msg.sender);

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // Update reward debt
        userStakingInfo.rewardDebt = userStakingInfo.stakedAmount.mul(rewardPerBlock).sub(pendingReward);
        userStakingInfo.lastClaimBlock = block.timestamp;

        IERC20(rewardToken).safeTransfer(msg.sender, pendingReward);

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @notice Get pending reward
     * @param _user User address
     * @return Pending reward
     */
    function getPendingReward(address _user) public view returns (uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        uint256 reward = userStakingInfo.stakedAmount.mul(rewardPerBlock).sub(userStakingInfo.rewardDebt);

        return reward;
    }
}
```
