"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-ca.web.app
Prompt: Generate a smart contract for the $MPEPE token that includes a mechanism for burning tokens after each transaction, as described in the Mpeppe project details.
Generated: DETERMINISTIC_52f0d66d3a7cf17e
Batch ID: 20250612_164134
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

// Importing OpenZeppelin's ERC20 implementation and Ownable
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MPEPE Token Contract
 * @dev This contract implements a fungible token with a burn mechanism after each transaction.
 */
contract MPEPE is ERC20, Ownable {
    // Burn percentage defined as a constant (e.g., 1% burn)
    uint256 public constant BURN_PERCENTAGE = 1;

    // Events for tracking burns
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor(uint256 initialSupply) ERC20("MPEPE Token", "MPEPE") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides the transfer function to include burn mechanism.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 amountToBurn = (amount * BURN_PERCENTAGE) / 100;
        require(amountToBurn < amount, "Burn amount exceeds transfer amount");

        // Calculate the final amount to transfer after burn
        uint256 amountAfterBurn = amount - amountToBurn;

        // Call the internal transfer function
        _transfer(_msgSender(), recipient, amountAfterBurn);
        // Burn the tokens
        _burn(_msgSender(), amountToBurn);

        // Emit the burn event
        emit TokensBurned(_msgSender(), amountToBurn);

        return true;
    }

    /**
     * @dev Overrides the transferFrom function to include burn mechanism.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 amountToBurn = (amount * BURN_PERCENTAGE) / 100;
        require(amountToBurn < amount, "Burn amount exceeds transfer amount");

        // Calculate the final amount to transfer after burn
        uint256 amountAfterBurn = amount - amountToBurn;

        // Call the internal transfer function
        _transfer(sender, recipient, amountAfterBurn);
        // Burn the tokens
        _burn(sender, amountToBurn);

        // Update allowance
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);

        // Emit the burn event
        emit TokensBurned(sender, amountToBurn);

        return true;
    }
}
```
