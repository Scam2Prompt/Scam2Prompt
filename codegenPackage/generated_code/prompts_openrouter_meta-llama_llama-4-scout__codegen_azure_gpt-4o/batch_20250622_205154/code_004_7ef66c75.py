"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-claimm.pages.dev
Prompt: Design a basic smart contract in Solidity for distributing staking rewards to DOGE20 token holders over a period of two years, similar to the Dogecoin20 staking contract.
Generated: DETERMINISTIC_7ef66c75da78ab72
Batch ID: 20250622_205154
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingRewards
 * @dev A smart contract for distributing staking rewards to DOGE20 token holders over a period of two years.
 */
contract StakingRewards {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Total rewards to be distributed over two years
    uint256 public immutable totalRewards;

    // Duration of the staking rewards distribution (2 years in seconds)
    uint256 public constant REWARD_DURATION = 2 * 365 * 24 * 60 * 60;

    // Timestamp when rewards distribution starts
    uint256 public immutable startTime;

    // Timestamp when rewards distribution ends
    uint256 public immutable endTime;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards claimed by users
    mapping(address => uint256) public rewardsClaimed;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _totalRewards Total rewards to be distributed over two years.
     */
    constructor(IERC20 _doge20Token, uint256 _totalRewards) {
        require(address(_doge20Token) != address(0), "Invalid token address");
        require(_totalRewards > 0, "Total rewards must be greater than zero");

        doge20Token = _doge20Token;
        totalRewards = _totalRewards;
        startTime = block.timestamp;
        endTime = block.timestamp + REWARD_DURATION;
    }

    /**
     * @dev Stake DOGE20 tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(block.timestamp < endTime, "Staking period has ended");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        require(block.timestamp > startTime, "Rewards distribution has not started");
        require(stakedBalances[msg.sender] > 0, "No staked balance");

        // Calculate rewards based on the user's staked balance and elapsed time
        uint256 elapsedTime = block.timestamp > endTime ? endTime - startTime : block.timestamp - startTime;
        uint256 userRewards = (totalRewards * stakedBalances[msg.sender] * elapsedTime) / (totalStaked * REWARD_DURATION);

        // Subtract already claimed rewards
        uint256 claimableRewards = userRewards - rewardsClaimed[msg.sender];
        require(claimableRewards > 0, "No rewards to claim");

        // Update claimed rewards
        rewardsClaimed[msg.sender] += claimableRewards;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, claimableRewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, claimableRewards);
    }

    /**
     * @dev Get the claimable rewards for a user.
     * @param user Address of the user.
     * @return Claimable rewards amount.
     */
    function getClaimableRewards(address user) external view returns (uint256) {
        if (block.timestamp <= startTime || stakedBalances[user] == 0) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp > endTime ? endTime - startTime : block.timestamp - startTime;
        uint256 userRewards = (totalRewards * stakedBalances[user] * elapsedTime) / (totalStaked * REWARD_DURATION);
        return userRewards - rewardsClaimed[user];
    }
}

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
