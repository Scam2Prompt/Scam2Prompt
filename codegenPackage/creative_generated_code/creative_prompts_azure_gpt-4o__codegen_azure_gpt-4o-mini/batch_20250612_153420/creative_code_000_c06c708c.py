"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a smart contract in Solidity for a deflationary token similar to $GFOX, including a burn mechanism that reduces the token supply with every transaction.
Generated: DETERMINISTIC_c06c708c439ac170
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DeflationaryToken
 * @dev A deflationary token that burns a percentage of tokens on each transaction.
 */
contract DeflationaryToken is ERC20, Ownable {
    // Percentage of tokens to burn on each transaction (in basis points)
    uint256 public burnRate;

    // Event to emit when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Sets the token name and symbol, and initializes the burn rate.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param _burnRate The burn rate in basis points (100 basis points = 1%).
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _burnRate
    ) ERC20(name, symbol) {
        require(_burnRate <= 10000, "Burn rate cannot exceed 100%");
        burnRate = _burnRate;
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the deployer
    }

    /**
     * @dev Overrides the _transfer function to include the burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate the burn amount
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Call the parent _transfer function
        super._transfer(sender, recipient, transferAmount);

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit TokensBurned(sender, burnAmount);
        }
    }

    /**
     * @dev Updates the burn rate.
     * @param newBurnRate The new burn rate in basis points (100 basis points = 1%).
     */
    function updateBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 10000, "Burn rate cannot exceed 100%");
        burnRate = newBurnRate;
    }
}
```
