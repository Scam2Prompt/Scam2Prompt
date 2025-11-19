"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: How can Open Ocean be applied to create a fallback handler in Ethereum smart contracts to prevent exploitation?
Generated: DETERMINISTIC_3f146ba5e82d1ea6
Batch ID: 20250612_155554
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

contract OpenOceanFallbackHandler {
    // State variable to store the owner of the contract
    address public owner;

    // Mapping to keep track of balances
    mapping(address => uint256) public balances;

    // Event to log deposits
    event Deposited(address indexed sender, uint256 amount);
    // Event to log withdrawals
    event Withdrawn(address indexed recipient, uint256 amount);
    // Event for fallback calls
    event FallbackCalled(address indexed sender, uint256 amount);

    // Modifier to restrict access to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to deposit Ether into the contract
    function deposit() external payable {
        require(msg.value > 0, "Must send non-zero amount");
        balances[msg.sender] += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    // Function to withdraw Ether from the contract
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Update balance before transfer to prevent reentrancy
        balances[msg.sender] -= amount;

        // Transfer the specified amount to the caller
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Fallback function to handle unexpected Ether transfers
    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value);
        // Optionally, revert the transaction to prevent Ether from being lost
        revert("Fallback: Ether transferred to contract");
    }

    // Function to retrieve the balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to check the balance of an account
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }

    // Function to withdraw funds by the owner (emergency withdraw)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");
        
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Function to destroy the contract and send remaining Ether to the owner
    function destroy() external onlyOwner {
        selfdestruct(payable(owner));
    }
}
```
