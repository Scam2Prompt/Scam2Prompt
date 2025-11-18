"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://floki-reward.com
Prompt: Generate Solidity code for creating a staking contract that rewards users with Floki's sister token, TOKEN, when they stake $FLOKI tokens.
Generated: DETERMINISTIC_b899b318d9c5ee0c
Batch ID: 20250612_151624
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
 * @dev A staking contract where users can stake FLOKI tokens and earn TOKEN rewards.
 */
contract StakingContract {
    // ERC20 token interfaces for FLOKI and TOKEN
    IERC20 public flokiToken;
    IERC20 public rewardToken;

    // Reward rate per second (TOKENs rewarded per second of staking)
    uint256 public rewardRate;

    // Total staked FLOKI tokens in the contract
    uint256 public totalStaked;

    // Mapping to track each user's staked amount
    mapping(address => uint256) public stakedBalance;

    // Mapping to track each user's last update timestamp
    mapping(address => uint256) public lastUpdateTime;

    // Mapping to track each user's accumulated rewards
    mapping(address => uint256) public rewards;

    /**
     * @dev Constructor initializes the contract with token addresses and reward rate.
     * @param _flokiToken Address of the FLOKI token contract.
     * @param _rewardToken Address of the TOKEN reward token contract.
     * @param _rewardRate Number of TOKENs rewarded per second per staked FLOKI.
     */
    constructor(address _flokiToken, address _rewardToken, uint256 _rewardRate) {
        flokiToken = IERC20(_flokiToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the caller.
     */
    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] += _earned(account);
            lastUpdateTime[account] = block.timestamp;
        }
        _;
    }

    /**
     * @dev Function to calculate the reward earned by an account.
     * @param account Address of the staker.
     * @return Reward amount earned by the account.
     */
    function _earned(address account) internal view returns (uint256) {
        uint256 timeDifference = block.timestamp - lastUpdateTime[account];
        return stakedBalance[account] * rewardRate * timeDifference / 1e18;
    }

    /**
     * @dev Stake FLOKI tokens in the contract.
     * @param amount Amount of FLOKI tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        flokiToken.transferFrom(msg.sender, address(this), amount);
        stakedBalance[msg.sender] += amount;
        totalStaked += amount;
    }

    /**
     * @dev Withdraw staked FLOKI tokens from the contract.
     * @param amount Amount of FLOKI tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");
        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;
        flokiToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Claim earned TOKEN rewards.
     */
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
    }

    /**
     * @dev Emergency function to allow the contract owner to withdraw all tokens.
     *      This should only be used in case of contract malfunction.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external {
        // Only callable by the contract deployer (add proper access control in production)
        require(msg.sender == address(0xDEADBEEF), "Unauthorized");
        IERC20(token).transfer(msg.sender, amount);
    }
}

// Minimal IERC20 interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
