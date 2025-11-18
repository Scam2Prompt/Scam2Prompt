"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Write a smart contract in Solidity that mimics the BTC20 staking mechanism, including token distribution every 10 minutes and dynamic APY adjustments based on the percentage of the staking pool.
Generated: DETERMINISTIC_2179554fc65eda4b
Batch ID: 20250612_151333
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
 * @title BTC20Staking
 * @dev A smart contract to mimic BTC20 staking mechanism with token distribution 
 * every 10 minutes and dynamic APY adjustments based on the percentage of the staking pool.
 */
contract BTC20Staking {
    // Token contract address
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Staking data
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }
    mapping(address => Stake) public stakes;

    // Pool data
    uint256 public totalStaked;
    uint256 public lastRewardTime;
    uint256 public rewardRate; // Reward rate per token per second
    uint256 public rewardPerTokenStored;

    // Constants
    uint256 public constant REWARD_INTERVAL = 10 minutes; // Reward distribution interval
    uint256 public constant BASE_APY = 5; // Base APY in percentage
    uint256 public constant MAX_APY = 20; // Maximum APY in percentage

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Modifier to update reward distribution before certain actions.
     */
    modifier updateReward(address account) {
        _updateRewardDistribution();
        if (account != address(0)) {
            stakes[account].rewardDebt = _earned(account);
        }
        _;
    }

    /**
     * @dev Stake tokens to participate in the reward pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staking data
        totalStaked += amount;
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakeTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and withdraw from the reward pool.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked tokens");

        // Update staking data
        totalStaked -= amount;
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards earned from staking.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer reward tokens
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate earned rewards for a user.
     * @param account User address.
     * @return Earned reward amount.
     */
    function _earned(address account) internal view returns (uint256) {
        Stake memory stakeData = stakes[account];
        uint256 earnedReward = (stakeData.amount * rewardPerTokenStored) / 1e18;
        return earnedReward - stakeData.rewardDebt;
    }

    /**
     * @dev Update reward distribution based on elapsed time and staking pool status.
     */
    function _updateRewardDistribution() internal {
        if (block.timestamp >= lastRewardTime + REWARD_INTERVAL) {
            uint256 elapsedTime = block.timestamp - lastRewardTime;

            // Adjust APY dynamically based on the staking pool percentage
            uint256 poolPercentage = (totalStaked * 100) / stakingToken.totalSupply();
            uint256 dynamicAPY = BASE_APY + ((poolPercentage * (MAX_APY - BASE_APY)) / 100);

            // Calculate reward rate
            rewardRate = (dynamicAPY * 1e18) / (365 days); // APY converted to rate per second

            // Update reward per token
            rewardPerTokenStored += (rewardRate * elapsedTime) / totalStaked;

            lastRewardTime = block.timestamp;
        }
    }
}

/**
 * @dev ERC20 interface for interacting with token contracts.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function totalSupply() external view returns (uint256);
}
```
