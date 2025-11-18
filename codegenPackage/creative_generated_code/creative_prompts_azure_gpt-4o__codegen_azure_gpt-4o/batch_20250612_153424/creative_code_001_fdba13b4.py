"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbiterrfinance.github.io
Prompt: Generate Solidity code for creating a staking pool similar to the ones described in Orbiter Finance, where users can deposit tokens and earn rewards.
Generated: DETERMINISTIC_fdba13b4888918fd
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title StakingPool
 * @dev A staking pool for users to deposit ERC20 tokens and earn rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingPool is Ownable {
    // ERC20 token used for staking
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Reward rate per second
    uint256 public rewardRate;

    // Last time rewards were updated
    uint256 public lastUpdateTime;

    // Accumulated rewards per token
    uint256 public rewardPerTokenStored;

    // User balances and reward data
    mapping(address => uint256) public userBalances;
    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public userRewardPerTokenPaid;

    // Total staked tokens
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking pool.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards before executing the function.
     * @param account Address of the user.
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Function to calculate the current reward per token.
     * @return Reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked;
    }

    /**
     * @dev Function to calculate earned rewards for a user.
     * @param account Address of the user.
     * @return Earned rewards.
     */
    function earned(address account) public view returns (uint256) {
        return
            ((userBalances[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            userRewards[account];
    }

    /**
     * @dev Function for users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        userBalances[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function for users to withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");
        userBalances[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function for users to claim rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards available");
        userRewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Function to update the reward rate. Only callable by the owner.
     * @param _rewardRate New reward rate per second.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
