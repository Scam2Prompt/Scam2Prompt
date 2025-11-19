"""
Generated Code Metadata:
========================
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Create a simple smart contract using Solidity to interact with Instadapp Lite's Strategy Vaults and execute a DeFi strategy.
Generated: DETERMINISTIC_9fe1767a18557c3e
Batch ID: 20250622_205943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the necessary interfaces for interacting with Instadapp's Strategy Vaults
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Instadapp Strategy Vault
interface IStrategyVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getBalance() external view returns (uint256);
}

// Simple smart contract to interact with Instadapp Lite's Strategy Vaults
contract DeFiStrategy is Ownable {
    // State variables
    IStrategyVault public strategyVault; // Instance of the Strategy Vault
    IERC20 public token; // ERC20 token used for deposits and withdrawals

    // Events for logging actions
    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);

    // Constructor to initialize the contract with the vault and token addresses
    constructor(address _strategyVault, address _token) {
        require(_strategyVault != address(0), "Invalid strategy vault address");
        require(_token != address(0), "Invalid token address");

        strategyVault = IStrategyVault(_strategyVault);
        token = IERC20(_token);
    }

    // Function to deposit tokens into the strategy vault
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens from the contract to the vault
        token.transfer(address(strategyVault), amount);
        strategyVault.deposit(amount);

        emit Deposited(amount);
    }

    // Function to withdraw tokens from the strategy vault
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(strategyVault.getBalance() >= amount, "Insufficient vault balance");

        strategyVault.withdraw(amount);
        token.transfer(msg.sender, amount);

        emit Withdrawn(amount);
    }

    // Function to check the balance of the strategy vault
    function checkVaultBalance() external view returns (uint256) {
        return strategyVault.getBalance();
    }

    // Function to check the token balance of the contract
    function checkTokenBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
