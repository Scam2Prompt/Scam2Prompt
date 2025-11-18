"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogcoin.pages.dev
Prompt: Generate a Solidity function to enforce a presale cap of 1000 ETH for a token sale, ensuring that any transactions exceeding the cap are rejected.
Generated: DETERMINISTIC_202d7c616965d412
Batch ID: 20250612_153420
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
 * @title PresaleCap contract
 * @dev Enforces a presale cap of 1000 ETH for a token sale.
 */
contract PresaleCap {
    // State variable to track the total amount of ETH raised in the presale
    uint256 public totalRaised;

    // Constant representing the presale cap (1000 ETH)
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Event emitted when a contribution is made
    event ContributionReceived(address indexed contributor, uint256 amount);

    // Event emitted when a transaction is rejected due to exceeding the cap
    event ContributionRejected(address indexed contributor, uint256 attemptedAmount);

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to contribute to the presale.
     * Rejects transactions that exceed the presale cap.
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than 0");

        // Ensure the contribution does not exceed the presale cap
        if (totalRaised + msg.value > PRESALE_CAP) {
            emit ContributionRejected(msg.sender, msg.value);
            revert("Presale cap exceeded"); // Reject the transaction
        }

        // Update the total amount raised
        totalRaised += msg.value;

        // Emit the contribution event
        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function for the owner to withdraw all ETH.
     */
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");

        // Transfer all ETH to the owner
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
