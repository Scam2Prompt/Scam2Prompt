"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimyourneiro.pages.dev
Prompt: Provide a Solidity smart contract example for managing the $NEIRO token on the Ethereum network, including details like the token name, symbol, and supply information outlined on the NEIRO site.
Generated: DETERMINISTIC_643d63ceb8c08ccb
Batch ID: 20250612_151343
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Context.sol";

// Contract for the NEIRO token
contract NEIRO is Context, ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million NEIRO tokens

    // Constructor to initialize token name, symbol and initial supply
    constructor() ERC20("NEIRO Token", "NEIRO") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint initial supply to the contract owner
    }

    // Function to mint new tokens (only owner can call this function)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
    }

    // Function to burn tokens from a specified address (only owner can call this function)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(_msgSender()) >= amount, "Insufficient balance to burn");

        _burn(_msgSender(), amount);
    }

    // Override the transfer function to include additional checks if needed
    function transfer(address to, uint256 amount) public virtual override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(to, amount);
    }

    // Override the transferFrom function to include additional checks if needed
    function transferFrom(address from, address to, uint256 amount) public virtual override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transferFrom(from, to, amount);
    }
}
```
