"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saita.pages.dev
Prompt: Provide code for integrating a staking pool feature into a decentralized exchange platform, inspired by the functionality mentioned on SaitaSwap.
Generated: DETERMINISTIC_8428fb2f40700847
Batch ID: 20250612_152739
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
 * @dev This contract allows users to stake tokens in a pool to earn rewards.
 * The functionality is designed for integration into a decentralized exchange platform.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingPool is Ownable {
    IERC20 public stakingToken; // Token that users will stake
    IERC20 public rewardToken;  // Token used for rewards

    uint256 public totalStaked;          // Total amount of tokens staked
    uint256 public rewardRatePerSecond;  // Reward rate per second
    uint256 public lastUpdateTime;       // Timestamp of the last update
    uint256 public rewardPerTokenStored; // Accumulated rewards per token

    mapping(address => uint256) public userStaked;       // Amount staked by each user
    mapping(address => uint256) public userRewardPaid;   // Rewards paid to each user
    mapping(address => uint256) public userRewards;      // Rewards owed to each user

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize staking and reward tokens.
     * @param _stakingToken Address of the token to be staked.
     * @param _rewardToken Address of the token used as rewards.
     */
    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Modifier to update the reward variables before function execution.
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculate the current reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastUpdateTime) * rewardRatePerSecond * 1e18) /
            totalStaked;
    }

    /**
     * @dev Calculate the total rewards earned by a user.
     * @param account Address of the user.
     */
    function earned(address account) public view returns (uint256) {
        return
            (userStaked[account] *
                (rewardPerToken() - userRewardPaid[account])) /
            1e18 +
            userRewards[account];
    }

    /**
     * @dev Stake tokens in the pool.
     * @param amount Amount of tokens to be staked.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        totalStaked += amount;
        userStaked[msg.sender] += amount;

        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the pool.
     * @param amount Amount of tokens to be withdrawn.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(userStaked[msg.sender] >= amount, "Insufficient staked balance");

        totalStaked -= amount;
        userStaked[msg.sender] -= amount;

        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        require(reward > 0, "No rewards to claim");

        userRewards[msg.sender] = 0; // Reset owed rewards
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Set the reward rate per second. Only callable by the owner.
     * @param _rewardRatePerSecond New reward rate.
     */
    function setRewardRate(uint256 _rewardRatePerSecond) external onlyOwner {
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Emergency function to withdraw all staking tokens. Only callable by the owner.
     */
    function emergencyWithdraw() external onlyOwner {
        stakingToken.transfer(owner(), stakingToken.balanceOf(address(this)));
    }

    /**
     * @dev Emergency function to withdraw all reward tokens. Only callable by the owner.
     */
    function emergencyRewardWithdraw() external onlyOwner {
        rewardToken.transfer(owner(), rewardToken.balanceOf(address(this)));
    }
}
```
