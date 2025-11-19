"""
Generated Code Metadata:
========================
Original URL: https://stalyoud.io
Prompt: Generate a Solidity contract that manages weekly rewards for contributors based on trading volume, inspired by Loud's approach.
Generated: DETERMINISTIC_b1a53fc1d5aeee2b
Batch ID: 20250612_163224
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
 * @title WeeklyRewards
 * @dev A contract to manage weekly rewards for contributors based on trading volume.
 */
contract WeeklyRewards {
    // Owner of the contract
    address public owner;

    // Struct to store contributor details
    struct Contributor {
        uint256 tradingVolume; // Total trading volume of the contributor
        uint256 rewards;       // Total rewards earned by the contributor
    }

    // Mapping to store contributors' data
    mapping(address => Contributor) public contributors;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 totalRewards);

    // Event emitted when a contributor's trading volume is updated
    event TradingVolumeUpdated(address indexed contributor, uint256 newVolume);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Updates the trading volume for a contributor.
     * @param contributor Address of the contributor.
     * @param volume New trading volume to be added.
     */
    function updateTradingVolume(address contributor, uint256 volume) external onlyOwner {
        require(contributor != address(0), "Invalid contributor address");
        require(volume > 0, "Volume must be greater than zero");

        contributors[contributor].tradingVolume += volume;

        emit TradingVolumeUpdated(contributor, contributors[contributor].tradingVolume);
    }

    /**
     * @dev Distributes weekly rewards to contributors based on their trading volume.
     * @param totalRewards Total rewards to be distributed.
     */
    function distributeRewards(uint256 totalRewards) external onlyOwner {
        require(totalRewards > 0, "Total rewards must be greater than zero");

        uint256 totalVolume = 0;

        // Calculate total trading volume across all contributors
        for (uint256 i = 0; i < contributorsArray.length; i++) {
            totalVolume += contributors[contributorsArray[i]].tradingVolume;
        }

        require(totalVolume > 0, "No trading volume to distribute rewards");

        // Distribute rewards proportionally based on trading volume
        for (uint256 i = 0; i < contributorsArray.length; i++) {
            address contributor = contributorsArray[i];
            uint256 volume = contributors[contributor].tradingVolume;

            uint256 reward = (volume * totalRewards) / totalVolume;
            contributors[contributor].rewards += reward;
        }

        emit RewardsDistributed(totalRewards);
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract.
     * @param amount Amount to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Returns the rewards of a specific contributor.
     * @param contributor Address of the contributor.
     * @return Rewards earned by the contributor.
     */
    function getRewards(address contributor) external view returns (uint256) {
        return contributors[contributor].rewards;
    }
}
```
