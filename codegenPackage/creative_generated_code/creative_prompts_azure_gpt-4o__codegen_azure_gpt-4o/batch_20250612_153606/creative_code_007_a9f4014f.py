"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokencatgirl.pages.dev
Prompt: Provide code for a decentralized application that allows users to farm and stake CATGIRL¢ tokens, incorporating gamified elements inspired by the Catgirl ecosystem.
Generated: DETERMINISTIC_a9f4014f93f73690
Batch ID: 20250612_153606
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

// Import OpenZeppelin libraries for ERC20 tokens and access control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract CatgirlFarm is Ownable, ReentrancyGuard {
    // Structure to represent a user's stake
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 rewardDebt;   // Rewards already claimed by user
        uint256 lastStakeTime; // Timestamp of last stake
    }

    // Token to be staked
    IERC20 public immutable stakingToken;

    // Reward token distributed
    IERC20 public immutable rewardToken;

    // Reward rate per second (adjustable by owner)
    uint256 public rewardRate;

    // Total staked tokens across all users
    uint256 public totalStaked;

    // Mapping of users to their stakes
    mapping(address => Stake) public userStakes;

    // Gamified cooldown period for stake withdrawal
    uint256 public withdrawCooldown = 7 days;

    // Events to track actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor initializes the staking and reward tokens along with the initial reward rate.
     * @param _stakingToken Address of the staking token (e.g., CATGIRL¢).
     * @param _rewardToken Address of the reward token.
     * @param _rewardRate Initial reward rate per second.
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stakes a specified amount of tokens into the farm.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake zero tokens");

        // Calculate pending rewards for the user
        Stake storage user = userStakes[msg.sender];
        uint256 pending = getPendingRewards(msg.sender);

        // Update user stake info
        user.amount += _amount;
        user.rewardDebt = pending;
        user.lastStakeTime = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes a specified amount of tokens from the farm.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external nonReentrant {
        Stake storage user = userStakes[msg.sender];
        require(user.amount >= _amount, "Insufficient staked tokens");
        require(block.timestamp >= user.lastStakeTime + withdrawCooldown, "Cooldown period active");

        // Calculate pending rewards and update user's stake info
        uint256 pending = getPendingRewards(msg.sender);
        user.amount -= _amount;
        user.rewardDebt = pending;

        // Update total staked
        totalStaked -= _amount;

        // Transfer staking tokens back to user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claims accumulated rewards for the user.
     */
    function claimRewards() external nonReentrant {
        uint256 pending = getPendingRewards(msg.sender);
        require(pending > 0, "No rewards available");

        // Update user reward debt
        userStakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, pending);

        emit Claimed(msg.sender, pending);
    }

    /**
     * @dev Calculates the pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function getPendingRewards(address _user) public view returns (uint256) {
        Stake storage user = userStakes[_user];
        if (user.amount == 0) {
            return 0;
        }

        uint256 accruedReward = (user.amount * rewardRate * (block.timestamp - user.lastStakeTime)) / 1e18;
        return accruedReward + user.rewardDebt;
    }

    /**
     * @dev Updates the reward rate (only callable by the owner).
     * @param _newRate New reward rate per second.
     */
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    /**
     * @dev Updates the withdrawal cooldown period (only callable by the owner).
     * @param _newCooldown New cooldown period in seconds.
     */
    function setWithdrawCooldown(uint256 _newCooldown) external onlyOwner {
        withdrawCooldown = _newCooldown;
    }
}
```

This Solidity code defines a decentralized farming contract for staking `CATGIRL¢` tokens with gamified elements, adhering to best practices and including error handling.
