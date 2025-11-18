"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.jp
Prompt: Write a Solidity smart contract to manage staking and unstaking of CAKE-BNB LP tokens on PancakeSwap, with functionality for tracking rewards and compounding intervals.
Generated: DETERMINISTIC_54a6549dfbb645d3
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingRewards
 * @dev A smart contract for staking CAKE-BNB LP tokens, tracking rewards, and enabling compounding intervals.
 */
contract StakingRewards {
    // Address of the ERC20 CAKE-BNB LP token
    IERC20 public stakingToken;

    // Address of the reward token
    IERC20 public rewardToken;

    // Mapping from user address to staking information
    mapping(address => StakerInfo) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second
    uint256 public rewardRate;

    // Compound interval in seconds
    uint256 public compoundInterval;

    // Last updated timestamp
    uint256 public lastUpdateTime;

    // Unclaimed rewards for all stakers
    uint256 public rewardsUnclaimed;

    // Staker information struct
    struct StakerInfo {
        uint256 stakedAmount; // Amount staked by the user
        uint256 rewardDebt;   // Rewards owed to the user
        uint256 lastCompound; // Last compound timestamp
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Compounded(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the CAKE-BNB LP token.
     * @param _rewardToken Address of the reward token.
     * @param _rewardRate Reward rate per second.
     * @param _compoundInterval Compounding interval in seconds.
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardRate,
        uint256 _compoundInterval
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        compoundInterval = _compoundInterval;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Modifier to update rewards for all stakers.
     */
    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 timeDiff = block.timestamp - lastUpdateTime;
            uint256 newRewards = timeDiff * rewardRate;
            rewardsUnclaimed += newRewards;
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @dev Stake CAKE-BNB LP tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer staking tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staker info
        StakerInfo storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.rewardDebt += (amount * rewardsUnclaimed) / totalStaked;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake CAKE-BNB LP tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external updateRewards {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        // Update staker info
        staker.stakedAmount -= amount;

        // Calculate rewards for the user and reset reward debt
        uint256 pendingRewards = (staker.stakedAmount * rewardsUnclaimed) / totalStaked - staker.rewardDebt;
        staker.rewardDebt = (staker.stakedAmount * rewardsUnclaimed) / totalStaked;

        // Transfer the staking tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Update total staked amount
        totalStaked -= amount;

        // Transfer rewards to the user
        if (pendingRewards > 0) {
            rewardToken.transfer(msg.sender, pendingRewards);
            emit RewardsClaimed(msg.sender, pendingRewards);
        }

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Compound rewards back into staking.
     */
    function compound() external updateRewards {
        StakerInfo storage staker = stakers[msg.sender];
        require(block.timestamp - staker.lastCompound >= compoundInterval, "Compound interval not reached");

        // Calculate pending rewards
        uint256 pendingRewards = (staker.stakedAmount * rewardsUnclaimed) / totalStaked - staker.rewardDebt;

        // Compound rewards back into staking
        require(pendingRewards > 0, "No rewards to compound");
        staker.stakedAmount += pendingRewards;
        staker.rewardDebt = (staker.stakedAmount * rewardsUnclaimed) / totalStaked;

        // Update total staked amount
        totalStaked += pendingRewards;

        // Reset last compound timestamp
        staker.lastCompound = block.timestamp;

        emit Compounded(msg.sender, pendingRewards);
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards amount.
     */
    function pendingRewards(address user) external view returns (uint256) {
        StakerInfo storage staker = stakers[user];
        return (staker.stakedAmount * rewardsUnclaimed) / totalStaked - staker.rewardDebt;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
