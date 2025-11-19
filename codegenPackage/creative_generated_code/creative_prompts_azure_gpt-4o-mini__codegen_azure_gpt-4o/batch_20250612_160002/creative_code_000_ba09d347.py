"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Generate a code snippet for a decentralized finance (DeFi) application that utilizes staking and farming features as described on EasyCake.
Generated: DETERMINISTIC_ba09d34743944c41
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DeFi Staking and Farming Contract
 * @dev Implements staking and farming features for decentralized finance applications.
 * Users can stake tokens and earn rewards over time.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DeFiStakingFarming is Ownable {
    // State variables
    IERC20 public stakingToken;      // Token users will stake
    IERC20 public rewardToken;       // Token users will earn as rewards
    uint256 public rewardRate;       // Reward rate per block
    uint256 public totalStaked;      // Total staked tokens
    uint256 private lastRewardBlock; // Last block where rewards were calculated
    uint256 private rewardPerTokenStored; // Accumulated reward rate per token

    mapping(address => uint256) private userStaked; // Amount staked by each user
    mapping(address => uint256) private userRewards; // Rewards earned by each user
    mapping(address => uint256) private userRewardDebt; // Rewards already paid to users

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking and reward tokens.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardRate Reward rate (tokens per block).
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Modifier to update rewards for the caller.
     */
    modifier updateRewards(address _user) {
        rewardPerTokenStored = rewardPerToken();
        lastRewardBlock = block.number;

        if (_user != address(0)) {
            userRewards[_user] = earned(_user);
            userRewardDebt[_user] = rewardPerTokenStored * userStaked[_user];
        }
        _;
    }

    /**
     * @dev Function to calculate reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored +
            ((block.number - lastRewardBlock) * rewardRate * 1e18) / totalStaked;
    }

    /**
     * @dev Function to calculate earned rewards for a user.
     * @param _user Address of the user.
     */
    function earned(address _user) public view returns (uint256) {
        return (userStaked[_user] * (rewardPerToken() - userRewardDebt[_user])) / 1e18 +
            userRewards[_user];
    }

    /**
     * @dev Function for users to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake 0 tokens");

        stakingToken.transferFrom(msg.sender, address(this), _amount);
        userStaked[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function for users to withdraw staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot withdraw 0 tokens");
        require(userStaked[msg.sender] >= _amount, "Not enough staked tokens");

        userStaked[msg.sender] -= _amount;
        totalStaked -= _amount;
        stakingToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function for users to claim rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        userRewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to update the reward rate. Only callable by the contract owner.
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
