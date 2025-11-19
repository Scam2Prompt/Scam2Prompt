"""
Generated Code Metadata:
========================
Original URL: https://ordifypro.pages.dev
Prompt: "Design a basic smart contract in Solidity for managing staking incentives and token allocation on the Ethereum blockchain, inspired by Ordify's tokenomics."
Generated: DETERMINISTIC_6cf88ac4436ed333
Batch ID: 20250622_210243
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
 * @title StakingIncentives
 * @dev A smart contract for managing staking incentives and token allocation.
 * Inspired by Ordify's tokenomics.
 */
contract StakingIncentives {
    // Token used for staking and rewards
    IERC20 public stakingToken;

    // Reward rate per second
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to reward debt
    mapping(address => uint256) public rewardDebt;

    // Last time rewards were updated
    uint256 public lastUpdateTime;

    // Accumulated rewards per token
    uint256 public accRewardPerToken;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the token used for staking.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Modifier to update rewards before executing a function.
     */
    modifier updateRewards() {
        accRewardPerToken += (block.timestamp - lastUpdateTime) * rewardRate / totalStaked;
        lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot stake 0 tokens");
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user balances and reward debt
        stakedBalances[msg.sender] += amount;
        rewardDebt[msg.sender] = stakedBalances[msg.sender] * accRewardPerToken;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user balances and reward debt
        stakedBalances[msg.sender] -= amount;
        rewardDebt[msg.sender] = stakedBalances[msg.sender] * accRewardPerToken;

        totalStaked -= amount;

        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external updateRewards {
        uint256 reward = stakedBalances[msg.sender] * accRewardPerToken - rewardDebt[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewardDebt[msg.sender] = stakedBalances[msg.sender] * accRewardPerToken;

        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Get the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards.
     */
    function pendingRewards(address user) external view returns (uint256) {
        uint256 _accRewardPerToken = accRewardPerToken + (block.timestamp - lastUpdateTime) * rewardRate / totalStaked;
        return stakedBalances[user] * _accRewardPerToken - rewardDebt[user];
    }
}

/**
 * @dev Interface for ERC20 token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
