"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the staking and reward distribution for Green Bitcoin ($GBTC) on the Ethereum blockchain.
Generated: DETERMINISTIC_0b521783ca31a6a4
Batch ID: 20250612_161353
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
 * @title Green Bitcoin Staking Contract
 * @dev This contract allows users to stake $GBTC tokens and earn rewards over time.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract GreenBitcoinStaking {
    // ERC20 token interface for $GBTC
    IERC20 public immutable GBTC;

    // Reward rate per token per second (scaled for precision, e.g. 1e18 = 1 GBTC reward per token per second)
    uint256 public rewardRate;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Mapping to track user stakes and reward data
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardDebt;
    mapping(address => uint256) public lastUpdateTime;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardWithdrawn(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the $GBTC token address and reward rate
    constructor(IERC20 _GBTC, uint256 _rewardRate) {
        require(address(_GBTC) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");
        GBTC = _GBTC;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake a specific amount of $GBTC tokens into the contract.
     * @param amount The amount of tokens to stake (must be approved beforehand).
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update user rewards before staking
        _updateRewards(msg.sender);

        // Transfer $GBTC tokens from the user to the contract
        require(GBTC.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake a specific amount of $GBTC tokens and withdraw rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        require(GBTC.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Withdraw accumulated rewards.
     */
    function withdrawRewards() external {
        // Update user rewards
        _updateRewards(msg.sender);

        // Calculate claimable rewards
        uint256 rewards = rewardDebt[msg.sender];
        require(rewards > 0, "No rewards available");

        // Reset reward debt and transfer tokens
        rewardDebt[msg.sender] = 0;
        require(GBTC.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardWithdrawn(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a specific user.
     * @param user The address of the user.
     */
    function _updateRewards(address user) internal {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
        if (timeElapsed > 0) {
            uint256 rewards = (stakedBalances[user] * rewardRate * timeElapsed) / 1e18;
            rewardDebt[user] += rewards;
            lastUpdateTime[user] = block.timestamp;
        }
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param user The address of the user.
     * @return The pending rewards.
     */
    function pendingRewards(address user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
        uint256 rewards = (stakedBalances[user] * rewardRate * timeElapsed) / 1e18;
        return rewardDebt[user] + rewards;
    }
}
```
