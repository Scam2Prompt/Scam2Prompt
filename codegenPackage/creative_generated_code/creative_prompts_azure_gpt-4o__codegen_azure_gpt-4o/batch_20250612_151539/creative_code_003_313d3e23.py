"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5ire.live
Prompt: Write a smart contract snippet to enforce the minimum (0.2 ETH) and maximum (40 ETH) allocation limits for the 5ire presale.
Generated: DETERMINISTIC_313d3e23296a372a
Batch ID: 20250612_151539
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
 * @title 5irePresale
 * @dev This contract enforces minimum and maximum allocation limits for a presale.
 */
contract 5irePresale {
    // Minimum and maximum contribution limits in Wei (1 ETH = 10^18 Wei)
    uint256 public constant MIN_ALLOCATION = 0.2 ether;
    uint256 public constant MAX_ALLOCATION = 40 ether;

    // Mapping to track contributions of each address
    mapping(address => uint256) public contributions;

    // Event emitted when a contribution is successful
    event ContributionReceived(address indexed contributor, uint256 amount);

    /**
     * @dev Allows users to contribute to the presale while enforcing allocation limits.
     */
    function contribute() external payable {
        // Ensure the sent value is within the allowed range
        require(msg.value >= MIN_ALLOCATION, "Contribution below minimum limit");
        require(msg.value <= MAX_ALLOCATION, "Contribution exceeds maximum limit");

        // Ensure total contributions by the sender don't exceed the maximum allowed
        uint256 newContribution = contributions[msg.sender] + msg.value;
        require(newContribution <= MAX_ALLOCATION, "Total contributions exceed maximum limit");

        // Update the contributions for the sender
        contributions[msg.sender] = newContribution;

        // Emit the event to log the contribution
        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Owner can reclaim funds after the presale ends (function not implemented here).
     * This should be implemented with access control.
     */
}
```
