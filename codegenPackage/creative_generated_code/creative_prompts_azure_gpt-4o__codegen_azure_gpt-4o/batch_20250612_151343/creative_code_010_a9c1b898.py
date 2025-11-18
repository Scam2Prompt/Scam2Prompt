"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hummingbirdonbnb.pages.dev
Prompt: Write a Solidity smart contract for a staking pool that mimics the partnership staking pools described on the webpage, allowing users to stake tokens and earn rewards.
Generated: DETERMINISTIC_a9c1b89859344c60
Batch ID: 20250612_151343
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
 * @title StakingPool
 * @dev A staking pool contract that allows users to stake ERC20 tokens and earn rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingPool is ReentrancyGuard {
    // Address of the ERC20 token used for staking
    IERC20 public stakingToken;

    // Address of the ERC20 token used for rewards
    IERC20 public rewardToken;

    // Total staked tokens in the pool
    uint256 public totalStaked;

    // Reward rate per second (amount of reward tokens generated per second per staked token)
    uint256 public rewardRate;

    // Last time rewards were calculated
    uint256 public lastRewardTimestamp;

    // Reward per token stored
    uint256 public rewardPerTokenStored;

    // Mapping to track staked amounts per user
    mapping(address => uint256) public balances;

    // Mapping to track rewards per user
    mapping(address => uint256) public userRewardPerTokenPaid;

    // Mapping to track accumulated rewards per user
    mapping(address => uint256) public rewards;

    /**
     * @dev Emitted when a user stakes tokens.
     * @param user Address of the user staking tokens.
     * @param amount Amount of tokens staked.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Emitted when a user withdraws staked tokens.
     * @param user Address of the user withdrawing tokens.
     * @param amount Amount of tokens withdrawn.
     */
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Emitted when a user claims rewards.
     * @param user Address of the user claiming rewards.
     * @param amount Amount of rewards claimed.
     */
    event RewardPaid(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking pool with the given tokens and reward rate.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Updates the reward variables to reflect the current rewards.
     */
    function updateReward(address account) internal {
        rewardPerTokenStored = rewardPerToken();
        lastRewardTimestamp = block.timestamp;

        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
    }

    /**
     * @dev Calculates the reward per token based on the elapsed time and reward rate.
     * @return Reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastRewardTimestamp) * rewardRate * 1e18) / totalStaked;
    }

    /**
     * @dev Calculates the earned rewards for a given user.
     * @param account Address of the user.
     * @return Earned rewards.
     */
    function earned(address account) public view returns (uint256) {
        return
            (balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) /
            1e18 +
            rewards[account];
    }

    /**
     * @dev Allows users to stake tokens into the pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");

        updateReward(msg.sender);

        stakingToken.transferFrom(msg.sender, address(this), amount);
        balances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens from the pool.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(balances[msg.sender] >= amount, "Insufficient staked balance");

        updateReward(msg.sender);

        balances[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimReward() external nonReentrant {
        updateReward(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _rewardRate New reward rate per second.
     */
    function setRewardRate(uint256 _rewardRate) external {
        // Add ownership checks here if necessary (e.g., onlyOwner modifier)
        updateReward(address(0));
        rewardRate = _rewardRate;
    }
}
```
