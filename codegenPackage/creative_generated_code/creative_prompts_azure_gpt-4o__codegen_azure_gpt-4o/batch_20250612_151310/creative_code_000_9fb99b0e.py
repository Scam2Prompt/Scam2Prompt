"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubatewhitelist.pages.dev
Prompt: Write a smart contract in Solidity that integrates a wallet connection feature similar to the one described on Decubate's whitelist portal. Ensure the contract supports staking functionality and calculates rewards based on APY and lock terms.
Generated: DETERMINISTIC_9fb99b0e1f7cc0e2
Batch ID: 20250612_151310
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
 * @dev A smart contract for staking tokens, calculating rewards based on APY, and supporting wallet connections.
 */
contract StakingContract {
    // Token address for staking
    address public stakingToken;

    // APY (Annual Percentage Yield) in basis points (e.g., 500 = 5.00%)
    uint256 public apy;

    // Struct to store stake details
    struct Stake {
        uint256 amount;       // Stake amount
        uint256 startTime;    // Time when staking started
        uint256 lockDuration; // Lock duration in seconds
        bool active;          // Stake status
    }

    // Mapping of user address to their stake details
    mapping(address => Stake) public stakes;

    // Events
    event StakeCreated(address indexed user, uint256 amount, uint256 lockDuration);
    event StakeWithdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the token to be staked.
     * @param _apy Annual Percentage Yield in basis points.
     */
    constructor(address _stakingToken, uint256 _apy) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_apy > 0, "APY must be greater than zero");

        stakingToken = _stakingToken;
        apy = _apy;
    }

    /**
     * @dev Modifier to check if the user has an active stake.
     */
    modifier hasActiveStake() {
        require(stakes[msg.sender].active, "No active stake found");
        _;
    }

    /**
     * @dev Function for users to create a stake.
     * @param _amount Amount of tokens to stake.
     * @param _lockDuration Lock duration in seconds.
     */
    function createStake(uint256 _amount, uint256 _lockDuration) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(_lockDuration > 0, "Lock duration must be greater than zero");

        // Transfer staking tokens from the user to the contract
        require(
            IERC20(stakingToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Create a new stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            lockDuration: _lockDuration,
            active: true
        });

        emit StakeCreated(msg.sender, _amount, _lockDuration);
    }

    /**
     * @dev Function to withdraw user's stake along with rewards.
     */
    function withdrawStake() external hasActiveStake {
        Stake memory userStake = stakes[msg.sender];
        
        // Check if the lock duration has passed
        require(
            block.timestamp >= userStake.startTime + userStake.lockDuration,
            "Stake is still locked"
        );

        // Calculate rewards based on APY
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = calculateReward(userStake.amount, stakingDuration);

        // Reset user's stake
        stakes[msg.sender].active = false;

        // Transfer staked amount and reward back to the user
        require(
            IERC20(stakingToken).transfer(msg.sender, userStake.amount + reward),
            "Token transfer failed"
        );

        emit StakeWithdrawn(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Private function to calculate staking rewards.
     * @param _amount Amount staked.
     * @param _duration Duration of staking in seconds.
     * @return Reward amount.
     */
    function calculateReward(uint256 _amount, uint256 _duration) private view returns (uint256) {
        // APY calculation: reward = (amount * apy * duration) / (100 * 365 * 24 * 60 * 60)
        return (_amount * apy * _duration) / (100 * 365 * 24 * 60 * 60);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
