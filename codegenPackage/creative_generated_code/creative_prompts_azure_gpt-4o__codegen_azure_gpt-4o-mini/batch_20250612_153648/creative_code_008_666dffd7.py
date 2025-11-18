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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract HelioPayment is Ownable {
    // Event to log successful payments
    event PaymentReceived(address indexed payer, uint256 amount, string qrCodeData);
    
    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Address of the accepted token (e.g., USDC)
    IERC20 public acceptedToken;

    /**
     * @dev Constructor to set the accepted token for payments
     * @param _acceptedToken Address of the ERC20 token to accept for payments
     */
    constructor(IERC20 _acceptedToken) {
        acceptedToken = _acceptedToken;
    }

    /**
     * @dev Function to handle payments
     * @param amount Amount of tokens to be paid
     * @param qrCodeData Data to encode in the QR code
     */
    function pay(uint256 amount, string memory qrCodeData) external {
        require(amount > 0, "Payment amount must be greater than zero");
        require(acceptedToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(acceptedToken.allowance(msg.sender, address(this)) >= amount, "Token allowance not granted");

        // Transfer tokens from payer to this contract
        bool success = acceptedToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the payer's balance
        balances[msg.sender] += amount;

        // Emit payment received event
        emit PaymentReceived(msg.sender, amount, qrCodeData);
    }

    /**
     * @dev Function to withdraw tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(acceptedToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = acceptedToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
    
    /**
     * @dev Function to check the balance of a user
     * @param user Address of the user
     * @return balance The balance of the user
     */
    function checkBalance(address user) external view returns (uint256 balance) {
        return balances[user];
    }
}
```
