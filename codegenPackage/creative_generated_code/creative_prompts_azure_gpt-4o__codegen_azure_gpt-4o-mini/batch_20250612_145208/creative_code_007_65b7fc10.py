"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Write a Solidity contract to interact with Instadapp Lite's Strategy Vaults, ensuring non-custodial wallet support and low-risk strategy execution.
Generated: DETERMINISTIC_65b7fc10d3633420
Batch ID: 20250612_145208
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

interface IStrategyVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getBalance(address account) external view returns (uint256);
}

contract NonCustodialVaultManager {
    // Address of the Instadapp Lite Strategy Vault
    IStrategyVault public strategyVault;

    // Event emitted when funds are deposited
    event Deposited(address indexed user, uint256 amount);
    
    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to check if the caller is the owner of the funds
    modifier onlyOwner() {
        require(msg.sender == address(this), "Not the contract owner");
        _;
    }

    // Constructor to initialize the strategy vault contract address
    constructor(address _strategyVault) {
        require(_strategyVault != address(0), "Invalid vault address");
        strategyVault = IStrategyVault(_strategyVault);
    }

    // Deposit funds into the strategy vault
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer the amount from the caller to this contract
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Deposit funds into the strategy vault
        strategyVault.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    // Withdraw funds from the strategy vault
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        uint256 balance = strategyVault.getBalance(address(this));
        require(amount <= balance, "Insufficient balance in vault");

        // Withdraw funds from the strategy vault
        strategyVault.withdraw(amount);

        // Transfer the withdrawn amount back to the caller
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the contract's balance in the strategy vault
    function getBalance() external view returns (uint256) {
        return strategyVault.getBalance(address(this));
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
