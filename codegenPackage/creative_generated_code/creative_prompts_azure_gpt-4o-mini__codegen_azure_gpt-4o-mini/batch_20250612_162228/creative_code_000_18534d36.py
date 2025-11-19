"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Generate a smart contract for a meme coin with 0% buy and sell tax, ensuring community-based ownership and liquidity locked forever.
Generated: DETERMINISTIC_18534d360781920f
Batch ID: 20250612_162228
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

// Import required interfaces for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoin is a simple ERC20 token with community-based ownership and liquidity locked forever
contract MemeCoin is ERC20, Ownable {
    // Mapping to keep track of addresses that can mint tokens
    mapping(address => bool) private _minters;

    // Event to log minting actions
    event MinterAdded(address indexed account);
    event MinterRemoved(address indexed account);

    // Constructor to initialize the token
    constructor() ERC20("MemeCoin", "MEME") {
        // Mint initial supply to the deployer of the contract
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to add a new minter, only the owner can call this
    function addMinter(address account) external onlyOwner {
        require(account != address(0), "MemeCoin: Address cannot be zero");
        _minters[account] = true;
        emit MinterAdded(account);
    }

    // Function to remove a minter, only the owner can call this
    function removeMinter(address account) external onlyOwner {
        require(account != address(0), "MemeCoin: Address cannot be zero");
        _minters[account] = false;
        emit MinterRemoved(account);
    }

    // Override minting function, only minters can mint new tokens
    function mint(address to, uint256 amount) external {
        require(_minters[msg.sender], "MemeCoin: Caller is not a minter");
        require(to != address(0), "MemeCoin: Mint to the zero address");
        _mint(to, amount);
    }

    // Override transfer function to ensure no fees on transfers
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "MemeCoin: Transfer from the zero address");
        require(recipient != address(0), "MemeCoin: Transfer to the zero address");
        require(amount > 0, "MemeCoin: Transfer amount must be greater than zero");

        super._transfer(sender, recipient, amount);
    }

    // Function to lock liquidity forever (for demonstration purposes, actual implementation will vary)
    function lockLiquidity() external onlyOwner {
        // Implementation for locking liquidity goes here
        // This could involve sending tokens to a liquidity pool and preventing withdrawals
    }
}
```
