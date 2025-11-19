"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Write a Solidity function to implement the staking mechanism for $DUM tokens, ensuring secure and efficient transactions on a decentralized exchange.
Generated: DETERMINISTIC_a96bbecb7c9d51db
Batch ID: 20250622_210821
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
 * @title StakingMechanism
 * @author [Your Name]
 * @notice This contract implements the staking mechanism for $DUM tokens.
 */
contract StakingMechanism is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of staking pool information
    mapping(uint256 => StakingPool) public stakingPools;

    // $DUM token contract
    IERC20 public dumToken;

    // Total number of staking pools
    uint256 public totalStakingPools;

    // Event emitted when a user stakes $DUM tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes $DUM tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _dumTokenAddress Address of the $DUM token contract
     */
    constructor(address _dumTokenAddress) {
        require(_dumTokenAddress != address(0), "DUM token address cannot be zero");

        dumToken = IERC20(_dumTokenAddress);
    }

    /**
     * @notice Creates a new staking pool
     * @param _poolId Unique identifier for the staking pool
     * @param _rewardPerBlock Reward per block for the staking pool
     * @param _startBlock Start block for the staking pool
     * @param _endBlock End block for the staking pool
     */
    function createStakingPool(
        uint256 _poolId,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) public {
        require(msg.sender == owner(), "Only the owner can create a staking pool");
        require(_poolId > 0, "Pool ID must be greater than zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(_startBlock < _endBlock, "Start block must be less than end block");

        stakingPools[_poolId] = StakingPool(_rewardPerBlock, _startBlock, _endBlock);
        totalStakingPools++;
    }

    /**
     * @notice Stakes $DUM tokens for a user
     * @param _poolId Unique identifier for the staking pool
     * @param _amount Amount of $DUM tokens to stake
     */
    function stake(uint256 _poolId, uint256 _amount) public {
        require(stakingPools[_poolId].rewardPerBlock > 0, "Staking pool does not exist");
        require(_amount > 0, "Staking amount must be greater than zero");

        StakingPool storage pool = stakingPools[_poolId];
        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];

        // Transfer $DUM tokens from user to contract
        dumToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        if (userInfo.poolId == 0) {
            userInfo.poolId = _poolId;
            userInfo.amount = _amount;
            userInfo.rewardDebt = 0;
        } else if (userInfo.poolId == _poolId) {
            userInfo.amount = userInfo.amount.add(_amount);
        } else {
            // User is already staking in another pool, need to unstake first
            require(false, "User is already staking in another pool");
        }

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstakes $DUM tokens for a user
     * @param _poolId Unique identifier for the staking pool
     * @param _amount Amount of $DUM tokens to unstake
     */
    function unstake(uint256 _poolId, uint256 _amount) public {
        require(stakingPools[_poolId].rewardPerBlock > 0, "Staking pool does not exist");
        require(_amount > 0, "Unstaking amount must be greater than zero");

        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];

        // Check if user is staking in the specified pool
        require(userInfo.poolId == _poolId, "User is not staking in this pool");

        // Check if user has sufficient staked amount
        require(userInfo.amount >= _amount, "User does not have sufficient staked amount");

        // Update user's staking information
        userInfo.amount = userInfo.amount.sub(_amount);
        userInfo.rewardDebt = userInfo.rewardDebt.sub(_amount);

        // Transfer $DUM tokens from contract to user
        dumToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claims rewards for a user
     * @param _poolId Unique identifier for the staking pool
     */
    function claimRewards(uint256 _poolId) public {
        require(stakingPools[_poolId].rewardPerBlock > 0, "Staking pool does not exist");

        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];

        // Check if user is staking in the specified pool
        require(userInfo.poolId == _poolId, "User is not staking in this pool");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender, _poolId);

        // Update user's reward debt
        userInfo.rewardDebt = userInfo.rewardDebt.add(rewards);

        // Transfer rewards to user
        dumToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculates rewards for a user
     * @param _user Address of the user
     * @param _poolId Unique identifier for the staking pool
     * @return Rewards for the user
     */
    function calculateRewards(address _user, uint256 _poolId) internal view returns (uint256) {
        UserStakingInfo storage userInfo = userStakingInfos[_user];
        StakingPool storage pool = stakingPools[_poolId];

        // Calculate rewards
        uint256 rewards = userInfo.amount.mul(pool.rewardPerBlock).mul(block.number.sub(pool.startBlock)).div(1e18);

        // Subtract user's reward debt
        rewards = rewards.sub(userInfo.rewardDebt);

        return rewards;
    }

    // Struct to store user's staking information
    struct UserStakingInfo {
        uint256 poolId;
        uint256 amount;
        uint256 rewardDebt;
    }

    // Struct to store staking pool information
    struct StakingPool {
        uint256 rewardPerBlock;
        uint256 startBlock;
        uint256 endBlock;
    }
}
```
