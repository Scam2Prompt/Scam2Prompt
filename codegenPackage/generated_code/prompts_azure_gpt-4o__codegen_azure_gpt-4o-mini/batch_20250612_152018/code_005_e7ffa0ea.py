"""
Generated Code Metadata:
========================
Original URL: https://boostaevo.pages.dev
Prompt: Create a smart contract on Ethereum to interact with Aevo's decentralized options vaults, incorporating security features and performance optimization for the OP stack-based L2.
Generated: DETERMINISTIC_e7ffa0ea0b9bd207
Batch ID: 20250612_152018
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for Aevo's decentralized options vaults
interface IAevoOptionsVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getVaultBalance() external view returns (uint256);
}

// Smart contract for interacting with Aevo's decentralized options vaults
contract AevoOptionsManager is Ownable, ReentrancyGuard {
    // State variables
    IAevoOptionsVault public optionsVault; // Address of the Aevo options vault
    IERC20 public token; // ERC20 token used for deposits and withdrawals

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the vault and token addresses
    constructor(address _optionsVault, address _token) {
        require(_optionsVault != address(0), "Invalid options vault address");
        require(_token != address(0), "Invalid token address");

        optionsVault = IAevoOptionsVault(_optionsVault);
        token = IERC20(_token);
    }

    // Function to deposit tokens into the options vault
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to this contract
        token.transferFrom(msg.sender, address(this), amount);
        // Approve the options vault to spend the tokens
        token.approve(address(optionsVault), amount);
        // Deposit tokens into the options vault
        optionsVault.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw tokens from the options vault
    function withdraw(uint256 amount) external nonReentrant onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(optionsVault.getVaultBalance() >= amount, "Insufficient vault balance");

        // Withdraw tokens from the options vault
        optionsVault.withdraw(amount);
        // Transfer tokens back to the owner
        token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the current balance of the vault
    function getVaultBalance() external view returns (uint256) {
        return optionsVault.getVaultBalance();
    }

    // Function to set a new options vault address (onlyOwner)
    function setOptionsVault(address _optionsVault) external onlyOwner {
        require(_optionsVault != address(0), "Invalid options vault address");
        optionsVault = IAevoOptionsVault(_optionsVault);
    }

    // Function to set a new token address (onlyOwner)
    function setToken(address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }
}
```
