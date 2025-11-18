"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website1-beo.pages.dev
Prompt: Generate a smart contract that supports long-term relationships and transparency in crypto projects, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_684c0e0b1d087e55
Batch ID: 20250612_150226
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
 * @title TransparentCryptoContract
 * @dev A smart contract for supporting long-term relationships and transparency in crypto projects.
 *      Reflects values of Innodapter ApS.
 */
contract TransparentCryptoContract {
    // Owner of the contract
    address public owner;

    // Mapping to track balances of participants
    mapping(address => uint256) public balances;

    // Event to emit when funds are deposited
    event FundsDeposited(address indexed participant, uint256 amount);

    // Event to emit when funds are withdrawn
    event FundsWithdrawn(address indexed participant, uint256 amount);

    // Event to emit when ownership is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to the owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to owner.");
        _;
    }

    /**
     * @dev Constructor to set the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Deposit funds to the contract. Updates the participant's balance.
     * Emits a FundsDeposited event.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        balances[msg.sender] += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw funds from the contract. Updates the participant's balance.
     * Emits a FundsWithdrawn event.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * Emits an OwnershipTransferred event.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address.");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to accept plain Ether transfers.
     */
    receive() external payable {
        deposit();
    }

    /**
     * @dev Function to handle calls that do not match any function signature.
     */
    fallback() external payable {
        deposit();
    }
}
```
