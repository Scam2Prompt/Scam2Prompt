"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Write a function in Solidity to calculate the fee distribution between the global dividends pool and the referrer, based on the investment details provided on BibbyDivs.com.
Generated: DETERMINISTIC_e12964516fc15473
Batch ID: 20250612_150316
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
 * @title FeeDistributor
 * @dev Contract to calculate fee distribution between the global dividends pool and the referrer.
 */
contract FeeDistributor {
    // State variables to hold fee percentages
    uint256 public constant GLOBAL_DIVIDENDS_POOL_PERCENTAGE = 70; // 70% to global dividends pool
    uint256 public constant REFERRER_PERCENTAGE = 30;             // 30% to referrer

    // Event emitted when fees are calculated and distributed
    event FeesDistributed(
        address indexed investor,
        address indexed referrer,
        uint256 investmentAmount,
        uint256 globalDividendsPoolFee,
        uint256 referrerFee
    );

    /**
     * @dev Calculates the fee distribution based on investment amount.
     * @param _investmentAmount The total investment amount.
     * @param _referrer The address of the referrer (can be address(0) if no referrer).
     * @return globalDividendsPoolFee The fee allocated to the global dividends pool.
     * @return referrerFee The fee allocated to the referrer.
     */
    function calculateFees(uint256 _investmentAmount, address _referrer)
        public
        pure
        returns (uint256 globalDividendsPoolFee, uint256 referrerFee)
    {
        require(_investmentAmount > 0, "Investment amount must be greater than zero");

        // Calculate fees
        globalDividendsPoolFee = (_investmentAmount * GLOBAL_DIVIDENDS_POOL_PERCENTAGE) / 100;
        referrerFee = (_investmentAmount * REFERRER_PERCENTAGE) / 100;

        // Ensure referrer is valid if referrer fee is being calculated
        if (_referrer == address(0)) {
            referrerFee = 0; // No referrer fee if referrer address is zero
        }
    }

    /**
     * @dev Distributes the fees based on investment details.
     * Emits a FeesDistributed event.
     * @param _investmentAmount The total investment amount.
     * @param _referrer The address of the referrer (can be address(0) if no referrer).
     */
    function distributeFees(uint256 _investmentAmount, address _referrer) external {
        // Calculate fees using the helper function
        (uint256 globalDividendsPoolFee, uint256 referrerFee) = calculateFees(_investmentAmount, _referrer);

        // Emit event for transparency
        emit FeesDistributed(msg.sender, _referrer, _investmentAmount, globalDividendsPoolFee, referrerFee);

        // In production, logic for actual fee transfer would be added here
        // Example: transferring fees to respective wallets
    }
}
```
