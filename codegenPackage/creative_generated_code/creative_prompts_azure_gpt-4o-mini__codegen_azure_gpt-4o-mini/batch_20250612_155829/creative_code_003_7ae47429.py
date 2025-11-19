"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Explain how to implement a withdrawal function in a Solidity contract that transfers profits back to the contract creator, as demonstrated in the OneinchSlippageBot.
Generated: DETERMINISTIC_7ae474297cfaec0b
Batch ID: 20250612_155829
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

/// @title Profit Withdrawal Contract
/// @author Your Name
/// @notice This contract allows the creator to withdraw profits from the contract
contract ProfitWithdrawal {
    // State variable to store the address of the contract creator
    address payable private owner;

    // Event to log withdrawals
    event Withdrawal(address indexed to, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    /// @notice Constructor to set the contract owner
    constructor() {
        owner = payable(msg.sender);
    }

    /// @notice Function to withdraw profits to the owner
    /// @dev Only the owner can call this function
    function withdraw(uint256 amount) external onlyOwner {
        // Ensure the contract has enough balance to withdraw
        require(address(this).balance >= amount, "Insufficient balance");

        // Transfer the specified amount to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawal(owner, amount);
    }

    /// @notice Function to receive Ether. This function is required to accept funds.
    receive() external payable {}

    /// @notice Function to get the balance of the contract
    /// @return The current balance of the contract
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
