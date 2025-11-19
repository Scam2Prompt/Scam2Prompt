"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Generate a smart contract code snippet in Solidity for a custom staking pool on Story Staking, incorporating dynamic interest rates and automated reward distribution.
Generated: DETERMINISTIC_17cea369ad8f97c4
Batch ID: 20250622_212605
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StoryStakingPool
 * @author [Your Name]
 * @notice A custom staking pool contract with dynamic interest rates and automated reward distribution.
 */
contract StoryStakingPool is Ownable {
    using SafeMath for uint256;

    // Struct to represent a staker's information
    struct Staker {
        uint256 principal; // Initial stake amount
        uint256 rewardDebt; // Reward debt for the staker
    }

    // Mapping of staker addresses to their information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution history
    mapping(uint256 => uint256) public rewardHistory;

    // Token contract instance for staking
    IERC20 public stakingToken;

    // Token contract instance for reward distribution
    IERC20 public rewardToken;

    // Dynamic interest rate per block
    uint256 public interestRate;

    // Total staked amount
    uint256 public totalStaked;

    // Reward distribution interval in blocks
    uint256 public rewardInterval;

    // Last reward distribution block
    uint256 public lastRewardBlock;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for the StoryStakingPool contract.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _interestRate Initial interest rate per block.
     * @param _rewardInterval Reward distribution interval in blocks.
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _interestRate,
        uint256 _rewardInterval
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        interestRate = _interestRate;
        rewardInterval = _rewardInterval;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake tokens in the pool.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        if (staker.principal == 0) {
            staker.rewardDebt = 0;
        }
        staker.principal = staker.principal.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens from the pool.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        Staker storage staker = stakers[msg.sender];
        require(staker.principal >= _amount, "Insufficient staked amount");

        // Update staker information
        staker.principal = staker.principal.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens from contract to user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update interest rate.
     * @param _newInterestRate New interest rate per block.
     */
    function updateInterestRate(uint256 _newInterestRate) external onlyOwner {
        interestRate = _newInterestRate;
    }

    /**
     * @notice Distribute rewards to stakers.
     */
    function distributeRewards() public {
        uint256 currentBlock = block.number;
        require(currentBlock.sub(lastRewardBlock) >= rewardInterval, "Insufficient blocks passed");

        // Calculate total rewards
        uint256 totalRewards = calculateRewards();

        // Update reward history
        rewardHistory[currentBlock] = totalRewards;

        // Distribute rewards to stakers
        for (address stakerAddress in stakers) {
            Staker storage staker = stakers[stakerAddress];
            uint256 stakerRewards = calculateStakerRewards(staker, totalRewards);
            staker.rewardDebt = staker.rewardDebt.add(stakerRewards);

            // Transfer rewards to staker
            rewardToken.transfer(stakerAddress, stakerRewards);

            emit RewardsDistributed(stakerAddress, stakerRewards);
        }

        lastRewardBlock = currentBlock;
    }

    /**
     * @notice Calculate total rewards for the current interval.
     * @return Total rewards.
     */
    function calculateRewards() internal view returns (uint256) {
        // Implement your reward calculation logic here
        // For demonstration purposes, assume 10% of total staked amount as rewards
        return totalStaked.mul(10).div(100);
    }

    /**
     * @notice Calculate rewards for a staker.
     * @param _staker Staker information.
     * @param _totalRewards Total rewards for the interval.
     * @return Staker's rewards.
     */
    function calculateStakerRewards(Staker storage _staker, uint256 _totalRewards) internal view returns (uint256) {
        // Implement your staker reward calculation logic here
        // For demonstration purposes, assume proportional rewards based on staker's principal
        return _totalRewards.mul(_staker.principal).div(totalStaked);
    }
}
```
