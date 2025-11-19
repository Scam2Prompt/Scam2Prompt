"""
Generated Code Metadata:
========================
Original URL: https://app-xai-games.pages.dev
Prompt: Create a smart contract that implements staking tiers and reward multipliers for esXAI tokens, ensuring compatibility with self-custody wallets and Ledger hardware wallets, as outlined on the Xai Staking webpage.
Generated: DETERMINISTIC_5e2653b02c5db674
Batch ID: 20250612_152527
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract XaiStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Staking token (esXAI)
    IERC20 public immutable stakingToken;

    // Staking tier structure
    struct Tier {
        uint256 minAmount;
        uint256 multiplier; // Multiplier in basis points (10000 = 1x)
        uint256 lockDuration; // Duration in seconds
    }

    // Staker information
    struct Staker {
        uint256 amount;
        uint256 tierIndex;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    // Staking tiers configuration
    Tier[] public tiers;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 tierIndex);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TierAdded(uint256 minAmount, uint256 multiplier, uint256 lockDuration);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _stakingToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;

        // Initialize default tiers (example values)
        tiers.push(Tier(1000 ether, 10000, 30 days));  // Tier 0: 1x, 30 days
        tiers.push(Tier(5000 ether, 12000, 60 days));  // Tier 1: 1.2x, 60 days
        tiers.push(Tier(10000 ether, 15000, 90 days)); // Tier 2: 1.5x, 90 days
    }

    /**
     * @dev Stake tokens into a specific tier
     * @param amount Amount of tokens to stake
     * @param tierIndex Index of the tier to stake into
     */
    function stake(uint256 amount, uint256 tierIndex) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(tierIndex < tiers.length, "Invalid tier index");
        require(amount >= tiers[tierIndex].minAmount, "Amount below tier minimum");

        Staker storage staker = stakers[msg.sender];

        // Claim any pending rewards before staking
        if (staker.amount > 0) {
            _claimRewards(msg.sender);
        }

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staker info
        staker.amount += amount;
        staker.tierIndex = tierIndex;
        staker.stakedAt = block.timestamp;
        staker.lastClaimed = block.timestamp;

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount, tierIndex);
    }

    /**
     * @dev Unstake tokens and claim rewards
     */
    function unstake() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked amount");

        // Check lock duration
        Tier memory tier = tiers[staker.tierIndex];
        require(block.timestamp >= staker.stakedAt + tier.lockDuration, "Tokens are locked");

        // Claim rewards
        _claimRewards(msg.sender);

        uint256 amount = staker.amount;

        // Reset staker info
        delete stakers[msg.sender];

        // Update total staked
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].amount > 0, "No staked amount");
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     * @param user Address of the staker
     */
    function _claimRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 reward = calculatePendingReward(user);

        if (reward > 0) {
            staker.lastClaimed = block.timestamp;
            stakingToken.safeTransfer(user, reward);
            emit RewardClaimed(user, reward);
        }
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param user Address of the staker
     * @return Amount of pending rewards
     */
    function calculatePendingReward(address user) public view returns (uint256) {
        Staker memory staker = stakers[user];
        if (staker.amount == 0) return 0;

        Tier memory tier = tiers[staker.tierIndex];
        uint256 timeStaked = block.timestamp - staker.lastClaimed;
        uint256 baseReward = rewardRate * timeStaked * staker.amount / 1e18;
        
        return baseReward * tier.multiplier / 10000;
    }

    /**
     * @dev Add a new staking tier (owner only)
     * @param minAmount Minimum amount required for this tier
     * @param multiplier Reward multiplier in basis points
     * @param lockDuration Duration tokens must be locked for this tier
     */
    function addTier(uint256 minAmount, uint256 multiplier, uint256 lockDuration) external onlyOwner {
        tiers.push(Tier(minAmount, multiplier, lockDuration));
        emit TierAdded(minAmount, multiplier, lockDuration);
    }

    /**
     * @dev Update reward rate (owner only)
     * @param newRate New reward rate per second
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Emergency withdraw tokens from contract (owner only)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
