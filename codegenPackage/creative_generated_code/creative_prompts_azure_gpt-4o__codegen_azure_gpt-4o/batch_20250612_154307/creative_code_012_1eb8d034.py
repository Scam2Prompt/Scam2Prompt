"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Generate a Solidity contract that implements a reward distribution mechanism for $STARS holders, based on the MemeVault staking protocol.
Generated: DETERMINISTIC_1eb8d03488adfb2f
Batch ID: 20250612_154307
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
 * @title RewardDistributor
 * @dev A contract to distribute rewards in $STARS tokens to stakers based on a MemeVault staking protocol.
 */
contract RewardDistributor {
    // Address of $STARS token contract
    IERC20 public starsToken;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Mapping to track reward balances of users
    mapping(address => uint256) public rewardBalances;

    // Reward per token staked (scaled by 1e18 for precision)
    uint256 public rewardPerToken;

    // Last updated reward per token value
    uint256 public lastRewardPerToken;

    // Last time rewards were updated
    uint256 public lastUpdateTime;

    // Reward rate per second in $STARS
    uint256 public rewardRate;

    // Events for tracking actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _starsToken Address of the $STARS token contract
     * @param _rewardRate Reward rate per second in $STARS
     */
    constructor(IERC20 _starsToken, uint256 _rewardRate) {
        require(address(_starsToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        starsToken = _starsToken;
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Updates the reward distribution variables.
     */
    function updateReward() internal {
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            rewardPerToken += (rewardRate * timeElapsed * 1e18) / totalStaked;
        }
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Stake $STARS tokens into the contract.
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        updateReward();

        if (stakedBalances[msg.sender] > 0) {
            // Calculate pending rewards for the user
            uint256 pendingReward = (stakedBalances[msg.sender] * (rewardPerToken - lastRewardPerToken)) / 1e18;
            rewardBalances[msg.sender] += pendingReward;
        }

        starsToken.transferFrom(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        lastRewardPerToken = rewardPerToken;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked $STARS tokens from the contract.
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        updateReward();

        // Calculate pending rewards for the user
        uint256 pendingReward = (stakedBalances[msg.sender] * (rewardPerToken - lastRewardPerToken)) / 1e18;
        rewardBalances[msg.sender] += pendingReward;

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        starsToken.transfer(msg.sender, amount);
        lastRewardPerToken = rewardPerToken;

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        updateReward();

        uint256 pendingReward = (stakedBalances[msg.sender] * (rewardPerToken - lastRewardPerToken)) / 1e18;
        rewardBalances[msg.sender] += pendingReward;
        lastRewardPerToken = rewardPerToken;

        uint256 rewardsToClaim = rewardBalances[msg.sender];
        require(rewardsToClaim > 0, "No rewards available to claim");

        rewardBalances[msg.sender] = 0;
        starsToken.transfer(msg.sender, rewardsToClaim);

        emit RewardClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev View function to check pending rewards for a user.
     * @param user Address of the user
     * @return Pending rewards for the user
     */
    function pendingRewards(address user) external view returns (uint256) {
        uint256 currentRewardPerToken = rewardPerToken;
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            currentRewardPerToken += (rewardRate * timeElapsed * 1e18) / totalStaked;
        }

        uint256 pendingReward = (stakedBalances[user] * (currentRewardPerToken - lastRewardPerToken)) / 1e18;
        return rewardBalances[user] + pendingReward;
    }
}

/**
 * @dev Interface for ERC20 token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
