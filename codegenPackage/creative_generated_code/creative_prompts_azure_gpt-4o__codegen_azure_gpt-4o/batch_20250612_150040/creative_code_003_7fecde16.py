"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Write a function in Solidity to validate the pricing logic for `.linea` domains based on the name length (3, 4, or 5+ characters) and duration, as described on the Linea domains website.
Generated: DETERMINISTIC_7fecde16b301a635
Batch ID: 20250612_150040
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
 * @title LineaDomainPricing
 * @dev This contract provides pricing validation logic for `.linea` domains.
 * Pricing is determined based on the domain name length and the registration duration.
 */
contract LineaDomainPricing {
    // Define pricing tiers per year in wei (example values, adjust as needed)
    uint256 public constant PRICE_3_CHAR = 1 ether; // Price for 3-character domains per year
    uint256 public constant PRICE_4_CHAR = 0.5 ether; // Price for 4-character domains per year
    uint256 public constant PRICE_5_PLUS_CHAR = 0.1 ether; // Price for 5+ character domains per year

    /**
     * @dev Validates the pricing logic for a `.linea` domain based on name length and duration.
     * @param name The domain name to validate.
     * @param duration The registration duration in years.
     * @param paymentAmount The amount of payment sent (in wei).
     * @return isValid True if the payment matches the expected price, otherwise false.
     * @return expectedPrice The expected price for the domain registration.
     */
    function validatePricing(string memory name, uint256 duration, uint256 paymentAmount)
        public
        pure
        returns (bool isValid, uint256 expectedPrice)
    {
        require(duration > 0, "Duration must be greater than 0 years");

        uint256 nameLength = bytes(name).length; // Get the length of the name
        require(nameLength >= 3, "Name length must be at least 3 characters");

        // Determine the price per year based on name length
        uint256 pricePerYear;
        if (nameLength == 3) {
            pricePerYear = PRICE_3_CHAR;
        } else if (nameLength == 4) {
            pricePerYear = PRICE_4_CHAR;
        } else {
            pricePerYear = PRICE_5_PLUS_CHAR;
        }

        // Calculate the expected price for the given duration
        expectedPrice = pricePerYear * duration;

        // Validate the payment amount
        isValid = (paymentAmount == expectedPrice);

        return (isValid, expectedPrice);
    }
}
```
