"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: Write a Solidity smart contract that is optimized for deployment on Linea's zkEVM ecosystem, ensuring compatibility with its EVM bytecode and leveraging low gas fees.
Generated: DETERMINISTIC_e7f9bf41837c9986
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title LineaOptimizedContract
/// @author Your Name
/// @notice This contract is optimized for deployment on Linea's zkEVM ecosystem.
/// @dev Compatible with EVM bytecode and designed to minimize gas costs.

contract LineaOptimizedContract {
    // State variables
    address public owner;
    uint256 public totalDeposits;

    // Events
    event Deposit(address indexed sender, uint256 amount);
    event Withdrawal(address indexed receiver, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /// @notice Constructor sets the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Allows anyone to deposit Ether into the contract
    /// @dev Emits a Deposit event on successful deposit
    receive() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        totalDeposits += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /// @notice Allows the owner to withdraw Ether from the contract
    /// @param _amount The amount of Ether to withdraw (in wei)
    /// @dev Emits a Withdrawal event on successful withdrawal
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(_amount <= address(this).balance, "Insufficient balance");
        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Withdrawal failed");
        emit Withdrawal(owner, _amount);
    }

    /// @notice Returns the contract's Ether balance
    /// @return The current balance of the contract in wei
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /// @notice Allows the owner to transfer ownership of the contract
    /// @param _newOwner The address of the new owner
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        owner = _newOwner;
    }
}
```
