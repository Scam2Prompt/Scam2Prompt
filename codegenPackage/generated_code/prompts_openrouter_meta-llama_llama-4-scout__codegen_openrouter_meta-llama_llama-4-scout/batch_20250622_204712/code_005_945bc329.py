"""
Generated Code Metadata:
========================
Original URL: https://olliivveemmaaiinn12893891bndjdbiqw.pages.dev
Prompt: "Create a simple staking contract that allows for active restakers to earn rewards in a Layer 2 network."
Generated: DETERMINISTIC_945bc329faf074dc
Batch ID: 20250622_204712
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
 * @title SimpleStakingContract
 * @author [Your Name]
 * @notice A simple staking contract for active restakers to earn rewards in a Layer2 network.
 */
contract SimpleStakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution
    mapping(address => uint256) public rewards;

    // Staking token address
    address public stakingToken;

    // Reward token address
    address public rewardToken;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardRate Reward rate per block
     */
    constructor(address _stakingToken, address _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid stake amount");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(amount);
        staker.lastUpdateBlock = block.number;

        totalStaked = totalStaked.add(amount);

        IERC20(stakingToken).safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(amount);
        staker.lastUpdateBlock = block.number;

        totalStaked = totalStaked.sub(amount);

        IERC20(stakingToken).safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Get staker information
     * @param user User address
     * @return Staker information
     */
    function getStakerInfo(address user) external view returns (uint256, uint256) {
        Staker storage staker = stakers[user];
        uint256 pendingRewards = calculatePendingRewards(staker);
        return (staker.stakedAmount, pendingRewards);
    }

    /**
     * @notice Calculate pending rewards for a staker
     * @param staker Staker information
     * @return Pending rewards
     */
    function calculatePendingRewards(Staker storage staker) internal view returns (uint256) {
        uint256 blocksElapsed = block.number.sub(staker.lastUpdateBlock);
        uint256 pendingRewards = blocksElapsed.mul(rewardRate).mul(staker.stakedAmount).div(totalStaked);
        return pendingRewards;
    }

    /**
     * @notice Distribute rewards to stakers
     */
    function distributeRewards() external {
        for (address user in stakers) {
            Staker storage staker = stakers[user];
            uint256 pendingRewards = calculatePendingRewards(staker);
            if (pendingRewards > 0) {
                rewards[user] = rewards[user].add(pendingRewards);
                staker.lastUpdateBlock = block.number;
                emit RewardsDistributed(user, pendingRewards);
            }
        }
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 claimableRewards = rewards[msg.sender];
        require(claimableRewards > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        IERC20(rewardToken).safeTransfer(msg.sender, claimableRewards);
    }

    struct Staker {
        uint256 stakedAmount;
        uint256 lastUpdateBlock;
    }
}
```
