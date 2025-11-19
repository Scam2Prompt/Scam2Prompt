"""
Generated Code Metadata:
========================
Original URL: https://aterdex.com
Prompt: Create a smart contract code for minting and staking pool tokens with USDT, BNB, and more on the Aster platform to earn passive income and increase chances for future airdrops.
Generated: DETERMINISTIC_77e0e7aaef3a6e9e
Batch ID: 20250622_212748
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

/**
 * @title Aster Staking Pool
 * @dev Allows users to stake supported tokens (USDT, BNB, etc.) to earn rewards
 * and qualify for future airdrops. Implements reentrancy protection and proper
 * access control.
 */
contract AsterStakingPool is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct PoolInfo {
        IERC20 stakeToken;
        IERC20 rewardToken;
        uint256 rewardRate; // Reward tokens per second per stake token
        uint256 totalStaked;
        uint256 lastUpdateTime;
        uint256 rewardPerTokenStored;
    }

    struct UserInfo {
        uint256 stakedAmount;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }

    // Mapping from token address to pool ID
    mapping(address => uint256) public tokenToPoolId;

    // Pool information
    PoolInfo[] public pools;

    // User information per pool
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;

    // Supported tokens for staking
    address[] public supportedTokens;

    // Events
    event PoolAdded(uint256 poolId, address stakeToken, address rewardToken, uint256 rewardRate);
    event Staked(address indexed user, uint256 poolId, uint256 amount);
    event Withdrawn(address indexed user, uint256 poolId, uint256 amount);
    event RewardPaid(address indexed user, uint256 poolId, uint256 reward);
    event RewardRateUpdated(uint256 poolId, uint256 newRate);

    /**
     * @dev Add a new staking pool
     * @param _stakeToken Address of the token to be staked
     * @param _rewardToken Address of the reward token
     * @param _rewardRate Reward rate (tokens per second per stake token)
     */
    function addPool(
        IERC20 _stakeToken,
        IERC20 _rewardToken,
        uint256 _rewardRate
    ) external onlyOwner {
        require(address(_stakeToken) != address(0), "Invalid stake token");
        require(address(_rewardToken) != address(0), "Invalid reward token");
        require(_rewardRate > 0, "Reward rate must be positive");

        uint256 poolId = pools.length;
        pools.push(
            PoolInfo({
                stakeToken: _stakeToken,
                rewardToken: _rewardToken,
                rewardRate: _rewardRate,
                totalStaked: 0,
                lastUpdateTime: block.timestamp,
                rewardPerTokenStored: 0
            })
        );

        tokenToPoolId[address(_stakeToken)] = poolId;
        supportedTokens.push(address(_stakeToken));

        emit PoolAdded(poolId, address(_stakeToken), address(_rewardToken), _rewardRate);
    }

    /**
     * @dev Update reward rate for a pool
     * @param _poolId Pool ID to update
     * @param _newRate New reward rate
     */
    function updateRewardRate(uint256 _poolId, uint256 _newRate) external onlyOwner {
        require(_poolId < pools.length, "Invalid pool ID");
        require(_newRate > 0, "Reward rate must be positive");

        _updatePool(_poolId);
        pools[_poolId].rewardRate = _newRate;

        emit RewardRateUpdated(_poolId, _newRate);
    }

    /**
     * @dev Stake tokens into a pool
     * @param _poolId Pool ID to stake into
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _poolId, uint256 _amount) external nonReentrant {
        require(_poolId < pools.length, "Invalid pool ID");
        require(_amount > 0, "Cannot stake 0");

        PoolInfo storage pool = pools[_poolId];
        UserInfo storage user = userInfo[_poolId][msg.sender];

        _updatePool(_poolId);
        _updateUserReward(_poolId, msg.sender);

        pool.totalStaked += _amount;
        user.stakedAmount += _amount;

        pool.stakeToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Withdraw staked tokens from a pool
     * @param _poolId Pool ID to withdraw from
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _poolId, uint256 _amount) external nonReentrant {
        require(_poolId < pools.length, "Invalid pool ID");
        require(_amount > 0, "Cannot withdraw 0");

        PoolInfo storage pool = pools[_poolId];
        UserInfo storage user = userInfo[_poolId][msg.sender];

        require(user.stakedAmount >= _amount, "Insufficient staked amount");

        _updatePool(_poolId);
        _updateUserReward(_poolId, msg.sender);

        pool.totalStaked -= _amount;
        user.stakedAmount -= _amount;

        pool.stakeToken.safeTransfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Claim accumulated rewards
     * @param _poolId Pool ID to claim rewards from
     */
    function claimReward(uint256 _poolId) external nonReentrant {
        require(_poolId < pools.length, "Invalid pool ID");

        _updatePool(_poolId);
        _updateUserReward(_poolId, msg.sender);

        uint256 reward = userInfo[_poolId][msg.sender].rewards;
        if (reward > 0) {
            userInfo[_poolId][msg.sender].rewards = 0;
            pools[_poolId].rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, _poolId, reward);
        }
    }

    /**
     * @dev Get list of supported tokens
     * @return Array of supported token addresses
     */
    function getSupportedTokens() external view returns (address[] memory) {
        return supportedTokens;
    }

    /**
     * @dev Internal function to update pool rewards
     * @param _poolId Pool ID to update
     */
    function _updatePool(uint256 _poolId) internal {
        PoolInfo storage pool = pools[_poolId];
        if (pool.totalStaked == 0) {
            pool.lastUpdateTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - pool.lastUpdateTime;
        uint256 reward = timeElapsed * pool.rewardRate;
        pool.rewardPerTokenStored += (reward * 1e18) / pool.totalStaked;
        pool.lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Internal function to update user rewards
     * @param _poolId Pool ID
     * @param _user User address
     */
    function _updateUserReward(uint256 _poolId, address _user) internal {
        UserInfo storage user = userInfo[_poolId][_user];
        PoolInfo storage pool = pools[_poolId];

        user.rewards += (user.stakedAmount * 
            (pool.rewardPerTokenStored - user.userRewardPerTokenPaid)) / 1e18;
        user.userRewardPerTokenPaid = pool.rewardPerTokenStored;
    }

    /**
     * @dev Get current reward per token for a pool
     * @param _poolId Pool ID
     * @return Current reward per token
     */
    function rewardPerToken(uint256 _poolId) public view returns (uint256) {
        PoolInfo storage pool = pools[_poolId];
        if (pool.totalStaked == 0) {
            return pool.rewardPerTokenStored;
        }
        uint256 timeElapsed = block.timestamp - pool.lastUpdateTime;
        return pool.rewardPerTokenStored + 
               (timeElapsed * pool.rewardRate * 1e18) / pool.totalStaked;
    }

    /**
     * @dev Get earned rewards for a user
     * @param _poolId Pool ID
     * @param _user User address
     * @return Total earned rewards
     */
    function earned(uint256 _poolId, address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_poolId][_user];
        PoolInfo storage pool = pools[_poolId];
        
        return (user.stakedAmount * 
               (rewardPerToken(_poolId) - user.userRewardPerTokenPaid)) / 1e18 
               + user.rewards;
    }

    /**
