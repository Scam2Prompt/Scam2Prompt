"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dre-8x7.pages.dev
Prompt: Develop a Solidity function to prevent overselling during a presale by checking the total FTM contributed against the cap of 3,000,000 FTM.
Generated: DETERMINISTIC_427f01fe4c7bf7dd
Batch ID: 20250612_152710
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

contract Presale {
    // Maximum contribution cap in FTM
    uint256 public constant MAX_CAP = 3000000 * 1e18; // Using 18 decimals for FTM
    // Total contributions received
    uint256 public totalContributions;
    
    // Event to log contributions
    event ContributionReceived(address contributor, uint256 amount);

    // Modifier to check if the contribution exceeds the cap
    modifier belowCap(uint256 amount) {
        require(totalContributions + amount <= MAX_CAP, "Contribution exceeds the cap");
        _;
    }

    /// @notice Function to contribute FTM to the presale
    /// @dev This function can be called by users to contribute FTM
    function contribute() external payable belowCap(msg.value) {
        // Update the total contributions
        totalContributions += msg.value;

        // Emit an event for the contribution
        emit ContributionReceived(msg.sender, msg.value);
    }

    /// @notice Function to withdraw excess contributions in case of overselling
    /// @dev Allows the contract owner to withdraw excess funds if needed
    function withdrawExcess() external {
        // Logic to withdraw excess funds, if any
        // Placeholder for actual implementation, as this functionality is dependent on the contract's design
    }
    
    /// @notice Function to get the current total contributions
    /// @return The total contributions received
    function getTotalContributions() external view returns (uint256) {
        return totalContributions;
    }
}
```
