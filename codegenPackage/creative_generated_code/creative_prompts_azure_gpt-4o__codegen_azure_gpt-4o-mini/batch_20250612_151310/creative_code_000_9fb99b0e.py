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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking tokens with rewards based on APY and lock terms.
 */
contract StakingContract is Ownable {
    // Token to be staked
    IERC20 public stakingToken;

    // Struct to hold staking details
    struct Stake {
        uint256 amount;        // Amount staked
        uint256 startTime;     // Timestamp when the stake was created
        uint256 duration;      // Lock duration in seconds
        bool withdrawn;        // Status of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Annual Percentage Yield (APY) in basis points (e.g., 1000 = 10%)
    uint256 public apy;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to set the staking token and initial APY.
     * @param _stakingToken The address of the token to be staked.
     * @param _apy The annual percentage yield in basis points.
     */
    constructor(IERC20 _stakingToken, uint256 _apy) {
        stakingToken = _stakingToken;
        apy = _apy;
    }

    /**
     * @dev Staking function to stake tokens with a specified lock duration.
     * @param amount The amount of tokens to stake.
     * @param duration The lock duration in seconds.
     */
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        require(stakes[msg.sender].amount == 0, "Existing stake must be withdrawn");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakes[msg.sender] = Stake(amount, block.timestamp, duration, false);
        emit Staked(msg.sender, amount, duration);
    }

    /**
     * @dev Withdraw staked tokens along with rewards after the lock period.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(block.timestamp >= userStake.startTime + userStake.duration, "Stake is still locked");
        require(!userStake.withdrawn, "Stake already withdrawn");

        // Calculate rewards
        uint256 reward = calculateReward(userStake.amount, userStake.duration);
        userStake.withdrawn = true;

        // Transfer the staked amount and rewards to the user
        require(stakingToken.transfer(msg.sender, userStake.amount + reward), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, reward);

        // Reset the user's stake
        delete stakes[msg.sender];
    }

    /**
     * @dev Function to calculate the reward based on stake amount and duration.
     * @param amount The amount staked.
     * @param duration The duration of the stake.
     * @return The calculated reward.
     */
    function calculateReward(uint256 amount, uint256 duration) internal view returns (uint256) {
        // APY is annual, converting it to reward for the given duration
        uint256 reward = (amount * apy * duration) / (365 days * 10000); // Basis points
        return reward;
    }

    /**
     * @dev Function to update the APY of the staking contract. Only owner can call.
     * @param newApy The new APY in basis points.
     */
    function updateApy(uint256 newApy) external onlyOwner {
        apy = newApy;
    }
}
```
