"""
Generated Code Metadata:
========================
Original URL: https://app-memecoin.online
Prompt: Generate a Solidity smart contract code for creating a new memecoin token with a similar functionality to the one on app-memecoin.online.
Generated: DETERMINISTIC_3d01cfc63a493922
Batch ID: 20250622_205436
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Memecoin contract inheriting from ERC20 and Ownable
contract Memecoin is ERC20, Ownable {
    // Initial supply of tokens
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Memecoin", "MEME") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the specified amount of tokens to the given address
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    // Function to transfer tokens with a fee (optional feature)
    function transferWithFee(address recipient, uint256 amount, uint256 fee) external returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(fee < amount, "Fee must be less than transfer amount");

        // Calculate the net amount to transfer after fee
        uint256 netAmount = amount - fee;

        // Transfer the net amount to the recipient
        _transfer(msg.sender, recipient, netAmount);
        // Transfer the fee to the owner
        _transfer(msg.sender, owner(), fee);

        return true;
    }
}
```
