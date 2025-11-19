"""
Generated Code Metadata:
========================
Original URL: https://dogee1.pages.dev
Prompt: Develop a Solidity-based rewards distribution mechanism for DOGE20 staking that aligns with the eco-friendly Proof-of-Stake model described on the website.
Generated: DETERMINISTIC_c7b94be065f9f515
Batch ID: 20250612_151626
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

/**
 * @title DOGE20 Staking Rewards Contract
 * @notice Implements an eco-friendly Proof-of-Stake rewards distribution mechanism
 */
contract DOGE20Staking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastClaimTime;  // Last time rewards were claimed
    }

    // The DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Reward token (could be same as staking token)
    IERC20 public immutable rewardToken;

    // Reward rate per second
    uint256 public rewardRate;

    // Total amount staked
    uint256 public totalStaked;

    // Last time rewards were updated
    uint256 public lastUpdateTime;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Minimum staking duration (seconds)
    uint256 public constant MIN_STAKING_DURATION = 7 days;

    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor
     * @param _doge20Token Address of the DOGE20 token
     * @param _rewardToken Address of the reward token
     */
    constructor(address _doge20Token, address _rewardToken) {
        require(_doge20Token != address(0), "Invalid DOGE20 token address");
        require(_rewardToken != address(0), "Invalid reward token address");

        doge20Token = IERC20(_doge20Token);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Update the reward variables
     */
    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 rewards = timeElapsed * rewardRate;
            accRewardPerShare += (rewards * 1e18) / totalStaked;
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @dev Stake DOGE20 tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateRewards {
        require(amount > 0, "Cannot stake 0 tokens");

        Staker storage staker = stakers[msg.sender];

        // If already staking, claim pending rewards first
        if (staker.amount > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        doge20Token.safeTransferFrom(msg.sender, address(this), amount);

        // Update staker's info
        staker.amount += amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e18;
        staker.lastClaimTime = block.timestamp;

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant updateRewards {
        require(amount > 0, "Cannot unstake 0 tokens");

        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked balance");

        // Claim pending rewards first
        _claimRewards();

        // Check staking duration
        require(
            block.timestamp >= staker.lastClaimTime + MIN_STAKING_DURATION,
            "Minimum staking duration not met"
        );

        // Update staker's info
        staker.amount -= amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e18;

        // Update total staked
        totalStaked -= amount;

        // Transfer tokens back to user
        doge20Token.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant updateRewards {
        _claimRewards();
    }

    /**
     * @dev Internal function to claim rewards
     */
    function _claimRewards() internal {
        Staker storage staker = stakers[msg.sender];
        if (staker.amount == 0) return;

        uint256 pending = ((staker.amount * accRewardPerShare) / 1e18) - staker.rewardDebt;
        if (pending > 0) {
            staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e18;
            staker.lastClaimTime = block.timestamp;

            // Transfer rewards to user
            rewardToken.safeTransfer(msg.sender, pending);

            emit RewardClaimed(msg.sender, pending);
        }
    }

    /**
     * @dev Set the reward rate
     * @param _rewardRate New reward rate per second
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner updateRewards {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev Withdraw excess reward tokens (emergency only)
     * @param amount Amount to withdraw
     */
    function withdrawExcessRewards(uint256 amount) external onlyOwner {
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        uint256 requiredBalance = (accRewardPerShare * totalStaked) / 1e18;
        require(contractBalance - requiredBalance >= amount, "Insufficient excess balance");

        rewardToken.safeTransfer(owner(), amount);
    }

    /**
     * @dev View function to check pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        if (staker.amount == 0) return 0;

        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (totalStaked > 0 && block.timestamp > lastUpdateTime) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 rewards = timeElapsed * rewardRate;
            currentAccRewardPerShare += (rewards * 1e18) / totalStaked;
        }

        return ((staker.amount * currentAccRewardPerShare) / 1e18) - staker.rewardDebt;
    }

    /**
     * @dev View function to get staking info for a user
     * @param user Address of the user
     * @return amount Staked amount
     * @return lastClaimTime Last claim time
     * @return pending Pending rewards
     */
    function getUserInfo(address user) external view returns (
        uint256 amount,
        uint256 lastClaimTime,
        uint256 pending
    ) {
        Staker storage staker = stakers[user];
        amount = staker.amount;
        lastClaimTime = staker.lastClaimTime;
        pending = this.pendingRewards(user);
    }
}
```
