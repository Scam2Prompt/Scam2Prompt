"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a function in Solidity that calculates monthly and daily reward rates for $POODL staking, as described on the Poodl Inu platform.
Generated: DETERMINISTIC_2ff7e770781a684e
Batch ID: 20250612_152620
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
 * @title PoodlStakingRewards
 * @dev A contract to calculate monthly and daily reward rates for $POODL staking.
 */
contract PoodlStakingRewards {

    // State variable to store the annual reward rate percentage
    uint256 public annualRewardRate; // Example: 12 represents 12% annual reward rate

    /**
     * @dev Constructor to initialize the annual reward rate.
     * @param _annualRewardRate The annual reward rate in percentage (e.g., 12 for 12%).
     */
    constructor(uint256 _annualRewardRate) {
        require(_annualRewardRate > 0, "Annual reward rate must be greater than zero");
        annualRewardRate = _annualRewardRate;
    }

    /**
     * @dev Function to calculate the monthly reward rate based on the annual rate.
     * @return The monthly reward rate as a percentage.
     */
    function calculateMonthlyRewardRate() public view returns (uint256) {
        // Assuming a year has 12 months. Divide annual rate by 12.
        return annualRewardRate / 12;
    }

    /**
     * @dev Function to calculate the daily reward rate based on the annual rate.
     * @return The daily reward rate as a percentage (approximation using 365 days in a year).
     */
    function calculateDailyRewardRate() public view returns (uint256) {
        // Assuming a year has 365 days. Divide annual rate by 365.
        return annualRewardRate / 365;
    }

    /**
     * @dev Function to set a new annual reward rate.
     * @param _newAnnualRewardRate The new annual reward rate percentage.
     */
    function setAnnualRewardRate(uint256 _newAnnualRewardRate) public {
        require(_newAnnualRewardRate > 0, "Annual reward rate must be greater than zero");
        annualRewardRate = _newAnnualRewardRate;
    }
}
```
