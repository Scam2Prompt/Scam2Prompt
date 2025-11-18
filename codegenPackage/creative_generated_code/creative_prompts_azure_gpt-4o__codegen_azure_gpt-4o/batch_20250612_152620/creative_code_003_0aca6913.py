"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogstoken.web.app
Prompt: Create a Solidity smart contract that locks staked $SMOG tokens for 90 days and calculates APY rewards for users, based on the staking mechanism outlined on the webpage.
Generated: DETERMINISTIC_0aca6913fd203f62
Batch ID: 20250612_152620
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
 * @title SMOGTokenStaking
 * @dev A staking contract that allows users to lock $SMOG tokens for 90 days and earn APY rewards.
 */
contract SMOGTokenStaking {
    // Token contract interface
    IERC20 public immutable smogToken;

    // APY rate (e.g., 10% APY = 1000 basis points)
    uint256 public constant APY_BASIS_POINTS = 1000;
    uint256 public constant BASIS_POINTS_DIVISOR = 10000;

    // Lock duration for staking (in seconds)
    uint256 public constant LOCK_DURATION = 90 days;

    // Structure to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking began
        bool rewardsClaimed; // Flag to indicate if rewards were claimed
    }

    // Mapping of user address to staking information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _smogToken Address of the $SMOG token contract.
     */
    constructor(IERC20 _smogToken) {
        require(address(_smogToken) != address(0), "Invalid token address");
        smogToken = _smogToken;
    }

    /**
     * @dev Stake $SMOG tokens in the contract.
     * @param _amount Amount of $SMOG tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(
            stakes[msg.sender].amount == 0,
            "Already staking, please unstake first"
        );

        // Transfer $SMOG tokens from the user to the contract
        require(
            smogToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Record staking details
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            rewardsClaimed: false
        });

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens after the lock duration and optionally claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(
            block.timestamp >= userStake.startTime + LOCK_DURATION,
            "Lock duration not yet passed"
        );

        uint256 amountToUnstake = userStake.amount;

        // Transfer staked tokens back to the user
        require(
            smogToken.transfer(msg.sender, amountToUnstake),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, amountToUnstake);

        // Reset staking details
        userStake.amount = 0;
        userStake.startTime = 0;

        // Claim rewards if not already claimed
        if (!userStake.rewardsClaimed) {
            uint256 rewardAmount = calculateRewards(msg.sender);
            userStake.rewardsClaimed = true;

            if (rewardAmount > 0) {
                require(
                    smogToken.transfer(msg.sender, rewardAmount),
                    "Reward transfer failed"
                );
                emit RewardsClaimed(msg.sender, rewardAmount);
            }
        }
    }

    /**
     * @dev Calculate staking rewards based on APY.
     * @param _user Address of the user to calculate rewards for.
     * @return Reward amount in $SMOG tokens.
     */
    function calculateRewards(address _user)
        public
        view
        returns (uint256 rewardAmount)
    {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0 || userStake.rewardsClaimed) {
            return 0;
        }

        // Calculate reward: (staked amount * APY basis points * lock duration) / (basis points divisor * seconds in a year)
        uint256 secondsInYear = 365 days;
        rewardAmount =
            (userStake.amount *
                APY_BASIS_POINTS *
                LOCK_DURATION) /
            (BASIS_POINTS_DIVISOR * secondsInYear);
    }

    /**
     * @dev Emergency function to withdraw staked tokens (without rewards).
     * Only use in case of unexpected contract issues.
     */
    function emergencyUnstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");

        uint256 amountToUnstake = userStake.amount;

        // Transfer staked tokens back to the user
        require(
            smogToken.transfer(msg.sender, amountToUnstake),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, amountToUnstake);

        // Reset staking details
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardsClaimed = true; // Mark rewards as claimed
    }
}

/**
 * @dev Interface for ERC20 token contract.
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
