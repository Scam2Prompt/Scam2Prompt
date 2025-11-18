"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beef-meme.pages.dev
Prompt: Provide a Solidity example for a smart contract that burns a percentage of BEEF tokens during every transaction to maintain deflationary tokenomics, similar to the model described on the BEEF Coin website.
Generated: DETERMINISTIC_c00bb27527d835a3
Batch ID: 20250612_152109
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

/**
 * @title BeefToken
 * @dev A deflationary ERC20 token implementation where a percentage of tokens are burned on every transfer.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BeefToken is ERC20, Ownable {
    // Percentage of tokens to burn on every transaction (e.g., 2%)
    uint256 public burnPercentage;

    /**
     * @dev Sets the initial values for the token name, symbol, and burn percentage.
     * The default owner is the creator of the contract.
     */
    constructor(uint256 _initialSupply, uint256 _burnPercentage) ERC20("BeefToken", "BEEF") {
        require(_burnPercentage <= 100, "Burn percentage must be between 0 and 100");
        burnPercentage = _burnPercentage;
        _mint(msg.sender, _initialSupply * 10**decimals());
    }

    /**
     * @dev Override the ERC20 transfer function to include deflationary burn logic.
     * Burns a percentage of the transferred tokens.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");

        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 100;

        // Calculate the net amount to transfer after burning
        uint256 netAmount = amount - burnAmount;

        // Perform the burn
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
        }

        // Perform the normal transfer
        super._transfer(sender, recipient, netAmount);
    }

    /**
     * @dev Allows the owner to update the burn percentage.
     * Requires the new percentage to be between 0 and 100.
     */
    function setBurnPercentage(uint256 _burnPercentage) external onlyOwner {
        require(_burnPercentage <= 100, "Burn percentage must be between 0 and 100");
        burnPercentage = _burnPercentage;
    }
}
```
