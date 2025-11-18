"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appbitcoinminetrixclaim.pages.dev
Prompt: Provide a Solidity implementation for the "Stake-to-Mine" contract that supports variable lock-in periods based on user staking preferences.
Generated: DETERMINISTIC_9f61722e4420cd86
Batch ID: 20250612_152240
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
 * @title StakeToMine
 * @dev A contract where users can stake tokens to earn rewards, with variable lock-in periods.
 * Users choose a lock-in period, affecting their rewards calculation.
 */
contract StakeToMine {
    // Token used for staking (ERC20 address)
    IERC20 public stakingToken;

    // Structure to hold stake information
    struct Stake {
        uint256 amount;        // Amount staked
        uint256 lockUntil;     // Timestamp until which the tokens are locked
        uint256 rewardsEarned; // Rewards earned for the stake
    }

    // Mapping of user address to their stake details
    mapping(address => Stake) public stakes;

    // Reward rate per second based on lock-in duration (example values for simplicity)
    mapping(uint256 => uint256) public rewardRates;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockUntil);
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token used for staking.
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);

        // Initialize reward rates for various lock-in durations
        rewardRates[30 days] = 1 ether;  // Example: 1 token per second for 30 days lock-in
        rewardRates[60 days] = 2 ether; // Example: 2 tokens per second for 60 days lock-in
        rewardRates[90 days] = 3 ether; // Example: 3 tokens per second for 90 days lock-in
    }

    /**
     * @dev Stake tokens with a chosen lock-in period.
     * @param amount Amount of tokens to stake.
     * @param lockPeriod Lock-in period in seconds (e.g., 30 days, 60 days, etc.).
     */
    function stake(uint256 amount, uint256 lockPeriod) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(rewardRates[lockPeriod] > 0, "Invalid lock-in period");

        // Transfer staking tokens from the user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Check if user already has an active stake
        Stake storage userStake = stakes[msg.sender];
        require(
            block.timestamp >= userStake.lockUntil,
            "Existing stake is still locked"
        );

        // Update user's stake details
        userStake.amount = amount;
        userStake.lockUntil = block.timestamp + lockPeriod;
        userStake.rewardsEarned = 0;

        emit Staked(msg.sender, amount, userStake.lockUntil);
    }

    /**
     * @dev Calculate rewards for a given stake based on elapsed time.
     * @param user Address of the user whose rewards are being calculated.
     * @return Total rewards earned.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (block.timestamp < userStake.lockUntil) {
            return 0; // No rewards if stake is still locked
        }

        uint256 lockPeriod = userStake.lockUntil - (userStake.lockUntil - block.timestamp);
        uint256 rate = rewardRates[lockPeriod];
        uint256 elapsedTime = lockPeriod;
        return elapsedTime * rate;
    }

    /**
     * @dev Withdraw staked tokens and rewards after lock-in period ends.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(
            block.timestamp >= userStake.lockUntil,
            "Stake is still locked"
        );

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer staked amount and rewards to the user
        require(
            stakingToken.transfer(msg.sender, userStake.amount + rewards),
            "Token transfer failed"
        );

        // Reset user's stake
        userStake.amount = 0;
        userStake.lockUntil = 0;
        userStake.rewardsEarned = 0;

        emit Withdrawn(msg.sender, userStake.amount, rewards);
    }

    /**
     * @dev Fetch stake details for a user.
     * @param user Address of the user.
     * @return Stake details (amount, lockUntil, rewardsEarned).
     */
    function getStake(address user)
        external
        view
        returns (
            uint256 amount,
            uint256 lockUntil,
            uint256 rewardsEarned
        )
    {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.lockUntil, userStake.rewardsEarned);
    }
}

/**
 * @dev Minimal ERC20 interface for token interactions.
 */
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
