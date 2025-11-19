"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibuswap.github.io
Prompt: Develop a smart contract for a yield farm that distributes rewards in BONE tokens, following the model used by ShibaSwap's WOOF feature.
Generated: DETERMINISTIC_3a45195f3b630d79
Batch ID: 20250612_155712
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
 * @title YieldFarmContract
 * @dev A smart contract for yield farming that distributes rewards in BONE tokens.
 *      This contract follows the model used by ShibaSwap's WOOF feature.
 *      Users stake tokens to earn BONE rewards over time.
 */
contract YieldFarmContract {
    // Struct to track user stakes
    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 rewardDebt;      // Reward debt (used for reward calculations)
        uint256 lastUpdatedTime; // Timestamp when the stake was last updated
    }

    // State variables
    address public immutable owner;       // Contract owner
    IERC20 public immutable stakingToken; // Token being staked
    IERC20 public immutable rewardToken;  // Token used for rewards (BONE)

    uint256 public rewardPerSecond;       // Reward rate per second
    uint256 public totalStaked;           // Total staked amount
    mapping(address => Stake) public stakes; // Mapping to track each user's stake

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "YieldFarmContract: Caller is not the owner");
        _;
    }

    modifier updateRewards(address _user) {
        // Update user's rewards before state changes
        if (_user != address(0)) {
            Stake storage userStake = stakes[_user];
            uint256 pendingRewards = calculatePendingRewards(_user);
            if (pendingRewards > 0) {
                userStake.rewardDebt += pendingRewards;
            }
            userStake.lastUpdatedTime = block.timestamp;
        }
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the token being staked.
     * @param _rewardToken Address of the reward token (BONE).
     * @param _rewardPerSecond Reward rate per second.
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardPerSecond) {
        require(address(_stakingToken) != address(0), "YieldFarmContract: Invalid staking token address");
        require(address(_rewardToken) != address(0), "YieldFarmContract: Invalid reward token address");

        owner = msg.sender;
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @dev Users can stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "YieldFarmContract: Cannot stake zero tokens");

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "YieldFarmContract: Failed to transfer tokens");

        // Update staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Users can withdraw their staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "YieldFarmContract: Insufficient staked tokens");

        // Update staking information
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "YieldFarmContract: Failed to transfer tokens");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Users can claim their pending rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        uint256 rewardAmount = userStake.rewardDebt;
        require(rewardAmount > 0, "YieldFarmContract: No rewards to claim");

        // Reset reward debt
        userStake.rewardDebt = 0;

        // Transfer rewards to the user
        require(rewardToken.transfer(msg.sender, rewardAmount), "YieldFarmContract: Failed to transfer rewards");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Calculates the pending rewards for a user.
     * @param _user Address of the user.
     * @return pendingRewards Amount of rewards pending.
     */
    function calculatePendingRewards(address _user) public view returns (uint256 pendingRewards) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdatedTime;
            pendingRewards = (userStake.amount * rewardPerSecond * timeElapsed) / totalStaked;
        }
    }

    /**
     * @dev Owner can update the reward rate.
     * @param _rewardPerSecond New reward rate per second.
     */
    function setRewardRate(uint256 _rewardPerSecond) external onlyOwner {
        rewardPerSecond = _rewardPerSecond;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
