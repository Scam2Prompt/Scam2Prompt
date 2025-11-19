"""
Generated Code Metadata:
========================
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Write a Solidity contract to interact with Instadapp Lite's Strategy Vaults, ensuring non-custodial wallet support and low-risk strategy execution.
Generated: DETERMINISTIC_65b7fc10d3633420
Batch ID: 20250612_145208
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Instadapp Strategy Vault
interface IStrategyVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

// Main contract to interact with Instadapp Lite's Strategy Vaults
contract InstadappStrategyManager is Ownable {
    // State variables
    IStrategyVault public strategyVault; // Instance of the strategy vault
    IERC20 public assetToken; // Token used for deposits and withdrawals

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the vault and token addresses
    constructor(address _strategyVault, address _assetToken) {
        require(_strategyVault != address(0), "Invalid strategy vault address");
        require(_assetToken != address(0), "Invalid asset token address");

        strategyVault = IStrategyVault(_strategyVault);
        assetToken = IERC20(_assetToken);
    }

    // Function to deposit tokens into the strategy vault
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        require(assetToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the strategy vault to spend the tokens
        assetToken.approve(address(strategyVault), amount);

        // Deposit tokens into the strategy vault
        strategyVault.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw tokens from the strategy vault
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(strategyVault.balanceOf(address(this)) >= amount, "Insufficient balance in vault");

        // Withdraw tokens from the strategy vault
        strategyVault.withdraw(amount);

        // Transfer tokens back to the owner
        require(assetToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of the contract in the strategy vault
    function getVaultBalance() external view returns (uint256) {
        return strategyVault.balanceOf(address(this));
    }

    // Function to set a new strategy vault (onlyOwner)
    function setStrategyVault(address _strategyVault) external onlyOwner {
        require(_strategyVault != address(0), "Invalid strategy vault address");
        strategyVault = IStrategyVault(_strategyVault);
    }

    // Function to set a new asset token (onlyOwner)
    function setAssetToken(address _assetToken) external onlyOwner {
        require(_assetToken != address(0), "Invalid asset token address");
        assetToken = IERC20(_assetToken);
    }
}
```
