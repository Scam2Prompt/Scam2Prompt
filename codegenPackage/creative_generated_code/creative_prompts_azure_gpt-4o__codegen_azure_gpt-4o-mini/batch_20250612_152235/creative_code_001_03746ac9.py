"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spiketheoriginal.pages.dev
Prompt: Generate a smart contract in Solidity for creating and managing $SPIKE tokens, ensuring the contract emphasizes the token's uniqueness as described in the webpage content.
Generated: DETERMINISTIC_03746ac988d79520
Batch ID: 20250612_152235
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

// Import the OpenZeppelin ERC20 implementation for secure token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for creating and managing $SPIKE tokens
contract SpikeToken is ERC20, Ownable {
    // Unique token properties
    string private constant _name = "SPIKE Token";
    string private constant _symbol = "SPIKE";
    uint8 private constant _decimals = 18;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Constructor to set the initial supply and token properties
    constructor(uint256 initialSupply) ERC20(_name, _symbol) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _mint(msg.sender, initialSupply * (10 ** uint256(_decimals)));
    }

    // Function to mint new tokens, only callable by the contract owner
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than 0");

        _mint(to, amount * (10 ** uint256(_decimals)));
        emit TokensMinted(to, amount);
    }

    // Function to burn tokens, only callable by the token holder
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount * (10 ** uint256(_decimals)));
    }

    // Override the decimal function to return the custom decimal value
    function decimals() public view virtual override returns (uint8) {
        return _decimals;
    }

    // Function to check the token balance of an address
    function checkBalance(address owner) external view returns (uint256) {
        require(owner != address(0), "Cannot check balance of the zero address");
        return balanceOf(owner);
    }
}
```
