"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20support.pages.dev
Prompt: Write a tutorial for integrating DOGE20 staking functionality into a decentralized application (dApp) using Ethereum smart contracts and the token address `0x2541A36BE4cD39286ED61a3E6AFC2307602489d6`.
Generated: DETERMINISTIC_910cf468da39d923
Batch ID: 20250612_152235
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
 * @title DOGE20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and earn rewards for their stakes.
 * Token address to integrate: 0x2541A36BE4cD39286ED61a3E6AFC2307602489d6
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20Staking is Ownable {
    // DOGE20 token address
    IERC20 public immutable doge20Token;

    // Mapping to track staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards for each staker
    mapping(address => uint256) public rewardBalances;

    // Total staked tokens
    uint256 public totalStaked;

    // Annual reward rate (e.g., 10% -> 1000 basis points)
    uint256 public annualRewardRateBasisPoints = 1000;

    // Timestamp when the staker last interacted with the contract
    mapping(address => uint256) public lastUpdate;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the DOGE20 token address
    constructor(address _doge20TokenAddress) {
        require(_doge20TokenAddress != address(0), "Invalid token address");
        doge20Token = IERC20(_doge20TokenAddress);
    }

    /**
     * @dev Modifier to calculate rewards for the user before proceeding.
     */
    modifier updateRewards(address _user) {
        if (lastUpdate[_user] > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdate[_user];
            rewardBalances[_user] += (stakedBalances[_user] * timeElapsed * annualRewardRateBasisPoints) / (10000 * 365 days);
        }
        lastUpdate[_user] = block.timestamp;
        _;
    }

    /**
     * @dev Function to stake DOGE20 tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake DOGE20 tokens.
     * @param _amount The amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        require(doge20Token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to claim rewards earned from staking.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = rewardBalances[msg.sender];
        require(rewards > 0, "No rewards available");

        rewardBalances[msg.sender] = 0;

        require(doge20Token.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to update the annual reward rate (basis points).
     * Can only be called by the contract owner.
     * @param _newRate New annual reward rate in basis points.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");
        annualRewardRateBasisPoints = _newRate;
    }

    /**
     * @dev Function to get the current rewards for a user.
     * @param _user The address of the user.
     * @return The current reward balance for the user.
     */
    function getPendingRewards(address _user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdate[_user];
        uint256 pendingRewards = rewardBalances[_user] + (stakedBalances[_user] * timeElapsed * annualRewardRateBasisPoints) / (10000 * 365 days);
        return pendingRewards;
    }
}
```
