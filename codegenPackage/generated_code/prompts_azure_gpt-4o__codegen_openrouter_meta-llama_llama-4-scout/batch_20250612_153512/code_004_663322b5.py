"""
Generated Code Metadata:
========================
Original URL: https://agora-ai.market
Prompt: Write a smart contract in Solidity to interact with Agora AI's tokenomics system, specifically for staking AGAI tokens.
Generated: DETERMINISTIC_663322b591ae5be7
Batch ID: 20250612_153512
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
 * @title Agora AI Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake AGAI tokens and earn rewards.
 */
contract AgoraAIStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // AGAI token contract
    IERC20 public agaiToken;

    // Staking pool structure
    struct StakingPool {
        uint256 totalStaked; // Total AGAI tokens staked in the pool
        uint256 rewardPerShare; // Reward per share
        uint256 lastRewardTime; // Last time rewards were distributed
    }

    // Mapping of user staking information
    mapping(address => mapping(uint256 => uint256)) public userStakingInfo;

    // Mapping of staking pools
    mapping(uint256 => StakingPool) public stakingPools;

    // Event emitted when user stakes AGAI tokens
    event Staked(address indexed user, uint256 poolId, uint256 amount);

    // Event emitted when user unstakes AGAI tokens
    event Unstaked(address indexed user, uint256 poolId, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 poolId, uint256 amount);

    /**
     * @param _agaiToken Address of the AGAI token contract
     */
    constructor(address _agaiToken) {
        agaiToken = IERC20(_agaiToken);

        // Initialize staking pool 0
        stakingPools[0] = StakingPool(0, 0, block.timestamp);
    }

    /**
     * @dev Stake AGAI tokens in a pool
     * @param _poolId ID of the staking pool
     * @param _amount Amount of AGAI tokens to stake
     */
    function stake(uint256 _poolId, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(stakingPools[_poolId].totalStaked >= 0, "Invalid pool");

        // Transfer AGAI tokens from user to contract
        agaiToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        userStakingInfo[msg.sender][_poolId] = userStakingInfo[msg.sender][_poolId].add(_amount);

        // Update staking pool
        stakingPools[_poolId].totalStaked = stakingPools[_poolId].totalStaked.add(_amount);

        emit Staked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Unstake AGAI tokens from a pool
     * @param _poolId ID of the staking pool
     * @param _amount Amount of AGAI tokens to unstake
     */
    function unstake(uint256 _poolId, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfo[msg.sender][_poolId] >= _amount, "Insufficient staked amount");

        // Update user's staking information
        userStakingInfo[msg.sender][_poolId] = userStakingInfo[msg.sender][_poolId].sub(_amount);

        // Update staking pool
        stakingPools[_poolId].totalStaked = stakingPools[_poolId].totalStaked.sub(_amount);

        // Transfer AGAI tokens from contract to user
        agaiToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Distribute rewards to stakers in a pool
     * @param _poolId ID of the staking pool
     */
    function distributeRewards(uint256 _poolId) external nonReentrant {
        StakingPool storage pool = stakingPools[_poolId];

        // Calculate rewards
        uint256 rewards = calculateRewards(_poolId);

        // Update reward per share
        pool.rewardPerShare = pool.rewardPerShare.add(rewards.div(pool.totalStaked));

        // Update last reward time
        pool.lastRewardTime = block.timestamp;

        emit RewardsDistributed(_poolId, rewards);
    }

    /**
     * @dev Calculate rewards for a pool
     * @param _poolId ID of the staking pool
     * @return Rewards for the pool
     */
    function calculateRewards(uint256 _poolId) internal view returns (uint256) {
        // TO DO: implement reward calculation logic
        return 0;
    }

    /**
     * @dev Get user's staking information
     * @param _user Address of the user
     * @param _poolId ID of the staking pool
     * @return User's staked amount
     */
    function getUserStakingInfo(address _user, uint256 _poolId) external view returns (uint256) {
        return userStakingInfo[_user][_poolId];
    }
}
```
