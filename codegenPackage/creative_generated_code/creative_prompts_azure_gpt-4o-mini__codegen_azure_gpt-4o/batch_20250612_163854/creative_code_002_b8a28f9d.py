"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venusutils.vercel.app
Prompt: What are the steps to implement bad debt calculations using Venus Utils in a smart contract?
Generated: DETERMINISTIC_b8a28f9df30782ba
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation of a smart contract for calculating bad debt using Venus Utils in Solidity.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import interfaces and libraries for Venus Utils (assume they are available)
import "@venusprotocol/contracts/utils/VenusUtils.sol"; // Hypothetical import for Venus Utils
import "@openzeppelin/contracts/access/Ownable.sol"; // OpenZeppelin Ownable for access control

/**
 * @title BadDebtCalculator
 * @dev A contract for calculating bad debt using Venus Utils
 */
contract BadDebtCalculator is Ownable {
    // Venus Protocol utility instance
    VenusUtils private venusUtils;

    // Event emitted when bad debt is calculated
    event BadDebtCalculated(address indexed user, uint256 badDebtAmount);

    /**
     * @dev Constructor to initialize Venus Utils instance
     * @param _venusUtilsAddress Address of the Venus Utils contract
     */
    constructor(address _venusUtilsAddress) {
        require(_venusUtilsAddress != address(0), "Invalid Venus Utils address");
        venusUtils = VenusUtils(_venusUtilsAddress);
    }

    /**
     * @dev Function to calculate bad debt for a given user
     * @param user Address of the user to calculate bad debt for
     * @return badDebtAmount Amount of bad debt for the user
     */
    function calculateBadDebt(address user) external view returns (uint256 badDebtAmount) {
        require(user != address(0), "Invalid user address");

        // Fetch account balances and liquidity data using Venus Utils
        (uint256 collateralValue, uint256 borrowValue) = venusUtils.getAccountLiquidity(user);

        // If borrowValue exceeds collateralValue, calculate bad debt
        if (borrowValue > collateralValue) {
            badDebtAmount = borrowValue - collateralValue;
        } else {
            badDebtAmount = 0; // No bad debt
        }

        return badDebtAmount;
    }

    /**
     * @dev Admin function to trigger bad debt calculation and emit event
     * @param user Address of the user to calculate bad debt for
     */
    function triggerBadDebtCalculation(address user) external onlyOwner {
        uint256 badDebtAmount = calculateBadDebt(user);

        // Emit event with the result
        emit BadDebtCalculated(user, badDebtAmount);
    }
}
```

### Notes in Code:
- Assumes the existence of a `VenusUtils` library or contract that provides a `getAccountLiquidity` function. Replace imports with actual Venus Protocol contracts accordingly.
- Includes proper error handling for invalid addresses.
- Uses OpenZeppelin's `Ownable` for role-based access control on administrative functions.
- Emits events for tracking bad debt calculations, providing transparency and auditability.
- Follows Solidity best practices for security and readability.
