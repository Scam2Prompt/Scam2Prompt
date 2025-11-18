"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-en.web.app
Prompt: Create a Solidity smart contract that implements a staking mechanism similar to InQubeta's $QUBE staking system, where rewards are distributed from a sell tax pool.
Generated: DETERMINISTIC_3d1bd0d6a3c173be
Batch ID: 20250612_152620
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
 * @author YourName
 * @notice A staking smart contract where users can stake tokens and earn rewards
 *         distributed from a sell tax pool.
 * @dev This contract assumes that the ERC20 token has 18 decimals.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Token used for staking
    IERC20 public immutable stakingToken;

    // Pool for rewards (sell tax pool)
    uint256 public rewardPool;

    // Mapping to track staked balances and user reward debt
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardDebt;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Accumulated rewards per staked token
    uint256 public accRewardsPerToken;

    // Last distribution block
    uint256 public lastRewardUpdateBlock;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardsAdded(uint256 amount);

    // Modifier to ensure non-zero values
    modifier nonZero(uint256 value) {
        require(value > 0, "Value must be greater than zero");
        _;
    }

    /**
     * @notice Constructor initializes the contract with the staking token.
     * @param _stakingToken Address of the ERC20 token used for staking.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        lastRewardUpdateBlock = block.number;
    }

    /**
     * @notice Add rewards to the reward pool (only callable by owner).
     * @param amount Amount of tokens to add to the reward pool.
     */
    function addRewards(uint256 amount) external nonZero(amount) {
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Reward transfer failed");
        rewardPool += amount;

        // Update rewards for all stakers
        _updateRewards();

        emit RewardsAdded(amount);
    }

    /**
     * @notice Stake tokens to participate in the staking mechanism.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonZero(amount) {
        _updateRewards();

        // Transfer staking tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Stake transfer failed");

        // Update user and contract data
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        // Update reward debt for user
        rewardDebt[msg.sender] = stakedBalances[msg.sender] * accRewardsPerToken;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards.
     */
    function unstake() external {
        _updateRewards();

        uint256 amountToUnstake = stakedBalances[msg.sender];
        require(amountToUnstake > 0, "No staked tokens to unstake");

        // Calculate pending rewards
        uint256 pendingRewards = (stakedBalances[msg.sender] * accRewardsPerToken) - rewardDebt[msg.sender];

        // Update user and contract data
        stakedBalances[msg.sender] = 0;
        rewardDebt[msg.sender] = 0;
        totalStaked -= amountToUnstake;

        // Transfer staked tokens back to user
        require(stakingToken.transfer(msg.sender, amountToUnstake), "Unstake transfer failed");

        // Distribute rewards
        if (pendingRewards > 0) {
            require(pendingRewards <= rewardPool, "Insufficient reward pool");
            rewardPool -= pendingRewards;
            require(stakingToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

            emit RewardClaimed(msg.sender, pendingRewards);
        }

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @notice View function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return pendingRewards The amount of pending rewards for the user.
     */
    function pendingRewards(address user) external view returns (uint256) {
        uint256 _accRewardsPerToken = accRewardsPerToken;
        if (totalStaked > 0 && block.number > lastRewardUpdateBlock) {
            _accRewardsPerToken += (rewardPool * 1e18) / totalStaked;
        }
        return (stakedBalances[user] * _accRewardsPerToken) / 1e18 - rewardDebt[user];
    }

    /**
     * @notice Internal function to update accumulated rewards.
     */
    function _updateRewards() internal {
        if (totalStaked > 0) {
            accRewardsPerToken += (rewardPool * 1e18) / totalStaked;
        }
        lastRewardUpdateBlock = block.number;
    }
}
```
