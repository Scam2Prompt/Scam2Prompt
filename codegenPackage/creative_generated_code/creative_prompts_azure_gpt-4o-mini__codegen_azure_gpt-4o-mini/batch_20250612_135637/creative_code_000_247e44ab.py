"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uyhybuygu7ytgt7yug.pages.dev
Prompt: Write a smart contract in Solidity for a token similar to $PSYOP that allows users to connect their wallets like MetaMask and Trust Wallet.
Generated: DETERMINISTIC_247e44abd2cc7493
Batch ID: 20250612_135637
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PSYOPToken
 * @dev This contract implements an ERC20 token with ownership control.
 */
contract PSYOPToken is ERC20, Ownable {
    // Mapping to keep track of user allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor to initialize the token with a name and symbol.
     * @param name Name of the token.
     * @param symbol Symbol of the token.
     * @param initialSupply Initial supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        require(initialSupply > 0, "Initial supply must be greater than zero.");
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the contract deployer
    }

    /**
     * @dev Function to mint new tokens.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     * Only the owner can call this function.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address.");
        require(amount > 0, "Mint amount must be greater than zero.");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero.");
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Function to approve an allowance for a spender.
     * @param spender The address that will spend the tokens.
     * @param amount The amount of tokens to allow.
     */
    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        require(spender != address(0), "Cannot approve the zero address.");
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to transfer tokens from one address to another.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address from, address to, uint256 amount) public virtual override returns (bool) {
        require(from != address(0), "Transfer from the zero address.");
        require(to != address(0), "Transfer to the zero address.");
        require(amount > 0, "Transfer amount must be greater than zero.");
        require(balanceOf(from) >= amount, "Insufficient balance for transfer.");
        
        _transfer(from, to, amount);
        _approve(from, msg.sender, allowance(from, msg.sender) - amount);
        return true;
    }
}
```
