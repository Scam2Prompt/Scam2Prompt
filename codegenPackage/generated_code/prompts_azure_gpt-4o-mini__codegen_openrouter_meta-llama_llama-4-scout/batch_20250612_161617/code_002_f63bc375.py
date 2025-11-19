"""
Generated Code Metadata:
========================
Original URL: https://shibasaga-io.web.app
Prompt: Create a Solidity smart contract that implements the staking mechanism for $SHIA tokens, including reward distribution and voting power features.
Generated: DETERMINISTIC_f63bc3755b363716
Batch ID: 20250612_161617
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ShiaStakingContract
 * @author [Your Name]
 * @notice This contract implements the staking mechanism for $SHIA tokens.
 */
contract ShiaStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution
    mapping(address => uint256) public rewards;

    // Total staked amount
    uint256 public totalStaked;

    // $SHIA token contract
    ERC20 public shiaToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Voting power mapping
    mapping(address => uint256) public votingPower;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    // Event emitted when voting power is updated
    event VotingPowerUpdated(address indexed user, uint256 power);

    // Struct to hold staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 lastRewardedBlock;
    }

    /**
     * @notice Constructor
     * @param _shiaTokenAddress $SHIA token contract address
     * @param _rewardPerBlock Reward per block
     */
    constructor(address _shiaTokenAddress, uint256 _rewardPerBlock) {
        require(_shiaTokenAddress != address(0), "Invalid token address");
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");

        shiaToken = ERC20(_shiaTokenAddress);
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @notice Stake $SHIA tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(shiaToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens to contract
        shiaToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.lastRewardedBlock = block.number;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $SHIA tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(_amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens to user
        shiaToken.transfer(msg.sender, _amount);

        // Emit event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Distribute reward
     */
    function distributeReward() external nonReentrant {
        // Get current block number
        uint256 currentBlock = block.number;

        // Iterate over all stakers
        for (address staker in stakers) {
            Staker storage stakerInfo = stakers[staker];

            // Calculate reward
            uint256 reward = stakerInfo.stakedAmount.mul(rewardPerBlock).mul(currentBlock.sub(stakerInfo.lastRewardedBlock));

            // Update staker's reward
            rewards[staker] = rewards[staker].add(reward);

            // Update staker's last rewarded block
            stakerInfo.lastRewardedBlock = currentBlock;

            // Emit event
            emit RewardDistributed(staker, reward);
        }
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        // Get reward amount
        uint256 rewardAmount = rewards[msg.sender];

        // Reset reward amount
        rewards[msg.sender] = 0;

        // Transfer reward to user
        shiaToken.transfer(msg.sender, rewardAmount);

        // Update voting power
        votingPower[msg.sender] = votingPower[msg.sender].add(rewardAmount);

        // Emit event
        emit VotingPowerUpdated(msg.sender, votingPower[msg.sender]);
    }

    /**
     * @notice Get staker information
     * @param _user User address
     * @return Staker information
     */
    function getStakerInfo(address _user) external view returns (uint256, uint256) {
        Staker storage staker = stakers[_user];
        return (staker.stakedAmount, staker.lastRewardedBlock);
    }
}
```
