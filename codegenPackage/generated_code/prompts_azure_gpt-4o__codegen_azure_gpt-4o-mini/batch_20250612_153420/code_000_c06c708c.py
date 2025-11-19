"""
Generated Code Metadata:
========================
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a smart contract in Solidity for a deflationary token similar to $GFOX, including a burn mechanism that reduces the token supply with every transaction.
Generated: DETERMINISTIC_c06c708c439ac170
Batch ID: 20250612_153420
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
 * @dev A deflationary ERC20 token that burns a percentage of tokens on every transaction.
 */
contract DeflationaryToken is ERC20, Ownable {
    // Percentage of tokens to burn on each transaction (in basis points)
    uint256 public burnRate; // e.g., 500 means 5%

    // Event emitted when the burn rate is updated
    event BurnRateUpdated(uint256 newBurnRate);

    /**
     * @dev Constructor that gives the deployer all initial tokens and sets the burn rate.
     * @param initialSupply The initial supply of tokens.
     * @param _burnRate The initial burn rate in basis points (100 basis points = 1%).
     */
    constructor(uint256 initialSupply, uint256 _burnRate) ERC20("DeflationaryToken", "DFT") {
        require(_burnRate <= 10000, "Burn rate must be <= 10000 basis points (100%)");
        burnRate = _burnRate;
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Updates the burn rate.
     * @param newBurnRate The new burn rate in basis points.
     */
    function updateBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 10000, "Burn rate must be <= 10000 basis points (100%)");
        burnRate = newBurnRate;
        emit BurnRateUpdated(newBurnRate);
    }

    /**
     * @dev Overrides the transfer function to include the burn mechanism.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the transfer amount is valid
        require(transferAmount > 0, "Transfer amount must be greater than zero");

        // Burn the tokens
        _burn(msg.sender, burnAmount);

        // Transfer the remaining tokens
        _transfer(msg.sender, recipient, transferAmount);
        return true;
    }

    /**
     * @dev Overrides the transferFrom function to include the burn mechanism.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the transfer amount is valid
        require(transferAmount > 0, "Transfer amount must be greater than zero");

        // Burn the tokens
        _burn(sender, burnAmount);

        // Transfer the remaining tokens
        _transfer(sender, recipient, transferAmount);

        // Update allowance
        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance - amount);

        return true;
    }
}
```
