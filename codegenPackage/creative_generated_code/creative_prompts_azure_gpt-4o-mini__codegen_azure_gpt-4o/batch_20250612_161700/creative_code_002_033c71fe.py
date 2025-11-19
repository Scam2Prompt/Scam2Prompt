"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a Solidity contract that allows users to stake their $MGLS tokens and earn rewards based on their share of the staking pool.
Generated: DETERMINISTIC_033c71fe902a85d2
Batch ID: 20250612_161700
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
 * @title StakingContract
 * @dev A contract that allows users to stake $MGLS tokens and earn rewards based on their share of the staking pool.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // ERC20 token to be staked ($MGLS token)
    IERC20 public token;

    // Total amount staked in the pool
    uint256 public totalStaked;

    // Rewards pool balance
    uint256 public rewardsPool;

    // Mapping of user address to staked balance
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to accumulated rewards
    mapping(address => uint256) public rewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws staked tokens
    event WithdrawnStake(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract with the $MGLS token
     * @param _token Address of the ERC20 $MGLS token contract
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Allows a user to stake a specified amount of $MGLS tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's staked balance and the total amount staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens
     */
    function withdrawStake() external {
        uint256 userStake = stakedBalances[msg.sender];
        require(userStake > 0, "No staked tokens to withdraw");

        // Reduce user's staked balance and update total staked
        stakedBalances[msg.sender] = 0;
        totalStaked -= userStake;

        // Transfer staked tokens back to the user
        require(token.transfer(msg.sender, userStake), "Token transfer failed");

        emit WithdrawnStake(msg.sender, userStake);
    }

    /**
     * @dev Allows a user to claim their accumulated rewards
     */
    function claimRewards() external {
        uint256 userRewards = calculateRewards(msg.sender);
        require(userRewards > 0, "No rewards available to claim");

        // Update the user's rewards balance
        rewards[msg.sender] = 0;
        rewardsPool -= userRewards;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, userRewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, userRewards);
    }

    /**
     * @dev Calculates the rewards for a given user based on their share of the staking pool
     * @param user Address of the user
     * @return The calculated reward amount
     */
    function calculateRewards(address user) public view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }
        // Reward amount is proportional to the user's share of the pool
        return (stakedBalances[user] * rewardsPool) / totalStaked;
    }

    /**
     * @dev Allows the contract owner to deposit rewards into the rewards pool
     * @param amount Amount of tokens to deposit as rewards
     */
    function depositRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer reward tokens from sender to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the rewards pool balance
        rewardsPool += amount;
    }
}
```
