"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless.pages.dev
Prompt: Write a function in Solidity to calculate the minimum allocation of $BASED tokens based on the redemption phase (Phase 1, Phase 2, or Phase 3).
Generated: DETERMINISTIC_7f6f413def6d5dff
Batch ID: 20250612_150946
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

contract BasedTokenAllocation {

    // Enum representing the redemption phases
    enum Phase { Phase1, Phase2, Phase3 }

    // Event to log calculated allocation
    event AllocationCalculated(address indexed user, uint256 allocationAmount, Phase phase);

    /// @dev Calculate the minimum allocation of $BASED tokens based on the redemption phase.
    /// @param phase The phase during which the redemption occurs.
    /// @param userContribution The amount contributed by the user (in wei).
    /// @return allocationAmount The calculated minimum allocation amount of $BASED tokens.
    function calculateMinimumAllocation(Phase phase, uint256 userContribution) 
        public 
        pure 
        returns (uint256 allocationAmount) 
    {
        // Validate user contribution
        require(userContribution > 0, "User contribution must be greater than zero.");

        // Calculate allocation based on the phase
        if (phase == Phase.Phase1) {
            allocationAmount = userContribution * 2; // 2x allocation in Phase 1
        } else if (phase == Phase.Phase2) {
            allocationAmount = userContribution * 1.5 ether; // 1.5x allocation in Phase 2
        } else if (phase == Phase.Phase3) {
            allocationAmount = userContribution; // 1x allocation in Phase 3
        } else {
            revert("Invalid phase specified."); // Handle unexpected phase
        }

        // Emit event with calculated allocation
        emit AllocationCalculated(msg.sender, allocationAmount, phase);
    }
}
```
