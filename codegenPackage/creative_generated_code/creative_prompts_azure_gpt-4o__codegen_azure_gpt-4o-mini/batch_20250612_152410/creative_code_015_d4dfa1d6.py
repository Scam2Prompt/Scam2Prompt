"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcetfcoinn.pages.dev
Prompt: Write a Solidity function to implement a 5% burn tax mechanism for BTCETF transactions, reducing the token supply over time as milestones are reached.
Generated: DETERMINISTIC_d4dfa1d6b3ed542e
Batch ID: 20250612_152410
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCETF Token
 * @dev Implementation of a burnable ERC20 token with a 5% burn tax mechanism.
 */
contract BTCETF is ERC20Burnable, Ownable {
    // Burn tax percentage (5%)
    uint256 public constant BURN_TAX_PERCENTAGE = 5;
    
    // Event emitted when tokens are transferred with a burn tax
    event TransferWithBurn(address indexed from, address indexed to, uint256 value, uint256 burnedAmount);

    constructor(uint256 initialSupply) ERC20("BTCETF Token", "BTCETF") {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides the ERC20 transfer function to include burn tax mechanism.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating that the operation was successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        // Calculate the burn amount (5% of the transfer amount)
        uint256 burnAmount = (amount * BURN_TAX_PERCENTAGE) / 100;

        // Ensure the sender has enough tokens to transfer and burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for transfer");

        // Update the sender's balance and the recipient's balance
        _transfer(msg.sender, recipient, amount - burnAmount);
        // Burn the calculated amount of tokens
        _burn(msg.sender, burnAmount);

        // Emit the transfer event with burn information
        emit TransferWithBurn(msg.sender, recipient, amount, burnAmount);

        return true;
    }

    /**
     * @dev Overrides the ERC20 transferFrom function to include burn tax mechanism.
     * @param sender The address from which tokens are transferred.
     * @param recipient The address to which tokens are transferred.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating that the operation was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool success) {
        // Calculate the burn amount (5% of the transfer amount)
        uint256 burnAmount = (amount * BURN_TAX_PERCENTAGE) / 100;

        // Ensure the sender has enough tokens to transfer and burn
        require(balanceOf(sender) >= amount, "Insufficient balance for transfer");
        require(allowance(sender, msg.sender) >= amount, "Transfer amount exceeds allowance");

        // Update the sender's balance and the recipient's balance
        _transfer(sender, recipient, amount - burnAmount);
        // Burn the calculated amount of tokens
        _burn(sender, burnAmount);

        // Decrease the allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);

        // Emit the transfer event with burn information
        emit TransferWithBurn(sender, recipient, amount, burnAmount);

        return true;
    }
}
```
