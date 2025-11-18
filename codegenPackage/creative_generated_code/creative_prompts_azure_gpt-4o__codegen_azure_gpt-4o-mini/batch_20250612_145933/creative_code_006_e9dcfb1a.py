"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-v2.vercel.app
Prompt: Create a smart contract that interacts with Beefy Finance's vaults to automate deposits and withdrawals based on predefined conditions.
Generated: DETERMINISTIC_e9dcfb1aa8c5f17c
Batch ID: 20250612_145933
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Beefy Finance's vaults
interface IBeefyVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _shares) external;
    function balanceOf(address _account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

contract BeefyAutomator is Ownable {
    // Address of the Beefy vault
    IBeefyVault public vault;
    // The token used for deposits/withdrawals
    IERC20 public token;

    // Events for deposit and withdrawal actions
    event Deposited(uint256 amount);
    event Withdrawn(uint256 shares);

    // Constructor to set vault and token addresses
    constructor(address _vault, address _token) {
        require(_vault != address(0), "Invalid vault address");
        require(_token != address(0), "Invalid token address");

        vault = IBeefyVault(_vault);
        token = IERC20(_token);
    }

    // Function to deposit tokens into the vault
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Approve the vault to spend tokens
        token.approve(address(vault), amount);
        // Deposit the tokens into the vault
        vault.deposit(amount);

        emit Deposited(amount);
    }

    // Function to withdraw tokens from the vault based on shares
    function withdraw(uint256 shares) external onlyOwner {
        require(shares > 0, "Shares must be greater than zero");
        require(vault.balanceOf(address(this)) >= shares, "Insufficient shares");

        // Withdraw tokens from the vault
        vault.withdraw(shares);

        emit Withdrawn(shares);
    }

    // Function to check the current balance of the vault in tokens
    function getVaultBalanceInTokens() external view returns (uint256) {
        uint256 shares = vault.balanceOf(address(this));
        uint256 pricePerShare = vault.getPricePerFullShare();
        return (shares * pricePerShare) / 1e18; // Adjusting for price decimals
    }

    // Function to withdraw all tokens from the vault
    function withdrawAll() external onlyOwner {
        uint256 shares = vault.balanceOf(address(this));
        if (shares > 0) {
            vault.withdraw(shares);
            emit Withdrawn(shares);
        }
    }

    // Fallback function to receive tokens
    receive() external payable {}
}
```
