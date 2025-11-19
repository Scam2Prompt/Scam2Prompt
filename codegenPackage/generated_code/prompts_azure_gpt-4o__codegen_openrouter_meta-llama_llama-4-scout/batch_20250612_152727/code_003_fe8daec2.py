"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-as.web.app
Prompt: Create a smart contract on Ethereum Layer 2 that facilitates double staking rewards for $PEPU tokens, ensuring compatibility with the Pepe Unchained ecosystem.
Generated: DETERMINISTIC_fe8daec2af89f76f
Batch ID: 20250612_152727
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
 * @title PepeUnchainedDoubleStakingRewards
 * @author [Your Name]
 * @notice A smart contract that facilitates double staking rewards for $PEPU tokens
 *         on Ethereum Layer 2, ensuring compatibility with the Pepe Unchained ecosystem.
 */
contract PepeUnchainedDoubleStakingRewards is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Constants
    address public immutable PEPU_TOKEN;
    address public immutable REWARDS_TOKEN;
    uint256 public immutable REWARDS_PER_BLOCK;

    // State variables
    mapping(address => uint256) public stakingBalances;
    mapping(address => uint256) public rewardsEarned;
    uint256 public totalStaked;
    uint256 public lastRewardBlock;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _pepuToken Address of the $PEPU token
     * @param _rewardsToken Address of the rewards token
     * @param _rewardsPerBlock Rewards per block
     */
    constructor(address _pepuToken, address _rewardsToken, uint256 _rewardsPerBlock) {
        PEPU_TOKEN = _pepuToken;
        REWARDS_TOKEN = _rewardsToken;
        REWARDS_PER_BLOCK = _rewardsPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake $PEPU tokens to earn double rewards
     * @param amount Amount of $PEPU tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid stake amount");
        require(IERC20(PEPU_TOKEN).balanceOf(msg.sender) >= amount, "Insufficient balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        IERC20(PEPU_TOKEN).safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake $PEPU tokens
     * @param amount Amount of $PEPU tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        IERC20(PEPU_TOKEN).safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        rewardsEarned[msg.sender] = 0;
        IERC20(REWARDS_TOKEN).safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a user
     * @param user Address of the user
     * @return Rewards earned by the user
     */
    function calculateRewards(address user) internal returns (uint256) {
        uint256 currentBlock = block.number;
        uint256 rewards = 0;

        if (totalStaked > 0) {
            uint256 stakingBlocks = currentBlock.sub(lastRewardBlock);
            rewards = stakingBlocks.mul(REWARDS_PER_BLOCK).mul(stakingBalances[user]).div(totalStaked);
            rewardsEarned[user] = rewardsEarned[user].add(rewards);
            lastRewardBlock = currentBlock;
        }

        return rewardsEarned[user];
    }

    /**
     * @notice Get user staking information
     * @param user Address of the user
     * @return Staking balance and rewards earned
     */
    function getUserStakingInfo(address user) external view returns (uint256, uint256) {
        return (stakingBalances[user], rewardsEarned[user]);
    }
}
```
