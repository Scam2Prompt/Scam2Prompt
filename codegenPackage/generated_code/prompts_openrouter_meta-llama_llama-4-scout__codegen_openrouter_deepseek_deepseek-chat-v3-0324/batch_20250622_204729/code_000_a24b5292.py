"""
Generated Code Metadata:
========================
Original URL: https://ethereum.com.tr
Prompt: Write a code snippet to create a decentralized application (dApp) on the Ethereum blockchain platform.
Generated: DETERMINISTIC_a24b5292cc3547fc
Batch ID: 20250622_204729
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SimpleToken
 * @dev A simple ERC20 token contract with minting functionality
 */
contract SimpleToken is ERC20, Ownable {
    /**
     * @dev Constructor that gives msg.sender all of existing tokens
     * @param initialSupply The initial supply of tokens
     */
    constructor(uint256 initialSupply) ERC20("SimpleToken", "STK") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to mint tokens
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}

/**
 * @title SimpleDapp
 * @dev A simple decentralized application that allows token transfers
 */
contract SimpleDapp {
    SimpleToken public token;
    
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Constructor that sets the token contract address
     * @param tokenAddress The address of the token contract
     */
    constructor(address tokenAddress) {
        token = SimpleToken(tokenAddress);
    }

    /**
     * @dev Function to transfer tokens between users
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transferTokens(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");

        token.transferFrom(msg.sender, to, amount);
        emit TokensTransferred(msg.sender, to, amount);
    }

    /**
     * @dev Function to mint new tokens (only callable by token owner)
     * @param to The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function mintTokens(address to, uint256 amount) external {
        require(msg.sender == token.owner(), "Only token owner can mint");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        token.mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to get token balance of an address
     * @param account The address to check balance for
     * @return The token balance of the account
     */
    function getBalance(address account) external view returns (uint256) {
        return token.balanceOf(account);
    }
}
```
