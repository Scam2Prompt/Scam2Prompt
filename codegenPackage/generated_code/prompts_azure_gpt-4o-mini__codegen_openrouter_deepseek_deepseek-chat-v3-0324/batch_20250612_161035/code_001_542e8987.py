"""
Generated Code Metadata:
========================
Original URL: https://presale-hypeloot.com
Prompt: Generate a Solidity smart contract that allows users to stake $HPLT tokens and receive daily rewards based on the amount staked, as described in the Hypeloot ecosystem.
Generated: DETERMINISTIC_542e8987babd1404
Batch ID: 20250612_161035
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

contract HPLTStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct StakeInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }

    // The HPLT token contract
    IERC20 public immutable hpltToken;

    // Reward rate per day (in basis points, 1 = 0.01%)
    uint256 public rewardRatePerDay;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping from user address to their stake info
    mapping(address => StakeInfo) public stakeInfo;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _hpltToken, uint256 _rewardRatePerDay) {
        require(_hpltToken != address(0), "HPLT token address cannot be zero");
        hpltToken = IERC20(_hpltToken);
        rewardRatePerDay = _rewardRatePerDay;
    }

    /**
     * @notice Stake HPLT tokens to earn rewards
     * @param amount The amount of HPLT tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        StakeInfo storage user = stakeInfo[msg.sender];

        // Claim any pending rewards first
        if (user.amount > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        hpltToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update user stake info
        user.amount += amount;
        user.rewardDebt = (user.amount * rewardRatePerDay) / 10000;
        user.lastClaimTime = block.timestamp;

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake HPLT tokens and claim rewards
     * @param amount The amount of HPLT tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        StakeInfo storage user = stakeInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked balance");

        // Claim any pending rewards first
        _claimRewards();

        // Update user stake info
        user.amount -= amount;
        user.rewardDebt = (user.amount * rewardRatePerDay) / 10000;

        // Update total staked
        totalStaked -= amount;

        // Transfer tokens back to user
        hpltToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        require(stakeInfo[msg.sender].amount > 0, "No staked balance");
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     */
    function _claimRewards() private {
        StakeInfo storage user = stakeInfo[msg.sender];
        uint256 pending = pendingRewards(msg.sender);

        if (pending > 0) {
            // Update last claim time
            user.lastClaimTime = block.timestamp;

            // Transfer rewards
            hpltToken.safeTransfer(msg.sender, pending);

            emit RewardClaimed(msg.sender, pending);
        }
    }

    /**
     * @notice Calculate pending rewards for a user
     * @param userAddress The address of the user
     * @return The amount of pending rewards
     */
    function pendingRewards(address userAddress) public view returns (uint256) {
        StakeInfo memory user = stakeInfo[userAddress];
        if (user.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - user.lastClaimTime;
        uint256 daysElapsed = timeElapsed / 1 days;
        
        if (daysElapsed == 0) return 0;
        
        return (user.amount * rewardRatePerDay * daysElapsed) / 10000;
    }

    /**
     * @notice Update the reward rate (only callable by owner)
     * @param newRate The new reward rate per day (in basis points)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate != rewardRatePerDay, "New rate must be different");
        rewardRatePerDay = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @notice Emergency withdraw all HPLT tokens from contract (only callable by owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = hpltToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        hpltToken.safeTransfer(owner(), balance);
    }
}
```
