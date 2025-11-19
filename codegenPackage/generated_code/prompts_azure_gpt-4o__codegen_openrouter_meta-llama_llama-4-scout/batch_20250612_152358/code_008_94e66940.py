"""
Generated Code Metadata:
========================
Original URL: https://appscottyclaims.pages.dev
Prompt: Develop a Solidity contract to lock liquidity for $SCOTTY tokens, ensuring rewards distribution and staking functionality for the Scotty AI cryptoverse.
Generated: DETERMINISTIC_94e66940e7466b9c
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ScottyAILiquidityLocker
 * @author [Your Name]
 * @notice This contract locks liquidity for $SCOTTY tokens and handles rewards distribution and staking functionality.
 */
contract ScottyAILiquidityLocker is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Mapping of reward distribution
    mapping(address => mapping(address => uint256)) public userRewards;

    // Total staking balance
    uint256 public totalStakingBalance;

    // $SCOTTY token contract
    ERC20 public scottyToken;

    // Reward token contract
    ERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param scottyTokenAddress $SCOTTY token contract address
     * @param rewardTokenAddress Reward token contract address
     * @param rewardPerBlock Reward per block
     */
    constructor(
        address scottyTokenAddress,
        address rewardTokenAddress,
        uint256 rewardPerBlock
    ) public {
        scottyToken = ERC20(scottyTokenAddress);
        rewardToken = ERC20(rewardTokenAddress);
        rewardPerBlock = rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake $SCOTTY tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid stake amount");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Failed to transfer $SCOTTY tokens");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStakingBalance = totalStakingBalance.add(amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake $SCOTTY tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStakingBalance = totalStakingBalance.sub(amount);

        // Transfer $SCOTTY tokens back to user
        require(scottyToken.transfer(msg.sender, amount), "Failed to transfer $SCOTTY tokens");

        // Update user's reward debt
        updateRewardDebt(msg.sender);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Update user's reward debt
     * @param user User address
     */
    function updateRewardDebt(address user) internal {
        // Calculate rewards earned
        uint256 rewardsEarned = calculateRewards(user);

        // Update user's reward debt
        rewardDebt[user] = rewardsEarned;
    }

    /**
     * @notice Calculate rewards earned by user
     * @param user User address
     * @return Rewards earned
     */
    function calculateRewards(address user) public view returns (uint256) {
        // Calculate block interval
        uint256 blockInterval = block.number.sub(lastRewardBlock);

        // Calculate rewards earned
        uint256 rewardsEarned = stakingBalances[user].mul(rewardPerBlock).mul(blockInterval);

        return rewardsEarned;
    }

    /**
     * @notice Distribute rewards to users
     */
    function distributeRewards() public nonReentrant {
        // Calculate total rewards earned
        uint256 totalRewardsEarned = calculateTotalRewards();

        // Distribute rewards to users
        for (address user in stakingBalances) {
            uint256 userRewardsEarned = calculateRewards(user);

            // Update user's rewards
            userRewards[msg.sender][user] = userRewards[msg.sender][user].add(userRewardsEarned);

            // Transfer rewards to user
            require(rewardToken.transfer(user, userRewardsEarned), "Failed to transfer rewards");

            emit RewardsDistributed(user, userRewardsEarned);
        }

        // Update last reward block
        lastRewardBlock = block.number;

        // Update total rewards distributed
        totalRewardsDistributed = totalRewardsDistributed.add(totalRewardsEarned);
    }

    /**
     * @notice Calculate total rewards earned
     * @return Total rewards earned
     */
    function calculateTotalRewards() public view returns (uint256) {
        // Calculate block interval
        uint256 blockInterval = block.number.sub(lastRewardBlock);

        // Calculate total rewards earned
        uint256 totalRewardsEarned = totalStakingBalance.mul(rewardPerBlock).mul(blockInterval);

        return totalRewardsEarned;
    }
}
```
