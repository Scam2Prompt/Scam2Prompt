"""
Generated Code Metadata:
========================
Original URL: https://apedcoin.com
Prompt: Generate a smart contract for the APED token ($APED) with a total supply of 1,000,000,000 and the specified contract address.
Generated: DETERMINISTIC_1657b00ef46dea1b
Batch ID: 20250612_135717
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

// APED Token Contract
contract APEDToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant _totalSupply = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("APED Token", "APED") {
        // Mint the total supply to the contract deployer
        _mint(msg.sender, _totalSupply);
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the specified amount of tokens
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
    }

    // Function to retrieve the total supply of the token
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
}
```
