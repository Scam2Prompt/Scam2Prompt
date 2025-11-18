"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halobulls-staking.vercel.app
Prompt: Generate code to deploy a staking smart contract compatible with the "Halo Gods Staking" platform using Solidity. Include functions for staking, withdrawing, and calculating rewards.
Generated: DETERMINISTIC_a2780f52df084981
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
 * @title HaloGodsStaking
 * @dev A staking smart contract compatible with the Halo Gods Staking platform.
 * Users can stake tokens, withdraw their stakes, and calculate rewards.
 */
contract HaloGodsStaking {
    // Address of the token contract
    IERC20 public stakingToken;

    // Struct to keep track of user staking information
    struct Stake {
        uint256 amount;   // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
    }

    // Mapping of user address to their stake information
    mapping(address => Stake) private stakes;

    // Reward rate per second (example: 1 token per day = 1 / (24*60*60) tokens per second)
    uint256 public rewardRate;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-specific functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the token contract to be staked.
     * @param _rewardRate Reward rate (tokens per second).
     */
    constructor(address _stakingToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Function for users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update user's staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function for users to withdraw their staked tokens along with rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 stakedDuration = block.timestamp - userStake.startTime;
        uint256 reward = userStake.amount * rewardRate * stakedDuration;

        // Transfer staked tokens and rewards back to the user
        require(
            stakingToken.transfer(msg.sender, userStake.amount + reward),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, userStake.amount);
        emit RewardPaid(msg.sender, reward);

        // Reset user's staking information
        userStake.amount = 0;
        userStake.startTime = 0;
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Pending reward amount.
     */
    function calculateReward(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakedDuration = block.timestamp - userStake.startTime;
        return userStake.amount * rewardRate * stakedDuration;
    }

    /**
     * @dev Owner-only function to update the reward rate.
     * @param _rewardRate New reward rate.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }
}

// Minimal IERC20 interface for token interactions
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
