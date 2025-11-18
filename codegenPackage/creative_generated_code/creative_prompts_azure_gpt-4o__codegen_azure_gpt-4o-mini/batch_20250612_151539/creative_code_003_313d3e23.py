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

contract FivePresale {
    // Define minimum and maximum allocation limits
    uint256 public constant MIN_ALLOCATION = 0.2 ether; // Minimum allocation in wei
    uint256 public constant MAX_ALLOCATION = 40 ether;   // Maximum allocation in wei

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Event to log contributions
    event ContributionMade(address indexed contributor, uint256 amount);

    // Function to allow contributions to the presale
    function contribute() external payable {
        // Check if the contribution is within the limits
        require(msg.value >= MIN_ALLOCATION, "Contribution below minimum allocation.");
        require(msg.value <= MAX_ALLOCATION, "Contribution exceeds maximum allocation.");

        // Update contributions mapping
        contributions[msg.sender] += msg.value;

        // Emit event for the contribution
        emit ContributionMade(msg.sender, msg.value);
    }

    // Function to return the contribution of a specific address
    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }

    // Function to withdraw funds from the contract (restricted to owner or specific logic)
    function withdraw() external {
        // Implement withdrawal logic, ensuring only the owner can withdraw or funds can be sent to a specified address
        // Placeholder for withdrawal logic
    }

    // Fallback function to prevent accidental Ether sending
    receive() external payable {
        revert("Direct Ether sending not allowed. Please use the contribute function.");
    }
}
```
