"""
Generated Code Metadata:
========================
Original URL: https://levva.net
Prompt: How can I implement staking for $LVVA to maximize my rewards on Levva's platform?
Generated: DETERMINISTIC_95d0001b9dd11702
Batch ID: 20250612_161317
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

contract LVVAStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staking position
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }

    // The LVVA token contract
    IERC20 public immutable lvvaToken;

    // Reward token (could be same as LVVA or different)
    IERC20 public immutable rewardToken;

    // Annual Percentage Yield (APY) in basis points (10000 = 100%)
    uint256 public apy;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event APYUpdated(uint256 newAPY);

    constructor(
        address _lvvaToken,
        address _rewardToken,
        uint256 _apy
    ) {
        require(_lvvaToken != address(0), "LVVA token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        
        lvvaToken = IERC20(_lvvaToken);
        rewardToken = IERC20(_rewardToken);
        apy = _apy;
    }

    /**
     * @notice Stake LVVA tokens to earn rewards
     * @param amount The amount of LVVA tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update any existing rewards before new stake
        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        lvvaToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake LVVA tokens and claim rewards
     * @param amount The amount of LVVA tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Claim any pending rewards first
        _claimRewards();

        // Update stake
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        lvvaToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     */
    function _claimRewards() private {
        uint256 reward = calculateRewards(msg.sender);
        if (reward > 0) {
            stakes[msg.sender].startTime = block.timestamp;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    /**
     * @notice Calculate pending rewards for a user
     * @param user The address of the user
     * @return The amount of reward tokens available
     */
    function calculateRewards(address user) public view returns (uint256) {
        if (stakes[user].amount == 0) return 0;

        uint256 stakedTime = block.timestamp - stakes[user].startTime;
        uint256 rewardPerYear = (stakes[user].amount * apy) / 10000;
        uint256 reward = (rewardPerYear * stakedTime) / 365 days;

        return reward;
    }

    /**
     * @notice Update the APY for staking rewards
     * @param newAPY The new APY in basis points (10000 = 100%)
     */
    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY <= 10000, "APY cannot exceed 100%");
        apy = newAPY;
        emit APYUpdated(newAPY);
    }

    /**
     * @notice Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(lvvaToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
