"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-def.pages.dev
Prompt: Design a staking system for $SCOTTY tokens, including a smart contract implementation that handles reward distribution and token locking.
Generated: DETERMINISTIC_7179cebc4325ca8b
Batch ID: 20250622_210348
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title Staking Contract for $SCOTTY tokens
 * @author [Your Name]
 * @notice This contract handles staking, reward distribution, and token locking for $SCOTTY tokens.
 */
contract StakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping (address => Staker) public stakers;

    // Mapping of reward distribution history
    mapping (uint256 => RewardDistribution) public rewardDistributions;

    // $SCOTTY token contract
    IERC20 public scottyToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Block number when reward distribution starts
    uint256 public rewardDistributionStart;

    // Block number when reward distribution ends
    uint256 public rewardDistributionEnd;

    // Reward distribution count
    uint256 public rewardDistributionCount;

    // Staker structure
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakeBlock;
    }

    // Reward distribution structure
    struct RewardDistribution {
        uint256 blockNumber;
        uint256 rewardAmount;
    }

    /**
     * @notice Constructor
     * @param _scottyToken $SCOTTY token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Reward per block
     * @param _rewardDistributionStart Block number when reward distribution starts
     * @param _rewardDistributionEnd Block number when reward distribution ends
     */
    constructor(
        address _scottyToken,
        address _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _rewardDistributionStart,
        uint256 _rewardDistributionEnd
    ) public {
        scottyToken = IERC20(_scottyToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        rewardDistributionStart = _rewardDistributionStart;
        rewardDistributionEnd = _rewardDistributionEnd;
    }

    /**
     * @notice Stake $SCOTTY tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Staking: Invalid amount");
        require(scottyToken.transferFrom(msg.sender, address(this), _amount), "Staking: Token transfer failed");

        Staker storage staker = stakers[msg.sender];
        if (staker.stakedAmount == 0) {
            staker.lastStakeBlock = block.number;
        } else {
            staker.rewardDebt = staker.rewardDebt.add(calculateReward(staker.stakedAmount, staker.lastStakeBlock, block.number));
        }

        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.lastStakeBlock = block.number;
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake $SCOTTY tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Unstaking: Invalid amount");
        require(stakers[msg.sender].stakedAmount >= _amount, "Unstaking: Insufficient staked amount");

        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt = staker.rewardDebt.add(calculateReward(staker.stakedAmount, staker.lastStakeBlock, block.number));
        staker.stakedAmount = staker.stakedAmount.sub(_amount);
        staker.lastStakeBlock = block.number;
        totalStaked = totalStaked.sub(_amount);

        require(scottyToken.transfer(msg.sender, _amount), "Unstaking: Token transfer failed");
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(staker.stakedAmount, staker.lastStakeBlock, block.number);
        staker.rewardDebt = staker.rewardDebt.add(reward);
        staker.lastStakeBlock = block.number;

        require(reward > 0, "Claim Rewards: No rewards to claim");
        require(rewardToken.transfer(msg.sender, reward), "Claim Rewards: Token transfer failed");
    }

    /**
     * @notice Calculate reward
     * @param _stakedAmount Staked amount
     * @param _lastStakeBlock Last stake block
     * @param _currentBlock Current block
     * @return Reward amount
     */
    function calculateReward(uint256 _stakedAmount, uint256 _lastStakeBlock, uint256 _currentBlock) internal view returns (uint256) {
        uint256 blocks = _currentBlock.sub(_lastStakeBlock);
        if (blocks > 0 && rewardDistributionStart <= _currentBlock && _currentBlock <= rewardDistributionEnd) {
            return _stakedAmount.mul(rewardPerBlock).mul(blocks);
        }
        return 0;
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Update reward distribution period
     * @param _newStart Block number when reward distribution starts
     * @param _newEnd Block number when reward distribution ends
     */
    function updateRewardDistributionPeriod(uint256 _newStart, uint256 _newEnd) public onlyOwner {
        rewardDistributionStart = _newStart;
        rewardDistributionEnd = _newEnd;
    }

    /**
     * @notice Distribute rewards
     */
    function distributeRewards() public onlyOwner {
        require(rewardDistributionCount < rewardDistributionEnd.sub(rewardDistributionStart), "Distribute Rewards: Reward distribution already ended");
        rewardDistributionCount++;
        uint256 rewardAmount = rewardToken.balanceOf(address(this));
        rewardDistributions[rewardDistributionCount] = RewardDistribution(block.number, rewardAmount);
        // Add logic to distribute rewards to stakers
    }

    /**
     * @notice Get staker information
     * @param _staker Staker address
     * @return Staker information
     */
    function getStakerInfo(address _staker) public view returns (uint256, uint256, uint256) {
        Staker storage staker = stakers[_staker];
        return (staker.stakedAmount, staker.rewardDebt, staker.lastStakeBlock);
    }
}
```
