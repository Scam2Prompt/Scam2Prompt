"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Create a Solidity contract to implement TG.Casino's staking system, including immediate reward distribution and revenue-based rewards.
Generated: DETERMINISTIC_8996762e54db1adb
Batch ID: 20250612_153517
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
 * @title TG.Casino Staking Contract
 * @dev Implements a staking system with immediate reward distribution and revenue-based rewards.
 */
contract TGCasinoStaking {
    // Struct to store staking information
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 rewardDebt;   // Rewards already paid to the staker
    }

    // Mapping to store stakes of each user
    mapping(address => Stake) public stakes;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Revenue pool for rewards distribution
    uint256 public revenuePool;

    // Reward per token staked (used for immediate reward distribution)
    uint256 public rewardPerToken;

    // Address of the admin (contract owner)
    address public admin;

    // Token used for staking (ERC20 compatible)
    IERC20 public stakingToken;

    // Events
    event StakeAdded(address indexed user, uint256 amount);
    event StakeRemoved(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RevenueAdded(uint256 amount);

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _stakingToken) {
        admin = msg.sender;
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Allows user to stake tokens and updates their stake info.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards before changing stake amount
        _updateRewards(msg.sender);

        // Transfer staking tokens to this contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update stake info
        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit StakeAdded(msg.sender, _amount);
    }

    /**
     * @dev Allows user to withdraw staked tokens and claim rewards.
     */
    function withdrawStake() external {
        Stake storage stakeInfo = stakes[msg.sender];
        uint256 userAmount = stakeInfo.amount;
        require(userAmount > 0, "No tokens staked");

        // Update rewards before withdrawing stake
        _updateRewards(msg.sender);

        // Reset user's stake info
        stakeInfo.amount = 0;
        stakeInfo.rewardDebt = 0;
        totalStaked -= userAmount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, userAmount), "Token transfer failed");

        emit StakeRemoved(msg.sender, userAmount);
    }

    /**
     * @dev Allows user to claim their pending rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 pendingReward = _pendingReward(msg.sender);
        require(pendingReward > 0, "No rewards available");

        // Update user's reward debt
        stakes[msg.sender].rewardDebt += pendingReward;

        // Transfer rewards from revenue pool
        require(revenuePool >= pendingReward, "Not enough revenue in pool");
        revenuePool -= pendingReward;

        require(
            stakingToken.transfer(msg.sender, pendingReward),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Allows admin to add revenue to the pool for rewards distribution.
     * @param _amount Amount of tokens to add to the revenue pool.
     */
    function addRevenue(uint256 _amount) external onlyAdmin {
        require(_amount > 0, "Cannot add zero revenue");

        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        revenuePool += _amount;
        emit RevenueAdded(_amount);
    }

    /**
     * @dev Updates reward information for a given user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        if (stakes[_user].amount > 0) {
            // Calculate pending rewards based on user stake
            uint256 pendingReward = _pendingReward(_user);
            stakes[_user].rewardDebt += pendingReward;

            // Deduct rewards from revenue pool
            require(revenuePool >= pendingReward, "Not enough revenue in pool");
            revenuePool -= pendingReward;
        }
    }

    /**
     * @dev Calculates pending rewards for a given user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function _pendingReward(address _user) internal view returns (uint256) {
        Stake storage stakeInfo = stakes[_user];
        uint256 userReward = (stakeInfo.amount * rewardPerToken) / 1e18;
        return userReward - stakeInfo.rewardDebt;
    }

    /**
     * @dev Updates the rewardPerToken value for immediate rewards distribution.
     * Admin can call this periodically based on revenue generated.
     * @param _rewardPerToken New reward per token value.
     */
    function updateRewardPerToken(uint256 _rewardPerToken) external onlyAdmin {
        rewardPerToken = _rewardPerToken;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
