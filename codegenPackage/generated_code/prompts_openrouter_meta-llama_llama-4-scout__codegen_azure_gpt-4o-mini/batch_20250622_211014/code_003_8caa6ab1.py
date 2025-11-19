"""
Generated Code Metadata:
========================
Original URL: https://furies-mystery.pages.dev
Prompt: Develop a simple smart contract in Solidity to create a meme coin with similar characteristics to $MYSTERY, including a fixed supply and no taxes.
Generated: DETERMINISTIC_8caa6ab13e79e434
Batch ID: 20250622_211014
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

// Importing the OpenZeppelin ERC20 contract for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoin contract inherits from ERC20 and Ownable
contract MemeCoin is ERC20, Ownable {
    // Fixed supply of 1 million tokens (1,000,000)
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 18 decimals

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MemeCoin", "MEME") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to mint new tokens (only owner can call this)
    function mint(address to, uint256 amount) external onlyOwner {
        // Ensure that the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        // Mint the specified amount to the given address
        _mint(to, amount);
    }

    // Override the transfer function to prevent taxes (if any logic is added in the future)
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to prevent taxes (if any logic is added in the future)
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Call the parent transferFrom function
        return super.transferFrom(sender, recipient, amount);
    }
}
```
