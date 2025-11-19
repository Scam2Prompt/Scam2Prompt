"""
Generated Code Metadata:
========================
Original URL: https://baloncer.finance
Prompt: Generate a smart contract code for launching a new token on the HyperEVM Native Dex, using Solidity programming language.
Generated: DETERMINISTIC_54205c3ca56e59ca
Batch ID: 20250622_212712
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for creating a new ERC20 token
contract MyToken is ERC20, Ownable {
    // Mapping to keep track of token holders' balances
    mapping(address => uint256) private _balances;

    // Event to log token minting
    event TokensMinted(address indexed to, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the tokens
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);
    }

    // Function to transfer tokens with error handling
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount <= balanceOf(msg.sender), "Insufficient balance for transfer");

        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }

    // Function to approve token spending with error handling
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        // Call the parent approve function
        return super.approve(spender, amount);
    }

    // Function to transfer tokens from one address to another
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount <= balanceOf(sender), "Insufficient balance for transfer");
        require(amount <= allowance(sender, msg.sender), "Transfer amount exceeds allowance");

        // Call the parent transferFrom function
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }
}
```
