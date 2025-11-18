"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokcoin.pages.dev
Prompt: Develop a smart contract in Solidity for managing GROK token transactions, including features for burning tokens and tracking total supply.
Generated: DETERMINISTIC_3c8e3b2c5f94b663
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// GROK Token contract inheriting from ERC20 and Ownable
contract GROKToken is ERC20, Ownable {
    // Mapping to track the burnable tokens
    mapping(address => uint256) private _burnedTokens;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply) ERC20("GROK Token", "GROK") {
        // Mint the initial supply of tokens to the deployer
        _mint(msg.sender, initialSupply);
    }

    // Function to burn a specific amount of tokens from the caller's address
    function burn(uint256 amount) external {
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Transfer tokens to the zero address to burn them
        _burn(msg.sender, amount);
        _burnedTokens[msg.sender] += amount;

        // Emit an event for the burning action
        emit TokensBurned(msg.sender, amount);
    }

    // Function to get the total supply of burned tokens for an account
    function burnedTokens(address account) external view returns (uint256) {
        return _burnedTokens[account];
    }

    // Override the _beforeTokenTransfer hook to track the total supply
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Add any additional logic needed before token transfer if necessary
    }

    // Function to safely increase the token supply, callable only by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        _mint(to, amount);
    }
}
```
