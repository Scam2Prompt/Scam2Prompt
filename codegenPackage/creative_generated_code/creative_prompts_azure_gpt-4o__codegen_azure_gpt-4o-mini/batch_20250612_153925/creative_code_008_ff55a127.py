"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.2y4f81.cn
Prompt: Generate code to integrate OKX’s native token (OKB) into a decentralized application (DApp) for transaction fee payments.
Generated: DETERMINISTIC_ff55a127d34b7c50
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the ERC20 interface to interact with the OKB token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the contract for the DApp
contract OKBPaymentDApp {
    // Address of the OKB token contract
    IERC20 public okbToken;

    // Event emitted when a payment is made
    event PaymentReceived(address indexed payer, uint256 amount);

    // Constructor to set the OKB token address
    constructor(address _okbTokenAddress) {
        // Ensure the provided address is a valid contract
        require(_okbTokenAddress != address(0), "Invalid token address");
        okbToken = IERC20(_okbTokenAddress);
    }

    // Function to make a payment using OKB tokens
    function payWithOKB(uint256 amount) external {
        // Validate the payment amount
        require(amount > 0, "Payment amount must be greater than zero");

        // Transfer OKB tokens from the payer to this contract
        // The payer must approve this contract to spend the tokens beforehand
        bool success = okbToken.transferFrom(msg.sender, address(this), amount);
        
        // Ensure the token transfer was successful
        require(success, "Token transfer failed");

        // Emit an event for the payment
        emit PaymentReceived(msg.sender, amount);
    }

    // Function to withdraw collected OKB tokens to a designated wallet
    function withdrawOKB(address to, uint256 amount) external {
        // Ensure this contract has the authority to withdraw tokens
        require(to != address(0), "Invalid withdrawal address");
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(okbToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of OKB tokens to the recipient
        bool success = okbToken.transfer(to, amount);
        
        // Ensure the withdrawal was successful
        require(success, "Withdrawal failed");
    }

    // Function to check the contract's OKB balance
    function getBalance() external view returns (uint256) {
        return okbToken.balanceOf(address(this));
    }
}
```
