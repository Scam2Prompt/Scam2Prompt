"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdoge-live.pages.dev
Prompt: Create a smart contract in Solidity that implements a staking mechanism similar to DOGE20, with dynamic rewards calculated per block and distributed over a fixed period.
Generated: DETERMINISTIC_c89ca5b7b52cb300
Batch ID: 20250612_153400
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
 * @title StakingContract
 * @dev Implements a staking mechanism with dynamic block-based rewards distributed over a fixed period.
 */
contract StakingContract {
    // Struct to represent staking details for each user
    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 startBlock;      // Block at which staking started
        uint256 rewardDebt;      // Reward debt to track already paid rewards
    }

    // Events
    event StakeAdded(address indexed user, uint256 amount);
    event StakeWithdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // State variables
    mapping(address => Stake) public stakes;          // Mapping to store stakes by user address
    uint256 public totalStaked;                       // Total amount of tokens staked
    uint256 public rewardPerBlock;                    // Dynamic reward distributed per block
    uint256 public rewardPeriod;                      // Fixed reward distribution period in blocks
    uint256 public lastRewardBlock;                   // Last block at which rewards were calculated
    uint256 public accruedRewardsPerShare;            // Accrued rewards per share (scaled by 1e18)

    IERC20 public stakingToken;                       // Token used for staking
 
    // Constants
    uint256 private constant SCALE = 1e18;            // Scaling factor for precision

    /**
     * @dev Initializes the staking contract.
     * @param _stakingToken Address of the ERC20 token users can stake.
     * @param _rewardPerBlock Reward amount distributed per block.
     * @param _rewardPeriod Duration of reward distribution in blocks.
     */
    constructor(
        IERC20 _stakingToken,
        uint256 _rewardPerBlock,
        uint256 _rewardPeriod
    ) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
        rewardPeriod = _rewardPeriod;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Modifier to update rewards before performing operations.
     */
    modifier updateRewards() {
        _updateRewards();
        _;
    }

    /**
     * @dev Internal function to update accrued rewards for all stakers.
     */
    function _updateRewards() internal {
        if (totalStaked > 0) {
            // Calculate rewards from the last update until the current block
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            uint256 totalReward = blocksSinceLastReward * rewardPerBlock;

            // Update accrued rewards per share
            accruedRewardsPerShare += (totalReward * SCALE) / totalStaked;
        }
        lastRewardBlock = block.number;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount Number of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer staking tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking details for the user
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += (_amount * accruedRewardsPerShare) / SCALE;
        userStake.amount += _amount;

        // Update total staked tokens
        totalStaked += _amount;

        emit StakeAdded(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param _amount Number of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update staking details for the user
        userStake.rewardDebt -= (_amount * accruedRewardsPerShare) / SCALE;
        userStake.amount -= _amount;

        // Update total staked tokens
        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit StakeWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their accrued rewards.
     */
    function claimRewards() external updateRewards {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingRewards = ((userStake.amount * accruedRewardsPerShare) / SCALE) - userStake.rewardDebt;

        require(pendingRewards > 0, "No rewards to claim");

        // Update user's reward debt
        userStake.rewardDebt += pendingRewards;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, pendingRewards);

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards amount.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake memory userStake = stakes[_user];
        uint256 adjustedAccruedRewardsPerShare = accruedRewardsPerShare;

        if (block.number > lastRewardBlock && totalStaked > 0) {
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            uint256 totalReward = blocksSinceLastReward * rewardPerBlock;
            adjustedAccruedRewardsPerShare += (totalReward * SCALE) / totalStaked;
        }

        return ((userStake.amount * adjustedAccruedRewardsPerShare) / SCALE) - userStake.rewardDebt;
    }
}

/**
 * @dev Minimal ERC20 interface for interacting with staking tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
