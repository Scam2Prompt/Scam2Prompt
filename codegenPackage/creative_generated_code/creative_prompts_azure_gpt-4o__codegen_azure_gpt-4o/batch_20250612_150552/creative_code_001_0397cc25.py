"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20claim-now.pages.dev
Prompt: Generate Solidity code for a staking smart contract that mimics the DOGE20 reward distribution mechanism, providing rewards to stakers over a two-year period based on their share of the staking pool.
Generated: DETERMINISTIC_0397cc25d96a50c1
Batch ID: 20250612_150552
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
 * @title Staking Contract with DOGE20-like Reward Distribution
 * @dev This contract allows users to stake tokens and earn rewards over a 2-year period
 *      based on their percentage share of the staking pool.
 */
contract StakingRewards {
    // ERC20 token interface
    IERC20 public stakingToken;

    // Constants
    uint256 public constant REWARD_DURATION = 730 days; // 2 years in seconds
    uint256 public constant REWARD_RATE = 1000 ether; // Total reward amount over 2 years

    // Staking state
    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardsDistributed;

    mapping(address => uint256) public userStake;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public userRewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to update reward calculations
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
     * @dev Constructor initializes the staking contract with the staking token.
     * @param _stakingToken The address of the ERC20 token to be staked.
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked += amount;
        userStake[msg.sender] += amount;

        // Transfer staking tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Stake transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(userStake[msg.sender] >= amount, "Insufficient staked balance");
        totalStaked -= amount;
        userStake[msg.sender] -= amount;

        // Transfer staking tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Withdrawal transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        userRewards[msg.sender] = 0;
        rewardsDistributed += reward;

        // Transfer reward tokens to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the reward per token based on the elapsed time and rewards rate.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }

        uint256 elapsedTime = block.timestamp - lastUpdateTime;
        uint256 reward = (elapsedTime * REWARD_RATE) / REWARD_DURATION;
        return rewardPerTokenStored + (reward * 1e18) / totalStaked;
    }

    /**
     * @dev Calculate the earned reward for a user.
     * @param account The address of the user.
     */
    function earned(address account) public view returns (uint256) {
        return
            ((userStake[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            userRewards[account];
    }
}

// ERC20 Token Interface
interface IERC20 {
    function totalSupply() external view returns (uint256);

    function balanceOf(address account) external view returns (uint256);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function allowance(address owner, address spender) external view returns (uint256);

    function approve(address spender, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
