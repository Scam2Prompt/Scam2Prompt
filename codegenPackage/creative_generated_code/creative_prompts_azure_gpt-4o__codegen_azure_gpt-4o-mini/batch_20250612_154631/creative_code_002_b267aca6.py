"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btt.usdc20.com
Prompt: Generate Solidity code for a smart contract that accepts USDC payments and stores the sender's address and payment amount.
Generated: DETERMINISTIC_b267aca6c4dccdb2
Batch ID: 20250612_154631
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

// Import the ERC20 interface for USDC
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract to accept USDC payments
contract USDCPaymentProcessor {
    // Event emitted when a payment is made
    event PaymentReceived(address indexed sender, uint256 amount);

    // Address of the USDC token contract
    IERC20 public usdcToken;

    // Mapping to store payment records
    mapping(address => uint256) public payments;

    // Constructor to set the USDC token address
    constructor(address _usdcTokenAddress) {
        require(_usdcTokenAddress != address(0), "Invalid USDC token address");
        usdcToken = IERC20(_usdcTokenAddress);
    }

    // Function to accept USDC payments
    function makePayment(uint256 amount) external {
        require(amount > 0, "Payment amount must be greater than zero");

        // Transfer USDC from the sender to this contract
        bool success = usdcToken.transferFrom(msg.sender, address(this), amount);
        require(success, "USDC transfer failed");

        // Store the payment record
        payments[msg.sender] += amount;

        // Emit an event for the payment
        emit PaymentReceived(msg.sender, amount);
    }

    // Function to withdraw USDC from the contract
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer USDC to the caller
        bool success = usdcToken.transfer(msg.sender, amount);
        require(success, "USDC withdrawal failed");
    }

    // Function to get the payment amount by sender
    function getPaymentAmount(address sender) external view returns (uint256) {
        return payments[sender];
    }
}
```
