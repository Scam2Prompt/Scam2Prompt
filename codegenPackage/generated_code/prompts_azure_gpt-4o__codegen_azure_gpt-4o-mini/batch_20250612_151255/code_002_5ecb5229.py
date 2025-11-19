"""
Generated Code Metadata:
========================
Original URL: https://claim-beef-meme.pages.dev
Prompt: Generate Solidity code for a smart contract that implements a deflationary token model similar to BEEF Coin, including token burning functionality to reduce supply over time.
Generated: DETERMINISTIC_5ecb5229cc094772
Batch ID: 20250612_151255
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DeflationaryToken
 * @dev Implementation of a deflationary ERC20 token with burning functionality.
 */
contract DeflationaryToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Percentage of tokens to burn on each transfer (in basis points)
    uint256 public burnRate;

    /**
     * @dev Constructor to initialize the token with a name, symbol, and initial supply.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param _burnRate The burn rate in basis points (100 basis points = 1%).
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnRate) 
        ERC20(name, symbol) 
    {
        require(_burnRate <= 10000, "Burn rate must be <= 10000 basis points (100%)");
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        burnRate = _burnRate;
    }

    /**
     * @dev Override the _transfer function to implement the burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the burn amount
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit TokensBurned(sender, burnAmount);
        }

        // Transfer the remaining tokens
        super._transfer(sender, recipient, transferAmount);
    }

    /**
     * @dev Function to update the burn rate.
     * @param newBurnRate The new burn rate in basis points.
     */
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 10000, "Burn rate must be <= 10000 basis points (100%)");
        burnRate = newBurnRate;
    }
}
```
