"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Develop a smart contract in Solidity that interacts with the MetaMask wallet for token transfers, ensuring the contract supports ERC-20 standards, as mentioned in the "MetaMask钱包虚拟币" section.
Generated: DETERMINISTIC_f7d925ad378d407a
Batch ID: 20250612_142608
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenTransfer
 * @dev A smart contract for transferring ERC20 tokens.
 */
contract TokenTransfer is Ownable {
    // Event emitted when tokens are successfully transferred
    event TokensTransferred(address indexed token, address indexed to, uint256 amount);

    /**
     * @dev Transfers ERC20 tokens from the contract to a specified address.
     * @param token The address of the ERC20 token contract.
     * @param to The address to which the tokens will be sent.
     * @param amount The amount of tokens to send.
     */
    function transferTokens(address token, address to, uint256 amount) external onlyOwner {
        // Ensuring the provided address is a valid contract
        require(token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Getting the contract instance
        IERC20 erc20Token = IERC20(token);
        
        // Checking the contract balance before transfer
        uint256 contractBalance = erc20Token.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Transferring tokens
        bool success = erc20Token.transfer(to, amount);
        require(success, "Token transfer failed");

        // Emitting the transfer event
        emit TokensTransferred(token, to, amount);
    }

    /**
     * @dev Allows the contract owner to withdraw any ERC20 tokens mistakenly sent to the contract.
     * @param token The address of the ERC20 token contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Withdraw amount must be greater than zero");

        IERC20 erc20Token = IERC20(token);
        
        // Checking the contract balance before withdrawal
        uint256 contractBalance = erc20Token.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Transferring tokens to the owner
        bool success = erc20Token.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }
}
```
