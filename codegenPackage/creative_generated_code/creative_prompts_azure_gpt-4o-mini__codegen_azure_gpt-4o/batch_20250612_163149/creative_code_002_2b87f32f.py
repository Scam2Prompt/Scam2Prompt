"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-tokens.com
Prompt: Generate code for a smart contract that allows users to stake tokens and earn $PEPE rewards through a passive income system.
Generated: DETERMINISTIC_2b87f32f8b70fcf3
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready smart contract written in Solidity for staking tokens and earning $PEPE rewards. This code assumes the use of the ERC20 standard for tokens.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenStaking
 * @dev A smart contract that allows users to stake ERC20 tokens and earn rewards in $PEPE tokens.
 */
contract TokenStaking {
    // ERC20 interface for interacting with staking token and rewards token
    IERC20 public stakingToken;
    IERC20 public rewardsToken;

    // Mapping to track staked balances and reward debts
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardDebt;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (determined by the supply of $PEPE rewards)
    uint256 public rewardRate;

    // Last timestamp when the rewards were updated
    uint256 public lastRewardTimestamp;

    // Accumulated rewards per token, scaled to avoid precision issues
    uint256 public accRewardsPerToken;

    // Events for transparency
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to ensure calls are only from valid addresses
    modifier onlyNonZeroAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _rewardsToken Address of the ERC20 token for rewards ($PEPE).
     * @param _rewardRate Reward rate per second in $PEPE.
     */
    constructor(
        address _stakingToken,
        address _rewardsToken,
        uint256 _rewardRate
    ) onlyNonZeroAddress(_stakingToken) onlyNonZeroAddress(_rewardsToken) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
        rewardRate = _rewardRate;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Updates the accumulated rewards per token.
     */
    function updateRewards() internal {
        if (totalStaked == 0) {
            lastRewardTimestamp = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
        uint256 totalRewards = timeElapsed * rewardRate;
        accRewardsPerToken += (totalRewards * 1e18) / totalStaked;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Rewards owed to the user.
     */
    function pendingRewards(address user) public view returns (uint256) {
        uint256 userRewards = ((stakedBalances[user] * accRewardsPerToken) / 1e18) - rewardDebt[user];
        return userRewards;
    }

    /**
     * @dev Function for users to stake tokens.
     * @param amount The number of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        updateRewards();

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staked balance and reward debt
        stakedBalances[msg.sender] += amount;
        rewardDebt[msg.sender] = (stakedBalances[msg.sender] * accRewardsPerToken) / 1e18;

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function for users to unstake their tokens.
     * @param amount The number of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        updateRewards();

        // Claim any pending rewards before unstaking
        uint256 rewards = pendingRewards(msg.sender);
        if (rewards > 0) {
            rewardsToken.transfer(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        // Update staked balance and reward debt
        stakedBalances[msg.sender] -= amount;
        rewardDebt[msg.sender] = (stakedBalances[msg.sender] * accRewardsPerToken) / 1e18;

        // Transfer unstaked tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Update total staked
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards without unstaking.
     */
    function claimRewards() external {
        updateRewards();

        // Calculate pending rewards
        uint256 rewards = pendingRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update reward debt
        rewardDebt[msg.sender] = (stakedBalances[msg.sender] * accRewardsPerToken) / 1e18;

        // Transfer rewards to the user
        rewardsToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }
}

/**
 * @dev Simplified ERC20 interface to interact with tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```

This code is designed to be functional and secure, following best practices for Solidity development. Make sure to thoroughly test the contract and deploy it on a test network before using it in production.
