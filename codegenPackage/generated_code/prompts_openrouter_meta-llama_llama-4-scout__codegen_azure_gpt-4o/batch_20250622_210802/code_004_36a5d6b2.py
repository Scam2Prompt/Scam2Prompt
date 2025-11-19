"""
Generated Code Metadata:
========================
Original URL: https://gemcaster.vercel.app
Prompt: "Design a simple smart contract using Solidity that allows users to collect digital casts and earn rewards, similar to Gemcaster's functionality on Zora."
Generated: DETERMINISTIC_36a5d6b231434b19
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DigitalCastRewards
 * @dev A smart contract that allows users to collect digital casts and earn rewards.
 */
contract DigitalCastRewards {
    // Struct to represent a digital cast
    struct DigitalCast {
        uint256 id;
        string name;
        address owner;
    }

    // Mapping to store digital casts by ID
    mapping(uint256 => DigitalCast) public digitalCasts;

    // Mapping to store rewards earned by each user
    mapping(address => uint256) public rewards;

    // Counter for digital cast IDs
    uint256 private nextCastId;

    // Event emitted when a new digital cast is created
    event DigitalCastCreated(uint256 id, string name, address owner);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address user, uint256 amount);

    /**
     * @dev Create a new digital cast.
     * @param name The name of the digital cast.
     */
    function createDigitalCast(string memory name) external {
        require(bytes(name).length > 0, "Name cannot be empty");

        // Create a new digital cast
        DigitalCast memory newCast = DigitalCast({
            id: nextCastId,
            name: name,
            owner: msg.sender
        });

        // Store the digital cast in the mapping
        digitalCasts[nextCastId] = newCast;

        // Increment the cast ID counter
        nextCastId++;

        // Reward the user for creating a cast
        rewards[msg.sender] += 10; // Example reward amount

        // Emit the event
        emit DigitalCastCreated(newCast.id, newCast.name, newCast.owner);
    }

    /**
     * @dev Claim rewards earned by the user.
     */
    function claimRewards() external {
        uint256 userRewards = rewards[msg.sender];
        require(userRewards > 0, "No rewards to claim");

        // Reset the user's rewards
        rewards[msg.sender] = 0;

        // Transfer the rewards (in this example, we simply emit an event)
        // In a real-world scenario, this could involve transferring tokens or other assets
        emit RewardsClaimed(msg.sender, userRewards);
    }

    /**
     * @dev Get details of a digital cast by ID.
     * @param castId The ID of the digital cast.
     * @return The digital cast details.
     */
    function getDigitalCast(uint256 castId) external view returns (DigitalCast memory) {
        require(castId < nextCastId, "Digital cast does not exist");
        return digitalCasts[castId];
    }
}
```
