"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clearpool.pages.dev
Prompt: What are the steps to implement a staking feature for CPOOL in a decentralized application using Clearpool's protocol?
Generated: DETERMINISTIC_839bb40e9a1eec89
Batch ID: 20250612_163338
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
 * @title Clearpool CPOOL Staking
 * @dev Implements a staking feature for CPOOL token in a decentralized application using Clearpool's protocol.
 * This contract allows users to stake CPOOL tokens, earn rewards, and withdraw their staked tokens and rewards.
 */
contract CPOOLStaking {
    // Address of the CPOOL token contract
    IERC20 public immutable cpoolToken;

    // Reward rate per second (e.g., in tokens per second)
    uint256 public rewardRate;

    // Tracks the total amount of tokens staked
    uint256 public totalStaked;

    // Mapping of user address to staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to reward debt
    mapping(address => uint256) public rewardDebt;

    // Last time the rewards were updated
    uint256 public lastRewardTime;

    // Accumulated rewards per token
    uint256 public accRewardPerToken;

    // Events for logging significant actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor initializes the contract with the CPOOL token address and reward rate
    constructor(address _cpoolToken, uint256 _rewardRate) {
        require(_cpoolToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        cpoolToken = IERC20(_cpoolToken);
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Modifier to update reward variables before executing a function.
     */
    modifier updateRewards() {
        if (block.timestamp > lastRewardTime && totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 rewards = timeElapsed * rewardRate;

            accRewardPerToken += rewards / totalStaked;
        }
        lastRewardTime = block.timestamp;
        _;
    }

    /**
     * @dev Allows users to stake CPOOL tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards {
        require(_amount > 0, "Stake amount must be greater than 0");

        // Update user's reward debt before staking
        stakedBalances[msg.sender] += _amount;
        rewardDebt[msg.sender] += (_amount * accRewardPerToken);

        totalStaked += _amount;

        // Transfer the tokens from the user to the contract
        require(
            cpoolToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens and claim rewards.
     */
    function withdraw(uint256 _amount) external updateRewards {
        require(
            stakedBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );

        // Calculate rewards owed to the user
        uint256 rewards = pendingRewards(msg.sender);

        // Update the staked balance and total staked
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Reset reward debt for the withdrawn amount
        rewardDebt[msg.sender] = stakedBalances[msg.sender] * accRewardPerToken;

        // Transfer the staked tokens back to the user
        require(cpoolToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Transfer the rewards to the user
        if (rewards > 0) {
            require(cpoolToken.transfer(msg.sender, rewards), "Reward transfer failed");
            emit RewardsClaimed(msg.sender, rewards);
        }

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Calculates the pending rewards for a user.
     * @param _user The user's address.
     * @return The amount of rewards pending for the user.
     */
    function pendingRewards(address _user) public view returns (uint256) {
        uint256 accumulatedReward = stakedBalances[_user] * accRewardPerToken;
        return accumulatedReward - rewardDebt[_user];
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
