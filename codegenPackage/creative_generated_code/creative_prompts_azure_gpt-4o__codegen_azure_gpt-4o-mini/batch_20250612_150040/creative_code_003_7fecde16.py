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

contract LineaDomainPricing {

    // Enum to represent the allowed name lengths
    enum NameLength { Short, Medium, Long }
    
    // Struct to hold pricing information
    struct Pricing {
        uint256 shortPrice;  // Price for 3-character domains
        uint256 mediumPrice; // Price for 4-character domains
        uint256 longPrice;   // Price for 5+ character domains
    }

    // Mapping to store pricing based on the duration in years
    mapping(uint256 => Pricing) public pricingByDuration;

    // Event to log the price validation
    event PriceValidated(address indexed requester, uint256 price);

    // Constructor to initialize pricing for different durations
    constructor() {
        // Example pricing setup: Yearly price can be adjusted as needed
        pricingByDuration[1] = Pricing(10 ether, 20 ether, 30 ether); // Prices for 1 year
        pricingByDuration[2] = Pricing(18 ether, 35 ether, 50 ether); // Prices for 2 years
        pricingByDuration[5] = Pricing(45 ether, 80 ether, 120 ether); // Prices for 5 years
    }

    // Function to validate pricing logic based on name length and duration
    function validatePricing(string memory domainName, uint256 duration) public view returns (uint256) {
        // Check if duration is valid
        require(duration == 1 || duration == 2 || duration == 5, "Invalid duration. Valid options: 1, 2, 5 years.");

        // Determine the length of the domain name
        uint256 nameLength = bytes(domainName).length;
        require(nameLength >= 3, "Domain name must be at least 3 characters long.");

        // Get the pricing for the specified duration
        Pricing memory pricing = pricingByDuration[duration];

        // Determine the price based on name length
        uint256 price;
        if (nameLength == 3) {
            price = pricing.shortPrice;
        } else if (nameLength == 4) {
            price = pricing.mediumPrice;
        } else {
            price = pricing.longPrice; // For names 5 characters or longer
        }

        emit PriceValidated(msg.sender, price); // Log the price validation
        return price; // Return the determined price
    }
}
```
