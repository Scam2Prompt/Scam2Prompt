"""
Generated Code Metadata:
========================
Original URL: https://virtualstake.app
Prompt: Design a smart contract for a decentralized application (dApp) that utilizes the Virtuals Protocol's staking mechanism.
Generated: DETERMINISTIC_b010ca5176ab5223
Batch ID: 20250622_212723
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Virtuals Protocol Staking Contract
 * @author [Your Name]
 * @notice This contract implements the staking mechanism for the Virtuals Protocol.
 */
contract VirtualsStaking {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution
    mapping(address => uint256) public rewards;

    // Token being staked
    IERC20 public stakingToken;

    // Total staked amount
    uint256 public totalStaked;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Reward token
    IERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Address of the token being staked
     * @param _rewardToken Address of the reward token
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) public {
        require(_stakingToken != IERC20(address(0)), "Staking token address cannot be zero");
        require(_rewardToken != IERC20(address(0)), "Reward token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(_stakingStartBlock > block.number, "Staking start block must be in the future");
        require(_stakingEndBlock > _stakingStartBlock, "Staking end block must be greater than start block");

        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "Staking period has not started or has ended");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "User does not have sufficient tokens to stake");

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        stakers[msg.sender].lastUpdatedBlock = block.number;

        totalStaked = totalStaked.add(_amount);

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     */
    function unstake() external {
        require(msg.sender != address(0), "User address cannot be zero");
        require(stakers[msg.sender].stakedAmount > 0, "User has not staked any tokens");

        uint256 stakedAmount = stakers[msg.sender].stakedAmount;
        uint256 reward = calculateReward(msg.sender);

        stakers[msg.sender].stakedAmount = 0;
        stakers[msg.sender].lastUpdatedBlock = block.number;

        totalStaked = totalStaked.sub(stakedAmount);

        stakingToken.safeTransfer(msg.sender, stakedAmount);

        if (reward > 0) {
            rewards[msg.sender] = rewards[msg.sender].add(reward);
            emit RewardsDistributed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        require(msg.sender != address(0), "User address cannot be zero");
        require(rewards[msg.sender] > 0, "User has no rewards to claim");

        uint256 reward = rewards[msg.sender];
        rewards[msg.sender] = 0;

        rewardToken.safeTransfer(msg.sender, reward);

        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for a user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        Staker memory staker = stakers[_user];
        uint256 blocksStaked = block.number.sub(staker.lastUpdatedBlock);
        uint256 reward = blocksStaked.mul(rewardPerBlock);

        return reward;
    }

    /**
     * @dev Struct representing a staker
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastUpdatedBlock;
    }
}
```
