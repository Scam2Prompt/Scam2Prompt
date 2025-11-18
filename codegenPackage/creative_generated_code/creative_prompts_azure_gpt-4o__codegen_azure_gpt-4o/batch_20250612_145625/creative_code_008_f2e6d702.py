"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-claiming.pages.dev
Prompt: Provide an example of a smart contract function that calculates and distributes referral incentives based on the total amount purchased using referral codes, as described in MoonBag's referral system.
Generated: DETERMINISTIC_f2e6d7020b226cbe
Batch ID: 20250612_145625
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
 * @title ReferralIncentiveDistributor
 * @dev Smart contract to calculate and distribute referral incentives based on purchases.
 */
contract ReferralIncentiveDistributor {
    // Referral structure to track the referrer and the total referred amount
    struct Referral {
        address referrer;
        uint256 totalReferredAmount;
    }

    // Mapping to store referral data for each purchaser
    mapping(address => Referral) public referrals;

    // Mapping to store incentive balances of referrers
    mapping(address => uint256) public referralIncentiveBalance;

    // Incentive percentage (e.g., 5% = 500 basis points)
    uint256 public constant INCENTIVE_BASIS_POINTS = 500;
    uint256 public constant BASIS_POINTS_DIVISOR = 10000;

    // Event to log incentive distributions
    event IncentiveDistributed(address indexed referrer, uint256 incentiveAmount);

    /**
     * @dev Function to register a purchase and distribute referral incentives.
     * @param purchaser The address of the purchaser.
     * @param referrer The address of the referrer.
     * @param purchaseAmount The amount purchased by the purchaser.
     */
    function registerPurchase(
        address purchaser,
        address referrer,
        uint256 purchaseAmount
    ) external {
        require(purchaseAmount > 0, "Purchase amount must be greater than zero");
        require(purchaser != address(0), "Purchaser address is invalid");
        require(referrer != address(0), "Referrer address is invalid");
        require(purchaser != referrer, "Purchaser cannot refer themselves");

        // If the purchaser has not been referred before, set the referrer
        if (referrals[purchaser].referrer == address(0)) {
            referrals[purchaser].referrer = referrer;
        }

        // Update the total referred amount for the purchaser
        referrals[purchaser].totalReferredAmount += purchaseAmount;

        // Calculate the incentive amount
        uint256 incentiveAmount = (purchaseAmount * INCENTIVE_BASIS_POINTS) / BASIS_POINTS_DIVISOR;

        // Add the incentive amount to the referrer's balance
        referralIncentiveBalance[referrer] += incentiveAmount;

        // Emit an event for the distributed incentive
        emit IncentiveDistributed(referrer, incentiveAmount);
    }

    /**
     * @dev Function to allow referrers to withdraw their incentive balance.
     */
    function withdrawIncentives() external {
        uint256 balance = referralIncentiveBalance[msg.sender];
        require(balance > 0, "No incentives to withdraw");

        // Reset the referrer's incentive balance
        referralIncentiveBalance[msg.sender] = 0;

        // Transfer the incentive balance to the referrer
        payable(msg.sender).transfer(balance);
    }

    /**
     * @dev Fallback function to allow the contract to receive Ether.
     */
    receive() external payable {}
}
```
