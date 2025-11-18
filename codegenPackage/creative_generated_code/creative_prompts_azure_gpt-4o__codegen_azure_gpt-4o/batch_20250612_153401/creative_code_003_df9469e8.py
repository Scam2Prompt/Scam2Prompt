"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Create a staking mechanism in Solidity for $ETFS tokens that distributes rewards from a sell tax pool, as described in ETFSwap's staking feature.
Generated: DETERMINISTIC_df9469e8b4bd05af
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title ETFS Staking Contract
 * @dev Implements staking functionality for ETFS tokens with reward distribution from a sell tax pool.
 */
contract ETFSStaking {
    // Token interface
    IERC20 public immutable etfsToken;

    // Address of the sell tax pool
    address public immutable sellTaxPool;

    // Total staked tokens across all users
    uint256 public totalStaked;

    // Mapping of user address to their staked balance
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to their reward balance
    mapping(address => uint256) public rewardBalances;

    // Last time rewards were distributed
    uint256 public lastRewardDistribution;

    // Reward rate per second
    uint256 public rewardRate;

    // Events for logging staking interactions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor to initialize contract variables.
     * @param _etfsToken Address of the ETFS token contract.
     * @param _sellTaxPool Address of the sell tax pool.
     * @param _rewardRate Initial reward rate per second.
     */
    constructor(address _etfsToken, address _sellTaxPool, uint256 _rewardRate) {
        require(_etfsToken != address(0), "Invalid token address");
        require(_sellTaxPool != address(0), "Invalid sell tax pool address");

        etfsToken = IERC20(_etfsToken);
        sellTaxPool = _sellTaxPool;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake ETFS tokens to participate in staking.
     * @param amount Amount of ETFS tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(etfsToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake ETFS tokens and optionally claim rewards.
     * @param amount Amount of ETFS tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(etfsToken.transfer(msg.sender, amount), "Token transfer failed");

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards for the caller.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update reward balance
        rewardBalances[msg.sender] += rewards;

        // Transfer rewards from the sell tax pool to the user
        require(etfsToken.transferFrom(sellTaxPool, msg.sender, rewards), "Reward transfer failed");

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update reward rate (only callable by owner).
     * @param newRate New reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external {
        // Placeholder for owner check (implement access control)
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Calculate pending rewards for a specific user.
     * @param user Address of the user.
     * @return Pending rewards.
     */
    function calculateRewards(address user) public view returns (uint256) {
        return stakedBalances[user] * rewardRate * (block.timestamp - lastRewardDistribution) / 1e18;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
