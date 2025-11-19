"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: Create a staking contract that supports compounding rewards and allows users to stake AITECH tokens for a specified lock term.
Generated: DETERMINISTIC_470c87ba8af9372d
Batch ID: 20250622_205709
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AITECH Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake AITECH tokens for a specified lock term and earn compounding rewards.
 */
contract AITECHStaking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Struct to represent a user's stake
    struct Stake {
        uint256 amount;
        uint256 lockTerm;
        uint256 rewardDebt;
        uint256 lastRewardTime;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Mapping of lock terms to their respective reward rates
    mapping(uint256 => uint256) public rewardRates;

    // AITECH token contract
    IERC20 public aitechToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;

    // Total reward debt
    uint256 public totalRewardDebt;

    // Reward per second
    uint256 public rewardPerSecond;

    // Event emitted when a user stakes AITECH tokens
    event Staked(address indexed user, uint256 amount, uint256 lockTerm);

    // Event emitted when a user unstakes AITECH tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _aitechToken AITECH token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        address _aitechToken,
        address _rewardToken,
        uint256 _rewardPerSecond
    ) {
        aitechToken = IERC20(_aitechToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @notice Sets the reward rate for a lock term
     * @param _lockTerm Lock term
     * @param _rewardRate Reward rate
     */
    function setRewardRate(uint256 _lockTerm, uint256 _rewardRate) public onlyOwner {
        rewardRates[_lockTerm] = _rewardRate;
    }

    /**
     * @notice Stakes AITECH tokens for a specified lock term
     * @param _amount Amount to stake
     * @param _lockTerm Lock term
     */
    function stake(uint256 _amount, uint256 _lockTerm) public {
        require(_amount > 0, "Invalid stake amount");
        require(rewardRates[_lockTerm] > 0, "Invalid lock term");

        // Transfer AITECH tokens to the contract
        aitechToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].lockTerm = _lockTerm;
        stakes[msg.sender].lastRewardTime = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount, _lockTerm);
    }

    /**
     * @notice Unstakes AITECH tokens
     */
    function unstake() public {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No stake found");

        // Distribute rewards
        distributeRewards(msg.sender);

        // Transfer AITECH tokens to the user
        aitechToken.safeTransfer(msg.sender, userStake.amount);

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].lockTerm = 0;
        stakes[msg.sender].rewardDebt = 0;
        stakes[msg.sender].lastRewardTime = 0;

        // Update total staked amount
        totalStaked = totalStaked.sub(userStake.amount);

        // Emit event
        emit Unstaked(msg.sender, userStake.amount);
    }

    /**
     * @notice Distributes rewards to a user
     * @param _user User address
     */
    function distributeRewards(address _user) internal {
        Stake storage userStake = stakes[_user];

        // Calculate rewards
        uint256 rewards = calculateRewards(_user);

        // Update user's reward debt
        userStake.rewardDebt = userStake.rewardDebt.add(rewards);

        // Update total reward debt
        totalRewardDebt = totalRewardDebt.add(rewards);

        // Transfer rewards to the user
        rewardToken.safeTransfer(_user, rewards);

        // Emit event
        emit RewardsDistributed(_user, rewards);
    }

    /**
     * @notice Calculates rewards for a user
     * @param _user User address
     * @return Rewards
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];

        // Calculate elapsed time
        uint256 elapsedTime = block.timestamp.sub(userStake.lastRewardTime);

        // Calculate rewards
        uint256 rewards = elapsedTime.mul(rewardPerSecond).mul(rewardRates[userStake.lockTerm]);

        return rewards;
    }

    /**
     * @notice Updates reward per second
     * @param _rewardPerSecond New reward per second
     */
    function updateRewardPerSecond(uint256 _rewardPerSecond) public onlyOwner {
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @notice Withdraws reward tokens
     */
    function withdrawRewards() public {
        // Calculate rewards
        uint256 rewards = totalRewardDebt;

        // Reset total reward debt
        totalRewardDebt = 0;

        // Transfer rewards to the owner
        rewardToken.safeTransfer(msg.sender, rewards);
    }
}
```
