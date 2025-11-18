"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimflockerztoken.pages.dev
Prompt: Create a smart contract in Solidity for staking $FLOCK tokens with a 342% APY, including functionality for claiming rewards and voting in a DAO.
Generated: DETERMINISTIC_c343b7c0675ec41c
Batch ID: 20250612_154010
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
 * @title FlockTokenStaking
 * @dev A staking smart contract for $FLOCK tokens that provides 342% APY rewards and enables voting functionality in a DAO.
 */
contract FlockTokenStaking {
    IERC20 public immutable flockToken; // Reference to the $FLOCK token contract
    uint256 public constant APY = 342; // Annual Percentage Yield (fixed at 342%)
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 startTime;     // Timestamp when staking started
        uint256 rewardClaimed; // Total rewards claimed by the user
    }

    mapping(address => Stake) public stakes; // Mapping to store staking details for each user
    uint256 public totalStaked;              // Total amount of tokens staked in the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(address _flockToken) {
        require(_flockToken != address(0), "Invalid token address");
        flockToken = IERC20(_flockToken);
    }

    /**
     * @dev Modifier to ensure the user has an active stake.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No active stake");
        _;
    }

    /**
     * @dev Stake a specified amount of $FLOCK tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(flockToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // If already staking, calculate and update rewards before adding new stake
            uint256 pendingReward = calculateReward(msg.sender);
            userStake.rewardClaimed += pendingReward;
        }

        userStake.amount += _amount;
        userStake.startTime = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake all staked tokens and claim pending rewards.
     */
    function unstake() external hasStake {
        Stake storage userStake = stakes[msg.sender];

        uint256 reward = calculateReward(msg.sender);
        uint256 totalReward = reward + userStake.rewardClaimed;

        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0; // Reset user's stake
        userStake.rewardClaimed = 0;
        totalStaked -= amountToUnstake;

        require(flockToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        require(flockToken.transfer(msg.sender, totalReward), "Reward transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardClaimed(msg.sender, totalReward);
    }

    /**
     * @dev Claim staking rewards without unstaking.
     */
    function claimRewards() external hasStake {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        userStake.rewardClaimed += reward;
        userStake.startTime = block.timestamp; // Reset staking time to prevent double rewards

        require(flockToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the staking reward for a user.
     * @param _user The address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime; // Time in seconds
        uint256 yearlyReward = (userStake.amount * APY) / 100;           // Annual reward
        uint256 reward = (yearlyReward * stakingDuration) / SECONDS_IN_YEAR;
        return reward;
    }

    /**
     * @dev DAO voting functionality for stakers.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _support Whether the user supports the proposal (true = yes, false = no).
     */
    function vote(uint256 _proposalId, bool _support) external hasStake {
        // Implement DAO voting logic here (e.g., interact with a DAO contract)
        // Placeholder: Emit a voting event
        emit Voted(msg.sender, _proposalId, _support);
    }

    // Event for voting
    event Voted(address indexed user, uint256 proposalId, bool support);
}

/**
 * @dev Minimal IERC20 interface for interacting with the $FLOCK token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
