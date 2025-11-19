"""
Generated Code Metadata:
========================
Original URL: https://opsec-1ne.pages.dev
Prompt: Develop a smart contract to integrate staking functionality for $OPSEC tokens, following the roadmap outlined for governance and DePIN development.
Generated: DETERMINISTIC_1c21abe2cab0a4a4
Batch ID: 20250612_151038
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

contract OPSECStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking details
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }

    // The OPSEC ERC20 token
    IERC20 public immutable opsToken;

    // Reward token (could be same as opsToken)
    IERC20 public immutable rewardToken;

    // Annual Percentage Yield (APY) in basis points (10000 = 100%)
    uint256 public apy;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of user to their stake
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event APYUpdated(uint256 newAPY);

    /**
     * @dev Constructor
     * @param _opsToken Address of OPSEC token
     * @param _rewardToken Address of reward token
     * @param _apy Initial APY in basis points
     */
    constructor(
        address _opsToken,
        address _rewardToken,
        uint256 _apy
    ) {
        require(_opsToken != address(0), "Invalid OPSEC token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_apy > 0, "APY must be greater than 0");

        opsToken = IERC20(_opsToken);
        rewardToken = IERC20(_rewardToken);
        apy = _apy;
    }

    /**
     * @dev Stake OPSEC tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(opsToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Claim any pending rewards first
        _claimRewards();

        // Transfer tokens from user to contract
        opsToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;
        userStake.rewardDebt = _calculateRewards(msg.sender);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake OPSEC tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        require(amount > 0, "Amount must be greater than 0");

        // Claim any pending rewards first
        _claimRewards();

        // Update stake
        userStake.amount -= amount;
        userStake.rewardDebt = _calculateRewards(msg.sender);
        totalStaked -= amount;

        // Transfer tokens back to user
        opsToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    /**
     * @dev Internal function to claim rewards
     */
    function _claimRewards() internal {
        uint256 rewardAmount = _calculateRewards(msg.sender);
        if (rewardAmount > 0) {
            Stake storage userStake = stakes[msg.sender];
            userStake.rewardDebt = 0;
            userStake.startTime = block.timestamp;

            rewardToken.safeTransfer(msg.sender, rewardAmount);
            emit RewardClaimed(msg.sender, rewardAmount);
        }
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @return rewardAmount Calculated reward amount
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 annualReward = (userStake.amount * apy) / 10000;
        uint256 rewardAmount = (annualReward * stakingDuration) / 365 days;

        return rewardAmount + userStake.rewardDebt;
    }

    /**
     * @dev View function to get pending rewards
     * @param user Address of the user
     * @return rewardAmount Pending reward amount
     */
    function pendingRewards(address user) external view returns (uint256) {
        return _calculateRewards(user);
    }

    /**
     * @dev Update APY (only owner)
     * @param newAPY New APY in basis points
     */
    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY > 0, "APY must be greater than 0");
        apy = newAPY;
        emit APYUpdated(newAPY);
    }

    /**
     * @dev Emergency withdraw all rewards (only owner)
     */
    function emergencyWithdrawRewards() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No rewards to withdraw");
        rewardToken.safeTransfer(owner(), balance);
    }

    /**
     * @dev Emergency recover ERC20 tokens (only owner)
     * @param tokenAddress Address of the token
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(opsToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
