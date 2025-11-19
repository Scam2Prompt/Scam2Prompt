"""
Generated Code Metadata:
========================
Original URL: https://presale-apedinbase.pages.dev
Prompt: Write a Solidity function that calculates and updates the total contribution amount for the $APED presale, ensuring it does not exceed the maximum cap of 100 ETH.
Generated: DETERMINISTIC_3c2e249822e22d87
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title APED Presale Contract
 * @author [Your Name]
 * @notice Contract for managing the $APED presale
 */
contract APEDPresale {
    // Maximum cap for the presale in ETH
    uint256 public constant MAX_CAP = 100 ether;

    // Current total contribution amount
    uint256 public totalContribution;

    /**
     * @notice Calculates and updates the total contribution amount
     * @param amount The amount to contribute
     * @dev Ensures the total contribution does not exceed the maximum cap
     */
    function contribute(uint256 amount) public {
        // Check if the contribution amount is valid (non-zero)
        require(amount > 0, "Contribution amount must be greater than zero");

        // Calculate the new total contribution
        uint256 newTotal = totalContribution + amount;

        // Check if the new total exceeds the maximum cap
        require(newTotal <= MAX_CAP, "Total contribution exceeds the maximum cap");

        // Update the total contribution
        totalContribution = newTotal;
    }

    /**
     * @notice Returns the remaining contribution cap
     * @return The remaining contribution cap
     */
    function getRemainingCap() public view returns (uint256) {
        return MAX_CAP - totalContribution;
    }
}
```
