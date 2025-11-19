"""
Generated Code Metadata:
========================
Original URL: https://velodrome-7zz.pages.dev
Prompt: "Implement a staking system for VELO tokens, enabling users to lock their tokens and convert them to veVELO, with corresponding incentives and fees distribution."
Generated: DETERMINISTIC_8c1a9524f6c89069
Batch ID: 20250622_205436
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

contract VeloStaking is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Token contracts
    IERC20 public immutable veloToken;
    IERC20 public immutable veVeloToken;

    // Staking parameters
    uint256 public constant MAX_LOCK_TIME = 4 * 365 days; // 4 years max lock
    uint256 public constant MIN_LOCK_TIME = 1 weeks; // 1 week min lock
    uint256 public constant FEE_PERCENT = 2; // 2% fee on early withdrawal
    address public feeCollector;

    // Staking data structures
    struct Stake {
        uint256 amount;
        uint256 unlockTime;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    uint256 public lastRewardTime;
    uint256 public accRewardPerShare;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event FeeCollected(address indexed user, uint256 amount);

    constructor(
        address _veloToken,
        address _veVeloToken,
        address _feeCollector
    ) {
        require(_veloToken != address(0), "Invalid VELO token address");
        require(_veVeloToken != address(0), "Invalid veVELO token address");
        require(_feeCollector != address(0), "Invalid fee collector address");

        veloToken = IERC20(_veloToken);
        veVeloToken = IERC20(_veVeloToken);
        feeCollector = _feeCollector;
        lastRewardTime = block.timestamp;
    }

    // Update reward variables
    function updateRewards() public {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            return;
        }

        uint256 timeElapsed = block.timestamp.sub(lastRewardTime);
        uint256 reward = calculateReward(timeElapsed);
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStaked));
        lastRewardTime = block.timestamp;
    }

    // Stake VELO tokens and receive veVELO
    function stake(uint256 amount, uint256 lockTime) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(lockTime >= MIN_LOCK_TIME, "Lock time too short");
        require(lockTime <= MAX_LOCK_TIME, "Lock time too long");

        updateRewards();

        // Transfer VELO tokens from user
        veloToken.safeTransferFrom(msg.sender, address(this), amount);

        // Calculate veVELO amount (1:1 ratio for now)
        uint256 veVeloAmount = amount;

        // Mint veVELO to user
        veVeloToken.safeTransfer(msg.sender, veVeloAmount);

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            claimRewards();
        }

        userStake.amount = userStake.amount.add(amount);
        userStake.unlockTime = block.timestamp.add(lockTime);
        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e18);

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount, userStake.unlockTime);
    }

    // Unstake VELO tokens
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp >= userStake.unlockTime, "Tokens still locked");

        updateRewards();

        uint256 amount = userStake.amount;
        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e18).sub(userStake.rewardDebt);

        // Burn veVELO from user (1:1 ratio)
        veVeloToken.safeTransferFrom(msg.sender, address(this), amount);

        // Transfer VELO back to user
        veloToken.safeTransfer(msg.sender, amount);

        // Transfer rewards if any
        if (pending > 0) {
            veloToken.safeTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        // Update state
        totalStaked = totalStaked.sub(amount);
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, amount);
    }

    // Early unstake with penalty
    function earlyUnstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp < userStake.unlockTime, "Use regular unstake");

        updateRewards();

        uint256 amount = userStake.amount;
        uint256 fee = amount.mul(FEE_PERCENT).div(100);
        uint256 amountAfterFee = amount.sub(fee);
        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e18).sub(userStake.rewardDebt);

        // Burn veVELO from user
        veVeloToken.safeTransferFrom(msg.sender, address(this), amount);

        // Transfer VELO back to user (minus fee)
        veloToken.safeTransfer(msg.sender, amountAfterFee);

        // Transfer fee to collector
        veloToken.safeTransfer(feeCollector, fee);

        // Transfer rewards if any
        if (pending > 0) {
            veloToken.safeTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        // Update state
        totalStaked = totalStaked.sub(amount);
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, amountAfterFee);
        emit FeeCollected(msg.sender, fee);
    }

    // Claim rewards without unstaking
    function claimRewards() public nonReentrant {
        updateRewards();

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount == 0) {
            return;
        }

        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e18).sub(userStake.rewardDebt);
        if (pending > 0) {
            veloToken.safeTransfer(msg.sender, pending);
            userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e18);
            emit RewardClaimed(msg.sender, pending);
        }
    }

    // Calculate current reward for time elapsed
    function calculateReward(uint256 timeElapsed) internal pure returns (uint256) {
        // Simplified reward calculation - in production this would use a proper reward schedule
        return timeElapsed.mul(1e18).div(365 days); // 1 VELO per staked token per year
    }

    // View function to get pending rewards
    function pendingRewards(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp.sub(lastRewardTime);
            uint256 reward = calculateReward(timeElapsed);
            currentAccRewardPerShare = currentAccRewardPerShare.add(reward.mul(1e18).div(totalStaked));
        }

        return userStake.amount.mul(currentAccRewardPerShare).div(1e18).sub(userStake.rewardDebt);
    }

    // Update fee collector address (onlyOwner in production)
    function setFeeCollector(address _feeCollector) external {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
    }
}
```
