"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-presales.pages.dev
Prompt: Write a smart contract in Solidity for staking $QUBE tokens that distributes rewards based on a 5% sell tax, as described in InQubeta's tokenomics.
Generated: DETERMINISTIC_9f5f007a1b81c787
Batch ID: 20250612_153420
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
 * @title QUBE Token Staking Contract
 * @author InQubeta
 * @notice This contract allows users to stake $QUBE tokens and earn rewards from a 5% sell tax.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract QUBEStaking {
    // Address of the $QUBE token contract
    IERC20 public immutable qubeToken;

    // Rewards pool (funded by the 5% sell tax)
    uint256 public rewardsPool;

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Mapping to track user rewards
    mapping(address => uint256) public rewardsEarned;

    // Event declarations
    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event ClaimRewards(address indexed user, uint256 rewards);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _qubeToken Address of the $QUBE token contract.
     */
    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = IERC20(_qubeToken);
    }

    /**
     * @dev Allows users to stake $QUBE tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer $QUBE tokens from the user to the contract
        require(qubeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staked balance and total staked amount
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Stake(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their $QUBE tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update staked balance and total staked amount
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer $QUBE tokens back to the user
        require(qubeToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstake(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Reset rewards for the user
        rewardsEarned[msg.sender] = 0;

        // Transfer rewards from the pool to the user
        require(qubeToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit ClaimRewards(msg.sender, rewards);
    }

    /**
     * @dev Updates the rewards pool from the 5% sell tax.
     * @param _amount Amount of tokens to add to the rewards pool.
     */
    function updateRewardsPool(uint256 _amount) external {
        require(_amount > 0, "Rewards pool update amount must be greater than zero");

        // Transfer $QUBE tokens from the sender to the contract
        require(qubeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Increase the rewards pool amount
        rewardsPool += _amount;
    }

    /**
     * @dev Calculates the rewards for a user based on their staked balance.
     * @param _user Address of the user.
     * @return Reward amount for the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }

        // Proportionate rewards: (User's staked balance / Total staked) * Rewards pool
        uint256 userStake = stakedBalances[_user];
        return (userStake * rewardsPool) / totalStaked;
    }
}
```
