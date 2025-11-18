"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contrack-dev.pages.dev
Prompt: Write a Solidity function to withdraw profits from a contract to the creator's address, similar to the `withdrawal` function in the UniswapSlippageBot contract.
Generated: DETERMINISTIC_3e8de1357e26bc52
Batch ID: 20250612_154741
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
 * @title ProfitWithdrawalContract
 * @dev A contract that allows the owner to withdraw profits accumulated in the contract.
 */
contract ProfitWithdrawalContract {
    address public owner;

    // Modifier to restrict access to the owner of the contract
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Withdraw all Ether balance from the contract to the owner's address
     * @dev Only the owner can call this function
     */
    function withdrawProfits() external onlyOwner {
        // Get the contract's balance
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal");

        // Transfer all funds to the owner's address
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Fallback function if no other function matches
    fallback() external payable {}
}
```
