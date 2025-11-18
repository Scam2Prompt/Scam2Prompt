"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-ai.market
Prompt: Write a smart contract in Solidity to interact with Agora AI's tokenomics system, specifically for staking AGAI tokens.
Generated: DETERMINISTIC_663322b591ae5be7
Batch ID: 20250612_153512
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
 * @title AgoraAI Tokenomics Staking Contract
 * @dev This contract allows users to stake AGAI tokens and earn rewards.
 * @author [Your Name]
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AgoraAIStaking {
    // Address of the AGAI token contract
    IERC20 public immutable agaiToken;

    // Reward rate (e.g., 1 token reward per token staked per year)
    uint256 public rewardRate = 100; // Basis points (1% reward rate annually)

    // Total staked balance
    uint256 public totalStaked;

    // Mapping of user addresses to staking balance
    mapping(address => uint256) private stakedBalances;

    // Mapping of user addresses to last updated timestamp
    mapping(address => uint256) private lastUpdated;

    // Mapping of user addresses to rewards earned but not withdrawn
    mapping(address => uint256) private rewards;

    // Event declarations for transparency
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the token contract address.
     * @param _agaiToken Address of the AGAI token contract.
     */
    constructor(IERC20 _agaiToken) {
        require(address(_agaiToken) != address(0), "Invalid token address");
        agaiToken = _agaiToken;
    }

    /**
     * @dev Stake AGAI tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update rewards before modifying the user's balance
        _updateRewards(msg.sender);

        // Transfer the tokens from sender to the contract
        require(agaiToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking balance and total staked amount
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        // Update the last updated timestamp for the user
        lastUpdated[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake AGAI tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update rewards before modifying the user's balance
        _updateRewards(msg.sender);

        // Update staking balance and total staked amount
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer the tokens from contract to user
        require(agaiToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw accumulated rewards.
     */
    function withdrawRewards() external {
        // Update rewards before withdrawal
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to withdraw");

        // Reset the user's reward balance
        rewards[msg.sender] = 0;

        // Transfer the reward tokens from contract to user
        require(agaiToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardWithdrawn(msg.sender, reward);
    }

    /**
     * @dev View function to check staked balance of a user.
     * @param _user Address of the user.
     * @return Staked balance of the user.
     */
    function stakedBalanceOf(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev View function to check rewards of a user.
     * @param _user Address of the user.
     * @return Rewards balance of the user.
     */
    function rewardsBalanceOf(address _user) external view returns (uint256) {
        uint256 pendingReward = _calculateReward(_user);
        return rewards[_user] + pendingReward;
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        uint256 pendingReward = _calculateReward(_user);
        rewards[_user] += pendingReward;
        lastUpdated[_user] = block.timestamp;
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        uint256 timeDiff = block.timestamp - lastUpdated[_user];
        uint256 userBalance = stakedBalances[_user];
        return (userBalance * rewardRate * timeDiff) / (365 days * 10000); // Annual reward rate in basis points
    }
}
```
