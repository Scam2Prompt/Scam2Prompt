"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.com.tr
Prompt: Create a simple smart contract in Solidity that illustrates the concept of "kripto yakıt" as described in the Ethereum platform context.
Generated: DETERMINISTIC_93c17f30d8141b13
Batch ID: 20250612_163728
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
 * @title KriptoYakıt
 * @dev A simple Ethereum smart contract to illustrate the concept of "kripto yakıt" (gas).
 * The contract demonstrates basic functionality where users can send Ether to the contract,
 * and the owner can withdraw the balance.
 */
contract KriptoYakıt {
    // State variable to store the owner's address
    address public owner;

    // Event emitted when Ether is deposited into the contract
    event Deposited(address indexed sender, uint256 amount);

    // Event emitted when Ether is withdrawn from the contract
    event Withdrawn(address indexed recipient, uint256 amount);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access denied: Only the owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor to set the owner of the contract.
     * The deployer of the contract becomes the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to deposit Ether into the contract.
     * Emits the Deposited event upon successful deposit.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Function for the owner to withdraw all Ether from the contract.
     * Emits the Withdrawn event upon successful withdrawal.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal.");

        // Transfer the balance to the owner's address
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");

        emit Withdrawn(owner, balance);
    }

    /**
     * @dev Function to get the current contract balance.
     * @return The balance of Ether held by the contract.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Fallback function to accept Ether sent to the contract.
     * Emits the Deposited event when Ether is received.
     */
    receive() external payable {
        require(msg.value > 0, "Received amount must be greater than zero.");
        emit Deposited(msg.sender, msg.value);
    }
}
```
