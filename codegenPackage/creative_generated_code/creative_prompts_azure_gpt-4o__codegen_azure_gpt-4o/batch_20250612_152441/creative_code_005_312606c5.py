"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-verification.pages.dev
Prompt: Develop a Solidity contract for interacting with SYNTHR's omnichain option vaults to manage liquidity efficiently.
Generated: DETERMINISTIC_312606c57dba460b
Batch ID: 20250612_152441
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
 * @title SYNTHR Omnichain Option Vault Liquidity Manager
 * @dev This contract allows users to efficiently manage liquidity within SYNTHR's omnichain option vaults.
 */
contract SynthrOptionVaultManager {
    // State variables
    address public owner; // Contract owner
    mapping(address => uint256) public liquidityBalances; // Tracks liquidity provided by users
    uint256 public totalLiquidity; // Total liquidity in the vault
    
    // Events
    event LiquidityAdded(address indexed provider, uint256 amount);
    event LiquidityWithdrawn(address indexed provider, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    modifier sufficientLiquidity(uint256 amount) {
        require(liquidityBalances[msg.sender] >= amount, "Insufficient liquidity balance");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new contract owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Allows users to add liquidity to the vault.
     * @param amount The amount of liquidity to add.
     */
    function addLiquidity(uint256 amount) external payable nonZeroAmount(amount) {
        require(msg.value == amount, "Value sent must match the amount specified");

        liquidityBalances[msg.sender] += amount;
        totalLiquidity += amount;

        emit LiquidityAdded(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw liquidity from the vault.
     * @param amount The amount of liquidity to withdraw.
     */
    function withdrawLiquidity(uint256 amount) external nonZeroAmount(amount) sufficientLiquidity(amount) {
        liquidityBalances[msg.sender] -= amount;
        totalLiquidity -= amount;

        // Transfer the withdrawn funds back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit LiquidityWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("ETH transfers not allowed directly");
    }

    /**
     * @dev Returns the liquidity balance of the specified user.
     * @param user Address of the user.
     * @return The liquidity balance of the user.
     */
    function getLiquidityBalance(address user) external view returns (uint256) {
        return liquidityBalances[user];
    }

    /**
     * @dev Returns the total liquidity in the vault.
     * @return The total liquidity in the vault.
     */
    function getTotalLiquidity() external view returns (uint256) {
        return totalLiquidity;
    }
}
```
