"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-in.web.app
Prompt: Generate code for a simple staking system, where users can stake $MPEPE tokens to earn rewards, using a De-Fi liquidity pool.
Generated: DETERMINISTIC_e4ef685211f1bfad
Batch ID: 20250622_212817
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract MPEPEStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking details
    struct UserStake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // The staking token (MPEPE)
    IERC20 public stakingToken;

    // Reward token (could be same as staking token)
    IERC20 public rewardToken;

    // Reward rate (tokens per second)
    uint256 public rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // Precision factor for reward calculation
    uint256 public constant PRECISION_FACTOR = 1e18;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Last update time for rewards
    uint256 public lastUpdateTime;

    // Minimum stake duration (in seconds)
    uint256 public minStakeDuration;

    // Mapping of user addresses to their staking details
    mapping(address => UserStake) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeDurationUpdated(uint256 newDuration);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakeDuration
    ) {
        require(_stakingToken != address(0), "Staking token cannot be zero address");
        require(_rewardToken != address(0), "Reward token cannot be zero address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
        lastUpdateTime = block.timestamp;
    }

    // Update reward variables
    function updateRewards() internal {
        if (totalStaked == 0) {
            lastUpdateTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        uint256 rewards = timeElapsed * rewardRate;
        accRewardPerShare += (rewards * PRECISION_FACTOR) / totalStaked;
        lastUpdateTime = block.timestamp;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        updateRewards();

        UserStake storage userStake = userStakes[msg.sender];

        if (userStake.amount > 0) {
            uint256 pending = (userStake.amount * accRewardPerShare) / PRECISION_FACTOR - userStake.rewardDebt;
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        userStake.amount += amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / PRECISION_FACTOR;
        userStake.lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        require(
            block.timestamp >= userStake.lastStakeTime + minStakeDuration,
            "Minimum stake duration not reached"
        );

        updateRewards();

        uint256 pending = (userStake.amount * accRewardPerShare) / PRECISION_FACTOR - userStake.rewardDebt;
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        userStake.amount -= amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / PRECISION_FACTOR;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        updateRewards();

        uint256 pending = (userStake.amount * accRewardPerShare) / PRECISION_FACTOR - userStake.rewardDebt;
        require(pending > 0, "No rewards to claim");

        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / PRECISION_FACTOR;
        safeTransferReward(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    // Safe reward transfer function
    function safeTransferReward(address to, uint256 amount) internal {
        uint256 balance = rewardToken.balanceOf(address(this));
        if (amount > balance) {
            rewardToken.safeTransfer(to, balance);
        } else {
            rewardToken.safeTransfer(to, amount);
        }
    }

    // View function to check pending rewards
    function pendingRewards(address user) external view returns (uint256) {
        UserStake storage userStake = userStakes[user];
        if (userStake.amount == 0 || totalStaked == 0) {
            return 0;
        }

        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (totalStaked > 0 && block.timestamp > lastUpdateTime) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 rewards = timeElapsed * rewardRate;
            currentAccRewardPerShare += (rewards * PRECISION_FACTOR) / totalStaked;
        }

        return (userStake.amount * currentAccRewardPerShare) / PRECISION_FACTOR - userStake.rewardDebt;
    }

    // Admin functions
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updateRewards();
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    function setMinStakeDuration(uint256 _minStakeDuration) external onlyOwner {
        minStakeDuration = _minStakeDuration;
        emit MinStakeDurationUpdated(_minStakeDuration);
    }

    function emergencyWithdraw() external nonReentrant {
        UserStake storage userStake = userStakes[msg.sender];
        uint256 amount = userStake.amount;
        require(amount > 0, "No staked amount");

        userStake.amount = 0;
        userStake.rewardDebt = 0;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
