"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clean-4dq.pages.dev
Prompt: Generate Solidity code for deploying a smart contract on SatoshiVM that utilizes native BTC as gas and is compatible with the EVM ecosystem.
Generated: DETERMINISTIC_7286fb4629b902b3
Batch ID: 20250612_152326
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
 * @title NativeBTCContract
 * @dev A smart contract designed for deployment on SatoshiVM, utilizing native BTC as gas.
 *      Compatible with the EVM ecosystem.
 */
contract NativeBTCContract {
    // State variable to store the owner's address
    address public owner;

    // Event to log deposits of native BTC
    event Deposit(address indexed sender, uint256 amount);

    // Event to log withdrawals of native BTC
    event Withdraw(address indexed recipient, uint256 amount);

    // Constructor - initializes the contract with the deployer's address as the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to deposit BTC-native gas into the contract.
     *      Emits a Deposit event upon successful deposit.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw BTC-native gas from the contract.
     * @param recipient Address to send BTC-native funds to.
     * @param amount Amount of BTC-native funds to withdraw.
     *      Emits a Withdraw event upon successful withdrawal.
     */
    function withdraw(address recipient, uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance in contract");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer the amount to the recipient
        (bool success, ) = recipient.call{value: amount}("");
        require(success, "Withdraw failed");

        emit Withdraw(recipient, amount);
    }

    /**
     * @dev Function to check the contract's balance.
     * @return The current balance of the contract in BTC-native gas.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Fallback function to handle unexpected BTC-native gas transfers.
     *      Allows the contract to accept BTC-native funds sent directly.
     */
    receive() external payable {
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Fallback function for non-specific calls.
     *      Ensures the contract does not mistakenly accept unsupported calls.
     */
    fallback() external payable {
        emit Deposit(msg.sender, msg.value);
    }
}
```
