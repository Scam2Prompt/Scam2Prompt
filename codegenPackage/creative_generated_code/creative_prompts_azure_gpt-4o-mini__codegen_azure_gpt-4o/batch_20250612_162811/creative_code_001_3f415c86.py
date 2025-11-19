"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-air-spring.nfts2.me
Prompt: Write a smart contract that tracks referrals and calculates earnings based on mints, inspired by the Zora Air Spring model.
Generated: DETERMINISTIC_3f415c8691e3d289
Batch ID: 20250612_162811
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
 * @title ReferralMintingContract
 * @dev This smart contract tracks referrals and calculates earnings based on minting activities.
 * Inspired by the Zora Air Spring model.
 */
contract ReferralMintingContract {
    // Struct to hold referrer data
    struct Referrer {
        uint256 totalReferrals; // Total number of referrals made
        uint256 earnings;       // Total earnings computed from referrals
    }

    // Mapping to track referrer data
    mapping(address => Referrer) public referrers;

    // Event emitted when a mint occurs
    event Minted(address indexed user, address indexed referrer, uint256 mintAmount, uint256 referrerEarnings);

    // Set the earnings percentage for referrals (e.g., 10%)
    uint256 public constant REFERRAL_PERCENTAGE = 10;

    /**
     * @dev Function to mint tokens with optional referral tracking.
     * @param referrer Address of the referrer (can be address(0) if no referrer).
     * @param mintAmount Amount of tokens being minted.
     */
    function mint(address referrer, uint256 mintAmount) external payable {
        require(mintAmount > 0, "Mint amount must be greater than zero");

        // Ensure referrer is not the same as the minting user
        require(referrer != msg.sender, "Referrer cannot be the minting user");

        // Handle referral logic if a referrer is provided
        if (referrer != address(0)) {
            // Calculate earnings for the referrer
            uint256 referrerEarnings = (mintAmount * REFERRAL_PERCENTAGE) / 100;

            // Update referrer data
            referrers[referrer].totalReferrals += 1;
            referrers[referrer].earnings += referrerEarnings;

            // Emit a mint event with referral information
            emit Minted(msg.sender, referrer, mintAmount, referrerEarnings);
        } else {
            // Emit a mint event without referral information
            emit Minted(msg.sender, address(0), mintAmount, 0);
        }

        // Logic to handle minting (e.g., transfer tokens, update balances) would go here.
        // This example assumes minting logic is handled externally or in conjunction with another contract.
    }

    /**
     * @dev Function to retrieve the referrer details.
     * @param referrer Address of the referrer.
     * @return totalReferrals Total number of referrals made by the referrer.
     * @return earnings Total earnings of the referrer.
     */
    function getReferrerDetails(address referrer) external view returns (uint256 totalReferrals, uint256 earnings) {
        Referrer memory data = referrers[referrer];
        return (data.totalReferrals, data.earnings);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
