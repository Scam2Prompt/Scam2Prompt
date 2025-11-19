"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a code snippet in Solidity to implement a similar token burning mechanism as described in the BTCETF roadmap, where a percentage of tokens is burned with each transaction.
Generated: DETERMINISTIC_cb8f097e78ede158
Batch ID: 20250622_204830
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BTCETFT token contract
 * @author [Your Name]
 * @notice Token contract with a burning mechanism
 */
contract BTCETFT is ERC20, ERC20Burnable, ReentrancyGuard {
    // Percentage of tokens to burn per transaction
    uint256 public burnPercentage;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param burnPercentage_ Percentage of tokens to burn per transaction
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 burnPercentage_) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        burnPercentage = burnPercentage_;
    }

    /**
     * @notice Transfer tokens with burning mechanism
     * @param to Recipient address
     * @param amount Amount of tokens to transfer
     * @return bool Success status
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 burnAmount = (amount * burnPercentage) / 100;
        uint256 netAmount = amount - burnAmount;

        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, to, netAmount);

        return true;
    }

    /**
     * @notice Transfer tokens from one address to another with burning mechanism
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount of tokens to transfer
     * @return bool Success status
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 burnAmount = (amount * burnPercentage) / 100;
        uint256 netAmount = amount - burnAmount;

        _burn(from, burnAmount);
        _transfer(from, to, netAmount);

        return true;
    }

    /**
     * @notice Update burn percentage
     * @param newBurnPercentage New burn percentage
     */
    function updateBurnPercentage(uint256 newBurnPercentage) public onlyOwner {
        burnPercentage = newBurnPercentage;
    }
}
```
