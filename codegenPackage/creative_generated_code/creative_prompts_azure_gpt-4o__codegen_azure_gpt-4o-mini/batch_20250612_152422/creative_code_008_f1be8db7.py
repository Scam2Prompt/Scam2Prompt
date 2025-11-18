"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-io.web.app
Prompt: Provide a detailed explanation of how to implement a zero buy-and-sell tax mechanism in a BEP20 token smart contract, referencing $GIGA's tokenomics.
Generated: DETERMINISTIC_f1be8db740c0c15b
Batch ID: 20250612_152422
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GigaToken
 * @dev Implementation of a BEP20 token with zero buy-and-sell tax mechanism
 */
contract GigaToken is ERC20, Ownable {
    // Mapping to track amounts of tokens held by each address
    mapping(address => bool) private _isExcludedFromTax;

    // Event emitted when an address is excluded from taxes
    event ExcludedFromTax(address indexed account);

    // Constructor to initialize the token with its name and symbol
    constructor() ERC20("Giga Token", "GIGA") {
        // Mint initial supply to the contract deployer's address
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    /**
     * @dev Function to exclude an address from tax.
     * @param account The address to exclude from buy/sell tax.
     */
    function excludeFromTax(address account) external onlyOwner {
        require(!_isExcludedFromTax[account], "Account is already excluded");
        _isExcludedFromTax[account] = true;
        emit ExcludedFromTax(account);
    }

    /**
     * @dev Function to include an address back to tax.
     * @param account The address to include back to buy/sell tax.
     */
    function includeInTax(address account) external onlyOwner {
        require(_isExcludedFromTax[account], "Account is not excluded");
        _isExcludedFromTax[account] = false;
    }

    /**
     * @dev Override the transfer function to implement the zero tax mechanism
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // If the sender is excluded from tax, proceed with the transfer
        require(amount > 0, "Transfer amount must be greater than zero");
        
        // If sender is excluded from tax, proceed without tax
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            // Implement any additional logic if needed for non-excluded accounts
            super._transfer(sender, recipient, amount);
        }
    }
}
```
