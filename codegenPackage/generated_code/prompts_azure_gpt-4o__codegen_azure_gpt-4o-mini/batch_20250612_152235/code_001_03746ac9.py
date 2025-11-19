"""
Generated Code Metadata:
========================
Original URL: https://spiketheoriginal.pages.dev
Prompt: Generate a smart contract in Solidity for creating and managing $SPIKE tokens, ensuring the contract emphasizes the token's uniqueness as described in the webpage content.
Generated: DETERMINISTIC_03746ac988d79520
Batch ID: 20250612_152235
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

// Contract for the $SPIKE token
contract SPIKE is ERC20, Ownable {
    // Unique token properties
    string private constant TOKEN_NAME = "SPIKE Token";
    string private constant TOKEN_SYMBOL = "SPIKE";
    uint8 private constant DECIMALS = 18;

    // Mapping to track unique token holders
    mapping(address => bool) private uniqueHolders;

    // Event emitted when a new unique holder is added
    event UniqueHolderAdded(address indexed holder);

    // Constructor to initialize the token with a total supply
    constructor(uint256 initialSupply) ERC20(TOKEN_NAME, TOKEN_SYMBOL) {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply * (10 ** uint256(DECIMALS)));
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        _mint(to, amount);
        _addUniqueHolder(to);
    }

    // Internal function to add a unique holder
    function _addUniqueHolder(address holder) internal {
        if (!uniqueHolders[holder]) {
            uniqueHolders[holder] = true;
            emit UniqueHolderAdded(holder);
        }
    }

    // Override the transfer function to track unique holders
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        _transfer(_msgSender(), recipient, amount);
        _addUniqueHolder(recipient);
        return true;
    }

    // Override the transferFrom function to track unique holders
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        _addUniqueHolder(recipient);
        return true;
    }

    // Function to check if an address is a unique holder
    function isUniqueHolder(address holder) external view returns (bool) {
        return uniqueHolders[holder];
    }
}
```
