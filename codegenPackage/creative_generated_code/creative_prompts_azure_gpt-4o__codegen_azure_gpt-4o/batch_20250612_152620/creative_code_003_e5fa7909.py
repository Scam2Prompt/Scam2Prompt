"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakachainpro.pages.dev
Prompt: Create a smart contract on the Naka Chain blockchain that facilitates a crypto giveaway with claim reference code validation.
Generated: DETERMINISTIC_e5fa79095e950e12
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
 * @title CryptoGiveaway
 * @dev Smart contract to facilitate crypto giveaways with claim reference code validation on Naka Chain.
 */
contract CryptoGiveaway {
    // Owner of the contract
    address public owner;

    // Mapping to store reference codes and their claim status
    mapping(string => bool) public claimedReferenceCodes;

    // Event emitted when a giveaway is claimed
    event GiveawayClaimed(address indexed claimant, uint256 amount, string referenceCode);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to deposit funds into the contract.
     * @notice The contract must have sufficient balance for successful giveaways.
     */
    function depositFunds() external payable onlyOwner {
        require(msg.value > 0, "Deposit must be greater than zero");
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract.
     * @notice Ensures the owner can recover their funds if needed.
     * @param amount The amount to withdraw in wei.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Allows a user to claim a giveaway using a valid reference code.
     * @param referenceCode The unique reference code provided for the giveaway.
     * @param amount The amount to claim in wei.
     */
    function claimGiveaway(string memory referenceCode, uint256 amount) external {
        // Validate parameters
        require(bytes(referenceCode).length > 0, "Reference code cannot be empty");
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Ensure the reference code has not been claimed already
        require(!claimedReferenceCodes[referenceCode], "Reference code already claimed");

        // Mark the reference code as claimed
        claimedReferenceCodes[referenceCode] = true;

        // Transfer the giveaway amount to the claimant
        payable(msg.sender).transfer(amount);

        // Emit an event for transparency
        emit GiveawayClaimed(msg.sender, amount, referenceCode);
    }

    /**
     * @dev Provides the contract balance for transparency.
     * @return The current contract balance in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
