"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-io-dashborad.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum that distributes rewards to stakers proportionally over a two-year period, as described in the Dogecoin20 roadmap.
Generated: DETERMINISTIC_0bfc0cc5a0e5873d
Batch ID: 20250612_153526
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
 * @title DOGE20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and receive proportional rewards over a 2-year period.
 */
contract DOGE20Staking {
    IERC20 public immutable doge20Token; // DOGE20 token contract
    uint256 public immutable rewardDuration; // Reward distribution duration in seconds (2 years)
    uint256 public immutable startTime; // Contract start time for rewards
    uint256 public immutable endTime; // Contract end time for rewards

    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardsPool; // Total rewards available for distribution
    uint256 public lastUpdateTime; // Last time the rewards were updated
    uint256 public rewardPerTokenStored; // Accumulated rewards per token

    mapping(address => uint256) public userStake; // User staking balances
    mapping(address => uint256) public userRewardPerTokenPaid; // User's reward-per-token snapshot
    mapping(address => uint256) public rewards; // User's earned rewards

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp < endTime ? block.timestamp : endTime;

        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    constructor(IERC20 _doge20Token, uint256 _rewardsPool) {
        require(address(_doge20Token) != address(0), "Invalid token contract");
        require(_rewardsPool > 0, "Rewards pool must be greater than zero");

        doge20Token = _doge20Token;
        rewardsPool = _rewardsPool;
        rewardDuration = 2 * 365 * 24 * 60 * 60; // 2 years
        startTime = block.timestamp;
        endTime = startTime + rewardDuration;
    }

    /**
     * @dev Stake DOGE20 tokens into the contract.
     * @param amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        totalStaked += amount;
        userStake[msg.sender] += amount;

        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param amount Amount of DOGE20 tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(userStake[msg.sender] >= amount, "Insufficient staked balance");

        totalStaked -= amount;
        userStake[msg.sender] -= amount;

        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards from staking.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;

        require(doge20Token.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Calculate the current reward per token.
     * @return Current reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }

        uint256 duration = block.timestamp < endTime ? block.timestamp : endTime - lastUpdateTime;
        return rewardPerTokenStored + (duration * rewardsPool / rewardDuration * 1e18 / totalStaked);
    }

    /**
     * @dev Calculate the earned rewards for a specific account.
     * @param account Address of the user.
     * @return Rewards earned by the user.
     */
    function earned(address account) public view returns (uint256) {
        return (userStake[account] * (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18) + rewards[account];
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
