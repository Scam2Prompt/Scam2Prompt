"""
Generated Code Metadata:
========================
Original URL: https://thorchain1.vercel.app
Prompt: Create a smart contract that integrates THORChain's liquidity savers vaults to allow single asset liquidity deposits and earn swap fees.
Generated: DETERMINISTIC_4bb6cfbcac74aa4e
Batch ID: 20250612_153400
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

// Interface for THORChain's liquidity savers vault
interface IThorchainVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getSwapFees() external view returns (uint256);
}

// Smart contract for integrating THORChain's liquidity savers vault
contract ThorchainLiquiditySaver is Ownable {
    // State variables
    IERC20 public asset; // The asset to be deposited
    IThorchainVault public vault; // The THORChain vault interface

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event FeesClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with asset and vault addresses
    constructor(address _asset, address _vault) {
        require(_asset != address(0), "Invalid asset address");
        require(_vault != address(0), "Invalid vault address");
        
        asset = IERC20(_asset);
        vault = IThorchainVault(_vault);
    }

    // Function to deposit a single asset into the vault
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer the asset from the user to this contract
        require(asset.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the vault to spend the asset
        asset.approve(address(vault), amount);

        // Deposit the asset into the THORChain vault
        vault.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw a single asset from the vault
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Withdraw the asset from the THORChain vault
        vault.withdraw(amount);

        // Transfer the asset back to the owner
        require(asset.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim swap fees earned from the vault
    function claimFees() external onlyOwner {
        uint256 fees = vault.getSwapFees();
        require(fees > 0, "No fees to claim");

        // Transfer the fees to the owner
        require(asset.transfer(msg.sender, fees), "Transfer failed");

        emit FeesClaimed(msg.sender, fees);
    }

    // Function to recover any ERC20 tokens sent to this contract by mistake
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(asset), "Cannot recover the main asset");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
