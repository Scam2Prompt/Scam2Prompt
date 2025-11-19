"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity function to implement staking for $GNS tokens, allowing users to earn real yield, as outlined in the Gains Network ecosystem.
Generated: DETERMINISTIC_9dbac38ac0e16f34
Batch ID: 20250612_152827
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
 * @title GNS Staking Contract
 * @author Gains Network
 * @notice This contract allows users to stake $GNS tokens and earn real yield.
 */
contract GNSStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // GNS token contract
    IERC20 public gnsToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Staking pool structure
    struct StakingPool {
        uint256 totalStaked; // Total GNS tokens staked
        uint256 totalRewards; // Total rewards accumulated
        uint256 lastUpdateTime; // Last update timestamp
        uint256 rewardRate; // Reward rate per second
    }

    // Mapping of user staking information
    mapping(address => mapping(uint256 => uint256)) public userStakingBalances;

    // Mapping of staking pools
    mapping(uint256 => StakingPool) public stakingPools;

    // Event emitted when user stakes GNS tokens
    event Staked(address indexed user, uint256 poolId, uint256 amount);

    // Event emitted when user unstakes GNS tokens
    event Unstaked(address indexed user, uint256 poolId, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 poolId, uint256 amount);

    /**
     * @notice Constructor
     * @param _gnsToken GNS token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _gnsToken, address _rewardToken) {
        require(_gnsToken != address(0), "GNS token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        gnsToken = IERC20(_gnsToken);
        rewardToken = IERC20(_rewardToken);

        // Initialize default staking pool
        stakingPools[0] = StakingPool(0, 0, block.timestamp, 1e18); // 1 GNS per second
    }

    /**
     * @notice Stake GNS tokens
     * @param _poolId Staking pool ID
     * @param _amount Amount of GNS tokens to stake
     */
    function stake(uint256 _poolId, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakingPools[_poolId].totalStaked >= 0, "Invalid staking pool");

        gnsToken.safeTransferFrom(msg.sender, address(this), _amount);

        userStakingBalances[msg.sender][_poolId] = userStakingBalances[msg.sender][_poolId].add(_amount);
        stakingPools[_poolId].totalStaked = stakingPools[_poolId].totalStaked.add(_amount);

        emit Staked(msg.sender, _poolId, _amount);
    }

    /**
     * @notice Unstake GNS tokens
     * @param _poolId Staking pool ID
     * @param _amount Amount of GNS tokens to unstake
     */
    function unstake(uint256 _poolId, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakingBalances[msg.sender][_poolId] >= _amount, "Insufficient staked balance");

        userStakingBalances[msg.sender][_poolId] = userStakingBalances[msg.sender][_poolId].sub(_amount);
        stakingPools[_poolId].totalStaked = stakingPools[_poolId].totalStaked.sub(_amount);

        gnsToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _poolId, _amount);
    }

    /**
     * @notice Claim rewards
     * @param _poolId Staking pool ID
     */
    function claimRewards(uint256 _poolId) external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender, _poolId);

        require(rewards > 0, "No rewards to claim");

        stakingPools[_poolId].totalRewards = stakingPools[_poolId].totalRewards.sub(rewards);
        userStakingBalances[msg.sender][_poolId] = 0; // Reset user balance

        rewardToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, _poolId, rewards);
    }

    /**
     * @notice Calculate rewards for user
     * @param _user User address
     * @param _poolId Staking pool ID
     * @return Rewards amount
     */
    function calculateRewards(address _user, uint256 _poolId) internal view returns (uint256) {
        uint256 stakedBalance = userStakingBalances[_user][_poolId];
        uint256 timeElapsed = block.timestamp.sub(stakingPools[_poolId].lastUpdateTime);
        uint256 rewards = stakedBalance.mul(stakingPools[_poolId].rewardRate).mul(timeElapsed);

        return rewards;
    }

    /**
     * @notice Update staking pool
     * @param _poolId Staking pool ID
     */
    function updateStakingPool(uint256 _poolId) external {
        stakingPools[_poolId].lastUpdateTime = block.timestamp;
    }
}
```
