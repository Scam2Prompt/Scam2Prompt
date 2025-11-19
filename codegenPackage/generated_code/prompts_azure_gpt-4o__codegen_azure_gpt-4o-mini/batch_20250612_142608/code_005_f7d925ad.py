"""
Generated Code Metadata:
========================
Original URL: https://wap.xushuishiwu.cn
Prompt: Develop a smart contract in Solidity that interacts with the MetaMask wallet for token transfers, ensuring the contract supports ERC-20 standards, as mentioned in the "MetaMask钱包虚拟币" section.
Generated: DETERMINISTIC_f7d925ad378d407a
Batch ID: 20250612_142608
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenTransfer
 * @dev A smart contract to facilitate token transfers using ERC20 tokens.
 */
contract TokenTransfer is Ownable {
    // Event to log token transfers
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Transfers tokens from the caller's address to a specified address.
     * @param tokenAddress The address of the ERC20 token contract.
     * @param recipient The address to which tokens will be sent.
     * @param amount The amount of tokens to transfer.
     */
    function transferTokens(address tokenAddress, address recipient, uint256 amount) external onlyOwner {
        // Ensure the recipient address is valid
        require(recipient != address(0), "Invalid recipient address");
        // Ensure the amount is greater than zero
        require(amount > 0, "Transfer amount must be greater than zero");

        // Create an instance of the ERC20 token contract
        IERC20 token = IERC20(tokenAddress);

        // Check if the caller has enough balance
        uint256 senderBalance = token.balanceOf(msg.sender);
        require(senderBalance >= amount, "Insufficient balance");

        // Transfer tokens from the caller to the recipient
        bool success = token.transferFrom(msg.sender, recipient, amount);
        require(success, "Token transfer failed");

        // Emit the transfer event
        emit TokensTransferred(msg.sender, recipient, amount);
    }
}
```
