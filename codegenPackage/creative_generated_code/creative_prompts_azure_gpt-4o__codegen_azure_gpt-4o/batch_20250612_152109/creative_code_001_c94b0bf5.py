"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-a.pages.dev
Prompt: Generate Solidity code for an ERC-20 staking smart contract similar to DOGE20, which distributes rewards proportionally to stakers over a two-year period.
Generated: DETERMINISTIC_c94b0bf5633769f5
Batch ID: 20250612_152109
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
 * @title ERC-20 Staking Contract
 * @notice This contract allows users to stake ERC-20 tokens and earn proportional rewards
 * over a two-year period.
 */
contract ERC20Staking {
    // ERC-20 token contract address
    IERC20 public immutable stakingToken;

    // Duration for rewards distribution (2 years in seconds)
    uint256 public constant REWARD_DURATION = 2 * 365 * 24 * 60 * 60;

    // Total rewards pool
    uint256 public immutable totalRewards;

    // Contract start timestamp
    uint256 public immutable startTime;

    // Mapping of user stakes
    mapping(address => uint256) public stakes;

    // Mapping of user reward claims
    mapping(address => uint256) public rewardsClaimed;

    // Total staked tokens
    uint256 private totalStaked;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Address of the ERC-20 token to be staked
     * @param _totalRewards Total reward pool to be distributed over the staking period
     */
    constructor(IERC20 _stakingToken, uint256 _totalRewards) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_totalRewards > 0, "Total rewards must be greater than zero");

        stakingToken = _stakingToken;
        totalRewards = _totalRewards;
        startTime = block.timestamp;
    }

    /**
     * @notice Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user stake and total staked tokens
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens from the contract
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user stake and total staked tokens
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim proportional rewards based on staking duration and amount
     */
    function claimRewards() external {
        // Calculate claimable rewards
        uint256 claimableRewards = _calculateRewards(msg.sender);

        require(claimableRewards > 0, "No rewards available to claim");

        // Update rewards claimed
        rewardsClaimed[msg.sender] += claimableRewards;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, claimableRewards);

        emit RewardsClaimed(msg.sender, claimableRewards);
    }

    /**
     * @notice View function to calculate rewards for a user
     * @param user Address of the user
     * @return Rewards claimable by the user
     */
    function viewRewards(address user) external view returns (uint256) {
        return _calculateRewards(user);
    }

    /**
     * @dev Internal function to calculate rewards for a user
     * @param user Address of the user
     * @return Rewards claimable by the user
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        // Ensure staking has started
        if (block.timestamp <= startTime) {
            return 0;
        }

        // Calculate staking duration (capped to REWARD_DURATION)
        uint256 stakingDuration = block.timestamp - startTime;
        if (stakingDuration > REWARD_DURATION) {
            stakingDuration = REWARD_DURATION;
        }

        // User's staking proportion
        uint256 userStakeProportion = (stakes[user] * 1e18) / totalStaked;

        // Total rewards earned over the staking period
        uint256 totalRewardForUser = (totalRewards * stakingDuration) / REWARD_DURATION;

        // Proportional rewards less already claimed
        return ((totalRewardForUser * userStakeProportion) / 1e18) - rewardsClaimed[user];
    }
}

/**
 * @dev Minimal ERC-20 interface for interacting with the staking token
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
