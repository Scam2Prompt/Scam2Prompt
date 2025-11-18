"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freedumfighert.pages.dev
Prompt: Develop a smart contract to manage staking pools for FreeDum Fighters, ensuring rewards are distributed according to the project's tokenomics.
Generated: DETERMINISTIC_8af4245502ebf0f5
Batch ID: 20250612_153424
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
 * @title FreeDum Fighters Staking Pool
 * @notice This smart contract manages staking pools and distributes rewards according to tokenomics.
 * @dev Ensure tokens are ERC20-compliant.
 */
contract StakingPool {
    // Struct to keep track of staking information for each user
    struct Stake {
        uint256 amount;        // Amount staked
        uint256 rewardDebt;    // Reward debt for this stake
        uint256 lastStakedAt;  // Timestamp of last staking action
    }

    // ERC20 token contract interface
    IERC20 public immutable rewardToken;
    IERC20 public immutable stakingToken;

    // Rewards distribution parameters
    uint256 public rewardPerTokenPerSecond;
    uint256 public totalStaked;

    // Mapping of user address to their staking details
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to ensure non-zero staking
    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Staking amount must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardPerTokenPerSecond Reward rate per token per second.
     */
    constructor(
        IERC20 _rewardToken,
        IERC20 _stakingToken,
        uint256 _rewardPerTokenPerSecond
    ) {
        rewardToken = _rewardToken;
        stakingToken = _stakingToken;
        rewardPerTokenPerSecond = _rewardPerTokenPerSecond;
    }

    /**
     * @notice Stake tokens into the pool.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonZeroAmount(amount) {
        Stake storage userStake = stakes[msg.sender];

        // Update rewards before modifying state
        _updateReward(msg.sender);

        // Transfer staking tokens from user to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update staking details
        userStake.amount += amount;
        userStake.lastStakedAt = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonZeroAmount(amount) {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update rewards before modifying state
        _updateReward(msg.sender);

        // Update staking details
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer staking tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards.
     */
    function claimReward() external {
        _updateReward(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 rewardToClaim = userStake.rewardDebt;

        require(rewardToClaim > 0, "No rewards to claim");
        userStake.rewardDebt = 0;

        // Transfer rewards to user
        require(rewardToken.transfer(msg.sender, rewardToClaim), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewardToClaim);
    }

    /**
     * @dev Internal function to calculate and update rewards.
     * @param user The address of the user to update rewards for.
     */
    function _updateReward(address user) internal {
        Stake storage userStake = stakes[user];

        // Calculate rewards based on staked amount and elapsed time
        uint256 pendingReward = ((block.timestamp - userStake.lastStakedAt) *
            userStake.amount *
            rewardPerTokenPerSecond) / 1e18;

        userStake.rewardDebt += pendingReward;
        userStake.lastStakedAt = block.timestamp;
    }

    /**
     * @notice Get pending reward for a user.
     * @param user The user's address.
     * @return The amount of pending reward.
     */
    function pendingReward(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];

        // Calculate pending reward without modifying state
        uint256 pendingReward = ((block.timestamp - userStake.lastStakedAt) *
            userStake.amount *
            rewardPerTokenPerSecond) / 1e18;

        return userStake.rewardDebt + pendingReward;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
