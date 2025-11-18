"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.org
Prompt: Generate Solidity code for deploying a non-custodial smart contract that integrates Morpho's optimized vaults for earning yield.
Generated: DETERMINISTIC_9577d036ed89e408
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title MorphoVaultYieldContract
 * @dev A non-custodial smart contract integrating with Morpho's vaults to optimize yield.
 * This contract allows users to deposit and withdraw tokens, earning yield through Morpho.
 */
interface IMorphoVault {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function getUserBalance(address user, address token) external view returns (uint256);
}

contract MorphoVaultYieldContract {
    // Address of the Morpho Vault contract
    IMorphoVault public morphoVault;

    // Mapping to track deposited balances of each user per token
    mapping(address => mapping(address => uint256)) public userBalances;

    /**
     * @dev Constructor to initialize the Morpho Vault address.
     * @param _morphoVault Address of the Morpho Vault contract.
     */
    constructor(address _morphoVault) {
        require(_morphoVault != address(0), "Invalid Morpho Vault address");
        morphoVault = IMorphoVault(_morphoVault);
    }

    /**
     * @dev Allows users to deposit tokens into the Morpho Vault to earn yield.
     * @param token Address of the token to deposit.
     * @param amount Amount of tokens to deposit.
     */
    function deposit(address token, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to this contract
        require(ERC20(token).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the Morpho Vault to spend the tokens
        require(ERC20(token).approve(address(morphoVault), amount), "Approval failed");

        // Deposit tokens into the Morpho Vault
        morphoVault.deposit(token, amount);

        // Update the user's balance
        userBalances[msg.sender][token] += amount;
    }

    /**
     * @dev Allows users to withdraw tokens they have deposited from the Morpho Vault.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(address token, uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[msg.sender][token] >= amount, "Insufficient balance");

        // Withdraw tokens from the Morpho Vault
        morphoVault.withdraw(token, amount);

        // Transfer tokens back to the user
        require(ERC20(token).transfer(msg.sender, amount), "Token transfer failed");

        // Update the user's balance
        userBalances[msg.sender][token] -= amount;
    }

    /**
     * @dev Returns the balance of tokens deposited by a user.
     * @param user Address of the user.
     * @param token Address of the token.
     * @return The user's deposited token balance.
     */
    function getUserBalance(address user, address token) external view returns (uint256) {
        return userBalances[user][token];
    }
}

/**
 * @dev Minimal ERC20 interface for token interactions.
 */
interface ERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
