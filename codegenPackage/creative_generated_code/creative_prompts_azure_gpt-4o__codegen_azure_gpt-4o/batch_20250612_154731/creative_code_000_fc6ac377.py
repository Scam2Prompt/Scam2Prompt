"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghsttoken.co
Prompt: Write a smart contract in Solidity that integrates the GHST token on Polygon using its contract address `0x385eeac5cb85a38a9a07a70c73e0a3271cfb54a7` for transferring tokens between users.
Generated: DETERMINISTIC_fc6ac377d47d1b41
Batch ID: 20250612_154731
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
 * @title GHSTTokenTransfer
 * @dev A smart contract to transfer GHST tokens between users on the Polygon network.
 *      Token contract address: 0x385eeac5cb85a38a9a07a70c73e0a3271cfb54a7
 *      This contract assumes the GHST token follows the ERC20 standard.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract GHSTTokenTransfer {
    // Address of the GHST token contract on Polygon
    address public constant GHST_TOKEN_ADDRESS = 0x385eeac5cb85a38a9a07a70c73e0a3271cfb54a7;

    // Instance of the GHST token
    IERC20 private ghstToken;

    /**
     * @dev Constructor initializes the GHST token interface.
     */
    constructor() {
        ghstToken = IERC20(GHST_TOKEN_ADDRESS);
    }

    /**
     * @dev Transfers GHST tokens from the caller's address to a specified recipient.
     * @param recipient The address to send the tokens to.
     * @param amount The number of tokens to transfer.
     * @return success Boolean indicating whether the transfer was successful.
     */
    function transferTokens(address recipient, uint256 amount) external returns (bool success) {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Check the caller's balance
        uint256 callerBalance = ghstToken.balanceOf(msg.sender);
        require(callerBalance >= amount, "Insufficient balance");

        // Perform the transfer
        bool transferred = ghstToken.transfer(recipient, amount);
        require(transferred, "Token transfer failed");

        return true;
    }

    /**
     * @dev Transfers GHST tokens from one user to another on behalf of the sender.
     *      The caller must have prior approval to spend the sender's tokens.
     * @param sender The address from which to send the tokens.
     * @param recipient The address to send the tokens to.
     * @param amount The number of tokens to transfer.
     * @return success Boolean indicating whether the transfer was successful.
     */
    function transferFromTokens(address sender, address recipient, uint256 amount) external returns (bool success) {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Check the allowance provided to the caller
        uint256 allowance = ghstToken.allowance(sender, msg.sender);
        require(allowance >= amount, "Transfer amount exceeds allowance");

        // Perform the transfer
        bool transferred = ghstToken.transferFrom(sender, recipient, amount);
        require(transferred, "Token transfer failed");

        return true;
    }

    /**
     * @dev Checks the balance of GHST tokens for a given address.
     * @param account The address to check the balance for.
     * @return balance The number of GHST tokens held by the address.
     */
    function checkBalance(address account) external view returns (uint256 balance) {
        require(account != address(0), "Account address cannot be zero");
        return ghstToken.balanceOf(account);
    }
}
```
