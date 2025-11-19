"""
Generated Code Metadata:
========================
Original URL: https://bookofeth-xyz.pages.dev
Prompt: "Create a simple Ethereum smart contract in Solidity for a token with a fixed supply of 100,000,000, similar to $BOOE."
Generated: DETERMINISTIC_00a871be343f7bd9
Batch ID: 20250622_210918
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for a fixed supply token
contract BooeToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant _totalSupply = 100_000_000 * 10 ** 18; // 100 million tokens with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("BooeToken", "BOOE") {
        // Mint the total supply to the contract deployer
        _mint(msg.sender, _totalSupply);
    }

    // Function to mint new tokens (only owner can call this)
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= _totalSupply, "Minting exceeds total supply");
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can call this)
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }

    // Override the transfer function to include additional checks if needed
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to include additional checks if needed
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
