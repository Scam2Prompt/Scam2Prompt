"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-v2.vercel.app
Prompt: Provide an example of using Beefy Finance's smart contracts for optimizing DeFi investments.
Generated: DETERMINISTIC_d01532da7e640eb1
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary OpenZeppelin contracts for security
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Beefy Finance's vault contract
interface IBeefyVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _shares) external;
    function balance() external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

// Main contract for interacting with Beefy Finance
contract BeefyDeFiOptimizer is Ownable {
    // State variables
    IERC20 public token; // Token to optimize (e.g., USDC)
    IBeefyVault public vault; // Beefy vault contract
    uint256 public vaultShares; // Shares owned in the vault

    // Event to log deposits
    event Deposited(uint256 amount);
    // Event to log withdrawals
    event Withdrawn(uint256 shares);

    // Constructor: Initialize with token and vault addresses
    constructor(address _token, address _vault) {
        token = IERC20(_token);
        vault = IBeefyVault(_vault);
    }

    // Function to deposit tokens into the Beefy vault
    function deposit(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the contract to this contract
        token.transferFrom(msg.sender, address(this), _amount);
        
        // Approve the vault to spend the tokens
        token.approve(address(vault), _amount);
        
        // Deposit tokens into the vault
        vault.deposit(_amount);
        
        // Update the vault shares
        vaultShares += _amount * vault.getPricePerFullShare();

        emit Deposited(_amount);
    }

    // Function to withdraw tokens from the Beefy vault
    function withdraw(uint256 _shares) external onlyOwner {
        require(_shares > 0, "Shares must be greater than 0");
        require(_shares <= vaultShares, "Cannot withdraw more than owned shares");

        // Withdraw tokens from the vault
        vault.withdraw(_shares);
        
        // Transfer withdrawn tokens to the owner
        uint256 amountWithdrawn = _shares / vault.getPricePerFullShare();
        token.transfer(msg.sender, amountWithdrawn);
        
        // Update the vault shares
        vaultShares -= _shares;

        emit Withdrawn(_shares);
    }

    // Function to check the current balance of the vault in tokens
    function getVaultBalance() external view returns (uint256) {
        return vault.balance();
    }

    // Function to check the total shares owned in the vault
    function getVaultShares() external view returns (uint256) {
        return vaultShares;
    }
}
```
