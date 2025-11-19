"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-reward.pages.dev
Prompt: How can I implement a feature to stake and harvest assets in a DApp, referencing the DApp Reward's staking process?
Generated: DETERMINISTIC_36b1c7fa8db540db
Batch ID: 20250612_140418
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
 * @title StakingRewards
 * @dev A smart contract for staking and harvesting rewards in a DApp. Users can stake tokens
 * and harvest rewards based on the staking process.
 */
contract StakingRewards {
    // State variables
    IERC20 public stakingToken; // Token that users can stake
    IERC20 public rewardToken;  // Token that will be distributed as rewards
    uint256 public rewardRate;  // Reward rate (tokens per second)
    uint256 public totalStaked; // Total staked tokens
    uint256 public lastUpdateTime; // Last time rewards were updated

    mapping(address => uint256) public userStake;        // User's staked tokens
    mapping(address => uint256) public userRewards;      // User's accumulated rewards
    mapping(address => uint256) public userRewardPerTokenPaid; // User's reward debt

    uint256 public rewardPerTokenStored; // Accumulated reward per token

    /**
     * @dev Constructor initializes the staking and reward tokens and the reward rate.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardRate Reward rate (tokens per second).
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Modifier to ensure reward calculation before state changes.
     */
    modifier updateReward(address _account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        // Update rewards for the user
        if (_account != address(0)) {
            userRewards[_account] = earned(_account);
            userRewardPerTokenPaid[_account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update state
        userStake[msg.sender] += _amount;
        totalStaked += _amount;
    }

    /**
     * @dev Withdraw staked tokens and harvest rewards.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot withdraw 0 tokens");
        require(userStake[msg.sender] >= _amount, "Insufficient staked tokens");

        // Update state
        userStake[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer staked tokens back to user
        stakingToken.transfer(msg.sender, _amount);
    }

    /**
     * @dev Harvest accumulated rewards.
     */
    function harvest() external updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to harvest");

        // Reset user's rewards
        userRewards[msg.sender] = 0;

        // Transfer reward tokens to user
        rewardToken.transfer(msg.sender, reward);
    }

    /**
     * @dev Calculate accumulated reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastUpdateTime) * rewardRate * 1e18) /
            totalStaked;
    }

    /**
     * @dev Calculate earned rewards for a user.
     * @param _account User's address.
     * @return Amount of rewards earned.
     */
    function earned(address _account) public view returns (uint256) {
        return
            (userStake[_account] * (rewardPerToken() - userRewardPerTokenPaid[_account])) /
            1e18 +
            userRewards[_account];
    }

    /**
     * @dev Allow the owner to update the reward rate.
     * @param _newRewardRate New reward rate (tokens per second).
     */
    function updateRewardRate(uint256 _newRewardRate) external {
        // Only callable by the contract owner (add a modifier for owner check in production)
        rewardRate = _newRewardRate;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
