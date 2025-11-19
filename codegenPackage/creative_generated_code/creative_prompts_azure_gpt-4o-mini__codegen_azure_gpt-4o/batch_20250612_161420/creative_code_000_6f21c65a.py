"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.web.app
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens that distributes rewards over two years based on the percentage of the staking pool.
Generated: DETERMINISTIC_6f21c65a6b24cb7b
Batch ID: 20250612_161420
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
 * @dev A staking contract for DOGE20 tokens that distributes rewards over two years based on the percentage of the staking pool.
 */
contract StakingContract {
    IERC20 public immutable stakingToken; // Reference to the DOGE20 token contract
    uint256 public constant REWARD_DURATION = 2 * 365 days; // Rewards distributed over 2 years
    uint256 public totalStaked; // Total tokens staked in the pool
    uint256 public rewardPool; // Total rewards available for distribution
    uint256 public startTime; // Start time of staking
    uint256 public endTime; // End time of staking

    mapping(address => uint256) public balances; // Tracks user staked balances
    mapping(address => uint256) public rewardDebt; // Tracks user reward debt

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    modifier onlyActiveStaking() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Staking not active");
        _;
    }

    modifier onlyAfterEnd() {
        require(block.timestamp > endTime, "Staking period not ended");
        _;
    }

    constructor(IERC20 _stakingToken, uint256 _rewardPool) {
        stakingToken = _stakingToken;
        rewardPool = _rewardPool;
        startTime = block.timestamp;
        endTime = block.timestamp + REWARD_DURATION;
    }

    /**
     * @dev Stake DOGE20 tokens in the contract.
     * @param amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external onlyActiveStaking {
        require(amount > 0, "Cannot stake zero tokens");

        stakingToken.transferFrom(msg.sender, address(this), amount); // Transfer tokens to contract
        _updateRewards(msg.sender); // Update user rewards

        balances[msg.sender] += amount; // Update user staked balance
        totalStaked += amount; // Update total staked balance

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param amount Amount of DOGE20 tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(balances[msg.sender] >= amount, "Insufficient staked balance");

        _updateRewards(msg.sender); // Update user rewards

        balances[msg.sender] -= amount; // Update user staked balance
        totalStaked -= amount; // Update total staked balance

        stakingToken.transfer(msg.sender, amount); // Transfer tokens back to the user

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender); // Update user rewards

        uint256 reward = rewardDebt[msg.sender]; // Get user's reward amount
        require(reward > 0, "No rewards available");

        rewardDebt[msg.sender] = 0; // Reset reward debt
        stakingToken.transfer(msg.sender, reward); // Transfer rewards to the user

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update user's reward debt.
     * @param user User address to update rewards for.
     */
    function _updateRewards(address user) internal {
        if (totalStaked > 0) {
            // Calculate user's share of rewards based on their staking percentage
            uint256 userShare = (balances[user] * rewardPool) / totalStaked;
            rewardDebt[user] += userShare;
        }
    }

    /**
     * @dev Get remaining reward pool balance.
     * @return Remaining reward pool balance.
     */
    function remainingRewards() external view returns (uint256) {
        return rewardPool - (rewardPool * (block.timestamp - startTime)) / REWARD_DURATION;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
