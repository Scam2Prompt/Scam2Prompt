"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Write a smart contract in Solidity for a staking pool that operates on the Linea network, supports compounding rewards, and adjusts investor tiers based on staking duration, similar to the pools described on SidusPad.
Generated: DETERMINISTIC_4d26f8820ab267d3
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title StakingPool
 * @author [Your Name]
 * @notice A staking pool smart contract that operates on the Linea network.
 *         Supports compounding rewards and adjusts investor tiers based on staking duration.
 */
contract StakingPool is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of investor addresses to their staking information
    mapping(address => Investor) public investors;

    // Mapping of tier thresholds based on staking duration
    mapping(uint256 => Tier) public tiers;

    // ERC20 token used for staking and rewards
    IERC20 public stakingToken;

    // Reward token used for compounding rewards
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;

    // Total reward amount
    uint256 public totalRewards;

    // Staking duration tier thresholds (in days)
    uint256[] public tierThresholds;

    // Reward rate per tier (in percentage)
    uint256[] public rewardRates;

    // Compounding interval (in seconds)
    uint256 public compoundingInterval;

    // Timestamp of last compounding
    uint256 public lastCompounding;

    /**
     * @dev Event emitted when an investor stakes tokens
     * @param investor Address of the investor
     * @param amount Staked amount
     */
    event Staked(address indexed investor, uint256 amount);

    /**
     * @dev Event emitted when an investor unstakes tokens
     * @param investor Address of the investor
     * @param amount Unstaked amount
     */
    event Unstaked(address indexed investor, uint256 amount);

    /**
     * @dev Event emitted when rewards are compounded
     * @param investor Address of the investor
     * @param amount Compounded reward amount
     */
    event Compounded(address indexed investor, uint256 amount);

    /**
     * @dev Struct representing an investor's staking information
     */
    struct Investor {
        uint256 stakedAmount;
        uint256 stakedAt;
        uint256 lastClaimed;
        uint256 rewardsEarned;
    }

    /**
     * @dev Struct representing a tier
     */
    struct Tier {
        uint256 threshold;
        uint256 rewardRate;
    }

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _tierThresholds Staking duration tier thresholds (in days)
     * @param _rewardRates Reward rates per tier (in percentage)
     * @param _compoundingInterval Compounding interval (in seconds)
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256[] memory _tierThresholds,
        uint256[] memory _rewardRates,
        uint256 _compoundingInterval
    ) {
        require(_tierThresholds.length == _rewardRates.length, "Tier thresholds and reward rates must have the same length");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        tierThresholds = _tierThresholds;
        rewardRates = _rewardRates;
        compoundingInterval = _compoundingInterval;
        lastCompounding = block.timestamp;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) public whenNotPaused {
        require(amount > 0, "Stake amount must be greater than 0");

        Investor storage investor = investors[msg.sender];
        investor.stakedAmount = investor.stakedAmount.add(amount);
        investor.stakedAt = investor.stakedAt == 0 ? block.timestamp : investor.stakedAt;

        totalStaked = totalStaked.add(amount);

        stakingToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) public whenNotPaused {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(investors[msg.sender].stakedAmount >= amount, "Unstake amount exceeds staked amount");

        Investor storage investor = investors[msg.sender];
        investor.stakedAmount = investor.stakedAmount.sub(amount);

        totalStaked = totalStaked.sub(amount);

        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public whenNotPaused {
        Investor storage investor = investors[msg.sender];

        uint256 stakingDuration = block.timestamp.sub(investor.stakedAt);
        uint256 tierIndex = getTierIndex(stakingDuration);
        uint256 rewardRate = rewardRates[tierIndex];
        uint256 rewardsEarned = investor.stakedAmount.mul(rewardRate).div(100);

        investor.rewardsEarned = investor.rewardsEarned.add(rewardsEarned);
        investor.lastClaimed = block.timestamp;

        rewardToken.transfer(msg.sender, rewardsEarned);

        emit Compounded(msg.sender, rewardsEarned);
    }

    /**
     * @dev Get tier index based on staking duration
     * @param stakingDuration Staking duration (in seconds)
     * @return Tier index
     */
    function getTierIndex(uint256 stakingDuration) public view returns (uint256) {
        for (uint256 i = 0; i < tierThresholds.length; i++) {
            if (stakingDuration >= tierThresholds[i] * 1 days) {
                return i;
            }
        }
        return tierThresholds.length - 1;
    }

    /**
     * @dev Compound rewards
     */
    function compoundRewards() public whenNotPaused {
        require(block.timestamp.sub(lastCompounding) >= compoundingInterval, "Compounding interval has not passed");

        for (address investor in investors) {
            Investor storage investor = investors[investor];
            uint256 stakingDuration = block.timestamp.sub(investor.stakedAt);
            uint256 tierIndex = getTierIndex(stakingDuration);
            uint256 rewardRate = rewardRates[tierIndex];
            uint256 rewardsEarned = investor.stakedAmount.mul(rewardRate).div(100);

            investor.stakedAmount = investor.stakedAmount.add(rewardsEarned);
            totalStaked = totalStaked.add(rewardsEarned);

            emit Compounded(investor, rewardsEarned);
        }

        lastCompounding = block.timestamp;
    }

    /**
     * @dev Pause the contract
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}
```
