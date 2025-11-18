"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Create a Solidity contract that calculates rewards for staking QUBE tokens, distributing them from the 5% sell tax reward pool, as described in the InQubeta staking system.
Generated: DETERMINISTIC_96b4a1b9ee9ed30c
Batch ID: 20250612_153400
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
 * @title InQubetaStakingReward
 * @dev A smart contract to calculate and distribute rewards for staking QUBE tokens.
 */
contract InQubetaStakingReward {
    // Address of the QUBE token contract
    address public immutable qubeToken;

    // Reward pool accumulated from the 5% sell tax
    uint256 public rewardPool;

    // Total staked QUBE tokens across all users
    uint256 public totalStaked;

    // Mapping to store staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to store claimable reward balances of users
    mapping(address => uint256) public rewardBalances;

    // Event emitted when a user stakes QUBE tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 reward);

    // Event emitted when rewards are added to the pool
    event RewardPoolUpdated(uint256 amount);

    /**
     * @dev Constructor to initialize the QUBE token address.
     * @param _qubeToken Address of the QUBE token contract.
     */
    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = _qubeToken;
    }

    /**
     * @dev Function for stakers to deposit QUBE tokens into the staking pool.
     * @param amount The amount of QUBE tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer QUBE tokens from the sender to this contract
        require(
            IERC20(qubeToken).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update the staked balance and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards for the staked tokens.
     */
    function claimRewards() external {
        uint256 userReward = calculateReward(msg.sender);
        require(userReward > 0, "No rewards available");

        // Update user's reward balance
        rewardBalances[msg.sender] = 0;

        // Deduct from reward pool
        rewardPool -= userReward;

        // Transfer the reward to the user
        require(
            IERC20(qubeToken).transfer(msg.sender, userReward),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, userReward);
    }

    /**
     * @dev Internal function to calculate the reward for a specific user based on their stake.
     * @param user Address of the user.
     * @return The calculated reward amount.
     */
    function calculateReward(address user) internal view returns (uint256) {
        if (totalStaked == 0 || stakedBalances[user] == 0) {
            return 0;
        }
        // User's proportional share of the reward pool
        return (rewardPool * stakedBalances[user]) / totalStaked;
    }

    /**
     * @dev Function to update the reward pool when new rewards are added (e.g., from sell tax).
     * @param amount The amount of QUBE tokens added to the reward pool.
     */
    function updateRewardPool(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer QUBE tokens from the sender to this contract
        require(
            IERC20(qubeToken).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update the reward pool
        rewardPool += amount;

        emit RewardPoolUpdated(amount);
    }

    /**
     * @dev Function to get claimable rewards for a user.
     * @param user Address of the user.
     * @return The claimable reward amount.
     */
    function getClaimableRewards(address user) external view returns (uint256) {
        return calculateReward(user);
    }
}

/**
 * @dev Interface for ERC20 token to enable interactions with QUBE token.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
