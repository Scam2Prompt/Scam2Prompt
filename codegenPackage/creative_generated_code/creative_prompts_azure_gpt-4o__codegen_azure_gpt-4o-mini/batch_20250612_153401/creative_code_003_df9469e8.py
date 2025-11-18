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
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ETFS Staking Contract
 * @dev This contract allows users to stake their ETFS tokens and earn rewards from a sell tax pool.
 */
contract ETFSStaking is Ownable, ReentrancyGuard {
    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of ETFS tokens staked
        uint256 rewardDebt; // Reward debt
    }

    IERC20 public etfsToken;                // ETFS token contract
    uint256 public accRewardPerShare;      // Accumulated rewards per share
    uint256 public totalStaked;             // Total amount of ETFS tokens staked
    uint256 public rewardPool;              // Total rewards available for distribution
    uint256 public lastRewardTimestamp;     // Last timestamp rewards were updated

    // Mapping of user address to UserInfo
    mapping(address => UserInfo) public userInfo;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardDistributed(uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the ETFS token address.
     * @param _etfsToken Address of the ETFS token contract.
     */
    constructor(IERC20 _etfsToken) {
        require(address(_etfsToken) != address(0), "Invalid token address");
        etfsToken = _etfsToken;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Updates the rewards for all stakers.
     */
    function updateRewards() internal {
        if (totalStaked == 0) {
            lastRewardTimestamp = block.timestamp;
            return;
        }

        // Calculate time elapsed since last reward update
        uint256 timeElapsed = block.timestamp - lastRewardTimestamp;

        // Calculate rewards based on the time elapsed (can define your logic here)
        uint256 rewardsToDistribute = timeElapsed * 10; // Example: 10 tokens per second

        // Update the accumulated rewards per share
        accRewardPerShare += rewardsToDistribute * 1e12 / totalStaked; // Adjusted for decimal precision
        rewardPool += rewardsToDistribute;
        lastRewardTimestamp = block.timestamp;

        emit RewardDistributed(rewardsToDistribute);
    }

    /**
     * @dev Allows users to stake ETFS tokens.
     * @param _amount Amount of ETFS tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");
        
        // Update rewards before staking
        updateRewards();

        // Transfer ETFS tokens from the user to the contract
        etfsToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount;
        user.rewardDebt = user.amount * accRewardPerShare / 1e12;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake ETFS tokens and claim rewards.
     * @param _amount Amount of ETFS tokens to unstake.
     */
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateRewards();

        // Calculate pending rewards
        uint256 pendingRewards = (user.amount * accRewardPerShare / 1e12) - user.rewardDebt;

        // Update user info
        user.amount -= _amount;
        user.rewardDebt = user.amount * accRewardPerShare / 1e12;

        // Transfer the unstaked ETFS tokens back to the user
        etfsToken.transfer(msg.sender, _amount);

        // Transfer pending rewards if any
        if (pendingRewards > 0) {
            require(rewardPool >= pendingRewards, "Insufficient rewards in pool");
            rewardPool -= pendingRewards;
            etfsToken.transfer(msg.sender, pendingRewards);
        }

        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to add rewards to the pool.
     * @param _amount Amount of ETFS tokens to add to the reward pool.
     */
    function addRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Cannot add 0 rewards");
        etfsToken.transferFrom(msg.sender, address(this), _amount);
        rewardPool += _amount;
    }

    /**
     * @dev View function to see the pending rewards for a user.
     * @param _user Address of the user to query.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
            uint256 rewardsToDistribute = timeElapsed * 10; // Example: 10 tokens per second
            currentAccRewardPerShare += rewardsToDistribute * 1e12 / totalStaked;
        }
        return (user.amount * currentAccRewardPerShare / 1e12) - user.rewardDebt;
    }
}
```
