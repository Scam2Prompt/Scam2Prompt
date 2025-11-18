"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solfixresolver.pages.dev
Prompt: Generate code to implement a staking pool mechanism for cryptocurrencies, ensuring compatibility with BNB Chain and Ethereum ERC20 tokens as outlined on the SolfixResolver webpage.
Generated: DETERMINISTIC_4c7d945a5ae46e59
Batch ID: 20250612_153655
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
 * @dev A smart contract for staking ERC20 tokens, compatible with Ethereum and BNB Chain.
 * Users can stake tokens to earn rewards based on the duration of their stake.
 */
contract StakingPool {
    // Struct to represent a staker's information
    struct Stake {
        uint256 amount; // Amount of tokens staked by the user
        uint256 timestamp; // Timestamp when the stake was created
    }

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Reward rate per second (example: 0.0001 reward tokens per second staked)
    uint256 public rewardRate;

    // Mapping to store staking data for each user
    mapping(address => Stake) public stakes;

    // Mapping to store rewards accumulated for each user
    mapping(address => uint256) public rewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking token and reward rate.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _rewardRate Rate of reward tokens per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure the staking amount is greater than zero.
     */
    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Allows a user to stake a specified amount of tokens.
     * @param amount Amount of tokens to be staked.
     */
    function stake(uint256 amount) external nonZeroAmount(amount) {
        // Transfer staking tokens from user to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update rewards for the user based on existing stake
        _updateRewards(msg.sender);

        // Update staking data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Update rewards before withdrawing
        _updateRewards(msg.sender);

        uint256 amount = userStake.amount;

        // Reset the staking data for the user
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their accumulated rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset the reward balance for the user
        rewards[msg.sender] = 0;

        // Transfer reward tokens to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update the rewards for a user.
     * @param user Address of the user whose rewards are being updated.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 duration = block.timestamp - userStake.timestamp;
            rewards[user] += (duration * rewardRate * userStake.amount) / 1e18;
            userStake.timestamp = block.timestamp; // Reset timestamp to prevent double-counting
        }
    }

    /**
     * @dev Retrieves the reward balance for a user.
     * @param user Address of the user.
     * @return reward The reward balance for the user.
     */
    function getRewardBalance(address user) external view returns (uint256 reward) {
        reward = rewards[user];
    }

    /**
     * @dev Retrieves the staking balance for a user.
     * @param user Address of the user.
     * @return amount The staking balance for the user.
     */
    function getStakingBalance(address user) external view returns (uint256 amount) {
        amount = stakes[user].amount;
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
