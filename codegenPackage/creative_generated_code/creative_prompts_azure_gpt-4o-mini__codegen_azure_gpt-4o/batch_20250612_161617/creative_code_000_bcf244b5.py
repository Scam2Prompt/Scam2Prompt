"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20io.pages.dev
Prompt: How can I implement staking for the DOGE20 token using Ethereum smart contracts to earn passive rewards?
Generated: DETERMINISTIC_bcf244b5bda9224f
Batch ID: 20250612_161617
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
 * @title DOGE20 Token Staking Contract
 * @dev A contract for staking DOGE20 tokens and earning passive rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DOGE20Staking {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Reward rate per second (e.g., 0.0001 tokens per second)
    uint256 public immutable rewardRate;

    // Mapping of user addresses to staking balances
    mapping(address => uint256) public stakingBalance;

    // Mapping of user addresses to reward debt
    mapping(address => uint256) public rewardDebt;

    // Mapping of user addresses to the last timestamp they interacted with the contract
    mapping(address => uint256) public lastUpdate;

    // Total staked tokens
    uint256 public totalStaked;

    /**
     * @dev Constructor function to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake DOGE20 tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate pending rewards
        uint256 pendingReward = calculateReward(msg.sender);

        // Update user's reward debt and staking balance
        rewardDebt[msg.sender] += pendingReward;
        stakingBalance[msg.sender] += _amount;

        // Update user's last update time
        lastUpdate[msg.sender] = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;
    }

    /**
     * @dev Claim rewards earned from staking.
     */
    function claimRewards() external {
        uint256 pendingReward = calculateReward(msg.sender);

        // Update user's reward debt
        rewardDebt[msg.sender] += pendingReward;

        // Update user's last update time
        lastUpdate[msg.sender] = block.timestamp;

        // Transfer the rewards to the user
        require(doge20Token.transfer(msg.sender, pendingReward), "Reward transfer failed");
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakingBalance[msg.sender];
        require(stakedAmount > 0, "No staked tokens to unstake");

        // Calculate pending rewards
        uint256 pendingReward = calculateReward(msg.sender);

        // Reset user's staking balance and reward debt
        stakingBalance[msg.sender] = 0;
        rewardDebt[msg.sender] = 0;

        // Update user's last update time
        lastUpdate[msg.sender] = block.timestamp;

        // Update total staked amount
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards to the user
        require(doge20Token.transfer(msg.sender, stakedAmount), "Token transfer failed");
        require(doge20Token.transfer(msg.sender, pendingReward), "Reward transfer failed");
    }

    /**
     * @dev Calculate the rewards earned by a user.
     * @param _user Address of the user.
     * @return Total rewards earned by the user.
     */
    function calculateReward(address _user) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdate[_user];
        return stakingBalance[_user] * rewardRate * timeElapsed / 1e18;
    }
}
```
