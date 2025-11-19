"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-in.web.app
Prompt: Develop a smart contract code snippet for staking $POODL tokens and earning rewards, based on the project's staking kennel mechanism.
Generated: DETERMINISTIC_faeb8d758775f024
Batch ID: 20250622_210650
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PoodlStakingKennel
 * @author [Your Name]
 * @notice A smart contract for staking $POODL tokens and earning rewards.
 */
contract PoodlStakingKennel is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // POODL token contract
    IERC20 public poodlToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Total staked POODL tokens
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last block number that reward was distributed
    uint256 public lastRewardBlock;

    // Staking kennel settings
    uint256 public stakingKennelId;

    // Event emitted when a user stakes POODL tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes POODL tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _poodlToken POODL token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Reward per block
     * @param _stakingKennelId Staking kennel ID
     */
    constructor(
        address _poodlToken,
        address _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _stakingKennelId
    ) public {
        require(_poodlToken != address(0), "POODL token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        poodlToken = IERC20(_poodlToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        stakingKennelId = _stakingKennelId;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake POODL tokens
     * @param _amount Amount of POODL tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.rewardDebt = staker.rewardDebt.add(_amount);

        totalStaked = totalStaked.add(_amount);

        // Transfer POODL tokens to the contract
        require(poodlToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer POODL tokens");

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake POODL tokens
     * @param _amount Amount of POODL tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(_amount);
        staker.rewardDebt = staker.rewardDebt.sub(_amount);

        totalStaked = totalStaked.sub(_amount);

        // Transfer POODL tokens to the user
        require(poodlToken.transfer(msg.sender, _amount), "Failed to transfer POODL tokens");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];

        // Calculate rewards
        uint256 rewards = calculateRewards(staker);

        // Update reward debt
        staker.rewardDebt = staker.stakedAmount;

        // Transfer rewards to the user
        require(rewardToken.transfer(msg.sender, rewards), "Failed to transfer rewards");

        emit RewardsDistributed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a staker
     * @param _staker Staker information
     * @return Rewards for the staker
     */
    function calculateRewards(Staker storage _staker) internal view returns (uint256) {
        uint256 rewards = 0;

        // Calculate rewards since last reward distribution
        if (_staker.stakedAmount > 0) {
            uint256 blocksElapsed = block.number.sub(lastRewardBlock);
            rewards = _staker.stakedAmount.mul(rewardPerBlock).mul(blocksElapsed);
        }

        // Update last reward block
        lastRewardBlock = block.number;

        return rewards;
    }

    /**
     * @dev Struct for staker information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }
}
```
