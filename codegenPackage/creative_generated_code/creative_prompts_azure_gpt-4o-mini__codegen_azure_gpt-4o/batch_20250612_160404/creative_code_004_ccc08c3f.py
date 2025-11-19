"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftdecentralizedapp.com
Prompt: Create an example of a smart contract for a self-custodial wallet as outlined on swiftdecentralizedapp.com.
Generated: DETERMINISTIC_ccc08c3ff5727ae8
Batch ID: 20250612_160404
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
 * @title SelfCustodialWallet
 * @dev A simple Ethereum-based self-custodial wallet that allows deposits,
 * withdrawals, and ownership management.
 */
contract SelfCustodialWallet {
    // The owner of the wallet
    address public owner;

    // Event emitted when funds are deposited into the wallet
    event Deposit(address indexed sender, uint256 amount);

    // Event emitted when funds are withdrawn from the wallet
    event Withdrawal(address indexed recipient, uint256 amount);

    // Event emitted when ownership of the wallet is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to only the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the wallet with the sender as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to allow the owner to withdraw funds.
     * @param amount The amount of Ether to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        payable(owner).transfer(amount);
        emit Withdrawal(owner, amount);
    }

    /**
     * @dev Function to transfer ownership of the wallet.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to check the current balance of the wallet.
     * @return The balance of the wallet in wei.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
