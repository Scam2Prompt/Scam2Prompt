"""
Generated Code Metadata:
========================
Original URL: https://decubate-platform.pages.dev
Prompt: Develop a smart contract to automate the staking and reward distribution process for a similar platform, inspired by Decubate's audited smart contracts.
Generated: DETERMINISTIC_0f7ecf418d7b428c
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, a popular language for smart contracts on the Ethereum blockchain.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A smart contract to automate the staking and reward distribution process.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Staker struct to store staker information
    struct Staker {
        uint256 stakeAmount;
        uint256 stakeTimestamp;
        uint256 rewardDebt;
    }

    // Mapping of staker addresses to their staker information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution history
    mapping(uint256 => uint256) public rewardHistory;

    // Reward token contract
    IERC20 public rewardToken;

    // Staked token contract
    IERC20 public stakedToken;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward distribution block
    uint256 public lastRewardBlock;

    // Reward distribution interval in blocks
    uint256 public rewardInterval;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _rewardToken Reward token contract address
     * @param _stakedToken Staked token contract address
     * @param _rewardPerBlock Reward per block
     * @param _rewardInterval Reward distribution interval in blocks
     */
    constructor(
        IERC20 _rewardToken,
        IERC20 _stakedToken,
        uint256 _rewardPerBlock,
        uint256 _rewardInterval
    ) public {
        rewardToken = _rewardToken;
        stakedToken = _stakedToken;
        rewardPerBlock = _rewardPerBlock;
        rewardInterval = _rewardInterval;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Staking amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];
        staker.stakeAmount = staker.stakeAmount.add(_amount);
        staker.stakeTimestamp = block.timestamp;

        totalStakedAmount = totalStakedAmount.add(_amount);

        stakedToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Unstaking amount must be greater than 0");
        require(stakers[msg.sender].stakeAmount >= _amount, "Insufficient staked amount");

        Staker storage staker = stakers[msg.sender];
        staker.stakeAmount = staker.stakeAmount.sub(_amount);

        totalStakedAmount = totalStakedAmount.sub(_amount);

        stakedToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Update reward distribution interval
     * @param _newRewardInterval New reward distribution interval in blocks
     */
    function updateRewardInterval(uint256 _newRewardInterval) public onlyOwner {
        rewardInterval = _newRewardInterval;
    }

    /**
     * @notice Distribute rewards
     */
    function distributeRewards() public {
        uint256 currentBlock = block.number;
        require(currentBlock.sub(lastRewardBlock) >= rewardInterval, "Not time to distribute rewards yet");

        uint256 rewards = calculateRewards();
        rewardHistory[currentBlock] = rewards;

        // Distribute rewards to stakers
        for (address staker in stakers) {
            Staker storage stakerInfo = stakers[staker];
            uint256 stakerRewards = stakerInfo.stakeAmount.mul(rewards).div(totalStakedAmount);
            staker.rewardDebt = staker.rewardDebt.add(stakerRewards);
            rewardToken.safeTransfer(staker, stakerRewards);

            emit RewardsDistributed(staker, stakerRewards);
        }

        lastRewardBlock = currentBlock;
    }

    /**
     * @notice Calculate rewards
     * @return Rewards to be distributed
     */
    function calculateRewards() internal view returns (uint256) {
        uint256 blocksElapsed = block.number.sub(lastRewardBlock);
        return blocksElapsed.mul(rewardPerBlock);
    }

    /**
     * @notice Get staker information
     * @param _staker Staker address
     * @return Staker information
     */
    function getStakerInfo(address _staker) public view returns (uint256, uint256, uint256) {
        Staker storage staker = stakers[_staker];
        return (staker.stakeAmount, staker.stakeTimestamp, staker.rewardDebt);
    }
}
```
