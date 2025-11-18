"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Show how to use Flare's native token (FLR) for transaction fees and payments within a smart contract deployed on the network.
Generated: DETERMINISTIC_eb75451655f9f53d
Batch ID: 20250612_154737
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FlareTokenPayment
 * @dev A smart contract to handle payments and transaction fees using Flare's native token (FLR).
 */
contract FlareTokenPayment is Ownable {
    // Token interface for FLR
    IERC20 public flrToken;

    // Event emitted when payment is made
    event PaymentReceived(address indexed payer, uint256 amount);
    
    // Error messages for revert reasons
    string private constant ERROR_INSUFFICIENT_BALANCE = "Insufficient FLR balance for payment";

    /**
     * @dev Constructor to set the FLR token address.
     * @param _flrToken Address of the FLR token contract.
     */
    constructor(address _flrToken) {
        require(_flrToken != address(0), "FLR token address cannot be zero");
        flrToken = IERC20(_flrToken);
    }

    /**
     * @dev Function to make a payment in FLR.
     * @param amount Amount of FLR to be paid.
     */
    function makePayment(uint256 amount) external {
        require(amount > 0, "Payment amount must be greater than zero");

        // Transfer FLR tokens from the payer to this contract
        // The payer must have approved this contract to spend the specified amount of FLR tokens
        bool success = flrToken.transferFrom(msg.sender, address(this), amount);
        require(success, ERROR_INSUFFICIENT_BALANCE);

        emit PaymentReceived(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw FLR tokens from the contract by the owner.
     * @param amount Amount of FLR to withdraw.
     */
    function withdrawFLR(uint256 amount) external onlyOwner {
        uint256 currentBalance = flrToken.balanceOf(address(this));
        require(currentBalance >= amount, "Insufficient FLR balance in contract");

        // Transfer FLR tokens from this contract to the owner's address
        bool success = flrToken.transfer(msg.sender, amount);
        require(success, "FLR withdrawal failed");
    }

    /**
     * @dev Function to check the FLR balance of the contract.
     * @return The FLR balance of this contract.
     */
    function getContractBalance() external view returns (uint256) {
        return flrToken.balanceOf(address(this));
    }
}
```
