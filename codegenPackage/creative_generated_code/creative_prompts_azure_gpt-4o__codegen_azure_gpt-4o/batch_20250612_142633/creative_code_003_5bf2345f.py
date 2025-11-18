"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jh1.xuexi02.top
Prompt: Write a smart contract that implements the energy reset mechanism described on the NAKA-Miner platform, where energy resets to 1400 daily and is consumed during aggregation tasks.
Generated: DETERMINISTIC_5bf2345fa404f61c
Batch ID: 20250612_142633
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
 * @title NAKA-Miner Energy Management Smart Contract
 * @dev Implements an energy reset and consumption mechanism for a platform
 * where each user has an energy balance that resets daily to 1400
 * and is used (consumed) during aggregation tasks.
 */
contract NakaMinerEnergy {
    // Energy constants
    uint256 public constant DAILY_ENERGY = 1400;

    // Struct to track user energy and last reset timestamp
    struct User {
        uint256 energy;
        uint256 lastReset; // Timestamp of the last reset
    }

    // Mapping of user address to their energy data
    mapping(address => User) private users;

    // Event to log energy consumption
    event EnergyConsumed(address indexed user, uint256 amount, uint256 remainingEnergy);

    // Event to log energy reset
    event EnergyReset(address indexed user, uint256 newEnergy);

    /**
     * @notice Consumes energy for a user performing an aggregation task.
     * @param _amount The amount of energy to consume.
     */
    function consumeEnergy(uint256 _amount) external {
        require(_amount > 0, "Energy amount must be greater than zero.");

        // Ensure the user's energy is reset before consumption
        resetEnergyIfNeeded(msg.sender);

        // Check if the user has enough energy
        require(users[msg.sender].energy >= _amount, "Insufficient energy.");

        // Deduct the energy
        users[msg.sender].energy -= _amount;

        // Emit event
        emit EnergyConsumed(msg.sender, _amount, users[msg.sender].energy);
    }

    /**
     * @notice Gets the current energy of the given user.
     * @param _user The address of the user.
     * @return The current energy balance of the user.
     */
    function getEnergy(address _user) external view returns (uint256) {
        // Calculate energy, accounting for automatic resets
        uint256 energy = users[_user].energy;

        if (block.timestamp >= startOfNextDay(users[_user].lastReset)) {
            energy = DAILY_ENERGY;
        }

        return energy;
    }

    /**
     * @notice Resets the user's energy to the daily maximum if the reset period has passed.
     * @param _user The address of the user to reset energy for.
     */
    function resetEnergyIfNeeded(address _user) internal {
        // Check if the user's energy needs to be reset
        if (block.timestamp >= startOfNextDay(users[_user].lastReset)) {
            // Reset energy to the daily maximum
            users[_user].energy = DAILY_ENERGY;
            users[_user].lastReset = block.timestamp;

            // Emit event
            emit EnergyReset(_user, DAILY_ENERGY);
        }
    }

    /**
     * @notice Calculates the start of the next day (UTC) given a timestamp.
     * @param _timestamp The current timestamp.
     * @return The timestamp for the start of the next day (UTC).
     */
    function startOfNextDay(uint256 _timestamp) public pure returns (uint256) {
        // 1 day = 86400 seconds
        return ((_timestamp / 86400) + 1) * 86400;
    }

    /**
     * @notice Initializes a user's energy if they are interacting with the platform for the first time.
     */
    function initializeUserEnergy() external {
        // If the user is interacting for the first time, initialize their energy and last reset time
        if (users[msg.sender].lastReset == 0) {
            users[msg.sender] = User(DAILY_ENERGY, block.timestamp);
        }
    }
}
```
