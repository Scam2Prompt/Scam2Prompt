"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdogecoin20-portal.pages.dev
Prompt: Write a smart contract code snippet for staking DOGE20 tokens on the Ethereum blockchain that distributes rewards based on the percentage of the staking pool.
Generated: DETERMINISTIC_3e092dac493b8376
Batch ID: 20250612_162346
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
 * @title Doge20TokenStaking
 * @dev Smart contract for staking DOGE20 tokens and distributing rewards based on staking pool percentage.
 */
contract Doge20TokenStaking {
    // Address of the DOGE20 token contract
    IERC20 public doge20Token;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // Mapping of staker address to their staked balance
    mapping(address => uint256) public stakedBalances;

    // Mapping of staker address to their pending rewards
    mapping(address => uint256) public pendingRewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the DOGE20 token contract
    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "Invalid token address");
        doge20Token = IERC20(_doge20Token);
    }

    /**
     * @dev Function to stake DOGE20 tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the staker to the contract
        require(
            doge20Token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking balances and total staked amount
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate and update pending rewards for a staker.
     * @param _rewardPool Total reward pool available for distribution.
     */
    function updateRewards(uint256 _rewardPool) external {
        require(totalStaked > 0, "No tokens staked");

        // Iterate over all stakers and update their pending rewards
        for (uint256 i = 0; i < totalStaked; i++) {
            // Calculate reward based on staker’s percentage in the pool
            address staker = msg.sender;
            uint256 stakerPercentage = (stakedBalances[staker] * 1e18) /
                totalStaked; // Scaled by 1e18 for precision
            uint256 reward = (_rewardPool * stakerPercentage) / 1e18;

            // Update pending rewards for the staker
            pendingRewards[staker] += reward;
        }
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        uint256 reward = pendingRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        pendingRewards[msg.sender] = 0;

        // Transfer reward tokens to the staker
        require(
            doge20Token.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to withdraw staked tokens.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            stakedBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );

        // Update staking balances and total staked amount
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer staked tokens back to the user
        require(
            doge20Token.transfer(msg.sender, _amount),
            "Withdrawal transfer failed"
        );

        emit Withdrawn(msg.sender, _amount);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
