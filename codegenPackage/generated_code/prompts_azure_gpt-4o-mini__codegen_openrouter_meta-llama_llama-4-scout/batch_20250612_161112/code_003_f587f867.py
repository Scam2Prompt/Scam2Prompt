"""
Generated Code Metadata:
========================
Original URL: https://greenbtcwebb.pages.dev
Prompt: Create a Solidity contract that enables users to stake their $GBTC tokens and earn rewards based on the gamified staking mechanics described on the Green Bitcoin site.
Generated: DETERMINISTIC_f587f86704a28dda
Batch ID: 20250612_161112
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
 * @title Green Bitcoin Staking Contract
 * @author [Your Name]
 * @notice This contract enables users to stake their $GBTC tokens and earn rewards based on gamified staking mechanics.
 */
contract GreenBitcoinStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // STRUCTS

    /**
     * @dev Staker struct to store user's staking information
     */
    struct Staker {
        uint256 stakedAmount; // Amount of $GBTC tokens staked
        uint256 rewardDebt; // Reward debt for the staker
        uint256 lastRewardTime; // Last reward time for the staker
    }

    // VARIABLES

    IERC20 public gbtcToken; // $GBTC token contract
    uint256 public totalStaked; // Total staked $GBTC tokens
    uint256 public totalRewards; // Total rewards distributed
    uint256 public rewardPerBlock; // Reward per block
    uint256 public lastRewardBlock; // Last reward block
    uint256 public stakingStartBlock; // Staking start block
    mapping(address => Staker) public stakers; // Mapping of staker addresses to their staking information

    // EVENTS

    /**
     * @dev Event emitted when a user stakes $GBTC tokens
     * @param user User's address
     * @param amount Amount of $GBTC tokens staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user unstakes $GBTC tokens
     * @param user User's address
     * @param amount Amount of $GBTC tokens unstaked
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when rewards are distributed
     * @param user User's address
     * @param amount Reward amount
     */
    event RewardDistributed(address indexed user, uint256 amount);

    // CONSTRUCTOR

    /**
     * @dev Constructor to initialize the contract
     * @param _gbtcToken $GBTC token contract address
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     */
    constructor(
        address _gbtcToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock
    ) {
        gbtcToken = IERC20(_gbtcToken);
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        lastRewardBlock = _stakingStartBlock;
    }

    // FUNCTIONS

    /**
     * @dev Function to stake $GBTC tokens
     * @param _amount Amount of $GBTC tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(
            gbtcToken.transferFrom(msg.sender, address(this), _amount),
            "Failed to transfer $GBTC tokens"
        );

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.lastRewardTime = block.timestamp;

        if (staker.stakedAmount == _amount) {
            staker.rewardDebt = 0;
        } else {
            staker.rewardDebt = staker.rewardDebt.add(_amount);
        }

        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake $GBTC tokens
     * @param _amount Amount of $GBTC tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(_amount <= stakers[msg.sender].stakedAmount, "Insufficient staked amount");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(_amount);
        staker.rewardDebt = staker.rewardDebt.sub(_amount);

        require(
            gbtcToken.transfer(msg.sender, _amount),
            "Failed to transfer $GBTC tokens"
        );

        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to distribute rewards
     */
    function distributeRewards() external nonReentrant {
        uint256 currentBlock = block.number;
        require(currentBlock >= stakingStartBlock, "Staking not started yet");

        uint256 rewards = calculateRewards();
        totalRewards = totalRewards.add(rewards);

        for (address stakerAddress in stakers) {
            Staker storage staker = stakers[stakerAddress];
            uint256 userReward = calculateUserReward(staker);
            staker.rewardDebt = staker.rewardDebt.add(userReward);

            require(
                gbtcToken.transfer(stakerAddress, userReward),
                "Failed to transfer reward"
            );

            emit RewardDistributed(stakerAddress, userReward);
        }

        lastRewardBlock = currentBlock;
    }

    /**
     * @dev Function to calculate rewards
     * @return Total rewards
     */
    function calculateRewards() internal view returns (uint256) {
        uint256 currentBlock = block.number;
        uint256 blocksElapsed = currentBlock.sub(lastRewardBlock);
        return blocksElapsed.mul(rewardPerBlock);
    }

    /**
     * @dev Function to calculate user rewards
     * @param _staker Staker struct
     * @return User reward
     */
    function calculateUserReward(Staker storage _staker) internal view returns (uint256) {
        uint256 stakedAmount = _staker.stakedAmount;
        uint256 rewardDebt = _staker.rewardDebt;
        uint256 rewards = calculateRewards();
        return stakedAmount.mul(rewards).div(totalStaked).sub(rewardDebt);
    }
}
```
