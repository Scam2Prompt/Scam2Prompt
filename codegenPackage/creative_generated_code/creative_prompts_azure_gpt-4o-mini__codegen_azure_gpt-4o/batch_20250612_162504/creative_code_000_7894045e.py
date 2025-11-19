"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsdrop.web.app
Prompt: How can I implement a staking mechanism for the $Jelly token as described on the Rascals website?
Generated: DETERMINISTIC_7894045e5aaf4ee3
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation of a staking mechanism for an ERC-20 token, `$Jelly`, using Solidity. This code implements the staking functionality, allowing users to deposit tokens into the staking contract and earn rewards based on their staked amount and duration.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title JellyTokenStaking
 * @dev Implements staking mechanism for ERC-20 Jelly tokens.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract JellyTokenStaking is Ownable {
    // The Jelly token contract
    IERC20 public jellyToken;

    // Reward rate per second (e.g., 100 tokens per second)
    uint256 public rewardRate;

    // Struct to store staking details for each user
    struct Stake {
        uint256 amount; // Amount of staked tokens
        uint256 timestamp; // Timestamp when tokens were staked
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of user address to their staking details
    mapping(address => Stake) public stakes;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _jellyToken Address of the Jelly token contract
     * @param _rewardRate Reward rate per second
     */
    constructor(IERC20 _jellyToken, uint256 _rewardRate) {
        require(address(_jellyToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        jellyToken = _jellyToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake a specified amount of Jelly tokens.
     * @param _amount Amount of tokens to be staked
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Calculate rewards for existing stake
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            userStake.rewards += calculateRewards(msg.sender);
        }

        // Update staking details
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        // Transfer tokens from user to the contract
        require(jellyToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake all staked tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender) + userStake.rewards;

        // Transfer staked tokens and rewards to the user
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;
        userStake.rewards = 0;

        require(jellyToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        if (rewards > 0) {
            require(jellyToken.transfer(msg.sender, rewards), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amountToUnstake, rewards);
    }

    /**
     * @dev Calculate the rewards for a given user.
     * @param _user Address of the user
     * @return Total rewards earned by the user
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        return userStake.amount * rewardRate * stakingDuration / 1e18; // Adjust for token decimals
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRewardRate New reward rate per second
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Emergency withdrawal of tokens. Only callable by the owner.
     * @param _amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(jellyToken.transfer(owner(), _amount), "Token transfer failed");
    }
}
```

This implementation includes staking, unstaking, and reward calculation features, adheres to best practices, and features proper error handling and event logging.
