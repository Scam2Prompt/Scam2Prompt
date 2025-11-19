"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usd-coin.net
Prompt: Provide an example of how to create a smart contract that utilizes USD Coin as a payment method.
Generated: DETERMINISTIC_c308718bb1cd4be7
Batch ID: 20250612_160526
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

// Importing the interface for the ERC20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract PaymentContract {
    // Address of the USD Coin (USDC) token contract
    IERC20 public usdcToken;

    // Event to log successful payments
    event PaymentReceived(address indexed payer, uint256 amount);

    // Constructor to set the USDC token address
    constructor(address _usdcTokenAddress) {
        require(_usdcTokenAddress != address(0), "USDC token address cannot be zero");
        usdcToken = IERC20(_usdcTokenAddress);
    }

    // Function to make a payment in USD Coin
    function makePayment(uint256 amount) external {
        require(amount > 0, "Payment amount must be greater than zero");

        // Transfer USDC from the payer to this contract
        bool success = usdcToken.transferFrom(msg.sender, address(this), amount);
        require(success, "USDC transfer failed");

        // Emit an event for the successful payment
        emit PaymentReceived(msg.sender, amount);
    }

    // Function to withdraw USDC from the contract
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        
        // Ensure the contract has enough USDC to withdraw
        uint256 contractBalance = usdcToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient funds in the contract");

        // Transfer USDC to the contract owner
        bool success = usdcToken.transfer(msg.sender, amount);
        require(success, "USDC withdrawal failed");
    }

    // Function to check the contract's USDC balance
    function getBalance() external view returns (uint256) {
        return usdcToken.balanceOf(address(this));
    }
}
```
