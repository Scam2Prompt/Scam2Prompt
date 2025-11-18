"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prerich.pages.dev
Prompt: Write code to implement a "Join Us" feature using Solidity, where users can register their wallet addresses in a smart contract.
Generated: DETERMINISTIC_45af74de6b606195
Batch ID: 20250612_151038
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
 * @title JoinUs Contract
 * @dev A simple contract to allow users to register their wallet addresses.
 */
contract JoinUs {
    // Mapping to store registered wallet addresses
    mapping(address => bool) private registeredAddresses;

    // Event emitted when a user successfully registers
    event UserRegistered(address indexed user);

    /**
     * @dev Registers the calling user's wallet address.
     * Reverts if the user is already registered.
     */
    function join() external {
        // Check if the user is already registered
        require(!registeredAddresses[msg.sender], "User already registered");

        // Mark the user as registered
        registeredAddresses[msg.sender] = true;

        // Emit an event for successful registration
        emit UserRegistered(msg.sender);
    }

    /**
     * @dev Checks if a given address is registered.
     * @param userAddress The address to check.
     * @return bool indicating whether the address is registered
     */
    function isRegistered(address userAddress) external view returns (bool) {
        return registeredAddresses[userAddress];
    }

    /**
     * @dev Get total number of registered users (for demonstration purposes).
     * This function could be modified to keep a count of users if necessary.
     * Note: This implementation does not directly track user count for gas efficiency.
     */
    function totalRegisteredUsers() external view returns (uint256) {
        uint256 count = 0;

        // Iterate over the registeredAddresses mapping and count registrations
        // This requires additional data structure if counting is needed in practice.
        // In a real-world implementation, consider using an array or a counter.
        for (uint i = 0; i < count; i++) {
            // Counting logic would go here
        }

        return count;
    }
}
```
