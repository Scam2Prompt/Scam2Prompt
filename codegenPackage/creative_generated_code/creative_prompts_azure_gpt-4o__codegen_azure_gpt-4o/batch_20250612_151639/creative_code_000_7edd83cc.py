"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful.bond
Prompt: Write a Solidity smart contract for an Ethereum-based DeFi application that integrates features similar to those described on paxful.bond.
Generated: DETERMINISTIC_7edd83cceda852e6
Batch ID: 20250612_151639
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
 * @title DeFi Bond Contract
 * @dev A smart contract for managing bonds in a decentralized finance application.
 */
contract DeFiBond {
    // Struct to represent a bond
    struct Bond {
        uint256 amount;        // Bond amount (in wei)
        uint256 interestRate;  // Interest rate (in basis points, e.g., 500 means 5%)
        uint256 duration;      // Bond duration in seconds
        uint256 createdAt;     // Timestamp when the bond was created
        bool isRedeemed;       // Flag to check if the bond is redeemed
    }

    // Mapping of user addresses to their bonds
    mapping(address => Bond[]) public bonds;

    // Event declarations for logging activities
    event BondIssued(address indexed user, uint256 amount, uint256 interestRate, uint256 duration);
    event BondRedeemed(address indexed user, uint256 amount);

    // Modifier to ensure a valid bond exists
    modifier validBond(address user, uint256 bondIndex) {
        require(bondIndex < bonds[user].length, "Invalid bond index.");
        require(!bonds[user][bondIndex].isRedeemed, "Bond already redeemed.");
        _;
    }

    /**
     * @dev Issue a new bond.
     * @param interestRate The interest rate for the bond (in basis points, e.g., 500 means 5%).
     * @param duration The duration of the bond in seconds.
     */
    function issueBond(uint256 interestRate, uint256 duration) external payable {
        require(msg.value > 0, "Bond amount must be greater than zero.");
        require(duration > 0, "Bond duration must be greater than zero.");

        // Create a new bond and store it in the user's list of bonds
        Bond memory newBond = Bond({
            amount: msg.value,
            interestRate: interestRate,
            duration: duration,
            createdAt: block.timestamp,
            isRedeemed: false
        });

        bonds[msg.sender].push(newBond);

        // Emit an event for bond issuance
        emit BondIssued(msg.sender, msg.value, interestRate, duration);
    }

    /**
     * @dev Redeem a bond that has matured.
     * @param bondIndex The index of the bond to redeem.
     */
    function redeemBond(uint256 bondIndex) external validBond(msg.sender, bondIndex) {
        Bond storage bond = bonds[msg.sender][bondIndex];

        // Ensure the bond has matured
        require(block.timestamp >= bond.createdAt + bond.duration, "Bond has not matured yet.");

        // Calculate the payout amount (principal + interest)
        uint256 interest = (bond.amount * bond.interestRate * bond.duration) / (10000 * 365 * 24 * 60 * 60); // Annualized interest
        uint256 payout = bond.amount + interest;

        // Mark the bond as redeemed
        bond.isRedeemed = true;

        // Transfer the payout to the user
        (bool success, ) = msg.sender.call{value: payout}("");
        require(success, "Transfer failed.");

        // Emit an event for bond redemption
        emit BondRedeemed(msg.sender, payout);
    }

    /**
     * @dev Fallback function to reject direct Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers are not supported.");
    }

    /**
     * @dev Receive Ether function to reject direct Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not supported.");
    }

    /**
     * @dev Get the details of a bond for a specific user.
     * @param user The address of the user.
     * @param bondIndex The index of the bond.
     * @return Bond details.
     */
    function getBondDetails(address user, uint256 bondIndex) external view returns (Bond memory) {
        require(bondIndex < bonds[user].length, "Invalid bond index.");
        return bonds[user][bondIndex];
    }
}
```
