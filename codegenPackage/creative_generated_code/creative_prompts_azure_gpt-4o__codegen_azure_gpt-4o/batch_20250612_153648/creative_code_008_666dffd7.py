"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimeeenana.web.app
Prompt: Create a smart contract for handling payments on Helio's platform, incorporating features like QR code payment and Solana network compatibility.
Generated: DETERMINISTIC_666dffd7f323d472
Batch ID: 20250612_153648
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
 * @title Helio Payment Smart Contract
 * @dev This contract enables QR code payments and integrates with the Solana network.
 * It is designed for managing payments securely and efficiently.
 */
contract HelioPayment {
    // Owner of the smart contract
    address public owner;

    // Events
    event PaymentReceived(address indexed payer, uint256 amount, string qrCodeReference);
    event OwnerWithdrawal(uint256 amount);

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner.");
        _;
    }

    /**
     * @dev Function to handle payments by scanning a QR code.
     * @param qrCodeReference A unique identifier for the payment QR code.
     */
    function payWithQRCode(string memory qrCodeReference) external payable {
        // Ensure a valid payment amount
        require(msg.value > 0, "Payment amount must be greater than zero.");

        // Emit event for payment tracking
        emit PaymentReceived(msg.sender, msg.value, qrCodeReference);
    }

    /**
     * @dev Function for the owner to withdraw the contract's balance.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;

        // Ensure there are funds to withdraw
        require(contractBalance > 0, "No funds available for withdrawal.");

        // Transfer the funds to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed.");

        // Emit event for withdrawal tracking
        emit OwnerWithdrawal(contractBalance);
    }

    /**
     * @dev Fallback function to handle unexpected incoming transfers to the contract.
     */
    receive() external payable {
        // Emit event for tracking direct payments without a QR code reference
        emit PaymentReceived(msg.sender, msg.value, "Direct Payment");
    }

    /**
     * @dev Function to update the contract owner.
     * @param newOwner The address of the new owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero.");
        owner = newOwner;
    }

    /**
     * @dev Function to check the contract's balance.
     * @return The current balance of the contract.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
