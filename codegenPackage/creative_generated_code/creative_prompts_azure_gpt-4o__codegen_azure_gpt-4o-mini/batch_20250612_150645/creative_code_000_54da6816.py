"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-pandoshi.web.app
Prompt: Write a smart contract in Solidity for a deflationary token with a buy-and-burn mechanism, similar to the PAMBO token described in the Pandoshi ecosystem.
Generated: DETERMINISTIC_54da6816a0793bf1
Batch ID: 20250612_150645
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
 * @dev A deflationary ERC20 token with a buy-and-burn mechanism.
 */
contract DeflationaryToken is ERC20, Ownable {
    // Percentage of tokens to be burned on each transaction (in basis points, 10000 = 100%)
    uint256 public burnPercentage;
    // Total supply of the token
    uint256 public totalSupply;

    // Events for logging burns
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that sets the token name, symbol, total supply, and burn percentage.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of tokens to mint.
     * @param _burnPercentage The percentage of tokens to burn on each transaction.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Burn percentage must not exceed 100%");
        require(initialSupply > 0, "Initial supply must be greater than 0");

        burnPercentage = _burnPercentage;
        totalSupply = initialSupply * (10 ** decimals());
        _mint(msg.sender, totalSupply);
    }

    /**
     * @dev Override the _transfer function to implement the buy-and-burn mechanism.
     * @param from The address sending tokens.
     * @param to The address receiving tokens.
     * @param amount The amount of tokens being transferred.
     */
    function _transfer(address from, address to, uint256 amount) internal override {
        require(from != address(0), "Transfer from the zero address");
        require(to != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 sendAmount = amount - burnAmount;

        // Call the parent transfer function
        super._transfer(from, to, sendAmount);

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(from, burnAmount);
            emit TokensBurned(from, burnAmount);
        }
    }

    /**
     * @dev Allows the owner to change the burn percentage.
     * @param newBurnPercentage The new burn percentage to set.
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage must not exceed 100%");
        burnPercentage = newBurnPercentage;
    }
}
```
