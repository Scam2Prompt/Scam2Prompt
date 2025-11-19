"""
Generated Code Metadata:
========================
Original URL: https://aibalancer-protocol.com
Prompt: "Design a smart contract for secure asset reallocation and rewards distribution in a DeFi ecosystem, inspired by AIBalancer Protocol's architecture."
Generated: DETERMINISTIC_7e04a606127cbdb3
Batch ID: 20250622_211508
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Smart Contract for Secure Asset Reallocation and Rewards Distribution
 * @dev Inspired by AIBalancer Protocol's architecture
 * Features:
 * - Secure asset reallocation
 * - Fair rewards distribution
 * - Non-reentrant
 * - Ownable with transferable ownership
 */
contract DeFiAssetManager is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a participant's stake
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // The reward token
    IERC20 public rewardToken;
    
    // The staking tokens (assets)
    IERC20[] public stakingTokens;
    
    // Total staked amount per token
    mapping(address => uint256) public totalStaked;
    
    // Accumulated rewards per share
    uint256 public accRewardsPerShare;
    
    // Total rewards distributed
    uint256 public totalRewardsDistributed;
    
    // Reward distribution rate (tokens per block)
    uint256 public rewardRate;
    
    // Last update block number
    uint256 public lastUpdateBlock;
    
    // Mapping from user address to token address to Stake
    mapping(address => mapping(address => Stake)) public stakes;
    
    // Events
    event Staked(address indexed user, address indexed token, uint256 amount);
    event Unstaked(address indexed user, address indexed token, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event AssetReallocated(address indexed fromToken, address indexed toToken, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    
    /**
     * @dev Constructor
     * @param _rewardToken Address of the reward token
     * @param _stakingTokens Array of staking token addresses
     * @param _rewardRate Initial reward distribution rate
     */
    constructor(
        address _rewardToken,
        address[] memory _stakingTokens,
        uint256 _rewardRate
    ) {
        require(_rewardToken != address(0), "Reward token cannot be zero address");
        require(_stakingTokens.length > 0, "Must provide at least one staking token");
        
        rewardToken = IERC20(_rewardToken);
        
        for (uint256 i = 0; i < _stakingTokens.length; i++) {
            require(_stakingTokens[i] != address(0), "Staking token cannot be zero address");
            stakingTokens.push(IERC20(_stakingTokens[i]));
        }
        
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }
    
    /**
     * @dev Update the reward calculations
     */
    modifier updateRewards() {
        if (block.number > lastUpdateBlock) {
            uint256 blocksPassed = block.number.sub(lastUpdateBlock);
            uint256 reward = blocksPassed.mul(rewardRate);
            
            if (totalStaked[address(rewardToken)] > 0) {
                accRewardsPerShare = accRewardsPerShare.add(
                    reward.mul(1e18).div(totalStaked[address(rewardToken)])
                );
                totalRewardsDistributed = totalRewardsDistributed.add(reward);
            }
            
            lastUpdateBlock = block.number;
        }
        _;
    }
    
    /**
     * @dev Stake tokens
     * @param _token Address of the token to stake
     * @param _amount Amount to stake
     */
    function stake(address _token, uint256 _amount) external nonReentrant updateRewards {
        require(_amount > 0, "Cannot stake 0");
        require(isValidStakingToken(_token), "Invalid staking token");
        
        IERC20 token = IERC20(_token);
        
        // Update user's stake and reward debt
        Stake storage userStake = stakes[msg.sender][_token];
        if (userStake.amount > 0) {
            uint256 pending = userStake.amount.mul(accRewardsPerShare).div(1e18).sub(userStake.rewardDebt);
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
            }
        }
        
        // Transfer tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        
        // Update stake
        userStake.amount = userStake.amount.add(_amount);
        userStake.rewardDebt = userStake.amount.mul(accRewardsPerShare).div(1e18);
        totalStaked[_token] = totalStaked[_token].add(_amount);
        
        emit Staked(msg.sender, _token, _amount);
    }
    
    /**
     * @dev Unstake tokens
     * @param _token Address of the token to unstake
     * @param _amount Amount to unstake
     */
    function unstake(address _token, uint256 _amount) external nonReentrant updateRewards {
        require(_amount > 0, "Cannot unstake 0");
        Stake storage userStake = stakes[msg.sender][_token];
        require(userStake.amount >= _amount, "Insufficient stake");
        
        // Claim pending rewards
        uint256 pending = userStake.amount.mul(accRewardsPerShare).div(1e18).sub(userStake.rewardDebt);
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
        }
        
        // Update stake
        userStake.amount = userStake.amount.sub(_amount);
        userStake.rewardDebt = userStake.amount.mul(accRewardsPerShare).div(1e18);
        totalStaked[_token] = totalStaked[_token].sub(_amount);
        
        // Transfer tokens back to user
        require(IERC20(_token).transfer(msg.sender, _amount), "Transfer failed");
        
        emit Unstaked(msg.sender, _token, _amount);
    }
    
    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant updateRewards {
        uint256 totalPending = 0;
        
        // Calculate pending rewards for all staked tokens
        for (uint256 i = 0; i < stakingTokens.length; i++) {
            address token = address(stakingTokens[i]);
            Stake storage userStake = stakes[msg.sender][token];
            
            if (userStake.amount > 0) {
                uint256 pending = userStake.amount.mul(accRewardsPerShare).div(1e18).sub(userStake.rewardDebt);
                if (pending > 0) {
                    totalPending = totalPending.add(pending);
                    userStake.rewardDebt = userStake.amount.mul(accRewardsPerShare).div(1e18);
                }
            }
        }
        
        require(totalPending > 0, "No rewards to claim");
        safeTransferReward(msg.sender, totalPending);
        
        emit RewardClaimed(msg.sender, totalPending);
    }
    
    /**
     * @dev Reallocate assets between tokens
     * @param _fromToken Token to reallocate from
     * @param _toToken Token to reallocate to
     * @param _amount Amount to reallocate
     */
    function reallocateAssets(
        address _fromToken,
        address _toToken,
        uint256 _amount
    ) external onlyOwner nonReentrant updateRewards {
        require(_fromToken != _toToken, "Cannot reallocate to same token");
        require(isValidStakingToken(_fromToken), "Invalid from token");
        require(isValidStakingToken(_toToken), "Invalid to token");
        require(totalStaked[_fromToken] >= _amount, "Insufficient balance");
        
        // Update totals
        totalStaked[_fromToken] = totalStaked[_fromToken].sub(_amount);
        totalStaked[_toToken] = totalStaked[_toToken].add(_amount);
        
        emit AssetReallocated(_fromToken, _toToken, _amount);
    }
    
    /**
     * @dev Update reward rate
     * @param _newRate New reward rate
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner updateRewards {
        require(_newRate != rewardRate, "Same rate");
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }
    
    /**
     * @dev Check if token is a valid staking token
     * @param _token Token address to check
     * @return bool True if valid
     */
    function isValidStakingToken(address _token) public view returns (bool) {
        for (uint256 i =
