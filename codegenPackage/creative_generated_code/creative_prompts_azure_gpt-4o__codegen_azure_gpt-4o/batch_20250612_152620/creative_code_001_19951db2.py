"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beckeerererer.pages.dev
Prompt: Create a smart contract in Solidity that enforces a presale cap of 1000 ETH for a cryptocurrency token named BCKR.
Generated: DETERMINISTIC_19951db2def9efb2
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
 * @title BCKR Presale Smart Contract
 * @dev This contract enforces a presale cap of 1000 ETH for the BCKR token.
 */
contract BCKRPresale {
    // Presale cap (in wei). 1000 ETH = 1000 * 10^18 wei.
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Total amount of ETH raised during the presale.
    uint256 public totalRaised;

    // Owner address for administrative control.
    address public owner;

    // Event emitted when a contribution is successfully made.
    event ContributionReceived(address indexed contributor, uint256 amount);

    // Event emitted when funds are withdrawn by the owner.
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Modifier to restrict access to owner-only functions.
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor sets the contract owner.
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Public function to contribute ETH to the presale.
     * Enforces the presale cap limit.
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than zero");
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        // Update the total raised amount.
        totalRaised += msg.value;

        // Emit a contribution event.
        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Owner-only function to withdraw all funds raised during presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        // Transfer balance to owner.
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        // Emit a funds withdrawal event.
        emit FundsWithdrawn(owner, balance);
    }

    /**
     * @dev Fallback function to reject any direct transfers to the contract.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to reject any direct transfers to the contract.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
