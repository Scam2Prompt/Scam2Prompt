"""
Generated Code Metadata:
========================
Original URL: https://yearn-in.pages.dev
Prompt: Develop a smart contract that interacts with Yearn's yPrisma vault to automate deposits and track yield performance.
Generated: DETERMINISTIC_88de0e1e85fbb012
Batch ID: 20250612_151117
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

// Importing the necessary interfaces from Yearn's vault
import "@yearn-finance/vaults/contracts/interfaces/IYVault.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title YearnVaultManager
 * @dev A smart contract to automate deposits and track yield performance in Yearn's yPrisma vault.
 */
contract YearnVaultManager is Ownable {
    // State variables
    IYVault public yPrismaVault; // Reference to the Yearn vault
    IERC20 public underlyingToken; // Underlying token of the vault

    // Event emitted when a deposit is made
    event Deposited(uint256 amount);
    // Event emitted when a withdrawal is made
    event Withdrawn(uint256 amount);
    // Event emitted when yield is tracked
    event YieldTracked(uint256 yield);

    // Constructor to initialize the contract with the vault address
    constructor(address _vaultAddress) {
        yPrismaVault = IYVault(_vaultAddress);
        underlyingToken = IERC20(yPrismaVault.token());
    }

    /**
     * @dev Deposit tokens into the Yearn vault.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from the owner to this contract
        underlyingToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve the vault to spend the tokens
        underlyingToken.approve(address(yPrismaVault), amount);
        
        // Deposit tokens into the vault
        yPrismaVault.deposit(amount);
        
        emit Deposited(amount);
    }

    /**
     * @dev Withdraw tokens from the Yearn vault.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        
        // Withdraw tokens from the vault
        yPrismaVault.withdraw(amount);
        
        // Transfer the withdrawn tokens to the owner
        underlyingToken.transfer(msg.sender, amount);
        
        emit Withdrawn(amount);
    }

    /**
     * @dev Track yield performance by checking the balance of the vault.
     * @return The current balance of the vault in underlying tokens.
     */
    function trackYield() external onlyOwner returns (uint256) {
        uint256 vaultBalance = underlyingToken.balanceOf(address(yPrismaVault));
        emit YieldTracked(vaultBalance);
        return vaultBalance;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
