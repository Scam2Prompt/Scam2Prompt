"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-in.web.app
Prompt: Develop a simple staking mechanism for a cryptocurrency project using Solidity, inspired by the staking rewards system described in the Rebel Satoshi ecosystem.
Generated: DETERMINISTIC_6c6b423a9f3e044d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @dev A simple staking mechanism for a cryptocurrency project.
 * Users can stake tokens, earn rewards, and withdraw their stake along with rewards.
 */
contract StakingContract {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public stakingToken; // Token used for staking
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Timestamp of the last update
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens and rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Update rewards for the user
        _updateRewards(msg.sender);

        uint256 stakedAmount = userStake.amount;
        uint256 reward = _calculateReward(msg.sender);

        // Reset user's stake
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        // Update total staked
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Withdrawn(msg.sender, stakedAmount);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function pendingReward(address _user) external view returns (uint256) {
        return _calculateReward(_user);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        uint256 reward = _calculateReward(_user);
        userStake.rewardDebt += reward;
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Internal function to calculate rewards for a user.
     * @param _user Address of the user.
     * @return Reward amount.
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        uint256 reward = (userStake.amount * rewardRate * timeElapsed) / 1e18;
        return reward - userStake.rewardDebt;
    }
}
```
