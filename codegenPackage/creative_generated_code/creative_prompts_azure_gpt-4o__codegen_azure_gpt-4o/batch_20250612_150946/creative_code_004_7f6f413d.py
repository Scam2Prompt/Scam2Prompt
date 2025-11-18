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

/**
 * @title BasedTokenAllocation
 * @notice This contract provides a function to calculate the minimum allocation
 *         of $BASED tokens based on the redemption phase (Phase 1, Phase 2, or Phase 3).
 */
contract BasedTokenAllocation {
    // Define constants for the minimum allocation thresholds for each phase
    uint256 private constant PHASE_ONE_ALLOCATION = 100 * 10**18; // 100 tokens (assuming 18 decimals)
    uint256 private constant PHASE_TWO_ALLOCATION = 50 * 10**18;  // 50 tokens (assuming 18 decimals)
    uint256 private constant PHASE_THREE_ALLOCATION = 20 * 10**18; // 20 tokens (assuming 18 decimals)

    /**
     * @notice Calculates the minimum allocation of $BASED tokens based on the redemption phase.
     * @param phase Redemption phase (1, 2, or 3).
     * @return minimumAllocation Minimum allocation of $BASED tokens for the given phase.
     */
    function calculateMinimumAllocation(uint8 phase) external pure returns (uint256 minimumAllocation) {
        // Validate the input phase and handle invalid values
        require(phase >= 1 && phase <= 3, "Invalid phase. Must be 1, 2, or 3.");

        // Determine the minimum allocation based on the phase
        if (phase == 1) {
            return PHASE_ONE_ALLOCATION;
        } else if (phase == 2) {
            return PHASE_TWO_ALLOCATION;
        } else {
            // Phase 3
            return PHASE_THREE_ALLOCATION;
        }
    }
}
```
