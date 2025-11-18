"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yifistake.finance
Prompt: Write a smart contract in Solidity to enable staking and farming of YI12 tokens, including functionality for claiming rewards and unfarming as described on the YI12 Stake Finance platform.
Generated: DETERMINISTIC_9045404a100d1b5d
Batch ID: 20250612_145125
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
 * @title YI12 Staking and Farming Contract
 * @dev A smart contract to enable staking, farming, claiming rewards, and unfarming of YI12 tokens.
 */
contract YI12StakeFinance {
    IERC20 public immutable yi12Token; // YI12 token contract address.

    uint256 private constant REWARD_RATE = 1e18; // Reward tokens per second per staked token.
    uint256 private constant PRECISION = 1e36; // Precision for reward calculations.

    struct StakeInfo {
        uint256 amount;          // Amount of tokens staked.
        uint256 rewardDebt;      // Reward debt for the staker.
        uint256 lastUpdatedTime; // Last time the staker interacted with the contract.
    }

    mapping(address => StakeInfo) public stakes; // Storing staking information for each user.
    uint256 public totalStaked;                 // Total tokens staked in the contract.

    event Staked(address indexed user, uint256 amount);
    event Unfarmed(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the YI12 token contract address.
     * @param _yi12Token Address of the YI12 token contract.
     */
    constructor(IERC20 _yi12Token) {
        require(address(_yi12Token) != address(0), "Invalid token address");
        yi12Token = _yi12Token;
    }

    /**
     * @dev Function to stake YI12 tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        StakeInfo storage userStake = stakes[msg.sender];

        // Update user rewards before modifying the stake.
        _updateRewards(msg.sender);

        // Transfer tokens to the contract.
        require(
            yi12Token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user's stake and total staked.
        userStake.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unfarm (withdraw) staked tokens.
     */
    function unfarm(uint256 _amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update rewards before modifying the stake.
        _updateRewards(msg.sender);

        // Update user's stake and total staked.
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user.
        require(yi12Token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unfarmed(msg.sender, _amount);
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming.
        _updateRewards(msg.sender);

        StakeInfo storage userStake = stakes[msg.sender];

        uint256 rewardsToClaim = userStake.rewardDebt;

        require(rewardsToClaim > 0, "No rewards available to claim");

        // Reset reward debt.
        userStake.rewardDebt = 0;

        // Transfer rewards to the user.
        require(yi12Token.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");

        emit Claimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Internal function to update rewards for a specific user.
     * @param _user Address of the user to update rewards for.
     */
    function _updateRewards(address _user) internal {
        StakeInfo storage userStake = stakes[_user];

        uint256 pendingReward = _calculateRewards(_user);

        userStake.rewardDebt += pendingReward;
        userStake.lastUpdatedTime = block.timestamp;
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return uint256 Pending reward amount.
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        StakeInfo storage userStake = stakes[_user];

        // Time difference since last update.
        uint256 timeElapsed = block.timestamp - userStake.lastUpdatedTime;

        // Calculate pending rewards based on staked amount and elapsed time.
        uint256 pendingReward = (userStake.amount * REWARD_RATE * timeElapsed) / PRECISION;

        return pendingReward;
    }

    /**
     * @dev Function to get user's staking information.
     * @param _user Address of the user.
     * @return amount Staked amount.
     * @return rewardDebt Pending rewards.
     * @return lastUpdatedTime Last updated time.
     */
    function getStakeInfo(address _user)
        external
        view
        returns (uint256 amount, uint256 rewardDebt, uint256 lastUpdatedTime)
    {
        StakeInfo storage userStake = stakes[_user];
        return (userStake.amount, userStake.rewardDebt, userStake.lastUpdatedTime);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
