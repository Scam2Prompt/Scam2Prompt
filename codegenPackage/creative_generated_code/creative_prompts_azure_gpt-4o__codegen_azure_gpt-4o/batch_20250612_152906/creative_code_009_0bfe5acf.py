"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayentest2.pages.dev
Prompt: Generate a Solidity contract for a staking mechanism that aligns with KAYEN Protocol's sustainable dual-token model and deflationary principles.
Generated: DETERMINISTIC_0bfe5acfd8f30cc2
Batch ID: 20250612_152906
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
 * @dev A staking mechanism that aligns with KAYEN Protocol's dual-token model and deflationary principles.
 * Allows users to stake tokens and earn rewards while maintaining sustainability.
 */
contract StakingContract {
    // Token interfaces
    IERC20 public stakingToken; // Token used for staking
    IERC20 public rewardToken;  // Token used for rewards

    // Structure to store user staking details
    struct Staker {
        uint256 amount;       // Amount of tokens staked
        uint256 rewardDebt;   // Reward debt for the staker (to avoid duplicates)
        uint256 lastStakedAt; // Timestamp of the last staking action
    }

    // State variables
    mapping(address => Staker) public stakers; // Mapping of stakers
    uint256 public totalStaked;               // Total amount of tokens staked
    uint256 public rewardRate;                // Reward rate (tokens per second)
    uint256 public lastRewardTimestamp;       // Last timestamp rewards were calculated
    uint256 public accumulatedRewardPerToken; // Accumulated rewards per staked token

    // Governance variables
    address public owner;                     // Contract owner

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyWithdrawal(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
            uint256 rewards = timeElapsed * rewardRate;
            accumulatedRewardPerToken += (rewards * 1e18) / totalStaked;
        }
        lastRewardTimestamp = block.timestamp;
        _;
    }

    /**
     * @dev Constructor initializes the staking and reward tokens.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardRate Initial reward rate (tokens per second).
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardRate
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards {
        require(_amount > 0, "Cannot stake zero tokens");

        Staker storage staker = stakers[msg.sender];
        uint256 pendingReward = (staker.amount * accumulatedRewardPerToken) /
            1e18 -
            staker.rewardDebt;

        if (pendingReward > 0) {
            rewardToken.transfer(msg.sender, pendingReward); // Pay out pending rewards
            emit RewardClaimed(msg.sender, pendingReward);
        }

        stakingToken.transferFrom(msg.sender, address(this), _amount);
        staker.amount += _amount;
        staker.rewardDebt =
            (staker.amount * accumulatedRewardPerToken) /
            1e18;
        staker.lastStakedAt = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external updateRewards {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked balance");

        uint256 pendingReward = (staker.amount * accumulatedRewardPerToken) /
            1e18 -
            staker.rewardDebt;

        if (pendingReward > 0) {
            rewardToken.transfer(msg.sender, pendingReward); // Pay out pending rewards
            emit RewardClaimed(msg.sender, pendingReward);
        }

        staker.amount -= _amount;
        staker.rewardDebt =
            (staker.amount * accumulatedRewardPerToken) /
            1e18;
        totalStaked -= _amount;
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Emergency withdrawal in case of unforeseen issues (for stakers only).
     */
    function emergencyWithdraw() external {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amount;

        require(amount > 0, "Nothing to withdraw");

        staker.amount = 0;
        staker.rewardDebt = 0;
        totalStaked -= amount;

        stakingToken.transfer(msg.sender, amount);
        emit EmergencyWithdrawal(msg.sender, amount);
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRate New reward rate (tokens per second).
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner updateRewards {
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user to check rewards for.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 currentAccumulatedRewardPerToken = accumulatedRewardPerToken;

        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
            uint256 rewards = timeElapsed * rewardRate;
            currentAccumulatedRewardPerToken += (rewards * 1e18) / totalStaked;
        }

        return
            (staker.amount * currentAccumulatedRewardPerToken) /
            1e18 -
            staker.rewardDebt;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
