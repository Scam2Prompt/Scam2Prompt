"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btconbase-ai.pages.dev
Prompt: Develop a smart contract that utilizes the low-cost transaction features of the Base chain for Bitcoin on Base.
Generated: DETERMINISTIC_83daefd982a28bcb
Batch ID: 20250612_155140
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

// Importing OpenZeppelin Contracts for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SmartContractExample
 * @dev A simple ERC20 token contract to demonstrate low-cost transactions on the Base chain
 */
contract SmartContractExample is ERC20, Ownable {
    // Event emitted for every token transfer
    event TokensTransferred(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Constructor that gives the deployer all initial tokens
     * @param initialSupply The initial supply of tokens to be minted
     */
    constructor(uint256 initialSupply) ERC20("BaseToken", "BTK") {
        // Mint the initial supply of tokens to the contract deployer
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Transfer tokens from the caller's account to another account
     * @param recipient The address of the recipient
     * @param amount The amount of tokens to transfer
     * @return success Returns true if the transfer was successful
     */
    function transferTokens(address recipient, uint256 amount) public returns (bool success) {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens
        _transfer(msg.sender, recipient, amount);
        
        // Emit event for transfer
        emit TokensTransferred(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Mint new tokens to a specified address
     * @param account The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function mintTokens(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        
        // Mint tokens
        _mint(account, amount);
    }

    /**
     * @dev Burn tokens from the caller's account
     * @param amount The amount of tokens to burn
     */
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Burn tokens
        _burn(msg.sender, amount);
    }
}
```
