"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lookscoin.com
Prompt: Write a smart contract using Solidity that implements a payment distribution mechanism for contributors in a product line, as described in the LookRev branch system.
Generated: DETERMINISTIC_f068616d511f6301
Batch ID: 20250612_153256
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
 * @title PaymentDistribution
 * @dev A smart contract to distribute payments among contributors in a product line
 *      based on predefined shares. Contributors are assigned a percentage share of revenue.
 */
contract PaymentDistribution {
    // Contributor structure to store their address and share percentage
    struct Contributor {
        address payable wallet;
        uint256 share; // Share percentage (e.g., 20 for 20%)
    }

    // Array of contributors
    Contributor[] public contributors;

    // Owner of the contract
    address public owner;

    // Total shares must equal 100%
    uint256 public totalShares;

    // Events for logging
    event PaymentReceived(address indexed from, uint256 amount);
    event PaymentDistributed(uint256 totalAmount);
    event ContributorAdded(address indexed wallet, uint256 share);
    event ContributorUpdated(address indexed wallet, uint256 newShare);

    /**
     * @dev Modifier to restrict access to contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a contributor to the payment system
     * @param wallet The address of the contributor
     * @param share The percentage share (must be between 1 and 100)
     */
    function addContributor(address payable wallet, uint256 share) external onlyOwner {
        require(wallet != address(0), "Invalid contributor address");
        require(share > 0 && share <= 100, "Share must be between 1 and 100");
        require(totalShares + share <= 100, "Total shares cannot exceed 100");

        contributors.push(Contributor(wallet, share));
        totalShares += share;

        emit ContributorAdded(wallet, share);
    }

    /**
     * @dev Update the share of an existing contributor
     * @param index The index of the contributor in the array
     * @param newShare The new percentage share (must be between 1 and 100)
     */
    function updateContributor(uint256 index, uint256 newShare) external onlyOwner {
        require(index < contributors.length, "Invalid contributor index");
        require(newShare > 0 && newShare <= 100, "Share must be between 1 and 100");

        // Update totalShares before modifying contributor share
        totalShares = totalShares - contributors[index].share + newShare;
        require(totalShares <= 100, "Total shares cannot exceed 100");

        contributors[index].share = newShare;

        emit ContributorUpdated(contributors[index].wallet, newShare);
    }

    /**
     * @dev Fallback function to receive payments
     */
    receive() external payable {
        emit PaymentReceived(msg.sender, msg.value);
        distributePayments(msg.value);
    }

    /**
     * @dev Distribute received payments among contributors
     * @param totalAmount The total payment amount to be distributed
     */
    function distributePayments(uint256 totalAmount) internal {
        require(totalShares == 100, "Total shares must equal 100 to distribute payments");

        for (uint256 i = 0; i < contributors.length; i++) {
            Contributor memory contributor = contributors[i];
            uint256 payment = (totalAmount * contributor.share) / 100;

            // Transfer the payment to the contributor
            (bool sent, ) = contributor.wallet.call{value: payment}("");
            require(sent, "Failed to send payment to contributor");
        }

        emit PaymentDistributed(totalAmount);
    }

    /**
     * @dev Get the number of contributors
     * @return The total number of contributors in the contract
     */
    function getContributorCount() external view returns (uint256) {
        return contributors.length;
    }

    /**
     * @dev Get the details of a specific contributor
     * @param index The index of the contributor in the array
     * @return The wallet address and share percentage of the contributor
     */
    function getContributorDetails(uint256 index) external view returns (address, uint256) {
        require(index < contributors.length, "Invalid contributor index");
        Contributor memory contributor = contributors[index];
        return (contributor.wallet, contributor.share);
    }
}
```
