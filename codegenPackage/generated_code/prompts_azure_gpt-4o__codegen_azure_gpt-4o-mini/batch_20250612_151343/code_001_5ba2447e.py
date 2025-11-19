"""
Generated Code Metadata:
========================
Original URL: https://basedonpepe.pages.dev
Prompt: Generate Solidity code for a smart contract that interacts with the Based $PEPE token on the BASE chain, specifically using the contract address `0x52b492a33E447Cdb854c7FC19F1e57E8BfA1777D` to verify token balances.
Generated: DETERMINISTIC_5ba2447ef53ed741
Batch ID: 20250612_151343
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

// Interface for the ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// Smart contract to interact with the Based $PEPE token
contract PepeTokenInteraction {
    // Address of the Based $PEPE token contract
    address public constant PEPE_TOKEN_ADDRESS = 0x52b492a33E447Cdb854c7FC19F1e57E8BfA1777D;

    // Instance of the ERC20 token interface
    IERC20 private pepeToken;

    // Constructor to initialize the token interface
    constructor() {
        pepeToken = IERC20(PEPE_TOKEN_ADDRESS);
    }

    // Function to get the balance of a specific address
    function getPepeBalance(address account) external view returns (uint256) {
        require(account != address(0), "Invalid address: zero address");
        uint256 balance = pepeToken.balanceOf(account);
        return balance;
    }

    // Function to transfer $PEPE tokens from the caller to a recipient
    function transferPepe(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Invalid address: zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Transfer tokens and handle potential failure
        bool success = pepeToken.transfer(recipient, amount);
        require(success, "Transfer failed");

        return success;
    }

    // Function to approve a spender to spend a specified amount of $PEPE tokens
    function approvePepe(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Invalid address: zero address");
        require(amount > 0, "Approval amount must be greater than zero");

        // Approve the spender and handle potential failure
        bool success = pepeToken.approve(spender, amount);
        require(success, "Approval failed");

        return success;
    }
}
```
