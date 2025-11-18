"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nibiruairdrop.pages.dev
Prompt: Using Nibiru Chain's whitepaper, create a smart contract for farming NIBI points based on user engagement metrics.
Generated: DETERMINISTIC_9cc19224d65c2c74
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented example of a farming smart contract for NIBI points using Solidity. This assumes Nibiru Chain is compatible with EVM (Ethereum Virtual Machine).

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NIBI Points Farming Contract
 * @dev This contract allows users to farm NIBI points based on engagement metrics.
 * Engagement metrics can include likes, shares, comments, or custom-defined actions.
 */
contract NibiFarming {

    // Owner of the contract
    address public owner;

    // Mapping to track user engagement points
    mapping(address => uint256) public userPoints;

    // Mapping to track if an address is allowed to allocate points (e.g., trusted dApps)
    mapping(address => bool) public allocators;

    // Events
    event PointsAllocated(address indexed user, uint256 points);
    event AllocatorAdded(address indexed allocator);
    event AllocatorRemoved(address indexed allocator);

    /**
     * @dev Modifier to allow only the contract owner to perform certain actions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Modifier to allow only approved allocators to allocate points.
     */
    modifier onlyAllocator() {
        require(allocators[msg.sender], "Only approved allocators can allocate points");
        _;
    }

    /**
     * @dev Constructor to initialize the contract and set the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to allocate NIBI points to a user.
     * @param _user The address of the user receiving points.
     * @param _points The number of points to allocate.
     */
    function allocatePoints(address _user, uint256 _points) external onlyAllocator {
        require(_user != address(0), "Invalid user address");
        require(_points > 0, "Points must be greater than zero");

        // Add points to the user's balance
        userPoints[_user] += _points;

        // Emit event for tracking
        emit PointsAllocated(_user, _points);
    }

    /**
     * @dev Function for the owner to add an approved allocator.
     * @param _allocator The address of the allocator to approve.
     */
    function addAllocator(address _allocator) external onlyOwner {
        require(_allocator != address(0), "Invalid allocator address");
        require(!allocators[_allocator], "Allocator is already approved");

        allocators[_allocator] = true;

        // Emit event for tracking
        emit AllocatorAdded(_allocator);
    }

    /**
     * @dev Function for the owner to remove an approved allocator.
     * @param _allocator The address of the allocator to remove.
     */
    function removeAllocator(address _allocator) external onlyOwner {
        require(allocators[_allocator], "Allocator is not approved");

        allocators[_allocator] = false;

        // Emit event for tracking
        emit AllocatorRemoved(_allocator);
    }

    /**
     * @dev Function to retrieve the NIBI points balance of a user.
     * @param _user The address of the user.
     * @return The user's NIBI points balance.
     */
    function getPoints(address _user) external view returns (uint256) {
        return userPoints[_user];
    }
}
```

This is a minimal smart contract that meets the specifications of farming NIBI points based on engagement metrics. You may expand on this by integrating with the underlying mechanics of the Nibiru Chain or adding additional features, such as reward redemption mechanisms or point expiration logic.
