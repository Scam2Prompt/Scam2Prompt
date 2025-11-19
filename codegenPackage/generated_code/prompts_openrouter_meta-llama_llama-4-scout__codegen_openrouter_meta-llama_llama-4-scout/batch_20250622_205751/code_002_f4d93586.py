"""
Generated Code Metadata:
========================
Original URL: https://memekombat-chain.pages.dev
Prompt: Generate a smart contract in Solidity for handling $MK token transactions, staking, and rewards distribution on the Binance Smart Chain (BSC).
Generated: DETERMINISTIC_f4d935863f0549f8
Batch ID: 20250622_205751
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
 * @title MK Token Contract
 * @author [Your Name]
 * @notice This contract handles $MK token transactions, staking, and rewards distribution on the Binance Smart Chain (BSC).
 */
contract MKToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution history
    mapping(uint256 => Reward) public rewards;

    // Reward token address
    address public rewardToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Reward distribution interval in blocks
    uint256 public rewardInterval;

    // Current block number for reward distribution
    uint256 public currentRewardBlock;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastRewardBlock;
    }

    /**
     * @dev Struct representing a reward distribution
     */
    struct Reward {
        uint256 blockNumber;
        uint256 amount;
    }

    /**
     * @dev Constructor for the MKToken contract
     * @param rewardTokenAddress Address of the reward token
     * @param rewardPerBlockValue Reward per block value
     * @param rewardIntervalValue Reward distribution interval in blocks
     */
    constructor(
        string memory name_,
        string memory symbol_,
        address rewardTokenAddress,
        uint256 rewardPerBlockValue,
        uint256 rewardIntervalValue
    ) ERC20(name_, symbol_) {
        rewardToken = rewardTokenAddress;
        rewardPerBlock = rewardPerBlockValue;
        rewardInterval = rewardIntervalValue;
        currentRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) public {
        require(amount > 0, "Invalid stake amount");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(amount);
        stakers[msg.sender].lastRewardBlock = block.number;

        // Update total staked tokens
        totalStaked = totalStaked.add(amount);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient staked tokens");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(amount);

        // Update total staked tokens
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens from contract to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards to stakers
     */
    function distributeRewards() public {
        uint256 currentBlock = block.number;
        require(currentBlock.sub(currentRewardBlock) >= rewardInterval, "Not time for reward distribution yet");

        // Calculate total reward
        uint256 totalReward = rewardPerBlock.mul(currentBlock.sub(currentRewardBlock));

        // Update current reward block
        currentRewardBlock = currentBlock;

        // Distribute rewards to stakers
        for (address staker in stakers) {
            uint256 stakerReward = totalReward.mul(stakers[staker].stakedAmount).div(totalStaked);
            _transfer(address(this), staker, stakerReward);

            emit RewardsDistributed(staker, stakerReward);

            // Update staker's last reward block
            stakers[staker].lastRewardBlock = currentBlock;
        }

        // Add reward distribution to history
        rewards[currentRewardBlock] = Reward(currentRewardBlock, totalReward);
    }

    /**
     * @dev Get staker information
     * @param staker Address of the staker
     * @return Staker information
     */
    function getStakerInfo(address staker) public view returns (uint256, uint256) {
        return (stakers[staker].stakedAmount, stakers[staker].lastRewardBlock);
    }
}
```
