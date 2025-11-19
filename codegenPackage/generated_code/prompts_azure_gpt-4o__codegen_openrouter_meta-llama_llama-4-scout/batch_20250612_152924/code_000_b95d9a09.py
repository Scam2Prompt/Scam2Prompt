"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Write a smart contract in Solidity for staking $MGLS tokens, ensuring users can earn rewards based on their share of the staking pool and annual returns percentage, as described in the Meme Moguls ecosystem.
Generated: DETERMINISTIC_b95d9a09b5f98958
Batch ID: 20250612_152924
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MemeMogulsStakingContract
 * @author [Your Name]
 * @notice A staking contract for $MGLS tokens in the Meme Moguls ecosystem.
 */
contract MemeMogulsStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public userStakes;

    // Mapping of user reward debt
    mapping(address => uint256) public userRewardDebt;

    // Total staking pool
    uint256 public totalStaked;

    // Annual returns percentage (in basis points, e.g., 10% = 1000)
    uint256 public annualReturnsPercentage;

    // $MGLS token contract
    IERC20 public mgLsToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Total rewards
    uint256 public totalRewards;

    /**
     * @dev Emitted when a user stakes $MGLS tokens
     * @param user The user's address
     * @param amount The amount of $MGLS tokens staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Emitted when a user unstakes $MGLS tokens
     * @param user The user's address
     * @param amount The amount of $MGLS tokens unstaked
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Emitted when rewards are distributed
     * @param user The user's address
     * @param amount The amount of rewards distributed
     */
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param mgLsTokenAddress The address of the $MGLS token contract
     * @param annualReturnsPercentage_ The annual returns percentage (in basis points)
     * @param rewardPerBlock_ The reward per block
     */
    constructor(
        address mgLsTokenAddress,
        uint256 annualReturnsPercentage_,
        uint256 rewardPerBlock_
    ) public {
        require(mgLsTokenAddress != address(0), "MGLS token address cannot be zero");
        require(annualReturnsPercentage_ > 0, "Annual returns percentage must be greater than zero");
        require(rewardPerBlock_ > 0, "Reward per block must be greater than zero");

        mgLsToken = IERC20(mgLsTokenAddress);
        annualReturnsPercentage = annualReturnsPercentage_;
        rewardPerBlock = rewardPerBlock_;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake $MGLS tokens
     * @param amount The amount of $MGLS tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");
        require(mgLsToken.transferFrom(msg.sender, address(this), amount), "Failed to transfer $MGLS tokens");

        // Update user's stake and reward debt
        if (userStakes[msg.sender] > 0) {
            _distributeRewards(msg.sender);
        }

        userStakes[msg.sender] = userStakes[msg.sender].add(amount);
        userRewardDebt[msg.sender] = userRewardDebt[msg.sender].add(amount);

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $MGLS tokens
     * @param amount The amount of $MGLS tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's stake and reward debt
        _distributeRewards(msg.sender);

        userStakes[msg.sender] = userStakes[msg.sender].sub(amount);
        userRewardDebt[msg.sender] = userRewardDebt[msg.sender].sub(amount);

        totalStaked = totalStaked.sub(amount);

        require(mgLsToken.transfer(msg.sender, amount), "Failed to transfer $MGLS tokens");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards to a user
     * @param user The user's address
     */
    function _distributeRewards(address user) internal {
        uint256 pendingRewards = _getPendingRewards(user);
        if (pendingRewards > 0) {
            userRewardDebt[user] = userRewardDebt[user].sub(pendingRewards);
            totalRewards = totalRewards.sub(pendingRewards);

            require(mgLsToken.transfer(user, pendingRewards), "Failed to transfer rewards");

            emit RewardsDistributed(user, pendingRewards);
        }
    }

    /**
     * @dev Get pending rewards for a user
     * @param user The user's address
     * @return The pending rewards
     */
    function _getPendingRewards(address user) internal view returns (uint256) {
        uint256 currentBlock = block.number;
        uint256 rewards = 0;

        if (currentBlock > lastRewardBlock && totalStaked > 0) {
            uint256 blocksElapsed = currentBlock.sub(lastRewardBlock);
            uint256 totalReward = blocksElapsed.mul(rewardPerBlock);
            uint256 userShare = userStakes[user].mul(annualReturnsPercentage).div(10000);

            rewards = userStakes[user].mul(totalReward).div(totalStaked).add(userShare);
        }

        return rewards;
    }

    /**
     * @dev Update reward variables
     */
    function _updateRewardVariables() internal {
        uint256 currentBlock = block.number;

        if (currentBlock > lastRewardBlock && totalStaked > 0) {
            uint256 blocksElapsed = currentBlock.sub(lastRewardBlock);
            uint256 totalReward = blocksElapsed.mul(rewardPerBlock);

            totalRewards = totalRewards.add(totalReward);
            lastRewardBlock = currentBlock;
        }
    }

    /**
     * @dev Get user staking information
     * @param user The user's address
     * @return The user's stake, reward debt, and pending rewards
     */
    function getUserStakingInfo(address user) external view returns (
        uint256 stake,
        uint256 rewardDebt,
        uint256 pendingRewards
    ) {
        stake = userStakes[user];
        rewardDebt = userRewardDebt[user];
        pendingRewards = _getPendingRewards(user);
    }
}
```
