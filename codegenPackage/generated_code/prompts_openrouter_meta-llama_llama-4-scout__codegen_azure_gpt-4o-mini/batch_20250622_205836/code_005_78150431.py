"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Develop a simple smart contract in Solidity to create and manage meme coins on the Binance Smart Chain, similar to Oracle Meme's Meme Coin Generator.
Generated: DETERMINISTIC_7815043153e8e83d
Batch ID: 20250622_205836
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoin is a simple ERC20 token contract for creating meme coins
contract MemeCoin is ERC20, Ownable {
    // Event emitted when a new meme coin is created
    event MemeCoinCreated(address indexed creator, string name, string symbol, uint256 initialSupply);

    // Constructor to initialize the meme coin with a name, symbol, and initial supply
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Minting the initial supply to the contract owner
        emit MemeCoinCreated(msg.sender, name, symbol, initialSupply);
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        _mint(to, amount);
    }

    // Function to burn tokens, only callable by the owner
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) public override onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        super.transferOwnership(newOwner);
    }
}
```

### Notes:
- This contract uses OpenZeppelin's ERC20 implementation for standard token functionality and security best practices.
- The contract allows the owner to mint and burn tokens, ensuring that only the creator can manage the supply.
- Events are emitted for important actions, such as creating a new meme coin.
- Proper error handling is implemented using `require` statements to ensure that invalid operations are not executed.
