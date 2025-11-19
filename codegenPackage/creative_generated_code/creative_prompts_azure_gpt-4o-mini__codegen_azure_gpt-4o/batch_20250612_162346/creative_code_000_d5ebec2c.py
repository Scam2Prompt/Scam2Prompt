"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claimyourdoge20.pages.dev
Prompt: How can I implement a staking smart contract for DOGE20 tokens on Ethereum to distribute rewards over two years?
Generated: DETERMINISTIC_d5ebec2c83bb1b2e
Batch ID: 20250612_162346
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
 * @dev A staking smart contract for DOGE20 tokens to distribute rewards over two years.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // The token being staked
    IERC20 public immutable stakingToken;

    // Reward distribution duration in seconds (2 years)
    uint256 public constant REWARD_DURATION = 2 * 365 * 24 * 60 * 60;

    // Reward rate per second
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Last time rewards were calculated
    uint256 public lastUpdateTime;

    // Accumulated rewards per token staked
    uint256 public rewardPerTokenStored;

    // Mapping from user address to staked amount
    mapping(address => uint256) public userStake;

    // Mapping from user address to rewards earned
    mapping(address => uint256) public userRewards;

    // Mapping from user address to last reward calculation
    mapping(address => uint256) public userRewardPerTokenPaid;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor initializes staking token and reward rate.
     * @param _stakingToken Address of the DOGE20 token contract.
     * @param _rewardPool Total amount of rewards to distribute over 2 years.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardPool) {
        stakingToken = _stakingToken;
        rewardRate = _rewardPool / REWARD_DURATION;
    }

    /**
     * @dev Modifier to update rewards for the user before performing actions.
     * @param _account User address for reward updates.
     */
    modifier updateReward(address _account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (_account != address(0)) {
            userRewards[_account] = earned(_account);
            userRewardPerTokenPaid[_account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculates the reward per token staked.
     * @return Reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + ((rewardRate * (block.timestamp - lastUpdateTime)) * 1e18 / totalStaked);
    }

    /**
     * @dev Calculates the rewards earned by a user.
     * @param _account User address.
     * @return Rewards earned.
     */
    function earned(address _account) public view returns (uint256) {
        return (userStake[_account] * (rewardPerToken() - userRewardPerTokenPaid[_account])) / 1e18 + userRewards[_account];
    }

    /**
     * @dev Stakes a specified amount of tokens.
     * @param _amount Amount to stake.
     */
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake 0 tokens");

        totalStaked += _amount;
        userStake[msg.sender] += _amount;

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraws staked tokens.
     * @param _amount Amount to withdraw.
     */
    function withdraw(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot withdraw 0 tokens");
        require(userStake[msg.sender] >= _amount, "Insufficient staked amount");

        totalStaked -= _amount;
        userStake[msg.sender] -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claims accumulated rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        userRewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Returns the balance of staked tokens for a user.
     * @param _account User address.
     * @return Staked amount.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return userStake[_account];
    }
}
```
