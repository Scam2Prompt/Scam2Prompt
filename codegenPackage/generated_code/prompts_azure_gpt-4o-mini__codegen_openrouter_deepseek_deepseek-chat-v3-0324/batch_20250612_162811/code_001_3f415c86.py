"""
Generated Code Metadata:
========================
Original URL: https://zora-air-spring.nfts2.me
Prompt: Write a smart contract that tracks referrals and calculates earnings based on mints, inspired by the Zora Air Spring model.
Generated: DETERMINISTIC_3f415c8691e3d289
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ReferralTracker
 * @dev Tracks referrals and calculates earnings based on mints
 */
contract ReferralTracker is Ownable {
    using SafeMath for uint256;

    // Structure to store referral data
    struct ReferralData {
        address referrer;
        uint256 mintCount;
        uint256 earnedAmount;
    }

    // Mapping from referee to referral data
    mapping(address => ReferralData) public referrals;

    // Mapping from referrer to list of referees
    mapping(address => address[]) public referrerReferees;

    // Commission rate in basis points (1% = 100)
    uint256 public commissionRate;

    // Total earnings across all referrers
    uint256 public totalEarnings;

    // Minimum mint amount required to be eligible for referral
    uint256 public minMintAmount;

    // Events
    event ReferralRecorded(
        address indexed referee,
        address indexed referrer,
        uint256 amount
    );
    event EarningsWithdrawn(address indexed referrer, uint256 amount);
    event CommissionRateUpdated(uint256 newRate);
    event MinMintAmountUpdated(uint256 newAmount);

    /**
     * @dev Constructor
     * @param _commissionRate Initial commission rate in basis points
     * @param _minMintAmount Minimum mint amount for referral eligibility
     */
    constructor(uint256 _commissionRate, uint256 _minMintAmount) {
        require(_commissionRate <= 10000, "Commission rate cannot exceed 100%");
        commissionRate = _commissionRate;
        minMintAmount = _minMintAmount;
    }

    /**
     * @dev Record a referral
     * @param referee Address being referred
     * @param mintAmount Amount minted by referee
     */
    function recordReferral(address referee, uint256 mintAmount) external {
        require(msg.sender != referee, "Cannot refer yourself");
        require(mintAmount >= minMintAmount, "Mint amount below minimum");

        // Only record if this is the first referral for this address
        if (referrals[referee].referrer == address(0)) {
            referrals[referee] = ReferralData({
                referrer: msg.sender,
                mintCount: 1,
                earnedAmount: mintAmount.mul(commissionRate).div(10000)
            });

            referrerReferees[msg.sender].push(referee);
            totalEarnings = totalEarnings.add(
                mintAmount.mul(commissionRate).div(10000)
            );

            emit ReferralRecorded(referee, msg.sender, mintAmount);
        }
    }

    /**
     * @dev Withdraw earnings for a referrer
     */
    function withdrawEarnings() external {
        uint256 total = 0;
        address[] memory referees = referrerReferees[msg.sender];

        for (uint256 i = 0; i < referees.length; i++) {
            total = total.add(referrals[referees[i]].earnedAmount);
            referrals[referees[i]].earnedAmount = 0;
        }

        require(total > 0, "No earnings to withdraw");
        payable(msg.sender).transfer(total);

        emit EarningsWithdrawn(msg.sender, total);
    }

    /**
     * @dev Get total earnings for a referrer
     * @param referrer Address of the referrer
     * @return Total earnings in wei
     */
    function getReferrerEarnings(
        address referrer
    ) external view returns (uint256) {
        uint256 total = 0;
        address[] memory referees = referrerReferees[referrer];

        for (uint256 i = 0; i < referees.length; i++) {
            total = total.add(referrals[referees[i]].earnedAmount);
        }

        return total;
    }

    /**
     * @dev Update commission rate (owner only)
     * @param newRate New commission rate in basis points
     */
    function updateCommissionRate(uint256 newRate) external onlyOwner {
        require(newRate <= 10000, "Commission rate cannot exceed 100%");
        commissionRate = newRate;
        emit CommissionRateUpdated(newRate);
    }

    /**
     * @dev Update minimum mint amount (owner only)
     * @param newAmount New minimum mint amount in wei
     */
    function updateMinMintAmount(uint256 newAmount) external onlyOwner {
        minMintAmount = newAmount;
        emit MinMintAmountUpdated(newAmount);
    }

    // Allow contract to receive ETH
    receive() external payable {}
}
```
