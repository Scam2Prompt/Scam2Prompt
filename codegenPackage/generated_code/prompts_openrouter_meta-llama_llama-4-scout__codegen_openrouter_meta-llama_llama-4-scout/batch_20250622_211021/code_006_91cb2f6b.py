"""
Generated Code Metadata:
========================
Original URL: https://connectautofixing.vercel.app
Prompt: Design a staking system for a cryptocurrency using a smart contract, including functions for staking, unstaking, and rewarding stakers with additional coins or tokens.
Generated: DETERMINISTIC_91cb2f6bb6e2fadf
Batch ID: 20250622_211021
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
 * @title Staking System Smart Contract
 * @author [Your Name]
 * @notice This contract provides a basic staking system for a cryptocurrency.
 */
contract StakingSystem is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping (address => Staker) public stakers;

    // Mapping of reward token addresses to their respective reward rates
    mapping (address => uint256) public rewardRates;

    // Mapping of reward token addresses to their respective reward tokens
    mapping (address => ERC20) public rewardTokens;

    // Event emitted when a user stakes tokens
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed staker, uint256 amount);

    // Event emitted when a reward is distributed to a staker
    event RewardDistributed(address indexed staker, uint256 amount);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakeAmount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    /**
     * @dev Initializes the staking system contract
     * @param _rewardTokenAddress Address of the reward token
     * @param _rewardRate Reward rate per block
     */
    constructor(address _rewardTokenAddress, uint256 _rewardRate) public {
        rewardTokens[_rewardTokenAddress] = ERC20(_rewardTokenAddress);
        rewardRates[_rewardTokenAddress] = _rewardRate;
    }

    /**
     * @dev Allows a user to stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        staker.stakeAmount = staker.stakeAmount.add(_amount);
        staker.lastStakeTime = block.timestamp;

        // Transfer tokens from user to contract
        ERC20(msg.sender).transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(stakers[msg.sender].stakeAmount >= _amount, "Insufficient stake amount");

        Staker storage staker = stakers[msg.sender];
        staker.stakeAmount = staker.stakeAmount.sub(_amount);

        // Transfer tokens from contract to user
        ERC20(address(this)).transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distributes rewards to stakers
     */
    function distributeRewards() external nonReentrant {
        for (address staker in stakers) {
            Staker storage stakerInfo = stakers[staker];
            uint256 reward = calculateReward(stakerInfo);
            if (reward > 0) {
                stakerInfo.rewardDebt = stakerInfo.rewardDebt.add(reward);
                rewardTokens[address(this)].transfer(staker, reward);
                emit RewardDistributed(staker, reward);
            }
        }
    }

    /**
     * @dev Calculates the reward for a staker
     * @param _staker Staker's information
     * @return Reward amount
     */
    function calculateReward(Staker storage _staker) internal view returns (uint256) {
        uint256 rewardRate = rewardRates[address(this)];
        uint256 timeElapsed = block.timestamp.sub(_staker.lastStakeTime);
        return _staker.stakeAmount.mul(rewardRate).mul(timeElapsed);
    }

    /**
     * @dev Updates the reward rate for a reward token
     * @param _rewardTokenAddress Address of the reward token
     * @param _newRewardRate New reward rate
     */
    function updateRewardRate(address _rewardTokenAddress, uint256 _newRewardRate) external {
        require(msg.sender == owner(), "Only the owner can update the reward rate");
        rewardRates[_rewardTokenAddress] = _newRewardRate;
    }

    /**
     * @dev Gets the staker information
     * @param _staker Address of the staker
     * @return Staker's information
     */
    function getStakerInfo(address _staker) external view returns (uint256, uint256, uint256) {
        Staker storage staker = stakers[_staker];
        return (staker.stakeAmount, staker.rewardDebt, staker.lastStakeTime);
    }
}
```
