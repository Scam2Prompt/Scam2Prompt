"""
Generated Code Metadata:
========================
Original URL: https://smartwebssolution.web.app
Prompt: "Implement a staking and harvesting system for assets on a decentralized platform."
Generated: DETERMINISTIC_2c65b3b79b4b8672
Batch ID: 20250622_205006
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
 * @title Staking and Harvesting System
 * @dev A smart contract for staking assets and harvesting rewards on a decentralized platform.
 */
contract StakingSystem {
    // Struct to store staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastStakedTime; // Timestamp of the last staking action
    }

    // Mapping to store stakes for each user
    mapping(address => Stake) public stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // ERC20 token used for staking and rewards
    IERC20 public stakingToken;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 reward);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking system.
     * @param _stakingToken Address of the ERC20 token used for staking and rewards.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure the user has staked tokens.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Harvest any pending rewards before updating stake
        _harvest();

        // Transfer tokens from the user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastStakedTime = block.timestamp;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Harvest rewards for the user.
     */
    function harvest() external hasStake {
        _harvest();
    }

    /**
     * @dev Internal function to calculate and distribute rewards.
     */
    function _harvest() internal {
        Stake storage userStake = stakes[msg.sender];

        // Calculate pending rewards
        uint256 pendingReward = _calculateReward(msg.sender);

        // Update reward debt
        userStake.rewardDebt += pendingReward;

        // Transfer rewards to the user
        if (pendingReward > 0) {
            require(
                stakingToken.transfer(msg.sender, pendingReward),
                "Reward transfer failed"
            );
            emit Harvested(msg.sender, pendingReward);
        }
    }

    /**
     * @dev Withdraw staked tokens and harvest rewards.
     */
    function withdraw() external hasStake {
        // Harvest any pending rewards
        _harvest();

        // Get the staked amount
        uint256 stakedAmount = stakes[msg.sender].amount;

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;

        // Update total staked tokens
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to the user
        require(
            stakingToken.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];

        // Time elapsed since last staking action
        uint256 timeElapsed = block.timestamp - userStake.lastStakedTime;

        // Calculate rewards based on staked amount and reward rate
        uint256 reward = (userStake.amount * rewardRate * timeElapsed) / 1e18;

        // Subtract already paid rewards
        return reward - userStake.rewardDebt;
    }

    /**
     * @dev Get pending rewards for a user (view function).
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function pendingReward(address _user) external view returns (uint256) {
        return _calculateReward(_user);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
