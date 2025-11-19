"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20io.pages.dev
Prompt: Generate a sample smart contract for the DOGE20 staking mechanism that distributes rewards over two years.
Generated: DETERMINISTIC_60d56cc2036a5827
Batch ID: 20250612_161617
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
 * @title DOGE20 Staking Contract
 * @dev A smart contract for staking DOGE20 tokens and distributing rewards over a 2-year period.
 */
contract Doge20Staking {
    // Token interface to interact with DOGE20 tokens
    IERC20 public immutable doge20Token;

    // Duration constants
    uint256 public constant REWARD_PERIOD = 730 days; // 2 years in seconds

    // Reward distribution parameters
    uint256 public totalRewardPool; // Total reward pool to be distributed over 2 years
    uint256 public immutable rewardRate; // Reward per second

    // Struct for staker information
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt used to calculate pending rewards
        uint256 lastInteraction; // Timestamp of the last staking interaction
    }

    // Mapping from address to staker information
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to ensure the user has staked
    modifier hasStaked(address _user) {
        require(stakers[_user].stakedAmount > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Constructor to initialize staking contract.
     * @param _doge20Token Address of the DOGE20 token contract
     * @param _rewardPool Initial reward pool to be distributed
     */
    constructor(address _doge20Token, uint256 _rewardPool) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_rewardPool > 0, "Reward pool must be greater than zero");

        doge20Token = IERC20(_doge20Token);
        totalRewardPool = _rewardPool;
        rewardRate = _rewardPool / REWARD_PERIOD;
    }

    /**
     * @dev Function for users to stake DOGE20 tokens.
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];

        // Update rewards before changing state
        updateRewards(msg.sender);

        // Transfer tokens to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker's data
        staker.stakedAmount += _amount;
        staker.lastInteraction = block.timestamp;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function for users to unstake their tokens.
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external hasStaked(msg.sender) {
        require(_amount > 0, "Unstaking amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= _amount, "Insufficient staked amount");

        // Update rewards before changing state
        updateRewards(msg.sender);

        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, _amount), "Token transfer failed");

        // Update staker's data
        staker.stakedAmount -= _amount;
        staker.lastInteraction = block.timestamp;

        // Update total staked tokens
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to claim accrued rewards.
     */
    function claimRewards() external hasStaked(msg.sender) {
        updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        uint256 pendingReward = staker.rewardDebt;
        require(pendingReward > 0, "No rewards available to claim");

        // Reset reward debt after claiming
        staker.rewardDebt = 0;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param _user Address of the staker
     */
    function updateRewards(address _user) internal {
        Staker storage staker = stakers[_user];

        uint256 elapsedTime = block.timestamp - staker.lastInteraction;
        uint256 newRewards = (staker.stakedAmount * rewardRate * elapsedTime) / totalStaked;

        staker.rewardDebt += newRewards;
        staker.lastInteraction = block.timestamp;
    }

    /**
     * @dev Function to retrieve pending rewards for a user.
     * @param _user Address of the user
     * @return Pending reward amount
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 elapsedTime = block.timestamp - staker.lastInteraction;
        uint256 newRewards = (staker.stakedAmount * rewardRate * elapsedTime) / totalStaked;

        return staker.rewardDebt + newRewards;
    }
}

/**
 * @dev Interface for ERC20 tokens
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
